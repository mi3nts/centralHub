
#### Setting up the External hard drive

- Checking if the HD is connected 
```
sudo apt-get install lshw
sudo lshw -class disk -short 
```
Be sure the hard drive you want to use is formatted in the **_ext4_** filesystem. 

- Mounting the HD
```
sudo su
mount /dev/sda1 /mnt
```

- Transfer your root partition to the new drive:
```
sudo rsync -axv / /mnt
cp /boot/cmdline.txt /boot/cmdline.txt.bak
nano /boot/cmdline.txt

```
- Change the lines as follows:

```
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/sda1 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait rootdelay=5
```
- Chnaging the Boot Order 
```
nano /mnt/etc/fstab
```
Then add the following line:
```
/dev/sda1       /               ext4    defaults,noatime  0       1
```
Make sure to get the spacing right 

Comment the SD Boot 
```
#/dev/mmcblk0p7  /               ext4    defaults,noatime  0       1

```

Then restart the system.
