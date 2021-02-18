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
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f"human(name='{self.name}', age={self.age}, energy={self.energy})"

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy of {self.energy}.'

    def grow(self) -> None:
        self.age = self.age + 1
        # self.age += 1

        if (potential_energy >= Human.MAX_ENERGY):
            left_over_amount = potential_energy - Human.MAX_ENERGY
            self.energy = Human.MAX_ENERGY
            return left_over_amount
        else:
            left_over_amount = Human.MAX_ENERGY - potential_energy
            return left_over_amount

    def reproduce(self) -> bool:
        if self.energy >= Human.REPRODUCE_ENERGY:
            self.energy = self.energy - Human.REPRODUCE_ENERGY
            return True
        else:
            return False

    def move(self, distance: int) -> bool:
        required_energy = (Human.MOVE_ENERGY + distance)

        if self.energy >= (Human.MOVE_ENERGY + distance):
            self.energy = self.energy - required_energy
            return True
        else:
            return False

    def move(self):
        return if self.energy >= required_energy
