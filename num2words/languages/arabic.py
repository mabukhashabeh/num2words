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
    
    def convert(self, number: Union[int, float], to: str = 'cardinal', 
                gender: str = 'm', **kwargs) -> str:
        """
        Convert number to Arabic words.
        
        Args:
            number: Integer or float
            to: 'cardinal' or 'ordinal'
            gender: 'm' (masculine) or 'f' (feminine)
        
        Returns:
            str: Number in Arabic words
        """
        # Validate parameters
        to = self._settings.validate_conversion_type(to)
        gender = self._settings.validate_gender(gender)
        
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
