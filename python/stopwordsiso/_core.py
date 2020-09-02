import json
from typing import Iterable, Set, Union

import pkg_resources

name = "stopwordsiso"

STOPWORDS_FILE = pkg_resources.resource_filename(name, "stopwords-iso.json")

# All language code is ISO 639-1
_STOPWORDS_ALL = {}

with open(STOPWORDS_FILE, encoding="utf-8") as json_data:
    _STOPWORDS_ALL = json.load(json_data)

_LANGS = set(_STOPWORDS_ALL.keys())


def langs() -> Set[str]:
    """Return set of support languages.

    Returns
    -------
    Set[str]
        a set of all support languages, in ISO 639-1 language code.
    """
    return _LANGS


def has_lang(lang: str) -> bool:
    """Check if has stopwords for a language.

    Parameters
    ----------
    lang : str
        a language to check, in ISO 639-1 language code.

    Returns
    -------
    bool
        True if available, False otherwise.
    """
    return lang in _LANGS


def stopwords(langs: Union[str, Iterable[str]]) -> Set[str]:
    """Get a set of stopwords of all requested language.

    Parameters
    ----------
    lang : str, Iterable[str]
        language or a set/list of languages for stopwords, in ISO 639-1 language code.

        stopwordsiso.stopwords("en")  # English stopwords
        stopwordsiso.stopwords(["de", "id", "zh"])  # German, Indonesian, and Chinese stopwords
        stopwordsiso.stopwords("xxx")  # an empty set will be returned for unknown language

    Returns
    -------
    Set[str]
        a set of all stopwords, from every requested languages, combined.
    """
    words = set()

    if langs:
        if type(langs) == str:
            if has_lang(langs):
                words.update(_STOPWORDS_ALL[langs])
        else:
            try:
                iter(langs)  # test if langs is iterable
                for lang in langs:
                    if has_lang(lang):
                        words.update(_STOPWORDS_ALL[lang])
            except TypeError:
                print("'langs' has to be string or iterable.'")

    return words
