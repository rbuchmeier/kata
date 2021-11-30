from main import *
import unittest

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(roman_numeral(1), 'I')
        self.assertEqual(roman_numeral(2), 'II')
        self.assertEqual(roman_numeral(3459), 'MMMCDLIX')
        self.assertEqual(roman_numeral(45), 'XLV')

class TestBaseIndexConversion(unittest.TestCase):
    def test_base_index_conversion(self):
        self.assertEqual(convert_number_to_base_indexes(2), [0, 0])
        self.assertEqual(convert_number_to_base_indexes(4), [0, 1])
        self.assertEqual(convert_number_to_base_indexes(5), [1])

class TestRomanByBaseAndMagnitude(unittest.TestCase):
    def test_roman_by_base_and_magnitude(self):
        self.assertEqual(get_roman_from_base([0], 0), 'I')
        self.assertEqual(get_roman_from_base([0, 0], 0), 'II')
        self.assertEqual(get_roman_from_base([0, 1], 0), 'IV')
        self.assertEqual(get_roman_from_base([0, 2], 0), 'IX')
        self.assertEqual(get_roman_from_base([0, 0], 1), 'XX')
        self.assertEqual(get_roman_from_base([0, 0], 1), 'XX')
        self.assertEqual(get_roman_from_base([1, 0], 1), 'LX')
        self.assertEqual(get_roman_from_base([0, 2], 1), 'XC')
        self.assertEqual(get_roman_from_base([0, 1], 2), 'CD')
        self.assertEqual(get_roman_from_base([0, 2], 2), 'CM')

class TestListFromNumber(unittest.TestCase):
    def test_list_from_number(self):
        self.assertEqual(get_list_from_number(2), [2])
        self.assertEqual(get_list_from_number(3459), [3, 4, 5, 9])

if __name__ == '__main__':
    unittest.main()
