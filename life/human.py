from animal import Animal
from clothing import Clothing

class Human(Animal):
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20


    def __init__(self, name:str, age:int=0, energy:int=Animal.MAX_ENERGY) -> None:
        super().__init__(name)
        self.clothing = []

    def dress(self, clothing: Clothing):
        self.clothing.add(clothing)

    def undress(self, clothing: Clothing):
        self.clothing.remove(clothing)

