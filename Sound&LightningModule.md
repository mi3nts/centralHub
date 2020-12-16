# Sound and Lightning Module

## DFRobot Analog Sound Level Meter (SEN0232:)

#### The SEN0232 from DFRobot is a sensor that can accurately measure the sound levels of it's surrounding enviornment.
#### It is a plug and play that uses a low noise microphone.

### Sensor Specifications:

<img src="https://dfimg.dfrobot.com//data/SEN0232/SEN0232-6W4A9955.jpg?imageView2/1/w/564/h/376" width="500" height="310">

Dimensions: 60mm x 43mm 

Measurement Range: 30dBA ~ 130dBA 

Input Voltage: 3.3 ~ 5.0V 

Output Voltage: 0.6 ~ 2.6V 

### Board Overview:

<img src="https://raw.githubusercontent.com/DFRobot/DFRobotMediaWikiImage/master/Image/SoundLevelMeterBoardConnector.png" width="388" height="275">


Number | Label | Description |
----------- | ----- | -------- |
1 | A | Analog Signal Output (0.6~2.6V) |
2 | + | Power VCC (3.3~5.0V) |
3 | - | Power GND (0V) | 



## DFRobot Lightning Distance Sensor (SEN0290:)

#### This sensor uses AMS AS3935 Franklin lightning sensor IC and Coilcraft's MA5532-AE antenna to examine lightning distance, intensity, and frequency both indoors or outdoors.

### Sensor Specifications:
<img src="https://dfimg.dfrobot.com//data/SEN0290/SEN0290.jpg?imageView2/1/w/564/h/376" width="400" height="240">

Dimensions: 30.0mm x 22.0mm

Input Voltage: 3.3V ~ 5.5V

Maximum Detection Range: 40 km

Distance Detection Resolution: 1 ~ 4 km

Intensity Detection Resolution: 21 bits

Interface: Gravity I2C (Addresses: 0x03, 0x02, 0x01)

### Board Overview:

<img src="https://raw.githubusercontent.com/DFRobot/Wiki/SEN0290/DFRobot_SEN0290/image/SEN0290_overview.png" width="400" height="267">

Number | Label | Description |
----------- | ----- | -------- |
1 | VCC | Power VCC（3.3 ~ 5.5V） |
2 | GND | Power GND |
3 | SCL | I2C clock signal | 
4 | SDA | I2C data signal |
5 | ADDR | I2C address DIP switch |
6 | IRQ | Lightning alarm interrupt pin |
7 | PWR | Power indicator (red) | 



## Pro Audio External Lavalier Microphone (DP-LM20GP:)

#### The Pro Audio External Lavalier Microphone is a high quality mic that's ideal for video use. It even comes with a lapel clip to connect onto objects easily, as well as a foam windscreen to keep out unwanted noise. 

### Microphone Specifications:
<img src="https://cdn.shopify.com/s/files/1/0260/8948/8444/products/dp-lm20gp_540x.png?v=1564762192">

Frequency Range: 35Hz ~ 18KHz 

Sensitivity: -30dB +/-3dB / 0dB=1V/Pa, 1kHz

Cable length: Microphone: 1.2m

Mic Adapter: 11cm

Connector: Mini USB plug

## Assembly
### Materials Needed
* 3-D Printed Base
* 3-D Printed "I" Stand
* M3 Screws, Washers, and Nuts
* M5 Screws, Washers, and Screw-On Tabs
* M3 Spacers
* Metal Stand
* Sound and Lighting Protection Cube
* PG7s and PG9s
* DFRobot Analog Sound Level Meter
* DFRobot Lightning Distance Sensor
* Audino Base
* 1/4 inch Drill Bit
* 1/2 inch Spade Bit
* 5/8 insh Spade Bit

### Step 1

Take your 3-D Printed Base and attach the DFRobot Analog Sound Level Meter as shown below uswing M3 Screws, Washers, and Nuts. Make sure your screws are oriented correctly to ensure your sensor will fit in the Protective Cube.

<img src="https://drive.google.com/uc?export=view&id=16hcOdLom1ZOnJx4oCnghUC_kzMpiftju" width="262" height="225"/> <img src="https://drive.google.com/uc?export=view&id=1dNmhgkILELsR8finxkSXPTyehYhdaiLL" width="262" height="225"/> <img src="https://drive.google.com/uc?export=view&id=1Nvcusx4DL2SgWKDgUutua8wzZCXe41FH" width="262" height="225"/>

### Step 2

Flip the enitre thing over, then attach the Audino Base using M3 Screws, Washers, and Nuts as shown below. Make sure your screws are oriented correctly to ensure your sensor will fit in the Protective Cube.

<img src="https://drive.google.com/uc?export=view&id=1OwqXUEIF22hA17F2CdsVUnWghXUXyF8v" width="262" height="225"/><img src="https://drive.google.com/uc?export=view&id=1a9Yn_72ZSQhyXEUABEgW5Uo3IkGmAZIx" width="262" height="225"/><img src="https://drive.google.com/uc?export=view&id=1xTwCKDjK6G4ofytVibjVACVc6W5skC5P" width="262" height="225"/>

### Step 3

Attach the 3-D Printed I stand to the 3-D Printed Base as shown in the image using M3 Screws, Washers, and Nuts. Make sure your screws are oriented correctly to ensure your sensor will fit in the Protective Cube.
<img src="https://drive.google.com/uc?export=view&id=1ObR1M-KjYW1ZzrN6zFnW26-wdjFLgd4s" width="262" height="225"/><img src="https://drive.google.com/uc?export=view&id=1j1mXqVR8ciDzvledHoYNqa2g9mgY46kN" width="262" height="225"/><img src="https://drive.google.com/uc?export=view&id=1c3wocuKA3Z1uKOVvge1e0s_y3z15RWnO" width="262" height="225"/>


### Step 4

Attach the DFRobot Lightning Distance Sensor to the top of the I stand as shown in the image using M3 Screws, Washers, and Nuts. Make sure your screws are oriented correctly to ensure your sensor will fit in the Protective Cube.
***Insert Inage Here***

### Step 5

Set your sensor aside and grab your Protective Cube. Orient the cube as shown in the image below.
***insert image here***

### Step 6

Drill 2 holes as shown using the 1/4 inch drill bit, 3 holes as shown using the 1/2 inch spade bit, and one hole as shown using the 5/8 inch spade bit
***insert image here***

### Step 7

Place PG7s in the 1/2 inch spade holes, and a PG9 in the single 5/8 inch spade hole as shown in the images below
***insert image here***

### Step 8

Put the M5 screw and washer in the 1/4 inch holes inside the cube, and put the screw-on tab on the outside of the cube
***insert image here***

### Step 9

Orient the tabs so that they are veritcal and parallel to eachother, and slide the metal stand onto the tabs as shown in the image below
***insert image here***

### Step 10

Take the sensor, and insert M3 screws into the corner holes of the base as shown in the image below. Then, you put the M3 spacers on the screws as shown in the image below. Hot glue the spacers to the 3-D Printed base after the spacers are in place
***insert imagem here***

### Step 11

Place Sensor in Protective Cube, and screw the M3 screws with M3 spacers into the holes provided inside the cube
***insert image here***
