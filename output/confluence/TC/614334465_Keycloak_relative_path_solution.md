---
id: confluence:614334465
source: confluence
type: page
space: TC
title: Keycloak relative path solution
author: Minh Trang Nguyen (Unlicensed)
date: '2025-02-07'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/614334465
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/614334465
---
# Keycloak relative path solution

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/614334465  

## Content

Upgrading from Keycloak version 24.0.5 to 25.0.6 caused an issue because the relative path no longer worked after the upgrade. All applications still rely on the "/auth" prefix in the HTTP relative path, and removing this path has proven difficult. As a result, all applications now need to update the Keycloak URL to remove the "/auth" path, which would require significant effort from developers to modify repositories.

Several attempts were made to resolve this, such as adjusting the AWS load balancer, but these solutions were unsuccessful. The effective solution involves adding a sidecar with an Nginx image, which will act as a reverse proxy. The Nginx configuration will forward traffic without rewriting the URL, thus preventing issues with redirects that might cause clients to reject the connection, and ensuring the old URL continues to function properly.

This solution is only viable after upgrading to Keycloak version 25.0.6 and removing the "/auth" HTTP relative path. Since version 25.0.6 introduces new database migrations, performing a Helm rollback is not possible. Rolling back to the previous version would cause the application to fail due to incompatible database changes. To roll back, a point-in-time recovery of the Keycloak database is also required.

## Solution

The solution is relatively simple. The ConfigMap will be mounted in the sidecar, which will handle all Keycloak connections and forward them to the Keycloak instance.

**Advantages**

* Utilize a public Docker image without modifications.
* Modify only Helm values with minimal impact.
* Support both old and new URLs simultaneously.

### **Configmap**

The goal is to keep Keycloak running on port 8080, ensuring that when the sidecar is removed in the future, the existing Keycloak settings remain unchanged.

The configuration ensures that traffic for all new Keycloak URLs is forwarded directly. However, if the path contains “/auth,” the traffic will be forwarded without the “/auth”.

apiVersion: v1
kind: ConfigMap
metadata:
name: keycloak-nginx
data:
default.conf: |
server {
listen 8000;
server\_name \_;
# Default reverse proxy to Keycloak
location / {
proxy\_pass http://localhost:8080;
include /etc/nginx/conf.d/proxy\_params;
}
# Handle /auth with or without trailing slash and remove prefix
location /auth {
rewrite ^/auth(/.\*)$ /$1 break; # Remove /auth prefix for subpaths
rewrite ^/auth$ / break; # Redirect /auth to root `/`
proxy\_pass http://localhost:8080/;
include /etc/nginx/conf.d/proxy\_params;
}
# Enable gzip compression for performance
gzip on;
gzip\_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
gzip\_vary on;
}
proxy\_params: |
# Proxy settings for performance, security, and compatibility
proxy\_http\_version 1.1;
proxy\_set\_header Connection "";
proxy\_set\_header Host $host;
proxy\_set\_header X-Real-IP $remote\_addr;
proxy\_set\_header X-Forwarded-For $proxy\_add\_x\_forwarded\_for;
proxy\_set\_header X-Forwarded-Proto $scheme;
# WebSocket support
proxy\_set\_header Upgrade $http\_upgrade;
proxy\_set\_header Connection "Upgrade";
# Keepalive optimization
proxy\_buffering on;
proxy\_buffers 16 4k;
proxy\_busy\_buffers\_size 8k;
proxy\_connect\_timeout 5s;
proxy\_read\_timeout 60s;
proxy\_send\_timeout 60s;

### **Helm chart values changes**

These Helm value changes are temporary and should be removed once all applications have migrated to use the Keycloak URL without the “/auth” path.

* Added an extra volume for the ConfigMap configuration.
* The "service.http" must be disabled; otherwise, HTTP requests will be forwarded to the Keycloak instance. Since "service.http" is disabled, port 8080 must be exposed to ensure Keycloak remains accessible.
* Ingress must be configured to forward traffic to the Nginx sidecar.
* The Nginx container's port 8000 must be exposed by adding an extra container port.
* The sidecar mounts the ConfigMap with the custom configuration.
* The port 8000 needs to be added to the network policy, otherwise, the AWS load balancer will not be able to reach the target groups.

extraVolumes: |
- name: extensions
emptyDir: {}
- name: keycloak-nginx-volume
configMap:
name: keycloak-nginx
service:
type: NodePort
http:
enabled: false
extraPorts:
- name: nginxsidecar
port: 80
targetPort: nginxsidecar
protocol: TCP
ingress:
servicePort: nginxsidecar
extraContainerPorts:
- name: keycloakproxy
containerPort: 8000
containerPorts:
http: 8080
sidecars:
- name: nginxsidecar
image: nginxinc/nginx-unprivileged:1-alpine3.20-slim
imagePullPolicy: IfNotPresent
ports:
- name: nginxsidecar
containerPort: 8000
volumeMounts:
- name: keycloak-nginx-volume
mountPath: /etc/nginx/conf.d
networkPolicy:
extraIngress:
- ports:
- port: 8000
protocol: TCP

### Issuer ID url

After upgrading, the frontend URL needs to be updated, otherwise, the access token will continue returning the new issuer URL. Tokens needs to keep returning “https://keycloakdev.teqplay.nl/auth“.

### **Upgrade**

DEVELOP

helm upgrade keycloak-dev bitnami/keycloak -f values.dev.yaml --version 23.0.0

PRODUCTION

helm upgrade keycloak-dev bitnami/keycloak -f values.prod.yaml --version 23.0.0