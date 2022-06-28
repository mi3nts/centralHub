# CentralHub
![central Hub](https://github.com/mi3nts/centralHub/blob/master/res/centralHub.png)
</br>
</br>
The Central hub contains the following modules and it acts as the central data center for [LoRa packages](https://github.com/mi3nts/loRaNode) located near by. 

## Air Module 
 - Weather Shield
 - OPCN3  
 - SCD30  
 - HM3301 
 - BME280 
 - MGS001 
  
 ## Light Module 
- Camera                    
- GUVA-S12SD                
- Grove - Light Sensor v1.2 
- TSL2591                     
- VEML6075                  
- AS7262                    
- TMG3993                   
- APDS-9002                 
- Si1145                    

## Sound and Lightning Module 
- USB Mic:                    
- USB Sound Car Sabrent       
- Gravity Sound Level Monitor  
- Gravity Lightning Sensor 
- In this repository the firmware contains a Python script built on BirdNET (https://github.com/kahst/BirdNET-Analyzer) which can identify birds based on their sound.
- Create a virtual environment with the name birdsongs and install the required packages. 

  ```
  sudo apt-get install python3-venv
  python3 -m venv birdSongs
  source birdSongs/bin/activate
  sudo apt-get install build-essential libssl-dev libffi-dev python-dev
  pip3 install sounddevice
  pip3 install scipy
  pip3 install -U pip setuptools
  pip3  install pandas
  pip3 install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime
  sudo apt-get install llvm-10 lldb-10 llvm-10-dev libllvm10 llvm-10-runtime
  sudo update-alternatives --install /usr/bin/llvm-config llvm-config /usr/bin/llvm-config-10 10
  sudo update-alternatives --config llvm-config
  pip3 install llvmlite==0.35.0
  pip3 install librosa==0.9.1
  ```
 - Install the following packages to deal with the data through MQTT
  
  ```
  pip3 install pyserial
  pip3 install paho-mqtt
  pip3 install pyyaml==5.4.1
  pip3 install getmac
  pip3 install pynmea2
  pip3 install netifaces
  
  ```

## Main Module
- XU4  
- Radiation Sensor   
- USB Hub
- SD Card

## Lora Module 
- Rasberry Pi with LoRa 
- Jetson Nano 
- 5 port switch

## Power Module 
- 24 V power pack
- 5 v step down  
- 12 v step down 
- Power inlet 
- Plug

