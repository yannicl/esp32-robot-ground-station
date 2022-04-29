
import socket
from threading import Thread

localIP     = "0.0.0.0"
UDP_LOCAL_PORT   = 20935
#UDP_REMOTE_PORT   = 21935
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)


class Radio:

    def __init__(self):
        self._running = True
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((localIP, UDP_LOCAL_PORT))

        print("UDP radio up and listening")
        self.lastClientAddress = False

        self.udpThread = Thread(target=self.taskListeningForIncomingMessage)
        self.udpThread.start()


    def taskListeningForIncomingMessage(self):

        while(self._running):

            bytesAddressPair = self.socket.recvfrom(bufferSize)

            message = bytesAddressPair[0]

            address = bytesAddressPair[1]

            clientMsg = "Message from Client:{}".format(message)
            clientAddress  = "Client IP Address:{}".format(address)

            self.lastClientAddress = address
            
            print(clientMsg)
            print(clientAddress)

            # Sending a reply to client
            #if first: 
            #    UDPServerSocket.sendto(bytesToSend, address)
            #    first = False

    def send(self, message):
        if self.lastClientAddress:
            self.socket.sendto(message, self.lastClientAddress)