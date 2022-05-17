from vehicle import Vehicle

class Commander:

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.lastr = -200
        self.lastl = -200
        self.speedRatio = 5
        self.lastSpeedRatio = 0

    def onDistanceReading(self, distance):
        pass

    def onGearShiftUp(self):
        self.speedRatio += 1
        if (self.speedRatio > 10): 
            self.speedRatio = 10
        print('gear: ' + str(self.speedRatio))

    def onGearShiftDown(self):
        self.speedRatio -= 1
        if (self.speedRatio < 3): 
            self.speedRatio = 3
        print('gear: ' + str(self.speedRatio))


    def onJoystickReading(self, upDownReading: float, leftRightReading: float):

# based on https://home.kendra.com/mauser/joystick.html

        x = 100 * upDownReading
        y = -100 * leftRightReading
        v = (100-abs(x)) * (y/100) + y
        w = (100-abs(y)) * (x/100) + x
        r = int((v+w) /2)
        l = int((v-w)/2)
        #print ('x ' + str(x) + ", y " + str(y) + 'v ' + str(v) + ", w " + str(w) + 'r ' + str(r) + ", l " + str(l))

        if abs(r) < 10 and abs(l) < 10:
            r = 0
            l = 0

        if (self.lastr == r and self.lastl == l and self.speedRatio == self.lastSpeedRatio):
            pass
        else:
            print ('r ' + str(r) + ", l " + str(l))
            
        self.vehicle.setMotors(1 * r / 100 * self.speedRatio / 10, l / 100 * self.speedRatio / 10)

        self.lastr = r 
        self.lastl = l
        self.lastSpeedRatio = self.speedRatio
        
