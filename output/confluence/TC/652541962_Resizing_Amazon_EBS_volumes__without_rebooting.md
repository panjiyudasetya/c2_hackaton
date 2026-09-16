---
id: confluence:652541962
source: confluence
type: page
space: TC
title: Resizing Amazon EBS volumes, without rebooting
author: Richard van Klaveren
date: '2025-03-04'
url: https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652541962
explicit_links:
- confluence:https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652541962
---
# Resizing Amazon EBS volumes, without rebooting

**Space:** TC  
**URL:** https://teqplaybv.atlassian.net/wiki/spaces/TC/pages/652541962  

## Content

## Volume resize

In the Amazon console, select the EBS volume you want to resize. Click 'Actions', 'Modify Volume', enter the new size in GB and click 'Modify'. After a while, the volume will be resized for you. When the resize is done, check the kernel log on the host to ensure that the kernel has picked up the change:

$ sudo dmesg | grep capacity
[644073.378019] Setting capacity to 1572864000
[644073.378025] xvda: detected capacity change from 536870912000 to 805306368000

## Partition resize - MBR variant

This section applies to MBR partition tables, i.e., vintage MS-DOS type partition tables ;) This is the default, and this works fine up to 2TB. If you need more than 2TB you need to use GPT partition tables. For resizing those, see below.

The next step is to increase the partition containing the file system, and then the file system itself. We're assuming a single partition here, mounted at `/`. Use the `p` command in `fdisk` to examine the current state:

$ sudo fdisk /dev/xvda
Command (m for help): p
Disk /dev/xvda: 805.3 GB, 805306368000 bytes
255 heads, 63 sectors/track, 97906 cylinders, total 1572864000 sectors
Units = sectors of 1 \* 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000
Device Boot Start End Blocks Id System
/dev/xvda1 \* 16065 1048562549 524273242+ 83 Linux

Take note of the current start of the partition. The new partition **must start at the same sector**, otherwise you will **not** have a fun day.

Use the `d` command to delete the partition, and the `n` command to create a new partition. Use partition number 1, like the existing partition, and enter the correct start sector. Use the default value for the end sector. Set the bootable flag using `a`, and then check the results using `p` to see if everything is as it should be. If fdisk asks about removing a ext4 signature, **respond with no**, otherwise you will also **not** have a fun day ;)

Command (m for help): d
Selected partition 1
Partition 1 has been deleted.
Command (m for help): n
Partition type:
p primary (0 primary, 0 extended, 4 free)
e extended
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-1572863999, default 2048):
Using default value 2048
Last sector, +sectors or +size{K,M,G} (2048-1572863999, default 1572863999):
Using default value 1572863999
Command (m for help): a
Partition number (1-4): 1
Command (m for help): p
Disk /dev/xvda: 805.3 GB, 805306368000 bytes
255 heads, 63 sectors/track, 97906 cylinders, total 1572864000 sectors
Units = sectors of 1 \* 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x00000000
Device Boot Start End Blocks Id System
/dev/xvda1 \* 16065 1572863999 786423967+ 83 Linux

Note that the partition table is identical, except for the end sector. Use `w` to write the partition table to disk. After this step, you're committed ;) `fdisk` will complain about the system not being able to re-read the partition table, this is normal, don't worry:

Command (m for help): w
The partition table has been altered!
Calling ioctl() to re-read partition table.
WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.

As it suggests, we use `partprobe` to re-read the partition table:

$ sudo partprobe

## Partition resize - GPT variant

This section applies to GPT partition tables, which can have partitions larger than 2TB in size.

The first step is to resize the partition table itself. This is because a GPT table also stores metadata at the *end* of the disk, and this data needs to be moved. The easiest way to do this is to use `parted` for this:

$ sudo parted -l
Model: Xen Virtual Block Device (xvd)
Disk /dev/xvda: 26.8GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:
Number Start End Size Type File system Flags
1 1049kB 26.8GB 26.8GB primary ext4 boot
Warning: Not all of the space available to /dev/xvdg appears to be used, you can
fix the GPT to use all of the space (an extra 419430400 blocks) or continue with
the current setting?
Fix/Ignore? Fix <<<<<<<<<<<<< Answer with "Fix" here to let parted do it's thing <<<<<<<<<<<<<<<<
Model: Xen Virtual Block Device (xvd)
Disk /dev/xvdg: 1503GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:
Number Start End Size File system Name Flags
1 17.4kB 1288GB 1288GB ext4

As shown above, `parted` discovers the problem on `/dev/xvdg` in this case, and prompts whether you want to have it fixed. Answer `Fix` to make it do so.

Next, we will use `gdisk` to perform the partition resize. Depending on what/who created the partition, you might run into some alignment issue, examine the start sector of the new partition *carefully* to see if gdisk has not decided to change it for you. In this case, enter the expert menu with `x` and use `l` to change the alignment value. In the example I changed it to `2`.

First, examine the existing partition, and remove it:

$ sudo gdisk /dev/xvdg
GPT fdisk (gdisk) version 1.0.3
Partition table scan:
MBR: protective
BSD: not present
APM: not present
GPT: present
Found valid GPT with protective MBR; using GPT.
Command (? for help): p
Disk /dev/xvdg: 2936012800 sectors, 1.4 TiB
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 269B06AE-966C-43BA-8E64-1AE74EB9B224
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 2936012766
Partitions will be aligned on 8-sector boundaries
Total free space is 419430400 sectors (200.0 GiB)
Number Start (sector) End (sector) Size Code Name
1 34 2516582366 1.2 TiB 8300
Command (? for help): d
Using 1

Then, create the new partition using identical values, and inspect the result:

Command (? for help): n
Partition number (1-128, default 1): 1
First sector (34-2936012766, default = 40) or {+-}size{KMGTP}: 34
Information: Moved requested sector from 34 to 40 in
order to align on 8-sector boundaries.
Use 'l' on the experts' menu to adjust alignment
Last sector (40-2936012766, default = 2936012766) or {+-}size{KMGTP}:
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300):
Changed type of partition to 'Linux filesystem'
Command (? for help): p
Disk /dev/xvdg: 2936012800 sectors, 1.4 TiB
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 269B06AE-966C-43BA-8E64-1AE74EB9B224
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 2936012766
Partitions will be aligned on 8-sector boundaries
Total free space is 6 sectors (3.0 KiB)
Number Start (sector) End (sector) Size Code Name
1 40 2936012766 1.4 TiB 8300 Linux filesystem

Observe that the start sector has been changed to 40! Not good. Remove it, set alignment, and try again:

Command (? for help): d
Using 1
Command (? for help): x
Expert command (? for help): l
Enter the sector alignment value (1-65536, default = 2048): 2
Expert command (? for help): m
Command (? for help): n
Partition number (1-128, default 1): 1
First sector (34-2936012766, default = 34) or {+-}size{KMGTP}: 34
Last sector (34-2936012766, default = 2936012766) or {+-}size{KMGTP}:
Current type is 'Linux filesystem'
Hex code or GUID (L to show codes, Enter = 8300):
Changed type of partition to 'Linux filesystem'
Command (? for help): p
Disk /dev/xvdg: 2936012800 sectors, 1.4 TiB
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): 269B06AE-966C-43BA-8E64-1AE74EB9B224
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 2936012766
Partitions will be aligned on 2-sector boundaries
Total free space is 0 sectors (0 bytes)
Number Start (sector) End (sector) Size Code Name
1 34 2936012766 1.4 TiB 8300 Linux filesystem
Command (? for help): w
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!
Do you want to proceed? (Y/N): y
OK; writing new GUID partition table (GPT) to /dev/xvdg.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot or after you
run partprobe(8) or kpartx(8)
The operation has completed successfully.

Now, the start sector is identical to the original sector, meaning that everything will work as expected. As it suggests, we use `partprobe` to re-read the partition table:

$ sudo partprobe

## Filesystem resize

Now, we can resize the filesystem itself:

$ sudo resize2fs /dev/xvda1
resize2fs 1.42.9 (4-Feb-2014)
Filesystem at /dev/xvda1 is mounted on /; on-line resizing required
old\_desc\_blocks = 32, new\_desc\_blocks = 47
The filesystem on /dev/xvda1 is now 196605991 blocks long.

To verify, check with `df` that the amount of free space has indeed been increased:

$ df -ht ext4
Filesystem Size Used Avail Use% Mounted on
/dev/xvda1 739G 257G 452G 37% /