"""Settings and configuration for num2words package."""

from typing import Dict, Any
from pathlib import Path


class Settings:
    """Centralized settings for num2words package."""
    
    # Package metadata
    PACKAGE_NAME = "num2words"
    VERSION = "0.1.0"
    
    # Default configuration
    DEFAULT_LANGUAGE = "en"
    DEFAULT_CONVERSION_TYPE = "cardinal"
    DEFAULT_GENDER = "m"  # For Arabic
    
    # Supported languages
    SUPPORTED_LANGUAGES = {
        'en': 'english',
        'english': 'english',
        'ar': 'arabic',
        'arabic': 'arabic',
    }
    
    # Conversion types
    CONVERSION_TYPES = {
        'cardinal': 'cardinal',
        'ordinal': 'ordinal',
        'currency': 'currency',
    }
    
    # Supported currencies
    SUPPORTED_CURRENCIES = {
        'SAR': 'Saudi Riyal',
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'EGP': 'Egyptian Pound',
        'KWD': 'Kuwaiti Dinar',
        'JOD': 'Jordanian Dinar',
        'BHD': 'Bahraini Dinar',
        'IQD': 'Iraqi Dinar',
        'AED': 'UAE Dirham',
        'OMR': 'Omani Rial',
        'QAR': 'Qatari Riyal',
        'LBP': 'Lebanese Pound',
        'SYP': 'Syrian Pound',
        'TND': 'Tunisian Dinar',
        'DZD': 'Algerian Dinar',
        'MAD': 'Moroccan Dirham',
        'LYD': 'Libyan Dinar',
    }
    
    # Gender options (for Arabic)
    GENDER_OPTIONS = {
        'm': 'masculine',
        'masculine': 'masculine',
        'f': 'feminine',
        'feminine': 'feminine',
    }
    
    # Configuration file paths (JSON format, no dependencies)
    CONFIG_DIR = Path(__file__).parent.parent / "data"
    ENGLISH_CONFIG = CONFIG_DIR / "english.json"
    ARABIC_CONFIG = CONFIG_DIR / "arabic.json"
    
    # Decimal handling
    MAX_DECIMAL_DIGITS = 10
    MAX_DECIMAL_AS_NUMBER = 2  # Treat decimals with <= 2 digits as numbers
    
    # Scale limits
    MAX_SCALE_INDEX = 11  # Up to decillion
    
    # Special number handling
    INFINITY_WORDS = {
        'en': {
            'positive': 'infinity',
            'negative': 'negative infinity',
        },
        'ar': {
            'positive': 'اللانهاية',
            'negative': 'سالب اللانهاية',
        },
    }
    
    NaN_WORDS = {
        'en': 'not a number',
        'ar': 'ليس رقماً',
    }
    
    @classmethod
    def get_config_path(cls, language: str) -> Path:
        """Get configuration file path for a language."""
        language_map: Dict[str, Path] = {
            'english': cls.ENGLISH_CONFIG,
            'arabic': cls.ARABIC_CONFIG,
        }
        lang_key = cls.SUPPORTED_LANGUAGES.get(language.lower(), language.lower())
        return language_map.get(lang_key, cls.ENGLISH_CONFIG)
    
    @classmethod
    def validate_language(cls, language: str) -> str:
        """Validate and normalize language code."""
        lang_lower = language.lower()
        if lang_lower in cls.SUPPORTED_LANGUAGES:
            return cls.SUPPORTED_LANGUAGES[lang_lower]
        raise ValueError(
            f"Unsupported language: {language}. "
            f"Supported: {list(cls.SUPPORTED_LANGUAGES.keys())}"
        )
    
    @classmethod
    def validate_conversion_type(cls, conversion_type: str) -> str:
        """Validate conversion type."""
        conv_lower = conversion_type.lower()
        if conv_lower in cls.CONVERSION_TYPES:
            return cls.CONVERSION_TYPES[conv_lower]
        raise ValueError(
            f"Invalid conversion type: {conversion_type}. "
            f"Must be one of: {list(cls.CONVERSION_TYPES.keys())}"
        )
    
    @classmethod
    def validate_currency(cls, currency: str) -> str:
        """Validate currency code."""
        currency_upper = currency.upper()
        if currency_upper in cls.SUPPORTED_CURRENCIES:
            return currency_upper
        raise ValueError(
            f"Unsupported currency: {currency}. "
            f"Supported: {list(cls.SUPPORTED_CURRENCIES.keys())}"
        )
    
    @classmethod
    def validate_gender(cls, gender: str) -> str:
        """Validate gender option."""
        gender_lower = gender.lower()
        if gender_lower in cls.GENDER_OPTIONS:
            return gender_lower[0]  # Return 'm' or 'f'
        raise ValueError(
            f"Invalid gender: {gender}. "
            f"Must be one of: {list(cls.GENDER_OPTIONS.keys())}"
        )

