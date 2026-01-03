"""
Main converter module for num2words package.
"""

import math
from typing import Union, Dict

from .languages.english import EnglishConverter
from .languages.arabic import ArabicConverter
from .config.settings import Settings


class NumberConverter:
    """Main converter class that supports multiple languages."""
    
    _converters: Dict[str, Union[EnglishConverter, ArabicConverter]] = {}
    _initialized = False
    
    @classmethod
    def _initialize_converters(cls) -> None:
        """Lazy initialization of converters."""
        if not cls._initialized:
            cls._converters = {
                'en': EnglishConverter(),
                'english': EnglishConverter(),
                'ar': ArabicConverter(),
                'arabic': ArabicConverter(),
            }
            cls._initialized = True
    
    @classmethod
    def convert(cls, number: Union[int, float], lang: str = 'en', 
                to: str = 'cardinal', **kwargs) -> str:
        """
        Convert a number to words.
        
        Args:
            number: Integer or float to convert
            lang: Language code ('en', 'ar', 'english', 'arabic')
            to: Conversion type ('cardinal', 'ordinal')
            **kwargs: Additional language-specific parameters (e.g., gender for Arabic)
        
        Returns:
            str: Number in words
        
        Raises:
            ValueError: If language is not supported or number is invalid
            TypeError: If number is not numeric
            OverflowError: If number is too large
        """
        # Initialize converters if needed
        cls._initialize_converters()
        
        # Handle edge cases
        if not isinstance(number, (int, float)):
            raise TypeError(f"Number must be int or float, got {type(number).__name__}")
        
        # Handle infinity using settings
        if math.isinf(number):
            # Get language code for lookup
            lang_code = lang.lower()
            if lang_code in ('english', 'arabic'):
                lang_code = 'en' if lang_code == 'english' else 'ar'
            elif lang_code not in ('en', 'ar'):
                lang_code = 'en'  # Default to English
            
            infinity_words = Settings.INFINITY_WORDS.get(lang_code, Settings.INFINITY_WORDS['en'])
            if number > 0:
                return infinity_words['positive']
            else:
                return infinity_words['negative']
        
        # Handle NaN using settings
        if math.isnan(number):
            # Get language code for lookup
            lang_code = lang.lower()
            if lang_code in ('english', 'arabic'):
                lang_code = 'en' if lang_code == 'english' else 'ar'
            elif lang_code not in ('en', 'ar'):
                lang_code = 'en'  # Default to English
            
            return Settings.NaN_WORDS.get(lang_code, Settings.NaN_WORDS['en'])
        
        # Validate and normalize language
        normalized_lang = Settings.validate_language(lang)
        lang_key = lang.lower()
        
        # Get converter
        if lang_key not in cls._converters:
            raise ValueError(
                f"Unsupported language: {lang}. "
                f"Supported: {list(cls._converters.keys())}"
            )
        
        # Validate conversion type
        to = Settings.validate_conversion_type(to)
        
        converter = cls._converters[lang_key]
        return converter.convert(number, to=to, **kwargs)


def num2words(number: Union[int, float], lang: str = 'en', 
              to: str = 'cardinal', **kwargs) -> str:
    """
    Convert a number to words.
    
    Args:
        number: Integer or float to convert
        lang: Language code ('en', 'ar', 'english', 'arabic')
        to: Conversion type ('cardinal', 'ordinal')
        **kwargs: Additional language-specific parameters (e.g., gender='f' for Arabic)
    
    Returns:
        str: Number in words
    
    Examples:
        >>> num2words(42)
        'forty-two'
        >>> num2words(42, lang='ar')
        'اثنان وأربعون'
        >>> num2words(42, lang='ar', gender='f')
        'اثنتان وأربعون'
    
    Raises:
        ValueError: If language is not supported or number is invalid
        TypeError: If number is not numeric
    """
    return NumberConverter.convert(number, lang=lang, to=to, **kwargs)


def convert(number: Union[int, float], lang: str = 'en', 
           to: str = 'cardinal', **kwargs) -> str:
    """Alias for num2words for convenience."""
    return num2words(number, lang=lang, to=to, **kwargs)

