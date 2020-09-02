#!/usr/bin/env python3
"""Generates a table of ISO 639-1:2002 and writes to README.md."""

import json
import os.path
import time
import urllib.request
from html.parser import HTMLParser


class ISO6391TableParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        self._in_tr = (
            self._in_td
        ) = self._code_flag = self._country_flag = False
        self._reset_tdc()
        self._codes = []
        self._names = []
        super().__init__(*args, **kwargs)

    @property
    def code_to_name(self):
        if not hasattr(self, "_code_to_name"):
            c2n = {}
            for c, n in zip(self._codes, self._names):
                if c.isalpha() and c.islower():
                    c2n[c] = n
            self._code_to_name = c2n
        return self._code_to_name

    def _reset_tdc(self):
        self._tdc = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self._in_tr = True
            self._code_flag = self._country_flag = False
        elif self._in_tr and tag == "td":
            self._in_td = True
            self._code_flag = self._tdc == 1
            self._country_flag = self._tdc == 2
            self._tdc += 1

    def handle_endtag(self, tag):
        if tag == "tr":
            self._in_tr = False
            self._reset_tdc()
        elif tag == "td":
            self._in_td = False

    def handle_data(self, data):
        if self._in_td:
            if self._code_flag:
                self._codes.append(data)
            elif self._country_flag:
                self._names.append(data)


def tabulate():
    url = "http://www.loc.gov/standards/iso639-2/php/code_list.php"
    headers = {"User-Agent": "stopwords-iso/stopwords-iso"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("latin-1")

    parser = ISO6391TableParser()
    parser.feed(html)

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "stopwords-iso.json")) as f:
        sw = json.load(f)

    lines = [
        """\
| ISO 639-1 Code | Language | Included Here |
| -------------- | -------- | ------------- |"""
    ]
    check = "\u2713"
    template = "| {code} | {lang} | {incl} |"
    for k, v in parser.code_to_name.items():
        lines.append(
            template.format(code=k, lang=v, incl=check if k in sw else "")
        )
    with open(os.path.join(here, "README.md")) as f:
        readme = f.read()
    readme += """\

### List of Included Languages

_Last updated: {now}_

This table lists the entire set of ISO 639-1:2002 codes, with a check
mark indicating those language codes that are found in `stopwords-iso.json`.

The list of codes itself is from [www.loc.gov](http://www.loc.gov/standards/iso639-2/php/code_list.php), which is
the official "language codes list" and is linked to from [www.iso.org](https://www.iso.org/iso-639-language-codes.html).

{table}
""".format(
        now=time.ctime(), table="\n".join(lines)
    )
    with open(os.path.join(here, "README.md"), "w") as f:
        return f.write(readme)


if __name__ == "__main__":
    tabulate()
