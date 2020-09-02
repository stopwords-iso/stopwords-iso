import json
from typing import Iterable, Set, Union

import pkg_resources

name = "stopwordsiso"

STOPWORDS_FILE = pkg_resources.resource_filename(name, "stopwords-iso.json")

# All language code is ISO 639-1
_stopwords_all = {}

with open(STOPWORDS_FILE, encoding="utf-8") as json_data:
    _stopwords_all = json.load(json_data)

_langs = set(_stopwords_all.keys())


def langs() -> Set[str]:
    """Return set of support languages.

    Returns
    -------
    Set[str]
        a set of all support languages, in ISO 639-1 language codes.
    """
    return _langs


def has_lang(lang: str) -> bool:
    """Check if has stopwords for a language.

    Parameters
    ----------
    lang : str, Iterable[str]
        a language or a set/list of languages for stopwords.

    Returns
    -------
    bool
        True if available, False otherwise.
    """
    return lang in _langs


def stopwords(langs: Union[str, Iterable[str]]) -> Set[str]:
    """Get a set of stopwords of all requested language.

    Parameters
    ----------
    lang : str, Iterable[str]
        language or a set/list of languages for stopwords.

    Returns
    -------
    Set[str]
        a set of all stopwords, from every requested languages, combined.

        stopwords.stopwords("en")  # English stopwords
        stopwords.stopwords(["de", "id", "zh"])  # German, Indonesian, and Chinese stopwords
        stopwords.stopwords("xxx")  # an empty set will be returned for unknown language
    """

    """Get a set of stopwords of all requested language.

    """
    words = set()

    if langs:
        if type(langs) == str:
            if has_lang(langs):
                words.update(_stopwords_all[langs])
        else:
            try:
                iter(langs)  # test if langs is iterable
                for lang in langs:
                    if has_lang(lang):
                        words.update(_stopwords_all[lang])
            except TypeError:
                print("'langs' argument is not string nor iterable.'")

    return words
