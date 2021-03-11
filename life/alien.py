from flyingsuperpower import FlyingSuperPower
from invisibility_super_power import InvisibilitySuperPower
from livingthing import LivingThing


class Alien(LivingThing, FlyingSuperPower, InvisibilitySuperPower):

    def __init__(self):
        pass

    def fly(self):
        print("I am flying!!!")

    def turn_invisible(self):
        print("I am now invisible")

    def turn_visible(self):
        print("I am now visible")
