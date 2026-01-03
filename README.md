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
- `to` (str): Conversion type. Options: `'cardinal'`, `'ordinal'`. Default: `'cardinal'`
- `**kwargs`: Additional language-specific parameters:
  - `gender` (str): For Arabic, use `'m'` (masculine) or `'f'` (feminine). Default: `'m'`

**Returns:**
- `str`: The number in words

**Raises:**
- `TypeError`: If number is not int or float
- `ValueError`: If language is not supported

## Supported Languages

- **English** (`en`, `english`): Full support for cardinal and ordinal numbers
- **Arabic** (`ar`, `arabic`): Full support with gender options (masculine/feminine)

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

