class Caps:

    def __init__(self, string):
        self.string = string

    def getString(self):
        self.string.upper()

    def printString(self):
        print(self.string.upper())


attemptOne = Caps(input("Enter the text you want converted"))

attemptOne.getString()
attemptOne.printString()
