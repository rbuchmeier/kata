import unittest
from main import *

class TestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(1, 1)

class TestRoman(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(roman_numeral(1), 'I')
        self.assertEqual(roman_numeral(2), 'II')
        self.assertEqual(roman_numeral(3), 'III')
        self.assertEqual(roman_numeral(4), 'IV')
        self.assertEqual(roman_numeral(5), 'V')
        self.assertEqual(roman_numeral(8), 'VIII')
        self.assertEqual(roman_numeral(9), 'IX')
        self.assertEqual(roman_numeral(10), 'X')
        self.assertEqual(roman_numeral(31), 'XXXI')
        self.assertEqual(roman_numeral(345), 'CCCXLV')
        self.assertEqual(roman_numeral(458), 'CDLVIII')
        self.assertEqual(roman_numeral(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
