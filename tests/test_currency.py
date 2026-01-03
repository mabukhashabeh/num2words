"""Tests for currency conversion."""

import unittest
from numwordify import num2words


class TestCurrencyConversion(unittest.TestCase):
    """Test currency number to words conversion."""
    
    def test_usd_english(self):
        """Test USD conversion in English."""
        self.assertEqual(
            num2words(123.45, to='currency', currency='USD'),
            "one hundred twenty-three dollars and forty-five cents"
        )
        self.assertEqual(
            num2words(1.01, to='currency', currency='USD'),
            "one dollar and one cent"
        )
        self.assertEqual(
            num2words(0.50, to='currency', currency='USD'),
            "zero dollars and fifty cents"
        )
    
    def test_sar_arabic(self):
        """Test SAR conversion in Arabic."""
        result = num2words(323424.2, to='currency', currency='SAR', lang='ar')
        self.assertIn("ريال", result)
        self.assertIn("هللة", result)
        
        result = num2words(1.5, to='currency', currency='SAR', lang='ar')
        self.assertIn("ريال", result)
        self.assertIn("خمسون", result)
    
    def test_eur_english(self):
        """Test EUR conversion in English."""
        result = num2words(100.50, to='currency', currency='EUR')
        self.assertIn("euro", result)
        self.assertIn("cent", result)
    
    def test_egp_arabic(self):
        """Test EGP conversion in Arabic."""
        result = num2words(50.25, to='currency', currency='EGP', lang='ar')
        self.assertIn("جنيه", result)
        # Check for qirsh (قرش) or qurush (قروش)
        self.assertTrue("قرش" in result or "قروش" in result)
    
    def test_kwd_arabic(self):
        """Test KWD conversion in Arabic (1000 fils per dinar)."""
        result = num2words(50.250, to='currency', currency='KWD', lang='ar')
        # Check for dinar (دينار) or dinars (دنانير)
        self.assertTrue("دينار" in result or "دنانير" in result)
        # Check for fils (فلس) or fulus (فلوس)
        self.assertTrue("فلس" in result or "فلوس" in result)
    
    def test_zero_amount(self):
        """Test zero currency amounts."""
        result = num2words(0, to='currency', currency='USD')
        self.assertIn("zero", result)
        self.assertIn("dollar", result)
    
    def test_negative_currency(self):
        """Test negative currency amounts."""
        result = num2words(-100.50, to='currency', currency='USD')
        self.assertIn("negative", result)
    
    def test_invalid_currency(self):
        """Test invalid currency code."""
        with self.assertRaises(ValueError):
            num2words(100, to='currency', currency='INVALID')
    
    def test_currency_without_to_parameter(self):
        """Test that currency requires to='currency'."""
        # Should work as regular number
        result = num2words(100, currency='USD')
        self.assertIsInstance(result, str)
        self.assertNotIn("dollar", result)
    
    def test_all_supported_currencies(self):
        """Test all supported currencies."""
        currencies = ['SAR', 'USD', 'EUR', 'EGP', 'KWD']
        for currency in currencies:
            result = num2words(100.50, to='currency', currency=currency)
            self.assertIsInstance(result, str)
            self.assertTrue(len(result) > 0)
    
    def test_currency_plural_forms(self):
        """Test currency plural forms."""
        # Single unit
        result = num2words(1, to='currency', currency='USD')
        self.assertIn("dollar", result)
        self.assertNotIn("dollars", result)
        
        # Multiple units
        result = num2words(2, to='currency', currency='USD')
        self.assertIn("dollars", result)


if __name__ == '__main__':
    unittest.main()

