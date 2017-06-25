.. title: Coconut Lang
.. slug: coconut-lang
.. date: 2016-12-28 15:08:30 UTC-08:00
.. tags: programming
.. category:
.. link:
.. description:
.. type: text

With the trend in functional programming up, I noticed a new programming language called "coconut" that implements
functional programing "style". This is written on top of "python", the coconut language scripts are compiled and
translated to python.

For e.g, this factorial coconut program, will be translated to a valid python program.


::

    def factorial(n):
        """Compute n! where n is an integer >= 0."""
        case n:
            match 0:
                return 1
            match _ is int if n > 0:
                return n * factorial(n-1)
        else:
            raise TypeError("the argument to factorial must be an integer >= 0")



You can notice the pattern matching style in the above program, which is not a syntax in Python. This program will then
be converted into a valid python program.

Great many details can be found in the coconut-lang_ website.

.. _coconut-lang: http://coconut-lang.org/

