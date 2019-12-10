
#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import time
import sys

dataFolder    = mD.dataFolder
sabrentPorts  = mD.sabrentPorts
lookingForSensor = True
waitTime      = 10

def findSensor(serIn):
    startTime = time.time()
    while lookingForSensor:
        elapsedTime = time.time()-startTime

        for c in serIn.read():
            if chr(c) == '$':
                print("AirMarFound")
                return "airMar"

        if (elapsedTime)>waitTime :
            print("AirMarNotFound")
            return("ozone")


def main(portNum):

    if(len(sabrentPorts)>0):


        ser = serial.Serial(
        port= sabrentPorts[portNum],\
        baudrate = 4800,\
        parity   = serial.PARITY_NONE,\
        stopbits = serial.STOPBITS_ONE,\
        bytesize = serial.EIGHTBITS,\
        timeout=0)

        print("connected to: " + ser.portstr)

        sensor = findSensor(ser)

        print(sensor)

        if sensor == "airMar":
            ser.baudrate = 4800
            line = []
            while True:
                try:
                    for c in ser.read():
                        line.append(chr(c))
                        # print(chr(c))
                        if chr(c) == '\n':
                            dataString     = (''.join(line))
                            dataStringPost = dataString.replace('~', '')
                            print(dataStringPost)
                            # mSR.dataSplit(dataStringPost,datetime.datetime.now())
                            line = []
                            break
                except:
                    print("Incomplete String Read")
                    line = []

        if sensor == "ozone":

            ser.baudrate = 2400
            line = []
            while True:
                try:
                    for c in ser.read():
                        line.append(chr(c))
                        # print(chr(c))
                        if chr(c) == '\n':
                            dataString     = (''.join(line))
                            print(dataString)
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
    portNum = int(sys.argv[1])
    print("Number of Sabrent Devices: {0}".format(len(sabrentPorts)))
    print("Monitoring Sabrent Device on port: {0}".format(sabrentPorts[portNum]))
    main(portNum)
