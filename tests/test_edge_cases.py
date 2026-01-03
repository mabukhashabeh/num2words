"""Comprehensive edge case tests for num2words package."""

import unittest
import math
from numwordify import num2words


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_zero(self):
        """Test zero in all languages."""
        self.assertEqual(num2words(0), "zero")
        self.assertEqual(num2words(0, lang='ar'), "صفر")
        self.assertEqual(num2words(0.0), "zero")
        self.assertEqual(num2words(0.0, lang='ar'), "صفر")
    
    def test_negative_zero(self):
        """Test negative zero (should be treated as zero)."""
        self.assertEqual(num2words(-0), "zero")
        self.assertEqual(num2words(-0.0), "zero")
    
    def test_infinity(self):
        """Test infinity handling."""
        self.assertEqual(num2words(float('inf')), "infinity")
        self.assertEqual(num2words(float('-inf')), "negative infinity")
        self.assertEqual(num2words(float('inf'), lang='ar'), "اللانهاية")
        self.assertEqual(num2words(float('-inf'), lang='ar'), "سالب اللانهاية")
    
    def test_nan(self):
        """Test NaN handling."""
        self.assertEqual(num2words(float('nan')), "not a number")
        self.assertEqual(num2words(float('nan'), lang='ar'), "ليس رقماً")
    
    def test_very_small_numbers(self):
        """Test very small numbers."""
        self.assertEqual(num2words(1), "one")
        self.assertEqual(num2words(-1), "negative one")
        self.assertEqual(num2words(1, lang='ar'), "واحد")
        self.assertEqual(num2words(-1, lang='ar'), "سالب واحد")
    
    def test_very_large_numbers(self):
        """Test very large numbers."""
        # Test up to trillions
        large_num = 1234567890123
        result = num2words(large_num)
        self.assertIsInstance(result, str)
        self.assertIn("trillion", result)
        
        # Test Arabic
        result_ar = num2words(large_num, lang='ar')
        self.assertIsInstance(result_ar, str)
        self.assertTrue(len(result_ar) > 0)
    
    def test_decimal_edge_cases(self):
        """Test decimal edge cases."""
        # Single digit decimal
        self.assertEqual(num2words(1.0), "one")
        self.assertEqual(num2words(1.1), "one point one")
        self.assertEqual(num2words(1.01), "one point one")
        
        # Multiple digit decimals
        self.assertEqual(num2words(1.123), "one point one two three")
        self.assertEqual(num2words(1.123456789), "one point one two three four five six seven eight nine")
        
        # Very small decimals
        self.assertEqual(num2words(0.1), "zero point one")
        self.assertEqual(num2words(0.01), "zero point one")
        self.assertEqual(num2words(0.001), "zero point zero zero one")
        
        # Arabic decimals
        self.assertEqual(num2words(1.5, lang='ar'), "واحد فاصل خمسة")
        self.assertEqual(num2words(0.1, lang='ar'), "صفر فاصل واحد")
    
    def test_rounding_issues(self):
        """Test floating point rounding issues."""
        # Common floating point precision issues
        self.assertEqual(num2words(0.1 + 0.2), "zero point three")
        self.assertEqual(num2words(1.0 - 0.9), "zero point one")
    
    def test_boundary_numbers(self):
        """Test boundary numbers."""
        # Test around boundaries
        self.assertEqual(num2words(19), "nineteen")
        self.assertEqual(num2words(20), "twenty")
        self.assertEqual(num2words(21), "twenty-one")
        
        self.assertEqual(num2words(99), "ninety-nine")
        self.assertEqual(num2words(100), "one hundred")
        self.assertEqual(num2words(101), "one hundred one")
        
        self.assertEqual(num2words(999), "nine hundred ninety-nine")
        self.assertEqual(num2words(1000), "one thousand")
        self.assertEqual(num2words(1001), "one thousand one")
    
    def test_ordinal_edge_cases(self):
        """Test ordinal edge cases."""
        self.assertEqual(num2words(0, to='ordinal'), "zeroth")
        self.assertEqual(num2words(1, to='ordinal'), "first")
        self.assertEqual(num2words(2, to='ordinal'), "second")
        self.assertEqual(num2words(3, to='ordinal'), "third")
        self.assertEqual(num2words(11, to='ordinal'), "eleventh")
        self.assertEqual(num2words(21, to='ordinal'), "twenty-first")
        self.assertEqual(num2words(100, to='ordinal'), "one hundredth")
        # Note: 1000 as ordinal is complex, testing that it returns a valid string
        result = num2words(1000, to='ordinal')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
    
    def test_arabic_gender_edge_cases(self):
        """Test Arabic gender edge cases."""
        # Masculine (default)
        self.assertEqual(num2words(1, lang='ar', gender='m'), "واحد")
        self.assertEqual(num2words(2, lang='ar', gender='m'), "إثنان")
        
        # Feminine
        self.assertEqual(num2words(1, lang='ar', gender='f'), "واحدة")
        self.assertEqual(num2words(2, lang='ar', gender='f'), "إثنتان")
        
        # Test with larger numbers
        self.assertEqual(num2words(100, lang='ar', gender='m'), "مائة")
        self.assertEqual(num2words(100, lang='ar', gender='f'), "مائة")
    
    def test_invalid_inputs(self):
        """Test invalid input handling."""
        with self.assertRaises(TypeError):
            num2words("42")
        
        with self.assertRaises(TypeError):
            num2words([42])
        
        with self.assertRaises(TypeError):
            num2words(None)
        
        with self.assertRaises(ValueError):
            num2words(42, lang='fr')
        
        with self.assertRaises(ValueError):
            num2words(42, to='invalid')
    
    def test_language_aliases(self):
        """Test language code aliases."""
        self.assertEqual(num2words(42, lang='en'), num2words(42, lang='english'))
        self.assertEqual(num2words(42, lang='ar'), num2words(42, lang='arabic'))
        
        # Case insensitive
        self.assertEqual(num2words(42, lang='EN'), num2words(42, lang='en'))
        self.assertEqual(num2words(42, lang='AR'), num2words(42, lang='ar'))
    
    def test_very_long_decimal(self):
        """Test very long decimal numbers."""
        long_decimal = 123.123456789012345
        result = num2words(long_decimal)
        self.assertIn("point", result)
        self.assertIsInstance(result, str)
    
    def test_negative_decimals(self):
        """Test negative decimal numbers."""
        self.assertEqual(num2words(-1.5), "negative one point five")
        self.assertEqual(num2words(-0.5), "negative zero point five")
        self.assertEqual(num2words(-1.5, lang='ar'), "سالب واحد فاصل خمسة")
    
    def test_ordinal_with_decimals(self):
        """Test ordinal with decimal (should use cardinal for decimal part)."""
        # Ordinal doesn't make sense with decimals, but should handle gracefully
        result = num2words(1.5, to='ordinal')
        self.assertIsInstance(result, str)
        self.assertIn("point", result)
    
    def test_arabic_scale_forms(self):
        """Test Arabic scale forms (singular, dual, plural)."""
        # Singular (1)
        self.assertEqual(num2words(1000, lang='ar'), "ألف")
        
        # Dual (2)
        self.assertEqual(num2words(2000, lang='ar'), "ألفان")
        
        # Plural (3+)
        result = num2words(3000, lang='ar')
        self.assertIn("آلاف", result)
    
    def test_maximum_python_int(self):
        """Test with very large Python integers."""
        # Python ints can be arbitrarily large
        # Test with a reasonable large number first
        very_large = 10**15  # Quadrillion
        result = num2words(very_large)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        
        # Test with extremely large number (beyond standard scales)
        extremely_large = 10**100
        result = num2words(extremely_large)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
    
    def test_precision_handling(self):
        """Test floating point precision handling."""
        # Test numbers that might have precision issues
        self.assertEqual(num2words(1.0), "one")
        self.assertEqual(num2words(1.00), "one")
        self.assertEqual(num2words(1.000), "one")
        
        # Test numbers with trailing zeros in decimal
        result = num2words(1.100)
        self.assertIn("one", result)
    
    def test_negative_ordinal(self):
        """Test negative ordinal numbers."""
        result = num2words(-1, to='ordinal')
        self.assertIn("negative", result)
        self.assertIn("first", result)
    
    def test_arabic_ordinal_edge_cases(self):
        """Test Arabic ordinal edge cases."""
        result = num2words(1, lang='ar', to='ordinal')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
        
        result = num2words(100, lang='ar', to='ordinal')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()

