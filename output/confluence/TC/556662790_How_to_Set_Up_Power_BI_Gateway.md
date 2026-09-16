---
id: confluence:556662790
source: confluence
type: page
space: TC
title: How to Set Up Power BI Gateway
author: Yaren Aslan
date: '2025-11-19'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/556662790
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/556662790
---
# How to Set Up Power BI Gateway

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/556662790  

## Content

#### Step 1: Set Up the EC2 Windows Instance

1. **Create an EC2 Windows Instance in AWS**:

   * Ensure the required security groups are configured for VPN and internet access.
2. **Access the EC2 Machine**:

   * Log in to the EC2 instance using Remote Desktop.
3. **Install ODBC Data Source Administrator**:

   * Download and install the latest version of the ODBC Data Source Administrator from [here](https://www.postgresql.org/ftp/odbc/releases/).
   * Launch the ODBC Data Source Administrator application.
4. **Configure ODBC Data Source**:

   * Navigate to the **System DNS** tab and click **Add**.
   * Select **PostgreSQL Unicode(x64)** from the list and click **Finish**.
   * Enter the database credentials and verify the connection using the **Test** button.

     + If you receive the error `FATAL: no pg_hba.conf entry for host`, change SSL Mode to allow.

Note that the name of the Data Source must be the same as the way it is defined for the dashboard.

---

#### Step 2: Install Power BI Gateway

1. **Download Power BI Gateway**:

   * Download the latest version of the Power BI Gateway from [here](https://www.microsoft.com/en-us/download/details.aspx?id=53127&msockid=122ce4bec6236e0b2b5ff1fbc75c6fc2).
2. **Install the Gateway**:

   * Run the installation file and accept the default settings.
   * Ensure the system meets the minimum requirements before proceeding.
3. **Sign In**:

   * Log in with administrator credentials.
4. **Choose Gateway Setup Option**:

   * **New Gateway**: Select **Register a new gateway on this computer** if you're setting up a new gateway.
   * **Existing Gateway**: Select **Migrate, restore, or takeover an existing gateway** if you're transferring a gateway from another system. Then click **Next**.
5. **Configure the Gateway**:

   * Enter a name for the gateway and set a **Recovery Key**.
   * Save the recovery key securely (e.g., in Bitwarden).
   * Click **Configure** to complete the setup.

---

#### Step 3: Share the Gateway with Users

1. Open the **Power BI Dashboard**.
2. Go to the **Settings** menu located in the top-left corner.
3. select Manage connections and gateway.
4. Go to On-premises data gateway tab.
5. select the one that you created.
6. On the Status column, click on refresh and make sure its online.
7. Click on the …  and then go to Manage users.
8. Share the configured gateway with the required users.
9. Make sure that the PBI refreshed are enabled via this gateway

Your Power BI Gateway setup is now complete!

See also here, to learn how to connect each powerBI datasets to gateway.