<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/query-string.svg?longCache=True)](https://pypi.org/project/query-string/)
[![](https://img.shields.io/pypi/v/query-string.svg?maxAge=3600)](https://pypi.org/project/query-string/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/query-string.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/query-string.py/)

#### Installation
```bash
$ [sudo] pip install query-string
```

#### Features
+   Python 2/3 compatible

#### Functions
function|`__doc__`
-|-
`query_string.parse(string)` |return dict with query string data
`query_string.query_string(string)` |return dict with query string data. deprecated

#### Examples
```python
>>> import query_string

>>> query_string.parse('https://site.org/index.php?k=v&k2=v2&k3=v3#anchor')
{'k': 'v','k2': 'v2', 'k3': 'v3'}

>>> query_string.parse('k=v&k2=v2&k3=v3')
{'k': 'v','k2': 'v2', 'k3': 'v3'}
```

#### Links
+   [Query string - Wikipedia](https://en.wikipedia.org/wiki/Query_string)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>