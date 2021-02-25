from clothing import Clothing

class Human:

    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20

    # class attributes - each is a constant
    MAX_ENERGY = 100
    REPRODUCE_ENERGY = 20
    MOVE_ENERGY = 10

    # initialise the state of the instance
    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        # instance attributes/varibles
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.clothing = []

    def __repr__(self) -> str:
        return f"human(name='{self.__name}', age={self.__age}, energy={self.__energy})"

    def __str__(self) -> str:
        return f'{self.__name} is {self.__age} years old and has an energy of {self.__energy}.'

    def dress(self, clothing:Clothing) -> None:
        self.clothing.add(clothing)

    def grow(self) -> None:
        self.__age = self.__age + 1
        # self.__age += 1


    def eat(self, amount) -> int:
        potential_energy = self.energy + amount
        if (potential_energy >= Human.MAX_ENERGY):
            left_over_amount = potential_energy - Human.MAX_ENERGY
            self.__energy = Human.MAX_ENERGY
            return left_over_amount
        else:
            left_over_amount = potential_energy - Human.MAX_ENERGY
            return left_over_amount

    def reproduce(self) -> bool:
        if self.__energy >= Human.REPRODUCE_ENERGY:
            self.__energy = self.__energy - Human.REPRODUCE_ENERGY
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        required_energy = (Human.MOVE_ENERGY + distance)

        if self.__energy >= (Human.MOVE_ENERGY + distance):
            self.__energy = self.__energy - required_energy
            return True
        else:
            return False

    def undress(self, clothing:Clothing) -> None:
        self.clothing.remove(clothing)


