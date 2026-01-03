"""
Main converter module for numwordify package.
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
        
        # Validate currency if currency conversion
        if to == 'currency':
            currency = kwargs.get('currency', 'USD' if lang_key == 'english' else 'SAR')
            if hasattr(converter, 'currencies'):
                if currency not in converter.currencies:
                    raise ValueError(
                        f"Unsupported currency: {currency}. "
                        f"Supported: {list(converter.currencies.keys())}"
                    )
            kwargs['currency'] = currency
        
        return converter.convert(number, to=to, **kwargs)


def num2words(number: Union[int, float], lang: str = 'en', 
              to: str = 'cardinal', **kwargs) -> str:
    """
    Convert a number to words.
    
    Args:
        number: Integer or float to convert
        lang: Language code ('en', 'ar', 'english', 'arabic')
        to: Conversion type ('cardinal', 'ordinal', 'currency')
        **kwargs: Additional language-specific parameters:
            - currency: Currency code for currency conversion ('SAR', 'USD', 'EUR', 'EGP', 'KWD')
            - gender: For Arabic, use 'm' (masculine) or 'f' (feminine)
    
    Returns:
        str: Number in words
    
    Examples:
        >>> num2words(42)
        'forty-two'
        >>> num2words(42, lang='ar')
        'اثنان وأربعون'
        >>> num2words(42, lang='ar', gender='f')
        'اثنتان وأربعون'
        >>> num2words(123.45, to='currency', currency='USD')
        'one hundred twenty-three dollars and forty-five cents'
        >>> num2words(323424.2, to='currency', currency='SAR', lang='ar')
        'ثلاث مئة وثلاثة وعشرون آلاف وأربع مئة وأربعة وعشرون ريالات وعشرون هللات'
    
    Raises:
        ValueError: If language is not supported or number is invalid
        TypeError: If number is not numeric
    """
    return NumberConverter.convert(number, lang=lang, to=to, **kwargs)


def convert(number: Union[int, float], lang: str = 'en', 
           to: str = 'cardinal', **kwargs) -> str:
    """Alias for num2words for convenience."""
    return num2words(number, lang=lang, to=to, **kwargs)

