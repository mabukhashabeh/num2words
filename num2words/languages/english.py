"""
English number-to-words converter.
Uses YAML configuration for translations.
"""

from typing import Union, List
from .base import BaseConverter
from ..config.loader import ConfigLoader
from ..config.settings import Settings


class EnglishConverter(BaseConverter):
    """English language converter using YAML configuration."""
    
    def __init__(self):
        """Initialize English converter with configuration."""
        super().__init__()
        self.load_config('english')
        self._initialize_from_config()
    
    def _initialize_from_config(self) -> None:
        """Initialize converter data structures from configuration."""
        config = self.config
        self.ones: List[str] = config.get('ones', [])
        self.tens: List[str] = config.get('tens', [])
        self.ordinal_ones: List[str] = config.get('ordinal_ones', [])
        self.ordinal_tens: List[str] = config.get('ordinal_tens', [])
        self.scales: List[str] = config.get('scales', [])
        self.ordinal_scales: List[str] = config.get('ordinal_scales', [])
        self.zero: str = config.get('zero', 'zero')
        self.zeroth: str = config.get('zeroth', 'zeroth')
        self.hundred: str = config.get('hundred', 'hundred')
        self.negative_prefix: str = config.get('negative_prefix', 'negative')
        self.decimal_separator: str = config.get('decimal_separator', 'point')
        self.number_separator: str = config.get('number_separator', '-')
        self.scale_separator: str = config.get('scale_separator', ' ')
    
    def convert(self, number: Union[int, float], to: str = 'cardinal', **kwargs) -> str:
        """
        Convert number to English words.
        
        Args:
            number: Integer or float
            to: 'cardinal' or 'ordinal'
        
        Returns:
            str: Number in English words
        """
        # Validate conversion type
        to = self._settings.validate_conversion_type(to)
        
        is_negative, number = self._handle_negative(number)
        integer_part, decimal_value, decimal_str = self._handle_decimal(number)
        
        if integer_part == 0:
            result = self.zeroth if to == 'ordinal' else self.zero
        else:
            result = self._to_ordinal(integer_part) if to == 'ordinal' else self._to_cardinal(integer_part)
        
        if is_negative:
            result = f"{self.negative_prefix} {result}"
        
        if decimal_value is not None or decimal_str:
            if decimal_value is not None and decimal_value > 0:
                decimal_words = self._to_cardinal(decimal_value)
            elif decimal_str:
                decimal_words = ' '.join([self._to_cardinal(int(d)) for d in decimal_str])
            else:
                decimal_words = None
            
            if decimal_words:
                result += f' {self.decimal_separator} {decimal_words}'
        
        return result
    
    def _to_cardinal(self, number: int) -> str:
        """Convert integer to cardinal English words."""
        if number == 0:
            return self.zero
        
        if number < 20:
            return self.ones[number]
        
        if number < 100:
            tens_digit = number // 10
            ones_digit = number % 10
            if ones_digit == 0:
                return self.tens[tens_digit]
            return f"{self.tens[tens_digit]}{self.number_separator}{self.ones[ones_digit]}"
        
        if number < 1000:
            hundreds = number // 100
            remainder = number % 100
            result = f"{self.ones[hundreds]} {self.hundred}"
            if remainder > 0:
                result += f" {self._to_cardinal(remainder)}"
            return result
        
        # Handle larger numbers
        scale_index = 0
        result_parts = []
        
        while number > 0:
            chunk = number % 1000
            number = number // 1000
            
            if chunk > 0:
                chunk_words = self._to_cardinal(chunk)
                if scale_index > 0:
                    if scale_index < len(self.scales):
                        chunk_words += f"{self.scale_separator}{self.scales[scale_index]}"
                    else:
                        # For very large numbers beyond our scale list
                        chunk_words += f" (10^{scale_index * 3})"
                result_parts.insert(0, chunk_words)
            
            scale_index += 1
        
        return ' '.join(result_parts)
    
    def _to_ordinal(self, number: int) -> str:
        """Convert integer to ordinal English words."""
        if number == 0:
            return self.zeroth
        
        if number < 20:
            return self.ordinal_ones[number]
        
        if number < 100:
            tens_digit = number // 10
            ones_digit = number % 10
            if ones_digit == 0:
                return self.ordinal_tens[tens_digit]
            return f"{self.tens[tens_digit]}{self.number_separator}{self.ordinal_ones[ones_digit]}"
        
        if number < 1000:
            hundreds = number // 100
            remainder = number % 100
            result = f"{self.ones[hundreds]} {self.hundred}"
            if remainder > 0:
                result += f" {self._to_ordinal(remainder)}"
            else:
                result += "th"
            return result
        
        # For larger numbers, use cardinal + ordinal suffix
        scale_index = 0
        result_parts = []
        last_chunk = None
        
        temp_number = number
        while temp_number > 0:
            chunk = temp_number % 1000
            temp_number = temp_number // 1000
            if chunk > 0:
                last_chunk = (chunk, scale_index)
        
        temp_number = number
        scale_index = 0
        while temp_number > 0:
            chunk = temp_number % 1000
            temp_number = temp_number // 1000
            
            if chunk > 0:
                is_last = (chunk, scale_index) == last_chunk
                if is_last:
                    chunk_words = self._to_ordinal(chunk)
                else:
                    chunk_words = self._to_cardinal(chunk)
                
                if scale_index > 0:
                    if is_last:
                        if scale_index < len(self.ordinal_scales):
                            chunk_words += f"{self.scale_separator}{self.ordinal_scales[scale_index]}"
                        else:
                            chunk_words += f" (10^{scale_index * 3})"
                    else:
                        if scale_index < len(self.scales):
                            chunk_words += f"{self.scale_separator}{self.scales[scale_index]}"
                        else:
                            chunk_words += f" (10^{scale_index * 3})"
                
                result_parts.insert(0, chunk_words)
            
            scale_index += 1
        
        return ' '.join(result_parts)
