import unittest
from human import Human


class TestHuman(unittest.TestCase):

    def test_eat(self) -> None:
        # energy is full and try to eat
        human_ziga = Human("Ziga")
        self.assertEqual(human_ziga.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat more than required
        human_ziga = Human("Ziga", energy=90)
        self.assertEqual(human_ziga.eat(20), o, "Excess should 10.")

        # energy is below 100 and eat more than required
        human_ziga = Human("Ziga", energy=80)
        self.assertEqual(human_ziga.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat more than required
        human_ziga = Human("Ziga", energy=70)
        self.assertEqual(human_ziga.eat(20), -10, "Excess should be -10.")


    def test_grow(selfself):
         # new born and age
         human_ziga = Human("Ziga")
         human_ziga.grow()
         self.assertEqual(human_ziga.age, 1, "Age should be 1")


