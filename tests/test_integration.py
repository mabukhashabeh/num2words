"""Integration tests for num2words package."""

import unittest
from num2words import num2words, convert


class TestIntegration(unittest.TestCase):
    """Integration tests."""
    
    def test_convert_alias(self):
        """Test that convert is an alias for num2words."""
        self.assertEqual(convert(42), num2words(42))
        self.assertEqual(convert(42, lang='ar'), num2words(42, lang='ar'))
    
    def test_language_aliases(self):
        """Test language code aliases."""
        self.assertEqual(num2words(42, lang='en'), num2words(42, lang='english'))
        self.assertEqual(num2words(42, lang='ar'), num2words(42, lang='arabic'))
    
    def test_unsupported_language(self):
        """Test unsupported language error."""
        with self.assertRaises(ValueError):
            num2words(42, lang='fr')
    
    def test_large_numbers(self):
        """Test large number conversions."""
        # English
        result = num2words(1234567890)
        self.assertIn("billion", result)
        
        # Arabic
        result = num2words(1234567890, lang='ar')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()

