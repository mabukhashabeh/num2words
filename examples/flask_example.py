"""
Flask example usage of numwordify.
"""

from flask import Flask, jsonify, request
from numwordify import num2words

app = Flask(__name__)


@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        'message': 'Number to Words API',
        'endpoints': {
            '/convert/<number>': 'Convert number to words',
            '/health': 'Health check'
        },
        'supported_languages': ['en', 'ar', 'english', 'arabic']
    })


@app.route('/convert/<int:number>')
def convert_number(number):
    """
    Convert a number to words.
    
    Query parameters:
    - lang: Language code (en, ar, english, arabic). Default: en
    - to: Conversion type (cardinal, ordinal). Default: cardinal
    """
    lang = request.args.get('lang', 'en')
    to_type = request.args.get('to', 'cardinal')
    
    try:
        result = num2words(number, lang=lang, to=to_type)
        return jsonify({
            'success': True,
            'number': number,
            'result': result,
            'language': lang,
            'type': to_type
        })
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    except TypeError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


