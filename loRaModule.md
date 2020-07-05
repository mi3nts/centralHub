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

## LoRaWAN Gatewey:

This kit provides all the basic tools needed to collect and transfer data among all your LoRa nodes.

<img src="https://static-cdn.seeedstudio.site/media/catalog/product/cache/9d0ce51a71ce6a79dfa2a98d65a0f0bd/h/t/httpsstatics3.seeedstudio.comseeedimg2017-04npjxt95kqxosd6stvkza0prn.jpg" width="370" height="275">

Dimensions: 200mm x 130mm x 50mm

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

## Jetson Nano Developer Kit:

NVIDIA® Jetson Nano™ Developer Kit is a computer that lets you run multiple neural networks side by side for applications like image classification, object detection, segmentation, and speech processing.

CPU: Quad-core ARM A57 @ 1.43 GHz

#### Items Included:

-Jetson Nano Developer Kit

-Small paper card with quick start and support information

-Folded paper stand

<img src="https://developer.nvidia.com/sites/default/files/akamai/embedded/images/jetsonNano/JetsonNano-DevKit_Front-Top_Right_trimmed.jpg" width="316" height="257">


## WD 1TB Portable External Hard Drive: 

WD External HD is a portable harddrive in which you can store massive amounts of files, inculding photos, videos, and music.

<img src="https://images-na.ssl-images-amazon.com/images/I/818%2BOzCMXlL._AC_SL1500_.jpg" width="300" height="200">

Interface: USB 3.0/2.0

Dimensions: 4.33in x 3.21in x 0.64in

## WIWAV 5 Port Switch:

WIWAV's 5-Port Switch is a low power consumption device that series up to 5 Ethernet devices for critical applications in hazardous environments, such as smart traffic, factory automation, and outdoor access connection for video surveillance / FTTx and Wi-Fi coverage.

<img src="https://images-na.ssl-images-amazon.com/images/I/71xmV9A56uL._SL1500_.jpg" width="316" height="316">

Interface: 5 x RJ45

Transmission Speed: 10/100Mbps

Dimensions: 28mm x 118mm x 89mm

Range of Operating Temperatures: -30°C ~ +75°C
