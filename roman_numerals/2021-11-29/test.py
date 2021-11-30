import unittest
from main import *

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

class TestRomanNumerals(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(roman_numeral(1), 'I')
        self.assertEqual(roman_numeral(2), 'II')
        self.assertEqual(roman_numeral(4), 'IV')
        self.assertEqual(roman_numeral(5), 'V')
        self.assertEqual(roman_numeral(9), 'IX')
        self.assertEqual(roman_numeral(49), 'XLIX')
        self.assertEqual(roman_numeral(99), 'XCIX')
        self.assertEqual(roman_numeral(3333), 'MMMCCCXXXIII')
        self.assertEqual(roman_numeral(3999), 'MMMCMXCIX')
        self.assertEqual(roman_numeral(4000), 'Invalid')
        self.assertEqual(roman_numeral(0), 'Invalid')
        self.assertEqual(roman_numeral(-1), 'Invalid')

if __name__ == '__main__':
    unittest.main()
