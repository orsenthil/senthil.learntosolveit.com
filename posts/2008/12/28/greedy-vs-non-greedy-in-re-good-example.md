.. title: Greedy vs Non-Greedy in Re - Good Example
.. slug: greedy-vs-non-greedy-in-re-good-example
.. date: 2008-12-28 08:47:00
.. tags: python, regex, pattern-matching
.. category: Programming
.. description: Explanation of greedy vs non-greedy pattern matching in Python's regular expression module

Here is a good example to explain greedy vs, non-greedy search using module [re](http://docs.python.org/library/re.html) in Python.


    *The '\*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn't desired; if the RE is matched against '<H1>title</H1>', it will match the entire string, and not just '<H1>'. Adding '?' after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using .\*? in the previous expression will match only '<H1>'.*
