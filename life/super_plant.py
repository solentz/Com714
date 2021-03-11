from plant import Plant
from invisibility_super_power import InvisibilitySuperPower

class SuperPlant(Plant, InvisibilitySuperPower):

    MIN_INVISIBILITY_ENERGY = 3

    def __init__(self, name):
        super(SuperPlant, self).__init__(name)

    def turn_invisible(self):
        if self._energy >= SuperPlant.MIN_INVISIBILITY_ENERGY:
