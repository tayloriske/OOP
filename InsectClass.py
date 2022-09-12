import random

class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.miles = 0

    def lengthofflight(self):
        self.miles = random.randint(1,10)

    def get_miles(self):
        return self.miles