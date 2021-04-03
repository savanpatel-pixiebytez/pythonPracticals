class Vehicle:
    def left(self):
        print("Move one left")

    def right(self):
        print("Move one unit right")

    def front(self):
        print("Move one front")

    def back(self):
        print("Move one back")

    def brake(self):
        print("stop vehicle")

    def increaseSpeed(self, val):
        print('speed increased by ', val)

    def slowDown(self, val):
        print('decrease speed by ', val)

    def cruiseControl(self, val):
        print('moving with constant speed of ', val)

    def obstacleDetected(self, accuracy):
        if accuracy > 90:
            self.brake()
        elif accuracy > 50 and accuracy < 90:
            print("WARNING!!! Obstacle detected! ")
            self.slowDown(0.7)
        else:
            pass

    def circleAround(self):
        print("Moving circular")


class Drone(Vehicle):
    def __init__(self):
        print("Create function with ML and get accuracy of object detected and pass it to the obstacleDetected function")
        self.obstacleDetected(40)

    def moveUp(self):
        print("Moving up ")

    def moveDown(self):
        print("Moving down")

    def moveTopRight(self):
        print("Moving towards top left corner")

    def spiralUp(self):
        self.circleAround()
        self.moveUp()

    def hover(self):
        print('fix the altitude and hover on that place.')

    def moveAheadWithMaxSpeed(self):
        print("Making dorne position 45deg inclined and moving with increased speed to avoid air friction")


class Rover(Vehicle):
    def __init__(self):
        print("Create function with ML and get accuracy of object detected and pass it to the obstacleDetected function")
        self.obstacleDetected(40)

    def personDetected(self):
        print("ALERT!!! Elon found on mars... :>")

    def selfStandUp(self):
        print("Stand up auto after falling down")

    def gettingOutOfWater(self):
        print("if water is detected activate drone feature and lift the rover up and hover out to land or install peddals to get out")
