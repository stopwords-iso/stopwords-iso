Stopwords ISO
=======

[![Build Status](https://travis-ci.org/stopwords-iso/stopwords-iso.svg?branch=master)](https://travis-ci.org/stopwords-iso/stopwords-iso)
[![devDependencies Status](https://david-dm.org/stopwords-iso/stopwords-iso/dev-status.svg)](https://david-dm.org/stopwords-iso/stopwords-iso?type=dev)

The most comprehensive collection of stopwords for multiple languages.

The collection follows the ISO 639-1 language code.

If you only need stopwords for a specific language, there is a [separate collection for each](https://github.com/stopwords-iso).

### Usage

The collection is in [JSON format](https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json).
You are free to use this collection any way you like.
It is only currently published on [npm](https://www.npmjs.com/stopwords-iso), [bower](https://bower.io), and [pip](https://pypi.org/project/stopwordsiso/).

```sh
$ npm install stopwords-iso
```

```sh
$ bower install stopwords-iso
```

```sh
$ pip install stopwordsiso
```

```js
// Node
const stopwords = require('stopwords-iso'); // object of stopwords for multiple languages
const english = stopwords.en; // english stopwords
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

If you wish to remove or update some of the stopwords, please file an issue first before sending a PR on the repo of the specific language.

If you would like to add a stopword or a new set of stopwords, please add them as a new text file on the repo of the corresponding language.

### Credits

All stopwords sources are [listed here](https://github.com/stopwords-iso/stopwords-iso/blob/master/CREDITS.md).
