from planet import Planet
from typing import List
from non_planet import NonPlanet

import random


class Universe:

    def __init__(self) -> None:
        self.__planets = []
        self.__non_planet = []

    def __repr__(self) -> str:
        return f"universe(planets={len(self.__planets)})"

    def __str__(self) -> str:
        return f"The universe has {len(self.__planets)} planets."

    def generate_planet(self, names: List[str]) -> None:
        for name in names:
            planet = Planet(name)
            self.__planets.append(planet)

    def generate_non_planet(self, names: List[str]) -> None:
        for name in names:
            non_planet = NonPlanet(name)
            self.__planets.append(non_planet)

    def display(self) -> None:
        print("The planets:")
        for planet in self.__planets:
            print(planet)

        print("The non planets:")
        for non_planet in self.__non_planet:
            print(non_planet)
