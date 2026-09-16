---
id: confluence:1055293441
source: confluence
type: page
space: TC
title: Allure Reports in Cronjob
author: Francisco Jose Muros Muriano (Unlicensed)
date: '2025-12-18'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055293441
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055293441
---
# Allure Reports in Cronjob

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/1055293441  

## Content

This is the last step to do in order to be able to see the reports, there are two options for this, github pages or S3 bucket.

For github pages, something like this should work

wide760git config user.name "api-tests-bot"
git config user.email "ci@teqplay.nl"
git fetch origin
git checkout gh-pages || git checkout -b gh-pages
rm -rf \*
cp -r build/reports/allure-report/\* .
git add .
git commit -m "Allure report $(date '+%Y-%m-%d %H:%M')" || true
git push https://$TOKEN@github.com/teqplay/api-tests.git gh-pages

For S3 bucket

wide760aws s3 sync build/reports/allure-report s3://"BUCKET"/allure-reports/$(date +%F) --delete