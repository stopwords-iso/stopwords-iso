import json
from typing import List, Union

import pkg_resources

name = "stopwordsiso"

STOPWORDS_FILE = pkg_resources.resource_filename(name, "stopwords-iso.json")

# All language code is ISO 639-1
stopwords_all = {}

with open(STOPWORDS_FILE) as json_data:
    stopwords_all = json.load(json_data)

langs = list(stopwords_all.keys())


def list_lang() -> List[str]:
    return langs


def has_lang(lang: str) -> bool:
    return lang in langs


def stopwords(langs: Union[str, List[str]]) -> List[str]:
    words = list()

    if type(langs) == str:
        if has_lang(langs):
            words.extend(stopwords_all[langs])
    elif type(langs) == list:
        for lang in langs:
            if has_lang(lang):
                words.extend(stopwords_all[lang])

    words = list(set(words))
    words.sort()

    return words
