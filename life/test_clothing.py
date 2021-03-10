import unittest
from clothing import Clothing
from clothing_size import ClothingSize


class TestClothing(unittest.TestCase):

    def test_create_clothing(self):
        clothing = Clothing('red', 'silk', ClothingSize.MEDIUM)
        expect = "Clothing(colour='red', material='silk', size='medium')"
        self.assertEqual(expect, repr(clothing), "Clothing does not match")


if __name__ == '__main__':
    unittest.main()

