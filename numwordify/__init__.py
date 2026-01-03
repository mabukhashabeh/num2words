"""
numwordify - A lightweight, performant number-to-words converter
Supporting English and Arabic languages.
"""

__version__ = "0.1.0"
__author__ = "Mohammad Abu Khahsabeh"
__email__ = "abukhashabehmohammad@gmail.com"

from .converter import num2words, convert

__all__ = ["num2words", "convert"]

