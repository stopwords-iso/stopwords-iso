import json

# All language code is ISO 639-1

name = "stopwordsiso"

stopwods_all = ""

with open("stopwords-iso.json") as json_data:
    stopwords_all = json.load(json_data)

langs = list(stopwords_all.keys())


def list_lang():
    return langs


def has_lang(lang):
    return lang in langs


def stopwords(langs):
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
