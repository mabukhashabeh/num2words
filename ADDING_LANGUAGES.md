# Adding New Languages

This guide explains how to add support for a new language to numwordify.

## Overview

The numwordify package uses JSON configuration files (built-in, no dependencies) to store language translations. This makes it easy to:
- Add new languages
- Update existing translations
- Maintain consistency across languages

## Steps to Add a New Language

### 1. Create JSON Configuration File

Create a new JSON file in `numwordify/data/` directory. For example, `french.json`:

```json
{
  "language": "french",
  "code": "fr",
  "ones": [
    "",
    "un",
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "onze",
    "douze",
    "treize",
    "quatorze",
    "quinze",
    "seize",
    "dix-sept",
    "dix-huit",
    "dix-neuf"
  ],
  "tens": [
    "",
    "",
    "vingt",
    "trente",
    "quarante",
    "cinquante",
    "soixante",
    "soixante-dix",
    "quatre-vingt",
    "quatre-vingt-dix"
  ],
  "ordinal_ones": [
    "",
    "premier",
    "deuxième",
    "troisième"
  ],
  "scales": [
    "",
    "mille",
    "million",
    "milliard"
  ],
  "zero": "zéro",
  "hundred": "cent",
  "negative_prefix": "moins",
  "decimal_separator": "virgule",
  "number_separator": "-",
  "scale_separator": " "
}
```

### 2. Create Language Converter Class

Create a new converter class in `numwordify/languages/french.py`:

```python
"""
French number-to-words converter.
Uses YAML configuration for translations.
"""

from typing import Union
from .base import BaseConverter
from ..config.loader import ConfigLoader
from ..config.settings import Settings


class FrenchConverter(BaseConverter):
    """French language converter using YAML configuration."""
    
    def __init__(self):
        """Initialize French converter with configuration."""
        super().__init__()
        self.load_config('french')
        self._initialize_from_config()
    
    def _initialize_from_config(self) -> None:
        """Initialize converter data structures from configuration."""
        config = self.config
        self.ones = config.get('ones', [])
        self.tens = config.get('tens', [])
        # ... initialize other attributes
    
    def convert(self, number: Union[int, float], to: str = 'cardinal', **kwargs) -> str:
        """Convert number to French words."""
        # Implement conversion logic
        pass
    
    def _to_cardinal(self, number: int) -> str:
        """Convert integer to cardinal French words."""
        # Implement cardinal conversion
        pass
    
    def _to_ordinal(self, number: int) -> str:
        """Convert integer to ordinal French words."""
        # Implement ordinal conversion
        pass
```

### 3. Register Language in Settings

Update `numwordify/config/settings.py`:

```python
SUPPORTED_LANGUAGES = {
    'en': 'english',
    'english': 'english',
    'ar': 'arabic',
    'arabic': 'arabic',
    'fr': 'french',        # Add this
    'french': 'french',    # Add this
}

# Add config path
FRENCH_CONFIG = CONFIG_DIR / "french.yaml"
```

Update `get_config_path` method:

```python
language_map: Dict[str, Path] = {
    'english': cls.ENGLISH_CONFIG,
    'arabic': cls.ARABIC_CONFIG,
    'french': cls.FRENCH_CONFIG,  # Add this
}
```

### 4. Register Converter

Update `numwordify/converter.py`:

```python
from .languages.french import FrenchConverter

class NumberConverter:
    @classmethod
    def _initialize_converters(cls) -> None:
        if not cls._initialized:
            cls._converters = {
                'en': EnglishConverter(),
                'english': EnglishConverter(),
                'ar': ArabicConverter(),
                'arabic': ArabicConverter(),
                'fr': FrenchConverter(),      # Add this
                'french': FrenchConverter(), # Add this
            }
            cls._initialized = True
```

### 5. Add Special Words (if needed)

If your language has special words for infinity or NaN, update `Settings`:

```python
INFINITY_WORDS = {
    'en': {'positive': 'infinity', 'negative': 'negative infinity'},
    'ar': {'positive': 'اللانهاية', 'negative': 'سالب اللانهاية'},
    'fr': {'positive': 'infini', 'negative': 'moins infini'},  # Add this
}

NaN_WORDS = {
    'en': 'not a number',
    'ar': 'ليس رقماً',
    'fr': 'pas un nombre',  # Add this
}
```

### 6. Write Tests

Create test file `tests/test_french.py`:

```python
"""Tests for French number conversion."""

import unittest
from numwordify import num2words


class TestFrenchConversion(unittest.TestCase):
    """Test French number to words conversion."""
    
    def test_basic_numbers(self):
        """Test basic number conversions."""
        self.assertEqual(num2words(1, lang='fr'), "un")
        self.assertEqual(num2words(42, lang='fr'), "quarante-deux")
        # ... add more tests
```

### 7. Update Documentation

- Update `README.md` with new language examples
- Update `CHANGELOG.md`
- Update language list in documentation

## JSON Configuration Structure

### Required Fields

- `language`: Language name (e.g., "french")
- `code`: Language code (e.g., "fr")
- `ones`: List of words for 0-19
- `tens`: List of words for tens (20, 30, ..., 90)
- `zero`: Word for zero
- `hundred`: Word for hundred
- `negative_prefix`: Prefix for negative numbers
- `decimal_separator`: Word/character for decimal point

### Optional Fields

- `ordinal_ones`: List of ordinal words for 0-19
- `ordinal_tens`: List of ordinal words for tens
- `scales`: List of scale words (thousand, million, etc.)
- `ordinal_scales`: List of ordinal scale words
- `number_separator`: Separator for compound numbers (e.g., "twenty-one")
- `scale_separator`: Separator between number and scale

### Language-Specific Fields

Some languages may need additional fields:
- Arabic: `ones_masculine`, `ones_feminine`, `scales_dual`, `scales_plural`, `conjunction`
- Others: Add as needed for your language

## Best Practices

1. **Follow Existing Patterns**: Look at `english.yaml` and `arabic.yaml` as examples
2. **Test Thoroughly**: Write comprehensive tests for your language
3. **Handle Edge Cases**: Zero, negative numbers, decimals, very large numbers
4. **Documentation**: Update all relevant documentation
5. **Consistency**: Follow the same structure as existing languages

## Example: Complete French JSON

See `numwordify/data/english.json` for a complete example structure that you can adapt for your language.

## Questions?

If you need help adding a language, please:
1. Check existing language implementations
2. Open an issue on GitHub
3. Submit a pull request with your implementation

