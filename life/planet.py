from livingthing import LivingThing


class Planet:

    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.living_thing = []

    def __repr__(self) -> str:
        return f'planet(name={self.__name}, humans={self.__humans})'

    def __str__(self):
        return f'Planet {self.__name} has {len(self.__humans)} humans.'

    def add(self, living_thing: LivingThing) -> bool:
        if living_thing:
            self.__living_thing.append(living_thing)
            return True
        return False

    def remove(self, living_thing: LivingThing) -> bool:
        if living_thing in self.__living_things:
            self.__living_things.remove(living_thing)
            return True
        return False

    def has(self, living_thing: LivingThing) -> bool:
        if living_thing in self.__living_things:
            return True
        return False

    def population(self) -> int:
        return len(self.__living_things)


