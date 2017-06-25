.. title: Python Programming Patterns
.. slug: python-programming-patterns
.. date: 2016-09-04 16:19:13 UTC-07:00
.. tags: python
.. category:
.. link:
.. description:
.. type: text

I can write idiomatic code both in Python and Java. Sometimes, when working with large teams, I prefer Java over
Python. I am excited by the sturdiness, standardized and elaborate solutions written in Java. It gives me ample
opportunity to learn and understand the world better.

Python, on the other hand, is a simple language. The rules of usage are very simple. It seems to me that, the driving
force behind python, Guido Van Rossum,  always prefers simplicity over anything else.

Here are his thoughts on writing python programs that can be fast (quoted verbatim)


    - Avoid overengineering datastructures. Tuples are better than objects (try namedtuple too though). Prefer simple fields over getter/setter functions.

    - Built-in datatypes are your friends. Use more numbers, strings, tuples, lists, sets, dicts. Also check out the collections library, esp. deque.

    - Be suspicious of function/method calls; creating a stack frame is expensive.

    - Don't write Java (or C++, or Javascript, ...) in Python.

    - Are you sure it's too slow? Profile before optimizing!

    - The universal speed-up is rewriting small bits of code in C. Do this only when all else fails.﻿

    `Guido van Rossum`_

.. _Guido van Rossum: https://plus.google.com/115212051037621986145/posts/HajXHPGN752


It is best to adopt all these without shame, that is, writing simple programs, using most common data structures. The
above list creates a very low barrier for writing large programs. In addition to the above list, I think, if we ever
write a python program which gets deployed to production, (meaning there is money / life at stake), having it readable,
and having unit-tests and coverage will give confidence in the program. Making this a habit is a hard task, but if
something can be adopted from the good parts of Java world, then the discipline for these hard tasks can be cultivated
in the python world too.




