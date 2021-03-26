from flyingsuperpower import FlyingSuperPower
from human import Human

class SuperHuman(Human, FlyingSuperPower):

    MIN_FLY_ENERGY = 5

    def __init__(self, name: str) -> None:
        super(Human, self).__init__(name)

    def fly(self, distance: float) -> None:
        if self._energy >= SuperHuman.MIN_FLY_ENERGY:
            if self._energy >= distance:
                print("I am flying")
                self._energy -= distance
            else:
                print("It's too far to fly")
