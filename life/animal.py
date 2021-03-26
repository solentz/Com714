from livingthing import LivingThing


class Animal(LivingThing):
    MAX_ENERGY = 100
    MIN_ENERGY = 0
    REPRODUCE_ENERGY = 1

    def __init__(self, name: str, age: int = 0, energy: int = LivingThing.MAX_ENERGY, potential_energy=0) -> None:
        super().__init__(name)


    def __repr__(self) -> str:
        return f'animal(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def eat(self, amount) -> int:
        potential_energy = self.energy + amount

        if potential_energy > LivingThing.MAX_ENERGY:
            left_over_amount = potential_energy - LivingThing.MAX_ENERGY
            self._energy = LivingThing.MAX_ENERGY
        else:
            left_over_amount = LivingThing.MAX_ENERGY - potential_energy
            self._energy = potential_energy

        return left_over_amount

    def grow(self) -> None:
        self.age += 1

    def move(self, distance: int) -> bool:
        potential_energy = self.energy - distance

        if potential_energy >= LivingThing.MOVE_ENERGY:
            self.energy = potential_energy
            return True
        else:
            return False

    def reproduce(self) -> bool:
        potential_energy = self.energy - LivingThing.REPRODUCE_ENERGY

        if potential_energy >= LivingThing.MIN_ENERGY:
            self.energy = potential_energy
            return True
        else:
            return False
