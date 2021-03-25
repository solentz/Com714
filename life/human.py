from animal import Animal
from clothing import Clothing


class Human(Animal):
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20
    MAX_ENERGY = 10

    def __init__(self, name: str, age: int = 0, energy: int = MAX_ENERGY) -> None:
        super().__init__(name)
        self.clothing = []

    def __repr__(self) -> str:
        return f"human(name='{self._name}', age={self._age}, energy={self._energy})"

    def __str__(self) ->str:
        return f"{self._name} is {self._age} years old and has an energy level of {self._energy}."

    def dress(self, clothing: Clothing):
        self.clothing.add(clothing)

    def undress(self, clothing: Clothing):
        self.clothing.remove(clothing)
