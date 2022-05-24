from vehicle import Vehicle
import time

class Commander:

    PAUSE_COUNTER = 50
    AFTER_PAUSE_COUNTER = 50

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.lastr = -200
        self.lastl = -200
        self.speedRatio = 5
        self.lastSpeedRatio = 0
        self.pauseCounter = 0
        self.afterPauseCounter = 0
        self.startLapsTime = 0
        self.lapsCounter = 0
        self.midLapControl = False

    def onDistanceReading(self, distance):
        pass

    def onGearShiftUp(self):
        self.speedRatio += 1
        if (self.speedRatio > 10): 
            self.speedRatio = 10

    def onGearShiftDown(self):
        self.speedRatio -= 1
        if (self.speedRatio < 3): 
            self.speedRatio = 3


    def onJoystickReading(self, upDownReading: float, leftRightReading: float):
        if (self.pauseCounter):
            self.pauseCounter -= 1
            return
        if (self.afterPauseCounter):
            self.afterPauseCounter -= 1

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

        #if (self.lastr == r and self.lastl == l and self.speedRatio == self.lastSpeedRatio):
        #    pass
        #else:
        #    print ('r ' + str(r) + ", l " + str(l))
            
        self.vehicle.setMotors(1 * r / 100 * self.speedRatio / 10, l / 100 * self.speedRatio / 10)

        self.lastr = r 
        self.lastl = l
        self.lastSpeedRatio = self.speedRatio
        
    def onColorReading(self, color):
        if (color == "WHITE" or color == "BLACK") and not self.afterPauseCounter:
            self.pauseCounter = self.PAUSE_COUNTER
            self.afterPauseCounter = self.AFTER_PAUSE_COUNTER
            self.vehicle.setMotors(0, 0)
        if (color == "YELLOW" and self.midLapControl):
            elapsed_time = time.time() - self.startLapsTime 
            if (elapsed_time < 60) :
                print("Laps + " + str(self.lapsCounter + 1) + " in : " + str(elapsed_time) + " s")
                self.lapsCounter += 1
            self.startLapsTime = time.time()
            self.midLapControl = False
        if (color == "RED"):
            self.midLapControl = True
        