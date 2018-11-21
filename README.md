[![](https://img.shields.io/pypi/pyversions/query_string.svg?longCache=True)](https://pypi.org/pypi/query_string/)
[![](https://img.shields.io/pypi/v/query_string.svg?maxAge=3600)](https://pypi.org/pypi/query_string/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/query_string.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/query_string.py/)

#### Install
```bash
$ [sudo] pip install query_string
```

#### Features
+   Python 2/3 compatible

#### Functions
function|description
-|-
`query_string.parse(string)`|return dict with query string data
`query_string.query_string(string)`|return dict with query string data. deprecated

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>