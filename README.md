<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/query-string.svg?maxAge=3600)](https://pypi.org/project/query-string/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/query-string.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/query-string.py/actions)

### Installation
```bash
$ [sudo] pip install query-string
```

#### Features
+   Python 2/3 compatible

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
    <a href="https://readme42.com/">readme42.com</a>
</p>
