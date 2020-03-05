import json
from typing import Iterable, Set, Union

import pkg_resources

name = "stopwordsiso"

STOPWORDS_FILE = pkg_resources.resource_filename(name, "stopwords-iso.json")

# All language code is ISO 639-1
_stopwords_all = {}

with open(STOPWORDS_FILE) as json_data:
    _stopwords_all = json.load(json_data)

_langs = set(_stopwords_all.keys())


def langs() -> Set[str]:
    return _langs


def has_lang(lang: str) -> bool:
    return lang in _langs


def stopwords(langs: Union[str, Iterable[str]]) -> Set[str]:
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
