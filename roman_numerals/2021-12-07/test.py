import unittest
from main import *

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, 1)

class TestRoman(unittest.TestCase):
    def test_int_to_roman(self):
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(2), 'II')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(8), 'VIII')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(10), 'X')
        self.assertEqual(int_to_roman(31), 'XXXI')
        self.assertEqual(int_to_roman(345), 'CCCXLV')
        self.assertEqual(int_to_roman(458), 'CDLVIII')
        self.assertEqual(int_to_roman(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main()
