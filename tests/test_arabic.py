"""Tests for Arabic number conversion."""

import unittest
from num2words import num2words


class TestArabicConversion(unittest.TestCase):
    """Test Arabic number to words conversion."""
    
    def test_basic_numbers(self):
        """Test basic number conversions."""
        self.assertEqual(num2words(0, lang='ar'), "صفر")
        self.assertEqual(num2words(1, lang='ar'), "واحد")
        self.assertEqual(num2words(10, lang='ar'), "عشرة")
        self.assertEqual(num2words(15, lang='ar'), "خمسة عشر")
        self.assertEqual(num2words(20, lang='ar'), "عشرون")
        self.assertEqual(num2words(21, lang='ar'), "واحد وعشرون")
        self.assertEqual(num2words(99, lang='ar'), "تسعة وتسعون")
    
    def test_hundreds(self):
        """Test hundreds."""
        self.assertEqual(num2words(100, lang='ar'), "مئة")
        self.assertEqual(num2words(101, lang='ar'), "مئة وواحد")
        self.assertEqual(num2words(200, lang='ar'), "مئتان")
        self.assertEqual(num2words(999, lang='ar'), "تسع مئة وتسعة وتسعون")
    
    def test_thousands(self):
        """Test thousands."""
        self.assertEqual(num2words(1000, lang='ar'), "ألف")
        self.assertEqual(num2words(2000, lang='ar'), "ألفان")
        self.assertEqual(num2words(1234, lang='ar'), "ألف ومئتان وأربعة وثلاثون")
    
    def test_gender(self):
        """Test gender-specific forms."""
        # Masculine (default)
        self.assertEqual(num2words(1, lang='ar', gender='m'), "واحد")
        self.assertEqual(num2words(2, lang='ar', gender='m'), "اثنان")
        
        # Feminine
        self.assertEqual(num2words(1, lang='ar', gender='f'), "واحدة")
        self.assertEqual(num2words(2, lang='ar', gender='f'), "اثنتان")
    
    def test_negative_numbers(self):
        """Test negative numbers."""
        self.assertEqual(num2words(-1, lang='ar'), "سالب واحد")
        self.assertEqual(num2words(-42, lang='ar'), "سالب اثنان وأربعون")
    
    def test_decimal_numbers(self):
        """Test decimal numbers."""
        self.assertEqual(num2words(1.5, lang='ar'), "واحد فاصلة خمسة")
        self.assertEqual(num2words(123.45, lang='ar'), "مئة وثلاثة وعشرون فاصلة خمسة وأربعون")


if __name__ == '__main__':
    unittest.main()

