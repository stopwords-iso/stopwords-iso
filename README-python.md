stopwordsiso
=======

Collection of stopwords for multiple languages, using ISO 639-1 language code.

This Python package is based on [Stopwords ISO](https://github.com/stopwords-iso) project by Gene Diaz. You can see the full list of stopwords in every languages available there. Contribution to the word lists should also happen there.

Comparable packages also published on [npm](https://www.npmjs.com/stopwords-iso) and [bower](https://bower.io).

## Installation

```sh
$ pip install stopwordsiso
```

## Usage

```python
import stopwordsiso as stopwords

stopwords.has_lang("th")  # check if there is a stopwords for the language
stopwords.langs()  # return a set of all the supported languages
stopwords.stopwords("en")  # English stopwords
stopwords.stopwords(["de", "id", "zh"])  # German, Indonesian, and Chinese stopwords
stopwords.stopwords("xxx")  # an empty set will be returned for unknown language
```

## Stopwords Data

The entire collection is in JSON format and can be found at [`stopwords-iso.json`](https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json) in your `stopwordsiso/` Python package directory. You are free to use this collection any way you like.

Stopwords for each language is a list value with a key of respective language in ISO 639-1 language code, like this:

```json
{
    "af": [ "aan", "af", "al", "as", ],
    "ar": [ "آض", "آمينَ", "آه", "آهاً", ],
}
```

If you wish to add, remove, or update some of the stopwords, please go to **Stopwords ISO** project at https://github.com/stopwords-iso. 


## Credits

- All stopwords sources are [listed here](https://github.com/stopwords-iso/stopwords-iso/blob/master/CREDITS.md)
- Gene Diaz, stopwords compilation, npm and bower packages
- Arthit Suriyawongkul, Python utility and pip package
