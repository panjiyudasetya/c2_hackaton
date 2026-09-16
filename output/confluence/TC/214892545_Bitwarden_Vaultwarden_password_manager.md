---
id: confluence:214892545
source: confluence
type: page
space: TC
title: Bitwarden/Vaultwarden password manager
author: Michel Wilson
date: '2023-09-25'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214892545
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214892545
---
# Bitwarden/Vaultwarden password manager

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/214892545  

## Content

We use Bitwarden (the client) combined with Vaultwarden (the open-source backend variant) to manage all credentials within Teqplay. To access the credentials, an admin will send you an invite e-mail and grant you access to the collections associated with the projects/tasks you are participating in.

## Creating an account

When clicking the “Join Organization Now” button you will be redirected to the web vault to either login or to create an account. Since you don’t have an account yet, pick the “Create account” option. Fill in your name, and select a master password. Ideally this should be a pass*phrase*, so something really long that’s still easy to remember. Optionally you can include a hint, but be careful with the content of the hint  Note that if you forget your master password all your personal credentials will be lost. There is no password reset option, and no recovery option.

Next, login to the web vault using the master password you just selected. This will also cause the invitation to be accepted. Before you will actually see all the shared credentials however, your account still needs to be confirmed by an admin.

The last required step is to enable two-factor authentication for your account. For this you need to have a two-factor app on your phone. In the profile menu in the top-right corner (click the circle with your initials), go to “Account settings”, and then “Security”. Open the “Two-step login” tab, and click on “Manage” in the “Authenticator app” entry. Enter your master password again, and then scan the provided QR code with your authenticator app. Enter a verification code, and click “Turn on”.

For extra security, it is highly recommended to store the recovery code somewhere save. One good option would be to store the recovery code in your personal password manager. This code is a backup option that ensures you can login to your account if you lose your device containing the authenticator app.

## Browser add-on, mobile app

For ease of use it is highly recommended to install the Bitwarden browser add-on. You should be able to find it by searching for Bitwarden in the add-on store of your favourite browser, or by going to the [download page](https://bitwarden.com/download/) of Bitwarden.

When logging in to the add-on, be sure to first select the “Self-hosted” option under the e-mail address input box. The server URL to use is <https://vault.teqplay.nl>, all the other URLs can be left empty.

The exact same procedure can be used for the mobile app. Note that it is possible to have multiple accounts in the mobile app, it’s easy to switch between them: click on the circle with your initials to add a new account or to switch between accounts.

## Adding credentials

Adding new credentials should be pretty straightforward. Some important notes:

* When adding a URL, in some cases (when adding something.teqplay.nl/something.teqplay.com accounts in particular) it is very important and convenient to set the matching strategy to “host” instead of to “default”. This ensures that the account is only shown when going to something.teqplay.nl, and not when going to anything.teqplay.nl.
* If credentials are used on multiple websites, or in an app and on a website, please add a second URL to the existing credentials, and please do not add a copy of the same credentials with a different URL!

## Data migration

If you want to migrate your LastPass data, this is possible using the export/import functionality. Some care is needed however to only import your personal data, as all shared items have already been migrated!

To start, you need to export your LastPass vault. Go to “Advanced Options” in LastPass, select “Export”, and you should receive a validation mail. Click on the link in the mail, and then click “Export” again. It should ask for your master password again, and after that you will be able to download a `.csv` file containing the contents of your vault.

Next, open the `.csv` file in a spreadsheet program (OpenOffice works fine), and filter out the shared item. In OpenOffice, the AutoFilter option works really well (Ctrl-Shift-L), use this to deselect any shared item categories in the `grouping` column. Copy the filtered items, paste them in a new sheet, and save this sheet as a `.csv` file.

Finally you can import this data in Bitwarden. To do this, go to the Web Vault (<https://vault.teqplay.nl>), open the “Tools” tab and go to “Import data”. Pick “LastPass (csv)” in the drop down, and use the “Choose File” button to pick the `.csv` file you just saved.