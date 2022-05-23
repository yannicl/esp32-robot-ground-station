
import socket
from threading import Thread
import timeit
import json

localIP     = "0.0.0.0"
UDP_LOCAL_PORT   = 20935
#UDP_REMOTE_PORT   = 21935
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)


class Radio:

    def __init__(self):
        self._running = True
        self.lastColor = ""
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((localIP, UDP_LOCAL_PORT))

        print("UDP radio up and listening")
        self.lastClientAddress = ("192.168.0.220", UDP_LOCAL_PORT)

        self.udpThread = Thread(target=self.taskListeningForIncomingMessage)
        self.udpThread.start()


    def taskListeningForIncomingMessage(self):

        while(self._running):

            bytesAddressPair = self.socket.recvfrom(bufferSize)

            message = bytesAddressPair[0]

            address = bytesAddressPair[1]

            #clientMsg = "Message from Client:{}".format(message)
            #clientAddress  = "Client IP Address:{}".format(address)

            self.lastClientAddress = address
            
            try:
                messageJson = json.loads(message)
                if (messageJson and "color" in messageJson):
                    #print(messageJson["color"])
                    self.handleColor(messageJson["color"])
                else:
                    print(message)
            except Exception as err:
                print("Error: {0}".format(err))
                pass

            #print(clientMsg)
            #print(clientAddress)

            # Sending a reply to client
            #if first: 
            #    UDPServerSocket.sendto(bytesToSend, address)
            #    first = False

    def send(self, message):
        if self.lastClientAddress:
            self.socket.sendto(message, self.lastClientAddress)

    def setCommander(self, commander):
        self.commander = commander

    def handleColor(self, color):
        colorStr = ""
        brightness = color[3]
        r = color[0]
        g = color[1]
        b = color[2]
        if (brightness > 9):
            colorStr = "WHITE"
        elif (r == 0 and g == 0 and b == 0):
            colorStr = "BLACK"
        elif (r == 2 and g == 2 and b == 1):
            colorStr = "YELLOW"
        elif (r == 1 and g == 0 and b == 1):
            colorStr = "RED"
        elif (r == 0 and g == 1 and b == 1):
            colorStr = "GREEN"

        if (self.lastColor != colorStr):
            if (self.commander):
                self.commander.onColorReading(colorStr)

        self.lastColor = colorStr