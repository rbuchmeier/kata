import unittest
from main import *

class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

class TestUtils(unittest.TestCase):
    def test_get_nine_or_four(self):
        self.assertEqual(get_nine_or_four(4), 4)
        self.assertEqual(get_nine_or_four(42), 40)

        self.assertEqual(get_nine_or_four(92), 90)
        self.assertEqual(get_nine_or_four(952), 900)

        self.assertEqual(get_nine_or_four(32), 10000)

class TestGetRomanNumerals(unittest.TestCase):
    def test_basic_get_roman_numerals(self):
        self.assertEqual(get_roman_numeral(1), 'I')
        self.assertEqual(get_roman_numeral(2), 'II')
        self.assertEqual(get_roman_numeral(10), 'X')
        self.assertEqual(get_roman_numeral(1000), 'M')
        self.assertEqual(get_roman_numeral(50), 'L')

    def test_larger_number(self):
        self.assertEqual(get_roman_numeral(2222), 'MMCCXXII')
    
    def test_fours_and_nines(self):
        self.assertEqual(get_roman_numeral(4), 'IV')
        self.assertEqual(get_roman_numeral(9), 'IX')
        self.assertEqual(get_roman_numeral(40), 'XL')
        self.assertEqual(get_roman_numeral(94), 'XCIV')
        self.assertEqual(get_roman_numeral(3999), 'MMMCMXCIX')
    
    def test_ensure_maximum(self):
        self.assertEqual(get_roman_numeral(4000), 'Error, number cannot exceed 3999')

if __name__ == '__main__':
    unittest.main()