import unittest
from main import *

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

class TestRoman(unittest.TestCase):
    def test_roman(self):
        self.assertEqual(roman(1), 'I')
        self.assertEqual(roman(2), 'II')
        self.assertEqual(roman(3), 'III')
        self.assertEqual(roman(4), 'IV')
        self.assertEqual(roman(5), 'V')
        self.assertEqual(roman(8), 'VIII')
        self.assertEqual(roman(9), 'IX')
        self.assertEqual(roman(10), 'X')
        self.assertEqual(roman(31), 'XXXI')
        self.assertEqual(roman(345), 'CCCXLV')
        self.assertEqual(roman(458), 'CDLVIII')
        self.assertEqual(roman(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
