# num2words

A lightweight, performant Python package for converting numbers to words in English and Arabic. Designed to work seamlessly with Django, FastAPI, Flask, and other Python frameworks.

## Features

- **Lightweight**: Minimal dependencies, small package size
- **Performant**: Fast conversion with optimized algorithms
- **Easy to use**: Simple, intuitive API
- **Multi-language**: Supports English and Arabic
- **Framework agnostic**: Works with Django, FastAPI, Flask, and more
- **Type support**: Handles integers, floats, negative numbers, and decimals
- **Ordinal numbers**: Supports both cardinal and ordinal conversions
- **Comprehensive**: Handles edge cases including very large numbers, zero, infinity, and NaN

## Installation

```bash
pip install num2words
```

## Quick Start

### Basic Usage

```python
from num2words import num2words

# English
print(num2words(42))
# Output: "forty-two"

print(num2words(1234))
# Output: "one thousand two hundred thirty-four"

# Arabic
print(num2words(42, lang='ar'))
# Output: "اثنان وأربعون"

print(num2words(42, lang='ar', gender='f'))
# Output: "اثنتان وأربعون"
```

### Ordinal Numbers

```python
# English ordinals
print(num2words(1, to='ordinal'))
# Output: "first"

print(num2words(42, to='ordinal'))
# Output: "forty-second"

# Arabic ordinals
print(num2words(1, lang='ar', to='ordinal'))
# Output: "الواحد"
```

### Decimal Numbers

```python
print(num2words(123.45))
# Output: "one hundred twenty-three point forty-five"

print(num2words(123.45, lang='ar'))
# Output: "مئة وثلاثة وعشرون فاصلة خمسة وأربعون"
```

### Negative Numbers

```python
print(num2words(-42))
# Output: "negative forty-two"

print(num2words(-42, lang='ar'))
# Output: "سالب اثنان وأربعون"
```

### Currency Conversion

```python
# English
print(num2words(123.45, to='currency', currency='USD'))
# Output: "one hundred twenty-three dollars and forty-five cents"

print(num2words(100.50, to='currency', currency='EUR'))
# Output: "one hundred euros and fifty cents"

# Arabic
print(num2words(323424.2, to='currency', currency='SAR', lang='ar'))
# Output: "ثلاثة مائة و ثلاثة و عشرون ألف و أربعة مائة و أربعة و عشرون ريالاً و عشرون هللة"

print(num2words(50.25, to='currency', currency='SAR', lang='ar'))
# Output: "خمسون ريالاً و خمسة و عشرون هللة"

print(num2words(123.45, to='currency', currency='JOD', lang='ar'))
# Output: "مائة و ثلاثة و عشرون ديناراً و خمسة و أربعون قرشاً"

print(num2words(50.25, to='currency', currency='EGP', lang='ar'))
# Output: "خمسون جنيهاً و خمسة و عشرون قرشاً"

# Supported currencies: SAR, USD, EUR, EGP, KWD, JOD, BHD, IQD, AED, OMR, QAR, LBP, SYP, TND, DZD, MAD, LYD
```

## Usage with Web Frameworks

### Django

```python
# views.py
from django.http import JsonResponse
from num2words import num2words

def number_to_words(request, number):
    lang = request.GET.get('lang', 'en')
    result = num2words(int(number), lang=lang)
    return JsonResponse({'result': result})
```

### FastAPI

```python
from fastapi import FastAPI
from num2words import num2words

app = FastAPI()

@app.get("/convert/{number}")
async def convert_number(number: int, lang: str = "en"):
    return {"result": num2words(number, lang=lang)}
```

### Flask

```python
from flask import Flask, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route('/convert/<int:number>')
def convert_number(number):
    lang = request.args.get('lang', 'en')
    return jsonify({'result': num2words(number, lang=lang)})
```

## API Reference

### `num2words(number, lang='en', to='cardinal', **kwargs)`

Convert a number to words.

**Parameters:**
- `number` (int or float): The number to convert
- `lang` (str): Language code. Options: `'en'`, `'ar'`, `'english'`, `'arabic'`. Default: `'en'`
- `to` (str): Conversion type. Options: `'cardinal'`, `'ordinal'`, `'currency'`. Default: `'cardinal'`
- `**kwargs`: Additional language-specific parameters:
  - `currency` (str): Currency code for currency conversion. Options: `'SAR'`, `'USD'`, `'EUR'`, `'EGP'`, `'KWD'`, `'JOD'`, `'BHD'`, `'IQD'`, `'AED'`, `'OMR'`, `'QAR'`, `'LBP'`, `'SYP'`, `'TND'`, `'DZD'`, `'MAD'`, `'LYD'`. Default: `'USD'` for English, `'SAR'` for Arabic
  - `gender` (str): For Arabic, use `'m'` (masculine) or `'f'` (feminine). Default: `'m'`

**Returns:**
- `str`: The number in words

**Raises:**
- `TypeError`: If number is not int or float
- `ValueError`: If language is not supported

## Supported Languages

- **English** (`en`, `english`): Full support for cardinal, ordinal, and currency numbers
- **Arabic** (`ar`, `arabic`): Full support with gender options (masculine/feminine) and currency

## Supported Currencies

- **SAR** (Saudi Riyal): 100 halalas per riyal
- **USD** (US Dollar): 100 cents per dollar
- **EUR** (Euro): 100 cents per euro
- **EGP** (Egyptian Pound): 100 piastres per pound
- **KWD** (Kuwaiti Dinar): 1000 fils per dinar
- **JOD** (Jordanian Dinar): 100 piastres per dinar
- **BHD** (Bahraini Dinar): 1000 fils per dinar
- **IQD** (Iraqi Dinar): 1000 fils per dinar
- **AED** (UAE Dirham): 100 fils per dirham
- **OMR** (Omani Rial): 1000 baisa per rial
- **QAR** (Qatari Riyal): 100 dirhams per riyal
- **LBP** (Lebanese Pound): 100 piastres per pound
- **SYP** (Syrian Pound): 100 piastres per pound
- **TND** (Tunisian Dinar): 1000 millimes per dinar
- **DZD** (Algerian Dinar): 100 centimes per dinar
- **MAD** (Moroccan Dirham): 100 centimes per dirham
- **LYD** (Libyan Dinar): 1000 dirhams per dinar

All currencies are configurable via JSON files and can be easily extended. Arabic currency formatting follows proper grammatical rules with tanween (accusative case) for numbers 11 and above.

## Performance

The package is optimized for performance:
- No external dependencies
- Efficient algorithms for number conversion
- Minimal memory footprint
- Fast execution even for large numbers

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### 0.1.0
- Initial release
- English and Arabic language support
- Cardinal and ordinal number conversion
- Decimal and negative number support

