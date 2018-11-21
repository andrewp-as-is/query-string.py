#!/usr/bin/env python
import query_string

assert query_string.parse("") == {}
assert query_string.parse("https://site.com") == {}

data = dict(k="v",k2="v2",k3="v3")
assert query_string.parse("https://site.org/index.php?k=v&k2=v2&k3=v3") == data
assert query_string.parse("index.php?k=v&k2=v2&k3=v3") == data
assert query_string.parse("k=v&k2=v2&k3=v3") == data
