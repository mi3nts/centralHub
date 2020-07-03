# Lora Module 

## Setting up the External hard drive

- Checking if the HD is connected 
```
sudo apt-get install lshw
sudo lshw -class disk -short 
```
Output should look like this.
```
H/W path        Device     Class      Description
=================================================
/1/1/5/0.0.0    /dev/sda   disk       1TB My Passport 25E1
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

## Registering Lora Nodes

On your browser type in the ip address of the Lora Gateway(Rasberry Pi) 

Then go to the application tab and create an application under the credentials given below
![Lora Register](res/lora.png)

Under the application created click on the table icon. Here you can register your Lora Nodes. 
![Lora Register 2](res/lora2.png)

# Jetson 
## insatall Dependancies
```
sudo apt-get install screen
sudo apt-get install python3-pip
sudo pip3 install getmac
sudo pip3 install pyserial
sudo pip3 install netifaces
sudo pip3 install pynmea2
```
## Edit crontab with Nano 
export VISUAL=nano; crontab -e

# Adding nano previlegges  




# Pi 
## insatall Dependancies
```
sudo apt-get install screen
sudo apt-get install python3-pip
sudo pip3 install getmac
sudo pip3 install pyserial
sudo pip3 install netifaces
sudo pip3 install pynmea2
```
## Edit crontab with Nano 
export VISUAL=nano; crontab -e

# Jetson 
```
sudo adduser $USER dialout
sudo adduser $USER tty
sudo apt-get install screen
sudo apt-get install python3-pip
sudo pip3 install getmac
sudo pip3 install pyserial
sudo pip3 install netifaces
sudo pip3 install pynmea2
```

## Crontab 
```
@reboot cd /home/teamlary/gitHubRepos/centralHub/firmware/jetson && ./runAll.sh 
* * * * * rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw
*/2 * * * * cd /home/teamlary/gitHubRepos/centralHub/firmware/jetson && python3 skyCamReaderWithSave.py
2,4,6,8,12,14,16,18,22,24,26,28,32,34,36,38,42,44,46,48,52,54,56,58 * * * * cd /home/teamlary/gitHubRepos/CentralHub/firmware/jetson && python3 skyCamReaderNoSave.py
*/5 * * * * cd /home/teamlary/gitHubRepos/centralHub/firmware/jetson && python3 deleter.py
```
--
## LoRaWAN Gatewey:

This kit provides all the basic tools needed to collect and transfer data among all your LoRa nodes.

### Parts List:

Parts | Quantity | Details |
----------- | ----- | ----- |
Raspberry Pi 3 | 1 | https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-Model-Bplus-Product-Brief.pdf |
Seeeduino LoRaWAN with GPS | 1 | https://wiki.seeedstudio.com/Seeeduino_LoRAWAN/ |
Gateway module RHF0M301 – 868 | 1 | - |
PRI 2 Bridge RHF4T002 | 1 | -|
8GB Micro SD Card – Class 10 | 1 | - |
USB to UART Adapter | 1 | - |
0dBi Rubber Duck Antenna | 1 | - |
Micro USB Cable 20cm | 1 | - |
Micro USB Cable 100cm | 1 | - |
RJ45 Ethernet Cable 100cm | 1 | - |
5V/2.1A American Standard Adapter with Micro USB Connector | 1 | - |
