Stopwords ISO
=======

The most comprehensive collection of stopwords for multiple languages.

The collection follows the ISO 639-1 language code.

If you only need stopwords for a specific language, there is a [separate collection for each](https://github.com/stopwords-iso).

## Usage

The collection is in [JSON format](https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json).
You are free to use this collection any way you like.
It is only currently published on [npm](https://www.npmjs.com/stopwords-iso), [bower](https://bower.io), and [pip](https://pypi.org/project/stopwordsiso/).

### Node/JavaScript

```sh
$ npm install stopwords-iso
```

```sh
$ bower install stopwords-iso
```

```js
// Node
const stopwords = require('stopwords-iso');  // object of stopwords for multiple languages
const english = stopwords.en;  // English stopwords
```

### Python

```sh
$ pip install stopwordsiso
```

```python
# Python
import stopwordsiso as stopwords

stopwords.has_lang("th")  # check if there is a stopwords for the language
stopwords.langs()  # return a set of all the supported languages
stopwords.stopwords("en")  # English stopwords
stopwords.stopwords(["de", "id", "zh"])  # German, Indonesian, and Chinese stopwords
stopwords.stopwords("xxx")  # an empty set will be returned for unknown language
```

## Contributing

If you wish to remove or update some of the stopwords, please file an issue first before sending a PR on the repo of the specific language.

If you would like to add a stopword or a new set of stopwords, please add them as a new text file on the repo of the corresponding language.

## Credits

All stopwords sources are [listed here](https://github.com/stopwords-iso/stopwords-iso/blob/master/CREDITS.md).

### List of Included Languages

This table lists the entire set of ISO 639-1:2002 codes, with a check
mark indicating those language codes that are found in `stopwords-iso.json`.

The list of codes itself is from [www.loc.gov](http://www.loc.gov/standards/iso639-2/php/code_list.php), which is
the official "language codes list" and is linked to from [www.iso.org](https://www.iso.org/iso-639-language-codes.html).

| ISO 639-1 Code | Language | Included Here |
| -------------- | -------- | ------------- |
| aa | Afar |  |
| ab | Abkhazian |  |
| af | Afrikaans | ✓ |
| ak | Akan |  |
| sq | Albanian |  |
| am | Amharic |  |
| ar | Arabic | ✓ |
| an | Aragonese |  |
| hy | Armenian | ✓ |
| as | Assamese |  |
| av | Avaric |  |
| ae | Avestan |  |
| ay | Aymara |  |
| az | Azerbaijani |  |
| ba | Bashkir |  |
| bm | Bambara |  |
| eu | Basque | ✓ |
| be | Belarusian |  |
| bn | Bengali | ✓ |
| bh | Bihari languages |  |
| bi | Bislama |  |
| bo | Tibetan |  |
| bs | Bosnian |  |
| br | Breton | ✓ |
| bg | Bulgarian | ✓ |
| my | Burmese |  |
| ca | Catalan; Valencian | ✓ |
| cs | Czech | ✓ |
| ch | Chamorro |  |
| ce | Chechen |  |
| zh | Chinese | ✓ |
| cu | Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic |  |
| cv | Chuvash |  |
| kw | Cornish |  |
| co | Corsican |  |
| cr | Cree |  |
| cy | Welsh |  |
| da | Danish | ✓ |
| de | German | ✓ |
| dv | Divehi; Dhivehi; Maldivian |  |
| nl | Dutch; Flemish | ✓ |
| dz | Dzongkha |  |
| el | Greek, Modern (1453-) | ✓ |
| en | English | ✓ |
| eo | Esperanto | ✓ |
| et | Estonian | ✓ |
| ee | Ewe |  |
| fo | Faroese |  |
| fa | Persian | ✓ |
| fj | Fijian |  |
| fi | Finnish | ✓ |
| fr | French | ✓ |
| fy | Western Frisian |  |
| ff | Fulah |  |
| ka | Georgian |  |
| gd | Gaelic; Scottish Gaelic |  |
| ga | Irish | ✓ |
| gl | Galician | ✓ |
| gv | Manx |  |
| gn | Guarani |  |
| gu | Gujarati |  |
| ht | Haitian; Haitian Creole |  |
| ha | Hausa | ✓ |
| he | Hebrew | ✓ |
| hz | Herero |  |
| hi | Hindi | ✓ |
| ho | Hiri Motu |  |
| hr | Croatian | ✓ |
| hu | Hungarian | ✓ |
| ig | Igbo |  |
| is | Icelandic |  |
| io | Ido |  |
| ii | Sichuan Yi; Nuosu |  |
| iu | Inuktitut |  |
| ie | Interlingue; Occidental |  |
| ia | Interlingua (International Auxiliary Language Association) |  |
| id | Indonesian | ✓ |
| ik | Inupiaq |  |
| it | Italian | ✓ |
| jv | Javanese |  |
| ja | Japanese | ✓ |
| kl | Kalaallisut; Greenlandic |  |
| kn | Kannada |  |
| ks | Kashmiri |  |
| kr | Kanuri |  |
| kk | Kazakh |  |
| km | Central Khmer |  |
| ki | Kikuyu; Gikuyu |  |
| rw | Kinyarwanda |  |
| ky | Kirghiz; Kyrgyz |  |
| kv | Komi |  |
| kg | Kongo |  |
| ko | Korean | ✓ |
| kj | Kuanyama; Kwanyama |  |
| ku | Kurdish | ✓ |
| lo | Lao |  |
| la | Latin | ✓ |
| lv | Latvian | ✓ |
| li | Limburgan; Limburger; Limburgish |  |
| ln | Lingala |  |
| lt | Lithuanian | ✓ |
| lb | Luxembourgish; Letzeburgesch |  |
| lu | Luba-Katanga |  |
| lg | Ganda |  |
| mk | Macedonian |  |
| mh | Marshallese |  |
| ml | Malayalam |  |
| mi | Maori |  |
| mr | Marathi | ✓ |
| ms | Malay | ✓ |
| mg | Malagasy |  |
| mt | Maltese |  |
| mn | Mongolian |  |
| na | Nauru |  |
| nv | Navajo; Navaho |  |
| nr | Ndebele, South; South Ndebele |  |
| nd | Ndebele, North; North Ndebele |  |
| ng | Ndonga |  |
| ne | Nepali |  |
| nn | Norwegian Nynorsk; Nynorsk, Norwegian |  |
| nb | Bokmål, Norwegian; Norwegian Bokmål |  |
| no | Norwegian | ✓ |
| ny | Chichewa; Chewa; Nyanja |  |
| oc | Occitan (post 1500) |  |
| oj | Ojibwa |  |
| or | Oriya |  |
| om | Oromo |  |
| os | Ossetian; Ossetic |  |
| pa | Panjabi; Punjabi |  |
| pi | Pali |  |
| pl | Polish | ✓ |
| pt | Portuguese | ✓ |
| ps | Pushto; Pashto |  |
| qu | Quechua |  |
| rm | Romansh |  |
| ro | Romanian; Moldavian; Moldovan | ✓ |
| rn | Rundi |  |
| ru | Russian | ✓ |
| sg | Sango |  |
| sa | Sanskrit |  |
| si | Sinhala; Sinhalese |  |
| sk | Slovak | ✓ |
| sl | Slovenian | ✓ |
| se | Northern Sami |  |
| sm | Samoan |  |
| sn | Shona |  |
| sd | Sindhi |  |
| so | Somali | ✓ |
| st | Sotho, Southern | ✓ |
| es | Spanish; Castilian | ✓ |
| sc | Sardinian |  |
| sr | Serbian |  |
| ss | Swati |  |
| su | Sundanese |  |
| sw | Swahili | ✓ |
| sv | Swedish | ✓ |
| ty | Tahitian |  |
| ta | Tamil |  |
| tt | Tatar |  |
| te | Telugu |  |
| tg | Tajik |  |
| tl | Tagalog | ✓ |
| th | Thai | ✓ |
| ti | Tigrinya |  |
| to | Tonga (Tonga Islands) |  |
| tn | Tswana |  |
| ts | Tsonga |  |
| tk | Turkmen |  |
| tr | Turkish | ✓ |
| tw | Twi |  |
| ug | Uighur; Uyghur |  |
| uk | Ukrainian | ✓ |
| ur | Urdu | ✓ |
| uz | Uzbek |  |
| ve | Venda |  |
| vi | Vietnamese | ✓ |
| vo | Volapük |  |
| wa | Walloon |  |
| wo | Wolof |  |
| xh | Xhosa |  |
| yi | Yiddish |  |
| yo | Yoruba | ✓ |
| za | Zhuang; Chuang |  |
| zu | Zulu | ✓ |
