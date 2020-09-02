"""
Collection of stopwords for multiple languages.

Arthit Suriyawongkul
https://github.com/bact/stopwords-iso
"""

__version__ = "0.6.1"

__all__ = [
    "has_lang",
    "langs",
    "stopwords",
]

from ._core import has_lang, langs, stopwords
