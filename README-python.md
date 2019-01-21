stopwordsiso
=======

Collection of stopwords for multiple languages, using ISO 639-1 language code.

This Python package is based on [Stopwords ISO](https://github.com/stopwords-iso) project by Gene Diaz. You can see the full list of stopwords in every languages available there. Contribution to the word lists should also happen there.

Comparable packages also published on [npm](https://www.npmjs.com/stopwords-iso) and [bower](https://bower.io).

### Usage

The collection is in [JSON format](https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json).
You are free to use this collection any way you like.

```sh
$ pip install stopwordsiso
```

```python
import stopwordsiso as stopwords

stopwords.has_lang("th") # check if there is a stopwords list for the language
stopwords.list_lang() # list all the supported languages
stopwords.stopwords("en") # get a list of stopwords in a specific language
stopwords.stopwords(["de", "id", "zh"]) # get a combined list of stopwords in multiple languages
stopwords.stopwords("xxx") # an empty list will be returned, if the language is not supported
```

### Contributing

If you wish to add, remove, or update some of the stopwords, please go to Stopwords ISO project at https://github.com/stopwords-iso. 


### Credits

- Gene Diaz, stopwords compilation, npm and bower packages
- Arthit Suriyawongkul, pip package

All stopwords sources are [listed here](https://github.com/stopwords-iso/stopwords-iso/blob/master/CREDITS.md).
