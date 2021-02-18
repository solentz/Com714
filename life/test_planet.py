import unittest

from human import Human
from planet import Planet

class TestPlanet(unittest.TestCase):

    def test_add_human(self):

        # check: 0 population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: single human
        ziga = Human("Ziga")
        earth.add(ziga)
        self.assertEqual(earth.population(), 1, "Population should be 1.")

    def test_has(self):

        # check: does not have specified human
        earth = Planet("Earth")
        ziga = Human("Ziga")
        self.assertFalse(earth.has(ziga), "Should be false.")

        # check: has specified human
        earth.add(ziga)
        self.assertTrue(earth.has(ziga), "Should be true.")

    def test_population(self):

        # check: no population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: no population of one
        ziga = Human("Ziga")
        earth.add(ziga)
        self.assertEqual(earth.population(), 1, "Population should be 1")


if __name__ == '__main__':
    unittest.main()

