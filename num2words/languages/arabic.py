"""
Arabic number-to-words converter.
Uses YAML configuration for translations.
"""

from typing import Union, List
from .base import BaseConverter
from ..config.loader import ConfigLoader
from ..config.settings import Settings


class ArabicConverter(BaseConverter):
    """Arabic language converter using YAML configuration."""
    
    def __init__(self):
        """Initialize Arabic converter with configuration."""
        super().__init__()
        self.load_config('arabic')
        self._initialize_from_config()
    
    def _initialize_from_config(self) -> None:
        """Initialize converter data structures from configuration."""
        config = self.config
        self.ones_masculine: List[str] = config.get('ones_masculine', [])
        self.tens_masculine: List[str] = config.get('tens_masculine', [])
        self.ones_feminine: List[str] = config.get('ones_feminine', [])
        self.tens_feminine: List[str] = config.get('tens_feminine', [])
        self.hundreds: List[str] = config.get('hundreds', [])
        self.scales: List[str] = config.get('scales', [])
        self.scales_dual: List[str] = config.get('scales_dual', [])
        self.scales_plural: List[str] = config.get('scales_plural', [])
        self.zero: str = config.get('zero', 'صفر')
        self.negative_prefix: str = config.get('negative_prefix', 'سالب')
        self.decimal_separator: str = config.get('decimal_separator', 'فاصلة')
        self.ordinal_prefix: str = config.get('ordinal_prefix', 'ال')
        self.conjunction: str = config.get('conjunction', 'و')
        self.number_separator: str = config.get('number_separator', ' ')
        self.scale_separator: str = config.get('scale_separator', ' ')
        self.currencies: dict = config.get('currencies', {})
    
    def convert(self, number: Union[int, float], to: str = 'cardinal', 
                gender: str = 'm', **kwargs) -> str:
        """
        Convert number to Arabic words.
        
        Args:
            number: Integer or float
            to: 'cardinal', 'ordinal', or 'currency'
            gender: 'm' (masculine) or 'f' (feminine)
            **kwargs: Additional parameters
                - currency: Currency code (e.g., 'SAR', 'USD', 'EUR')
        
        Returns:
            str: Number in Arabic words
        """
        # Validate parameters
        to = self._settings.validate_conversion_type(to)
        gender = self._settings.validate_gender(gender)
        
        # Handle currency conversion
        if to == 'currency':
            currency = kwargs.get('currency', 'SAR')
            return self._to_currency(number, currency, gender)
        
        is_negative, number = self._handle_negative(number)
        integer_part, decimal_value, decimal_str = self._handle_decimal(number)
        
        if integer_part == 0:
            result = self.zero
        else:
            result = self._to_ordinal(integer_part, gender) if to == 'ordinal' else self._to_cardinal(integer_part, gender)
        
        if is_negative:
            result = f"{self.negative_prefix} {result}"
        
        if decimal_value is not None or decimal_str:
            if decimal_value is not None and decimal_value > 0:
                decimal_words = self._to_cardinal(decimal_value, gender)
            elif decimal_str:
                decimal_words = ' '.join([self._to_cardinal(int(d), gender) for d in decimal_str])
            else:
                decimal_words = None
            
            if decimal_words:
                result += f' {self.decimal_separator} {decimal_words}'
        
        return result
    
    def _to_cardinal(self, number: int, gender: str = 'm') -> str:
        """Convert integer to cardinal Arabic words."""
        if number == 0:
            return self.zero
        
        ones = self.ones_masculine if gender == 'm' else self.ones_feminine
        tens = self.tens_masculine if gender == 'm' else self.tens_feminine
        
        if number < 20:
            return ones[number]
        
        if number < 100:
            tens_digit = number // 10
            ones_digit = number % 10
            
            if ones_digit == 0:
                return tens[tens_digit]
            
            # Arabic uses "ones and tens" format
            return f"{ones[ones_digit]} {self.conjunction}{tens[tens_digit]}"
        
        if number < 1000:
            hundreds_digit = number // 100
            remainder = number % 100
            
            if remainder == 0:
                return self.hundreds[hundreds_digit]
            
            return f"{self.hundreds[hundreds_digit]} {self.conjunction}{self._to_cardinal(remainder, gender)}"
        
        # Handle larger numbers
        scale_index = 0
        result_parts = []
        
        while number > 0:
            chunk = number % 1000
            number = number // 1000
            
            if chunk > 0:
                if scale_index > 0:
                    # For scales, handle special cases
                    if chunk == 1:
                        chunk_words = self._get_scale_word(chunk, scale_index)
                    elif chunk == 2:
                        chunk_words = self._get_scale_word(chunk, scale_index)
                    else:
                        chunk_words = self._to_cardinal(chunk, gender)
                        scale_word = self._get_scale_word(chunk, scale_index)
                        chunk_words += f"{self.scale_separator}{scale_word}"
                else:
                    chunk_words = self._to_cardinal(chunk, gender)
                
                result_parts.insert(0, chunk_words)
            
            scale_index += 1
        
        return f' {self.conjunction}'.join(result_parts)
    
    def _get_scale_word(self, number: int, scale_index: int) -> str:
        """Get the appropriate scale word based on number."""
        if scale_index == 0:
            return ''
        
        if scale_index >= len(self.scales):
            return f"(10^{scale_index * 3})"
        
        if number == 1:
            return self.scales[scale_index]
        elif number == 2:
            if scale_index < len(self.scales_dual):
                return self.scales_dual[scale_index]
            return self.scales[scale_index]
        elif 3 <= number <= 10:
            if scale_index < len(self.scales_plural):
                return self.scales_plural[scale_index]
            return self.scales[scale_index]
        else:
            if scale_index < len(self.scales_plural):
                return self.scales_plural[scale_index]
            return self.scales[scale_index]
    
    def _to_ordinal(self, number: int, gender: str = 'm') -> str:
        """Convert integer to ordinal Arabic words."""
        # Arabic ordinals are complex, using simplified approach
        cardinal = self._to_cardinal(number, gender)
        return f"{self.ordinal_prefix}{cardinal}"
    
    def _to_currency(self, number: Union[int, float], currency: str, gender: str = 'm') -> str:
        """Convert number to currency words in Arabic."""
        if currency not in self.currencies:
            raise ValueError(
                f"Unsupported currency: {currency}. "
                f"Supported: {list(self.currencies.keys())}"
            )
        
        currency_info = self.currencies[currency]
        subunit_factor = currency_info.get('subunit_factor', 100)
        
        is_negative, number = self._handle_negative(number)
        
        # Convert to smallest unit (e.g., halalas, fils)
        total_subunits = int(round(number * subunit_factor))
        
        # Get main unit and subunit
        main_units = total_subunits // subunit_factor
        subunits = total_subunits % subunit_factor
        
        # Build result
        parts = []
        
        # Always show main units (even if zero when there are subunits)
        if main_units > 0 or (main_units == 0 and subunits > 0):
            if main_units == 0:
                main_words = self.zero
            else:
                main_words = self._to_cardinal(main_units, gender)
            
            # Arabic grammar: numbers 3-10 use plural, but 100, 1000, etc. use singular
            # Also, 1 always uses singular, 2 uses dual if available
            if main_units == 1:
                currency_name = currency_info['name']
            elif main_units == 2:
                # Use dual form if available, otherwise plural
                currency_name = currency_info.get('dual', currency_info.get('plural', currency_info['name']))
            elif main_units >= 3 and main_units <= 10:
                # Numbers 3-10 use plural
                currency_name = currency_info.get('plural', currency_info['name'])
            elif main_units % 100 == 0 or main_units % 1000 == 0:
                # Round hundreds and thousands use singular (مئة ريال، ألف ريال)
                currency_name = currency_info['name']
            else:
                # Other numbers use plural
                currency_name = currency_info.get('plural', currency_info['name'])
            
            # Arabic currency convention: for "one", put currency name first (ريال واحد)
            # For other numbers, put number first (خمسة ريالات، مئة ريال)
            if main_units == 1:
                parts.append(f"{currency_name} {main_words}")
            else:
                parts.append(f"{main_words} {currency_name}")
        
        if subunits > 0:
            subunit_words = self._to_cardinal(subunits, gender)
            # Use proper Arabic currency formatting based on real-world conventions
            # SAR: خمسون هللة (singular form even with plural numbers)
            # KWD/EGP/USD: عشرون فلساً، خمسة وعشرون قرشاً (tanween for all numbers)
            use_tanween = currency_info.get('use_tanween_for_subunit', False)
            subunit_always_singular = currency_info.get('subunit_always_singular', False)
            
            if subunits == 1:
                # Singular form
                if use_tanween:
                    subunit_name = currency_info.get('subunit_with_tanween', currency_info['subunit'])
                else:
                    subunit_name = currency_info['subunit']
            elif subunit_always_singular:
                # Some currencies (like SAR) use singular form even with plural numbers
                # خمسون هللة (not هللات), عشرون هللة (not هللات)
                subunit_name = currency_info.get('subunit_with_tanween', currency_info['subunit'])
            elif use_tanween:
                # For currencies that use tanween, apply it to all numbers (not just round tens)
                # خمسة وعشرون قرشاً، خمسة وسبعون قرشاً
                subunit_name = currency_info.get('subunit_with_tanween', currency_info['subunit'])
            else:
                # Other numbers use plural form
                subunit_name = currency_info.get('subunit_plural', currency_info['subunit'])
            parts.append(f"{subunit_words} {subunit_name}")
        
        if not parts:
            # Completely zero amount
            parts.append(f"{self.zero} {currency_info['name']}")
        
        result = f' {self.conjunction}'.join(parts)
        
        if is_negative:
            result = f"{self.negative_prefix} {result}"
        
        return result
