---
id: confluence:591822850
source: confluence
type: page
space: TC
title: Managing DNS records
author: Minh Trang Nguyen (Unlicensed)
date: '2025-02-10'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591822850
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591822850
---
# Managing DNS records

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/591822850  

## Content

The Development and Production environments use the same domain, "teqplay.com", but the DNS records for the Development cluster are located in a different hosted zone in Route53. DNS records for the Development cluster need to be created in the hosted zone "dev.teqplay.com".

## Delegation to dev.teqplay.com, test.teqplay.com

To publish DNS records in the hosted zone "dev.teqplay.com" or "test.teqplay.com", a DNS record was created in the main hosted zone "teqplay.com " that points to the "dev.teqplay.com" or "test.teqplay.com" zone. See the screenshot below for an example.

This DNS record entry is required, otherwise, AWS will not publish the records.

## Public and private hosting zone

DNS records are managed by two separate `external-dns` deployments and are installed in only the DEVELOP cluster in namespace `external-dns`.

The reason for using separate deployments is to provide better clarity and facilitate easier debugging by having distinct `external-dns` instances for public and private hosted zones. These external-dns were setup by running the following commands.

**public hosted zone**

helm upgrade --install external-dns-dev-public oci://registry-1.docker.io/bitnamicharts/external-dns -n external-dns \
--set provider=aws \
--set aws.zoneType=public \
--set aws.region=eu-west-1 \
--set 'domainFilters[0]=dev.teqplay.com' \
--set txtPrefix=external.dns.public. \
--set txtOwnerId=/hostedzone/Z038052928XYZU4SNK9G5 \
--set aws.preferCNAME=true \
--set policy=sync \
--set 'annotationFilter=external-dns.alpha.kubernetes.io/access notin (private)'

**private hosted zone**

helm upgrade --install external-dns-private oci://registry-1.docker.io/bitnamicharts/external-dns -n external-dns \
--set provider=aws \
--set aws.zoneType=private \
--set aws.region=eu-west-1 \
--set 'domainFilters[0]=dev.teqplay.com' \
--set txtPrefix=external.dns.private. \
--set txtOwnerId=/hostedzone/Z060232111LJCUDJX7KZT \
--set aws.preferCNAME=true \
--set policy=sync

An annotation filter has been added to the public external-dns deployment to prevent private DNS records from being included in the public hosted zone in Route 53.

## SSL certificates

The Development cluster domain, `dev.teqplay.com`, uses an SSL certificate issued by AWS, which is renewed annually.

## Management Route 53 DNS records

Every Helm chart associated with the domain `dev.teqplay.com` and installed in the DEVELOP cluster will automatically have its application URL synchronized with Route 53 through external-dns. The AWS Load Balancer Controller first creates an entry in the EC2 Load Balancer, sets a listener rule, and assigns the load balancer address in the Ingress. This address is then used as the CNAME value in Route 53.

### Add the domain to the private hosted zone

To add the domain to the private hosted zone, simply add an annotation to the Ingress resource object associated with the domain.

external-dns.alpha.kubernetes.io/access: private

The process is illustrated in the diagram below.

## Public or Private DNS records

It’s recommended to place development URLs behind a private DNS zone because development processes are not sufficiently tested to be publicly accessible. Applications in the development cluster may have vulnerabilities that could pose a threat. Setting up a new DNS zone and separating it into public and private zones is easier for a new domain url. The table below shows which applications should be placed in a private zone and which need to be in a public zone. The URLs of a private zone will only be available within the same VPC.

| **Tier** | **Application** | **DNS Zone** |
| --- | --- | --- |
| ais stream tier | ais-stream | private |
|  |  |  |
| ais tier | ship-history | private |
|  | area-monitor | private |
|  | berth-monitor | private |
|  | ais-diff | private |
|  | anchor-monitor | private |
|  | encounter-monitor | private |
|  | ais-replay | private |
|  |  |  |
| ship tier | event-history | private |
|  | vesselvoyage | public + private |
|  | portreporter monitor | private |
|  | portcall+ | private |
|  | event-replay | private |
|  |  |  |
| visits & voyages tier | smartfleet | private |
|  |  |  |
| portcall tier | portreporter-monitor | private |
|  | portreporter | public + private |
|  | portsupport | public + private (deprecated) |
|  | portpublisher | public + private (deprecated) |
|  |  |  |
| core-services tier | portmatcher | private |
|  | csi | private |
|  | poma | private |
|  | routescout | private |
|  | predictions | private |
|  |  |  |
| general-services tier | datascience | private |
|  | pdf-renderer | private |
|  | terminallineup | private |
|  | functional-monitoring | private |
|  | scrapeshark | private |
|  | nexmo | private |
|  |  |  |
| customer-services tier | vesselmatcher | public + private |
|  | bunkerplanner | public + private |
|  | fuelboss | public + private |
|  | datastore | private |
|  | ISPS | private |
|  | Ship spare logistics | public + private |
|  | Terminal planner | public + private |
|  |  |  |
|  | internal-api | private |
|  | external-api | public + private |