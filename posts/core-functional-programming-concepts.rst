.. title: Core Functional Programming Concepts
.. slug: core-functional-programming-concepts
.. date: 2016-12-27 18:04:16 UTC-08:00
.. tags: introduction
.. category:
.. link:
.. description:
.. type: text

Found this introductory post on `core functional programming concepts`_ dealing with the subject succinctly.
It is easy to approach functional programming, if we can recognize the following concepts held true by all the
functional programs, and languages facilitating them.

1. Functions are Pure

    * No side-effects, like printing something from the function.
    * When called with the same input, will always return the same output. We take that for granted, isn't it?

2. Functions are first-class and are of higher order.

    * Treat function names as variables.
    * Toss function (names) as an argument to a function, and as a return value from a function.

3. Variables are immutable.

    * Forget mutating variables in a program. If you want an updated value, create a new variable. When you are
      getting started with programming, you feel this is questionable. With experience under your belt, you start
      to prefer immutability of variables.

4. Functions have referential transparency.

    * It follows from functions are pure requirement. The referential transparency requirement is about substituting
      the function call with return value, wherever the function is called, should not change the state of the program.

5. Lambda Calculus

    * The mathematics behind functional programming. Take arguments and have a return valued. When evaluating multiple
      arguments, the function is evaluated one argument at a time, with result send to next one-arg-less function,
      kind of a tail-recursion. This concept is called currying.







.. _core functional programming concepts: https://thesocietea.org/2016/12/core-functional-programming-concepts/
