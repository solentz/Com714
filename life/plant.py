from livingthing import LivingThing

class Plant(LivingThing):
    MAX_ENERGY = 1

    def __init__(self,name: str) -> None:
        super().__init__(name)


    def __repr__(self) -> str:
        return f'plant(name={self.__energy}, {self.__name} age={self.age}.'

    def __str__(self) -> str:
        return f'The plant is called (name={self.__name}, age{self.__age} years old has energy={self.energy}.'


    def absorb(self, energy:int) -> int:
        potential_energy = self._energy +energy

        if potential_energy > LivingThing.MAX_ENERGY
            self._energy = LivingThing.MAX_ENERGY
            return  potential_energy - self._energy

        self._energy = potential_energy
            return 0

