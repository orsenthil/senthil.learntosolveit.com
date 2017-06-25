<html><body><p>Here is a good example to explain greedy vs, non-greedy search using module <a href="http://docs.python.org/library/re.html">re</a> in Python.



<i>



*?, +?, ??



The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible. Sometimes this behaviour isn’t desired; if the RE  is matched against '&lt;H1&gt;title&lt;/H1&gt;', it will match the entire string, and not just '&lt;H1&gt;'. Adding '?' after the qualifier makes it perform the match in non-greedy or minimal fashion; as few characters as possible will be matched. Using .*? in the previous expression will match only '&lt;H1&gt;'.

</i></p></body></html>