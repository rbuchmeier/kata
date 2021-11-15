import main
import unittest

class TestConverter(unittest.TestCase):
    def test_convert_to_roman_numeral(self):
        self.assertEqual(main.convert_to_roman_numeral(1), "I")
        self.assertEqual(main.convert_to_roman_numeral(2), "II")
        self.assertEqual(main.convert_to_roman_numeral(5), "V")
        self.assertEqual(main.convert_to_roman_numeral(8), "VIII")

    def test_fours(self):
        self.assertEqual(main.convert_to_roman_numeral(4), "IV")
    
    def test_nines(self):
        self.assertEqual(main.convert_to_roman_numeral(9), "IX")
    
    def test_multi_nines(self):
        self.assertEqual(main.convert_to_roman_numeral(99), "XCIX")
    
    def test_hundreds(self):
        self.assertEqual(main.convert_to_roman_numeral(100), "C")
        self.assertEqual(main.convert_to_roman_numeral(200), "CC")
    
    def test_thousands(self):
        self.assertEqual(main.convert_to_roman_numeral(1000), "M")
        self.assertEqual(main.convert_to_roman_numeral(2000), "MM")
    
    def test_eights_and_nines(self):
        self.assertEqual(main.convert_to_roman_numeral(89), "LXXXIX")

if __name__ == '__main__':
    unittest.main()
