<html><body><p>The question was:



In Python we can emulate multiline comments using triple-quoted

strings, but conceptually strings and comments are very different.

I.e. strings are objects, comments are auxillary text discarded at

compile time. Strings are objects created at runtime, comments are

not.



The answer from Steven D'Aprano:



Guido's time-machine strikes again.



</p><pre>



&gt;&gt;&gt; import dis

&gt;&gt;&gt; def test():

...     x = 1

...     """

...     This is a triple-quote comment.

...     """

...     return x

...

&gt;&gt;&gt; dis.dis(test)

  2           0 LOAD_CONST               1 (1)

              3 STORE_FAST               0 (x)



  6           6 LOAD_FAST                0 (x)

              9 RETURN_VALUE



</pre>



String literals -- not just triple-quoted strings, but any string 

literal -- that don't go anywhere are discarded by the Python compiler, 

precisely so they can be used as comments.</body></html>