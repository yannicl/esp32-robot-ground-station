import socket
from radio import Radio

class Vehicle:

    def __init__(self, radio: Radio):
        self.radio = radio

    def forward(self):
        msgFromServer       = '{"motorA": 32767}'
        bytesToSend         = str.encode(msgFromServer)
        self.radio.send(bytesToSend)

