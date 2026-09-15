---
id: confluence:148078597
source: confluence
type: page
space: TC
title: EKS cluster backup & restore
author: Darius Wattimena
date: '2023-06-14'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/148078597
explicit_links: []
---
# EKS cluster backup & restore

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/148078597  

## Content

## Prepare your system

1. Install the Kubernetes CLI (`kubectl`) if you don’t have it.

   * Follow <https://kubernetes.io/docs/tasks/tools/>
2. Install the Velero CLI with one of the following options:

   * Windows: `choco install velero`
   * Get the tarball via GitHub → <https://github.com/vmware-tanzu/velero/releases>
   * Follow the instructions on their website → <https://velero.io/docs/v1.9/basic-install/#install-the-cli>

---

## Set up the backup mechanism on the cluster

Execute the following steps only if you want to put the backups in a new s3 bucket:

1. If you need a new S3 bucket where the backups will be saved.

   aws s3api create-bucket --bucket <BUCKET\_NAME> --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
2. If you add a new bucket, change the AWS IAM policy for the Velero user.

   * Check if the bucket is already on the `s3_eks_backups` policy.
   * If not, add it to the two statements that need it.

     "arn:aws:s3:::<BUCKET\_NAME>/\*"

     and

     "arn:aws:s3:::<BUCKET\_NAME>"

Setting up the backup:

1. Install Velero in the cluster.

   * Execute the install step. (This will install resources on the cluster and spin up a pod)

     velero install --kubecontext <CLUSTER> --provider aws --plugins velero/velero-plugin-for-aws:v1.4.0 --bucket <BUCKET\_NAME> --backup-location-config region=eu-west-1 --snapshot-location-config region=eu-west-1 --secret-file .\credentials-velero
     + `--kubecontext` is followed by the alias of the cluster
     + `--bucket` is followed by the name of the bucket we just created.
     + `--secret-file` is followed by a file that contains the following structure

       [default]
       aws\_access\_key\_id=
       aws\_secret\_access\_key=

       Check LastPass for the needed access key and secret.
2. Create backup schedules

   * Daily schedule, keeping 7 days of data, running 3 am every day.

     velero schedule create daily-schedule --schedule="0 3 \* \* \*" --ttl 168h0m0s --kubecontext <CLUSTER>
   * Weekly schedule, keeping 8 weeks of data, running 4 am on Saturday.

     velero schedule create weekly-schedule --schedule="0 4 \* \* 6" --ttl 1344h0m0s --kubecontext <CLUSTER>
   * Monthly schedule, keeping 1 year of data, running at 5 am the 1st of the month.

     velero schedule create monthly-schedule --schedule="0 5 1 \* \*" --ttl 8760h0m0s --kubecontext <CLUSTER>

Now everything should be set up. To test out your backup mechanism, you can execute:

velero backup create --from-schedule daily-schedule --kubecontext <CLUSTER>

This will use the settings of the `daily-schedule` and create the needed backup. The result will be saved in the S3 bucket you specified.

---

## Restore a backup

velero restore create --from-backup <BACKUP\_NAME> --kubecontext <CLUSTER>

* Here the name of the backup contains `<SCHEDULE_NAME>-<CREATION_TIMESTAMP>,` for example, `daily-schedule-20221025125024`. You can also check the S3 bucket where this backup is stored.

## Partially restore a backup

This is basically the same command as restoring a backup with the exception that either:

* When we created our backup we specified which resources we wanted to include in this backup. This means that we can just follow the backup command we specified above.
* While restoring, we provide the resources we want to include in the restore.

For options, see:

* <https://velero.io/docs/v1.9/restore-reference/>
* velero restore create --help

## Creating a new cluster in case of an infrastructure failure

1. Create a new EKS cluster via the AWS interface. (This takes around 10+ minutes)
2. Create a node group of the amount of EC2 machines you need to run everything from your backup. This can be upped later if not enough.
3. Connecting to the new EKS cluster:

   aws eks update-kubeconfig --name <CLUSTER> --alias <CLUSTER>

   **NOTE: We don’t provide a role.** Nothing is set up when you create the cluster, so the role isn’t allowed. Next to this, we already have full access because we created the cluster.
4. Install Velero in the cluster.

   * Execute the install step. (This will install resources on the cluster and spin up a pod)

     velero install --kubecontext <CLUSTER> --provider aws --plugins velero/velero-plugin-for-aws:v1.4.0 --bucket <BUCKET\_NAME> --backup-location-config region=eu-west-1 --snapshot-location-config region=eu-west-1 --secret-file .\credentials-velero
     + `--kubecontext` is followed by the alias of the cluster we specified in the step before
     + `--bucket` is followed by the name of the bucket we just created.
     + `--secret-file` is followed by a file that contains the following structure

       [default]
       aws\_access\_key\_id=
       aws\_secret\_access\_key=

       Check LastPass for the needed access key and secret.
5. Restore the backup.

   velero restore create --from-backup <BACKUP\_NAME> --kubecontext <CLUSTER>
   * Here the name of the backup contains `<SCHEDULE_NAME>-<CREATION_TIMESTAMP>,` for example, `daily-schedule-20221025125024`.
   * We provide `--kubecontext` followed by the cluster name to avoid accidentally restoring a backup on the wrong cluster*.*

---

## Troubleshooting

Some general commands for troubleshooting that may be helpful:

* `velero backup describe <BACKUP_NAME>` - describe the details of a backup.
* `velero backup logs <BACKUP_NAME>` - fetch the logs for this specific backup. Useful for viewing failures and warnings, including resources that could not be backed up.
* `velero restore describe <RESTORE_NAME>` - describe the details of a restore
* `velero restore logs <RESTORE_NAME>` - fetch the logs for this specific restore. Useful for viewing failures and warnings, including resources that could not be restored.

More info, see <https://velero.io/docs/v1.3.2/troubleshooting/>

### What to do when a backup fails

1. Find the backup that failed.

   1. Via Lens, open the `Custom Resources` section
   2. Open `velero.io`
   3. Open `Backup`
   4. Copy the name of the backup that you think failed.
2. Call `velero backup describe <BACKUP_NAME>`, which will tell you if the backup succeeded.  
   An example response will contain the following lines indicating that something went wrong:

   Phase: PartiallyFailed (run `velero backup logs daily-schedule-20230614030033` for more information)
   Errors: 1
   Warnings: 0

   Or as follows when everything went well:

   Phase: Completed
   Errors: 0
   Warnings: 0
3. Once we found our backup that failed, searching the logs would be the next step. Execute `velero backup logs <BACKUP_NAME>`. It is highly suggested to filter on `level=error`.

   1. This can be achieved for Windows by running `velero backup logs <BACKUP_NAME> | Select-String "level=error"` in PowerShell.

#### Common backup issues that occur:

* The volume is deleted on the side of AWS, but the Persistent Volume Claim (PVC) and/or Persistent Volume (PV) still exist in the Kubernetes cluster.  
  This will result in the following log line:

  time="2023-06-14T03:00:51Z" level=error msg="Error backing up item" backup=velero/daily-schedule-20230614030033 error="error getting volume info: rpc error: code = Unknown desc = InvalidVolume.NotFound: The volume 'vol-0aba9a017cd317440' does not exist.\n\tstatus code: 400, requ
  est id: 7e47c204-9fad-48c5-9450-b7126c8cc283" logSource="pkg/backup/backup.go:417" name=datadir-mongodb-trangdev-0

  Please make sure the PVC is not used by anything. If this is the case, deleting the PVC and PV will resolve this issue on the next backup.