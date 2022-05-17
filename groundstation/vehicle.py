import socket
from radio import Radio

class Vehicle:

    def __init__(self, radio: Radio):
        self.radio = radio

    def setMotors(self, motorA: float, motorB: float):
        motorAInt = int(motorA * 90)
        motorBInt = int(motorB * 90)
        msgFromServer       = '{"motorA": ' + str(motorAInt) + ',"motorB": ' + str(motorBInt) + '}'
        bytesToSend         = str.encode(msgFromServer)
        self.radio.send(bytesToSend)

