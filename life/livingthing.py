

class LivingThing:


    MAX_ENERGY = 100
    REPRODUCE_ENERGY = 1



    # initialise the state of the instance
    def __init__(self,name: str) -> None:
        # instance attributes/varibles
        self._age = 0
        self._energy = 100
        self._name = name


    def __repr__(self) -> str:
        return f"livingthing(age='{self.__age}', energy={self.__energy}, name={self.__name})"

    def __str__(self) -> str:
        return f'{self.__age} years old and has an energy of {self.__energy} The LivingThing is called {self.__name}.'


    def grow(self) -> None:
        self.__age = self.__age + 1
        # self.__age += 1



    def reproduce(self) -> bool:
        if self.__energy >= LivingThing.REPRODUCE_ENERGY:
            self.__energy = self.__energy - LivingThing.REPRODUCE_ENERGY
            return True
        else:
            return False



