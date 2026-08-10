<!--
.. title: The Norway Problem in Yaml
.. slug: the-norway-problem-in-yaml
.. date: 2026-08-10 14:28:12 UTC+00:00
.. tags: 
.. category:
.. link:
.. description:
.. type: text
-->

Norway's [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) is NO. Under the YAML 1.1 spec, unquoted no (case-insensitive, along with yes, on, off, y, n, true, false) is treated as a boolean and not a string.

You can see the problem here.

```python
~ cat test.yaml
countries:
  - NO
  - SE
  - NL
  - IN
  - US
  - SG

~ python

>>> import yaml
>>> with open("test.yaml") as f:
...     data = yaml.safe_load(f)
...
>>> print(data)
{'countries': [False, 'SE', 'NL', 'IN', 'US', 'SG']}
```

This and other things are fixed [Kubernetes Flavored Yaml](https://kubernetes.io/docs/reference/encodings/kyaml/). Which has minimal syntax like, all flow style syntax with {} for objects and [] for arrays. All string values must be double-quoted.
