from livingthing import LivingThing


class Plant(LivingThing):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return f"plant(name={self._name}, age={self._age}, energy={self._energy}"

    def __str__(self):
        return f"The plant is called {self._name}, is {self._age} years old and has{self._energy} energy."

    def absorb(self, energy: int) -> int:
        potential_energy = self._energy + energy

        if potential_energy > LivingThing.MAX_ENERGY:
            self._energy = LivingThing.MAX_ENERGY
            return potential_energy - self._energy

            self._energy = potential_energy
            return False
