class Car:
    def __init__(self, x, y):
        self.width = 40
        self.height = 20

        self.xpos = x
        self.ypos = y
        self.velocity = 0

    def drive(self, v):
        self.velocity += 10
        self.xpos += self.velocity

    def stop(self):
        self.velocity = 0


myCar = Car(20, 20)

print("Speed: {}, xpos: {}".format(myCar.velocity, myCar.xpos))
myCar.drive(10)
print("Speed: {}, xpos: {}".format(myCar.velocity, myCar.xpos))
myCar.stop()
print("Speed: {}, xpos: {}".format(myCar.velocity, myCar.xpos))