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
        self.assertEqual(num2words(21, lang='ar'), "واحد و عشرون")
        self.assertEqual(num2words(99, lang='ar'), "تسعة و تسعون")
    
    def test_hundreds(self):
        """Test hundreds."""
        self.assertEqual(num2words(100, lang='ar'), "مائة")
        self.assertEqual(num2words(101, lang='ar'), "مائة و واحد")
        self.assertEqual(num2words(200, lang='ar'), "مائتان")
        self.assertEqual(num2words(999, lang='ar'), "تسعة مائة و تسعة و تسعون")
    
    def test_thousands(self):
        """Test thousands."""
        self.assertEqual(num2words(1000, lang='ar'), "ألف")
        self.assertEqual(num2words(2000, lang='ar'), "ألفان")
        self.assertEqual(num2words(1234, lang='ar'), "ألف و مائتان و أربعة و ثلاثون")
    
    def test_gender(self):
        """Test gender-specific forms."""
        # Masculine (default)
        self.assertEqual(num2words(1, lang='ar', gender='m'), "واحد")
        self.assertEqual(num2words(2, lang='ar', gender='m'), "إثنان")
        
        # Feminine
        self.assertEqual(num2words(1, lang='ar', gender='f'), "واحدة")
        self.assertEqual(num2words(2, lang='ar', gender='f'), "إثنتان")
    
    def test_negative_numbers(self):
        """Test negative numbers."""
        self.assertEqual(num2words(-1, lang='ar'), "سالب واحد")
        self.assertEqual(num2words(-42, lang='ar'), "سالب إثنان و أربعون")
    
    def test_decimal_numbers(self):
        """Test decimal numbers."""
        self.assertEqual(num2words(1.5, lang='ar'), "واحد فاصل خمسة")
        self.assertEqual(num2words(123.45, lang='ar'), "مائة و ثلاثة و عشرون فاصل خمسة و أربعون")


if __name__ == '__main__':
    unittest.main()

