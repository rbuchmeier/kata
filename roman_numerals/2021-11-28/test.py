import unittest
from main import *

class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

class TestRoman(unittest.TestCase):
    def test_roman_1(self):
        self.assertEqual(get_roman_numeral(1), 'I')
    
    def test_roman_2(self):
        self.assertEqual(get_roman_numeral(2), 'II')
    
    def test_roman_4(self):
        self.assertEqual(get_roman_numeral(4), 'IV')
    
    def test_roman_5(self):
        self.assertEqual(get_roman_numeral(5), 'V')

    def test_roman_9(self):
        self.assertEqual(get_roman_numeral(9), 'IX')
    
    def test_roman_49(self):
        self.assertEqual(get_roman_numeral(49), 'XLIX')
    
    def test_roman_negative(self):
        self.assertEqual(get_roman_numeral(-1), 'Invalid')
    
    def test_roman_3333(self):
        self.assertEqual(get_roman_numeral(3333), 'MMMCCCXXXIII')
    
    def test_roman_3999(self):
        self.assertEqual(get_roman_numeral(3999), 'MMMCMXCIX')
    
    def test_roman_4000(self):
        self.assertEqual(get_roman_numeral(4000), 'Invalid')
    
    def test_roman_0(self):
        self.assertEqual(get_roman_numeral(0), 'Invalid')
    

if __name__ == '__main__':
    unittest.main()
