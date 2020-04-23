class Bicycle():

    num_bicycles = 0

    def __init__(self):
        self.size = "M"
        self.chain = 11
        self.tire = 29
        self.num_bicycles += 1
        self.post_initialize()
        inventory.append(self)


    def post_initialize(self):
        circumference = self.tire * 3.14
        print("Circumference = ", circumference)

    def spares(self):
        print("Tire size =", self.tire)
        print("Chain size =", self.chain)


class MountainBike(Bicycle):

    def __init__(self):
        self.frontFork = "100mm"
        self.rearShock = "80mm"
        self.tire = 27.5


inventory = []

speeedyboi = Bicycle()
print(inventory)
