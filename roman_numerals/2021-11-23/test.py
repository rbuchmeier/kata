import unittest
from main import *

class BaseTest(unittest.TestCase):
    def test_base(self):
        self.assertTrue(True)

class TestRoman(unittest.TestCase):
    def test_roman_1(self):
        self.assertEqual(roman_numeral(1), 'I')
        self.assertEqual(roman_numeral(2), 'II')
        self.assertEqual(roman_numeral(4), 'IV')
        self.assertEqual(roman_numeral(9), 'IX')
        self.assertEqual(roman_numeral(99), 'XCIX')
        self.assertEqual(roman_numeral(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
