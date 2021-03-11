from flyingsuperpower import FlyingSuperPower
from invisibility_super_power import InvisibilitySuperPower
from livingthing import LivingThing


class Alien(LivingThing, FlyingSuperPower, InvisibilitySuperPower):

    def __init__(self, name, powers):
        self.SUPER_POWERS = powers
        super(LivingThing, self).__init__(name)
        pass

    def fly(self, distance: float) -> None:
        if "fly" in self.SUPER_POWERS:
            print("i am flying")
        else:
            print("can't fly yet!")
        pass

    def turn_invisible(self):
        pass

    def turn_visible(self):
        pass
