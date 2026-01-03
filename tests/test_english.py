"""Tests for English number conversion."""

import unittest
from num2words import num2words


class TestEnglishConversion(unittest.TestCase):
    """Test English number to words conversion."""
    
    def test_basic_numbers(self):
        """Test basic number conversions."""
        self.assertEqual(num2words(0), "zero")
        self.assertEqual(num2words(1), "one")
        self.assertEqual(num2words(10), "ten")
        self.assertEqual(num2words(15), "fifteen")
        self.assertEqual(num2words(20), "twenty")
        self.assertEqual(num2words(21), "twenty-one")
        self.assertEqual(num2words(99), "ninety-nine")
    
    def test_hundreds(self):
        """Test hundreds."""
        self.assertEqual(num2words(100), "one hundred")
        self.assertEqual(num2words(101), "one hundred one")
        self.assertEqual(num2words(200), "two hundred")
        self.assertEqual(num2words(999), "nine hundred ninety-nine")
    
    def test_thousands(self):
        """Test thousands."""
        self.assertEqual(num2words(1000), "one thousand")
        self.assertEqual(num2words(1001), "one thousand one")
        self.assertEqual(num2words(1234), "one thousand two hundred thirty-four")
        self.assertEqual(num2words(10000), "ten thousand")
        self.assertEqual(num2words(123456), "one hundred twenty-three thousand four hundred fifty-six")
    
    def test_millions(self):
        """Test millions."""
        self.assertEqual(num2words(1000000), "one million")
        self.assertEqual(num2words(1234567), "one million two hundred thirty-four thousand five hundred sixty-seven")
    
    def test_negative_numbers(self):
        """Test negative numbers."""
        self.assertEqual(num2words(-1), "negative one")
        self.assertEqual(num2words(-42), "negative forty-two")
        self.assertEqual(num2words(-123), "negative one hundred twenty-three")
    
    def test_decimal_numbers(self):
        """Test decimal numbers."""
        self.assertEqual(num2words(1.5), "one point five")
        self.assertEqual(num2words(123.45), "one hundred twenty-three point forty-five")
        self.assertEqual(num2words(0.5), "zero point five")
    
    def test_ordinal_numbers(self):
        """Test ordinal numbers."""
        self.assertEqual(num2words(1, to='ordinal'), "first")
        self.assertEqual(num2words(2, to='ordinal'), "second")
        self.assertEqual(num2words(3, to='ordinal'), "third")
        self.assertEqual(num2words(21, to='ordinal'), "twenty-first")
        self.assertEqual(num2words(100, to='ordinal'), "one hundredth")
    
    def test_type_errors(self):
        """Test type error handling."""
        with self.assertRaises(TypeError):
            num2words("42")
        
        with self.assertRaises(TypeError):
            num2words([42])


if __name__ == '__main__':
    unittest.main()

