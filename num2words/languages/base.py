"""
Base converter class for language implementations.
"""

from abc import ABC, abstractmethod
from typing import Tuple, Optional, Union, Dict, Any
from ..config.settings import Settings


class BaseConverter(ABC):
    """Base class for all language converters."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize converter with configuration.
        
        Args:
            config: Language configuration dictionary. If None, will be loaded.
        """
        self._config = config
        self._settings = Settings
    
    @property
    def config(self) -> Dict[str, Any]:
        """Get language configuration."""
        if self._config is None:
            raise ValueError("Configuration not loaded. Call load_config() first.")
        return self._config
    
    def load_config(self, language: str) -> None:
        """
        Load configuration for the language.
        
        Args:
            language: Language code
        """
        from ..config.loader import ConfigLoader
        self._config = ConfigLoader.load_language_config(language)
    
    @abstractmethod
    def convert(self, number: Union[int, float], to: str = 'cardinal', **kwargs) -> str:
        """
        Convert a number to words.
        
        Args:
            number: Integer or float to convert
            to: Conversion type ('cardinal', 'ordinal')
            **kwargs: Additional language-specific parameters
        
        Returns:
            str: Number in words
        """
        pass
    
    def _handle_negative(self, number: Union[int, float]) -> Tuple[bool, Union[int, float]]:
        """Handle negative numbers.
        
        Returns:
            Tuple of (is_negative, absolute_value)
        """
        if number < 0:
            return True, abs(number)
        return False, number
    
    def _handle_decimal(self, number: Union[int, float]) -> Tuple[Union[int, float], Optional[int], Optional[str]]:
        """Handle decimal numbers.
        
        Returns:
            tuple: (integer_part, decimal_value, decimal_str)
            - integer_part: The integer part of the number
            - decimal_value: The decimal part as an integer (e.g., 5 for 0.5, 45 for 0.45)
              None if decimal has more than MAX_DECIMAL_AS_NUMBER digits
            - decimal_str: The decimal part as a string for digit-by-digit reading
              None if no decimal part
        """
        if isinstance(number, float):
            integer_part = int(number)
            # Convert to string and split to get decimal part
            # Use configurable precision
            precision = self._settings.MAX_DECIMAL_DIGITS
            num_str = f"{number:.{precision}f}"
            if '.' in num_str:
                decimal_str = num_str.split('.')[1].rstrip('0')
                if decimal_str:
                    # Limit to configured precision
                    max_digits = self._settings.MAX_DECIMAL_DIGITS
                    if len(decimal_str) > max_digits:
                        decimal_str = decimal_str[:max_digits]
                    # For configured digits or less, treat as number; for more, read digit by digit
                    max_as_number = self._settings.MAX_DECIMAL_AS_NUMBER
                    decimal_value = int(decimal_str) if len(decimal_str) <= max_as_number else None
                    return integer_part, decimal_value, decimal_str
            return integer_part, None, None
        return number, None, None

