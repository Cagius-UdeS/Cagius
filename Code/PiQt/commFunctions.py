import serial
import json


class SerialComm:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.serial = serial.Serial(port, baud, timeout=1)
        print('Init serial port')


    def sendMsg(self, message):
        #j = (json.dumps(JSon)+'\n').encode()
        self.serial.write(message)


    def readMsg(self):
        received_data = self.serial.read() 
        print(received_data)
        #return json.loads(rawJSon)


    def isMessageAvailable(self):
        return self.serial.in_waiting > 0


class MessageIO:


    def __init__(self):
        self.devices = []


    def addDevice(self, dev):
        self.devices.append(dev)
        print('Adding device')

    def sendMessage(self,deviceIndex,msg):
        #print('Sending message')
        self.devices[deviceIndex].sendMsg(msg)

    def readMessage(self, deviceIndex):
        dev = self.devices[deviceIndex]

        if dev.isMessageAvailable():
            #print('Message available')
            try:
                #print('Message read')
                print(dev.readMsg())
            except:
                #print('Message not read')
                return None
        else:
            #print('no message')
            return None
