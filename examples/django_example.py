"""
Django example usage of num2words.

Add this to your Django views.py or create a separate views file.
"""

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from num2words import num2words


@require_http_methods(["GET"])
def number_to_words(request, number):
    """
    Django view to convert number to words.
    
    URL pattern (in urls.py):
    path('convert/<int:number>/', views.number_to_words, name='number_to_words'),
    """
    lang = request.GET.get('lang', 'en')
    to_type = request.GET.get('to', 'cardinal')
    
    try:
        result = num2words(int(number), lang=lang, to=to_type)
        return JsonResponse({
            'success': True,
            'number': number,
            'result': result,
            'language': lang
        })
    except (ValueError, TypeError) as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)


# Django template filter example
# Add to your templatetags/number_filters.py
from django import template
from num2words import num2words

register = template.Library()

@register.filter(name='num2words')
def num2words_filter(value, lang='en'):
    """Django template filter for num2words."""
    try:
        return num2words(int(value), lang=lang)
    except (ValueError, TypeError):
        return value

# Usage in template:
# {{ 42|num2words }}
# {{ 42|num2words:"ar" }}

