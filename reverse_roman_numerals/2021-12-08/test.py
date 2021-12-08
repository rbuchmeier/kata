import unittest
from main import *

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

class TestRoman(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('II'), 2)
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('VIII'), 8)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('XXXI'), 31)
        self.assertEqual(roman_to_int('CCCXLV'), 345)
        self.assertEqual(roman_to_int('CDLVIII'), 458)
        self.assertEqual(roman_to_int('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()
