from vehicle import Vehicle

class Commander:

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def onDistanceReading(self, distance):
        pass

    def onJoystickReading(self, upDownReading: int, leftRightReading: int):    
        self.vehicle.forward()
