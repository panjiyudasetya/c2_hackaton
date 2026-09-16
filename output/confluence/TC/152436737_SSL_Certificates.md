---
id: confluence:152436737
source: confluence
type: page
space: TC
title: SSL Certificates
author: Jamie de Leest
date: '2025-11-11'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/152436737
explicit_links: []
---
# SSL Certificates

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/152436737  

## Content

## Reimporting in AWS

We make use of the AWS Certificate Manager to manage our certificates in AWS. The `*.teqplay.nl` certificate is imported in two regions (`eu-west-1` and `us-east-1`). This certificate is used by our Application Load Balancers, all our CloudFront distributions and many more.

### Preparing the certificate for import

We need to prepare 3 different parts of the certificate to reimport it into AWS:

1. The certificate body
2. The certificate private key
3. The certificate chain

Here the certificate chain can be the trickier one to configure as it needs to be provided in the correct order, which is as follows:

1. `Sectigo RSA Domain Validation Secure Server CA`
2. `USERTrust RSA Certification Authority`

If this ever changes, you can easily find the current chain by going to one of our websites and viewing details of the certificate information.

The certificate chain details in Google Chrome

This chain should already be provided in the files we receive from our certificate provider. In the `Linux` folder, there should be a file called `star_teqplay_nl.ca-bundle`. If not, creating our own chain can be done easily by creating and copying the content from the `Root Certificates`.

### Reimporting the certificate

1. Go to the AWS Certificate Manager
2. Select the certificate we want to reimport (e.g. the `*.teqplay.nl` one).
3. Press the `Reimport` button (it should be somewhere in the top right of the page).
4. In the `Certificate body` field, provide the content of the `star_teqplay_nl.crt`.
5. In the `Certificate private key` field, provide the content of the `STAR_teqplay_nl.key`.
6. In the `Certificate chain` field, provide the prepared content we did in the prepare step or content of the `Linux/star_teqplay_nl.ca-bundle` file.

Do not forget to do this for all regions this certificate is used! (`eu-west-1` and `us-east-1`)

# Obtaining a new certificate

Best option is to re-use the existing certificate signing request (CSR), this way the private key does not need to be changed. You should receive a new public key (certificate) and possibly a new CA bundle/chain of trust (these can be downloaded in the web UI of Xolphin).

# Platform (EC2 instances)

Platform instances are running in Tomcat behind Apache. All SSL is done in Apache, so this is where the keys need to be updated.

* Check in `/etc/apache2/sites-enabled` where it looks for ssl certificates
* Replace `/etc/ssl/star_teqplay_nl.crt` with the new certificate
* Optionally (if it has changed) replace `/etc/ssl/WILDCARD_teqplay_nl.ca-bundle` with the new CA bundle
* Optionally (if it has changed) replace `/etc/ssl/private/STAR_teqplay_nl.key` with the new CA bundle
* Restart Apache by doing `sudo systemctl restart apache2`

If you want do do this automatically, you can create a script to easily update these files on all the EC2 servers. First, save the public key and CA bundle locally, and note down the file names. Then, create and edit the script:

wide760cat > update.sh <<EOT
certificate=star\_teqplay\_nl.crt
cabundle=bundle.crt
echo "Updating SSL certificate on $1"
ssh $1 'sudo tee /etc/ssl/star\_teqplay\_nl.crt > /dev/null' < $certificate
ssh $1 'sudo tee /etc/ssl/WILDCARD\_teqplay\_nl.ca-bundle > /dev/null' < $cabundle
ssh $1 'sudo systemctl restart apache2'
EOT
chmod a+x update.sh

Adapt the first two lines to match the files you downloaded. Then, for each server, do the following:

wide760./update.sh ubuntu@backenddev.teqplay.nl

This will update the certificates and restart Apache `httpd` to reload.

# AWS Certificate Manager

For Cloudfront and API manager, the certificate needs to be uploaded in ACM (AWS Certificate Manager). Ensure that you use the **us-east-1** region! Use "Import a certificate" to upload the new certificate. Copy-paste the data in the relevant input areas, and give the certificate a descriptive name, including the year in which it was issued.

# AWS Cloudfront

To update all frontend distributions to use the new certificate, you can either change them all by hand, or use the following script (please make sure to edit it to use the correct certificate ARNs, these can be found in ACM):

wide760old\_certificate='arn:aws:acm:us-east-1:050356841556:certificate/7490ed3f-80de-4193-8ff7-b85aad9036aa'
new\_certificate='arn:aws:acm:us-east-1:050356841556:certificate/41811051-41d2-4fbd-ab4c-7569bc671abb'
distributions=(
$(aws cloudfront list-distributions | jq \
--arg certificate $old\_certificate \
-r '.DistributionList.Items[] | select(.ViewerCertificate.Certificate == $certificate) | .Id')
)
echo "Distributions being updated"
echo "---------------------------"
printf "%s\n" "${distributions[@]}"
for i in "${distributions[@]}"; do
jqoperation="
.DistributionConfig |
del(.ViewerCertificate.IAMCertificateId) |
.ViewerCertificate.ACMCertificateArn = \"$new\_certificate\" |
.ViewerCertificate.Certificate = \"$new\_certificate\" |
.ViewerCertificate.CertificateSource = \"acm\"
"
previous=$(aws cloudfront get-distribution-config --id $i)
update=$(echo "$previous" | jq "$jqoperation")
result=$(aws cloudfront update-distribution --id $i --distribution-config "$update" --if-match $(echo "$previous" | jq -r '.ETag'))
echo "$(echo $result | jq -r '.Distribution.Id + ": " + .Distribution.Status')"
done

# AWS API Gateway

The API gateway uses regional endpoints, and these require the certificate to be uploaded to the **eu-west-1** region... So, you can repeat the ACM procedure, but now using another region! Then, you can open each custom domain name and change the certificate. Note the ARN of the new certificate, the nice name you give to the certificate in ACM is not shown/used for some reason.

# Update SSL Certificate in Rabbitmq

update the secret `rabbitmq-tls` in the `brokers` namespace with the certificate

Secret data:

1. The certificate body (star\_teqplay\_nl.crt) → tls.crt
2. The certificate private key (STAR\_teqplay\_nl.key) → tls.key
3. The certificate chain (star\_teqplay\_nl.ca-bundle) → ca.crt

# Updating the certificate on IRIS connection

The connection we make to Iris / Hamis is being protected using:

1. An IP filter (only backend currently is allowed)
2. A certificate presented upon connecting to secure the connection.
3. A username password as part of the SOAP authentication.

The IRIS certificate is shared between IRIS for Amsterdam and Rotterdam and stored in `/etc/teqplay` folder in backend. Originally it was part of the resources of platform as well.

In order to test the connection, SoapUI can be used with a tunnel to [backend.teqplay.nl](http://backend.teqplay.nl) to mimic the connection from the right IP (using tinyProxy).

When a new certificate is presented by the team (expected 2030), the following steps are foreseen:

1. Convert the keystore from the p12 format (in a .pfx extension) to a jks format (somehow the p12 format is not running well under current tomcat version, and gives an 'ínvalid password' error. command: `keytool -importkeystore -srckeystore original.p12 -srcstoretype pkcs12 -srcalias 1 -destkeystore converted.jks -deststoretype jks -deststorepass ******** -destalias 1`
2. Upload the certificate in backend and backenddev in `/etc/teqplay`
3. Update the system.conf to refer to the right certificate in `hamisPortcallNlamsAdapter` and `hamisPortcallNlrtmAdapter` and update password for the keystore