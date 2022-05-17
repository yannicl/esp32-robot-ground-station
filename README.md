# esp32-robot-ground-station

## Local dev
Simulate vehicle sending data and receving order
``` nc -u 127.0.0.1 20935

Debug vehicle
echo -n '{"motorA": 10000, "motorB": -10000}' > /dev/udp/0.0.0.0/20935



from machine import Pin, SoftI2C
import time
import json
from app.radio import Radio
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
i2c.scan()
from app.goplus2 import GoPlus2
motor = GoPlus2(i2c)
motor.writeMotorASpeed(0)