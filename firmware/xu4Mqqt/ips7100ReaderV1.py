#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import sys

dataFolder  = mD.dataFolder
ipsPort     = mD.ipsPort
baudRate    = 115200

def main():
    ser = serial.Serial(
    port= nanoPorts[portNum],\
    baudrate=baudRate,\
    parity  =serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

    print(" ")
    print("Connected to: " + ser.portstr)
    print(" ")

        #this will store the line
    line = []

    while True:
        try:
            for c in ser.read():
                line.append(chr(c))
                if chr(c) == '\n:
                    dataString     = (''.join(line))
                    dataStringPost = dataString.replace('\n', '')
                    print("================")
                    print(dataStringPost)
                    # mSR.dataSplit(dataStringPost,datetime.datetime.now())
                    line = []
                    break
        except:
            print("Incomplete String Read")
            line = []
    ser.close()


if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    print("Monitoring IPS7100 on port: {0}".format(ipsPort) + " with baudrate " + str(baudRate))
    