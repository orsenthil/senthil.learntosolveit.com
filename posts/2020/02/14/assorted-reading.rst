.. title: Reading List : Memory Safety, RSA, Maths, and Learning
.. slug: assorted-reading
.. date: 2020-02-14 02:51:32 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text


`Time safety is more important than memory safety`_

.. admonition:: time safety

   I see choosing "new" languages (or frameworks) as very risky propositions to
   the life of a project. These languages are less likely to be around in ten or
   twenty years time (newer and better Rusts and Gos are likely to form in the
   years ahead) and in the meantime require you to constantly expend effort to
   prevent your projects from being turned into a brick by
   language/environment/library changes. In contrast my old C projects from 5-8
   years ago still compile and run, with one particular example only needing a
   small modification. It's not perfect, but C is much more likely to be the
   "safe" option if time x usefulness of your project is a goal.


Argues that we spend time quickly adopting new languages and frameworks, take it for granted that anything we write
will be short-lived. Author argues that it is wrong philosophy to adopt, and I agree with him.

Choose to experiment, but build something that lasts.

----

`OpenSSH 8.2 released`_

.. admonition:: rsa compromise

    It is now possible[1] to perform chosen-prefix attacks against the
    SHA-1 algorithm for less than USD$50K. For this reason, we will be
    disabling the "ssh-rsa" public key signature algorithm by default in a
    near-future release.

    The better alternatives include:

    The RFC8332 RSA SHA-2 signature algorithms rsa-sha2-256/512. These
    algorithms have the advantage of using the same key type as
    "ssh-rsa" but use the safe SHA-2 hash algorithms. These have been
    supported since OpenSSH 7.2 and are already used by default if the
    client and server support them.

    The ssh-ed25519 signature algorithm. It has been supported in
    OpenSSH since release 6.5.

    The RFC5656 ECDSA algorithms: ecdsa-sha2-nistp256/384/521. These
    have been supported by OpenSSH since release 5.7.

We definitely need a better name for these algorithms. RSA, the term, is so much easier to remember and associate than
SHA-2, ED25519, and ECDSA.

----

`Frank Ramsey - A Genius By All Tests for Genius`_

.. admonition:: genius

   Ramsey did all this, and more, in an alarmingly short lifespan. He died at the
   age of 26 probably from leptospirosis (bacteria from the feces of animals)
   contracted by swimming in the river Cam.

   Rather than focus on a ‘oneness’ or God, like his brother Michael, he thought
   the good life was to be found within our human, fallible, ways of being.

An article about polymath Ramsey who contributed to the field of mathematics, computer science, economics and otherss

----


`Thinking Of Mathematics — An Essay On Eyes-free Computing`_

.. admonition:: once a mathematician, always a mathematician

   At its heart, mathematics is about understanding the underlying structure
   inherent in a given area of interest —and where no such structure exists —to
   deﬁne the minimal structure that is needed to make forward progress.

   The phases involved in the creative process were ﬁrst described by German
   physiologist Herman Helmholtz in the late nineteenth century. He identiﬁed
   three stages of creativity:

   saturation,
   incubation and
   illumination

   These three stages have since been augmented with the additional step of
   veriﬁcation by the scientiﬁc community.

.. admonition::  mathematical techniques are algorithms

   Speciﬁc mathematical techniques e.g., differentiation, integration or the
   Simplex method are algorithms.

   1. To truly appreciate an algorithm and understand how it works, one needs to
      be able to run it by hand on a representative set of examples.

   2. In mathematics, this translates to being able to differentiate or integrate
      a given expression.  

   3. The latter requires a set of semi-mechanical steps and this is where one
      uses aids such as scratch memory provided by pencil and paper —something for
      which I needed to compensate.

   4. However, a true understanding of the underlying algorithm is far more
      important than any speciﬁc technique that one might devise for running the
      algorithm on speciﬁc instances.


I could relate to author's experience in solving some problems.

1. Finding the day of the week. I went by the logic that, 1st January of 1900 was a Monday, and then I figured out
hte day of the week. This problem was given in the book, Let us C, by Yashwant Kanetkar.

2. Playing a nimm like game. I had a designed a similar game called 21-match stick game in the college. It was a very
simple game, wherein the player forced to pick the last match stick looses. This was again from the exercise in the
Yashwant Kanetkar book.

As I recollect, I think, I had a good saturation phase in reading the "Let us C" book by reading, reviewing.
Incubation by trial and errors, and development of the game itself was illumninatiom and when I let my friends play
it, it was the verification stage.

----

`Humans should learn Maths`_

.. admonition:: definitions of maths, science and computing

    Writing: a means to store knowledge in a brain-independent form that can be easily replicated, transmitted and preserved

    Mathematics: a methodology for constructing abstract systems, reasoning about them precisely and finding connections between them

    Science: a methodology for finding abstract systems which map closely to the real world

    Computing: a way to arrange inanimate systems to simulate arbitrary abstract systems

.. admonition:: Maths learning rituals

    Ritual 1: Learn to read and write proofs

    Ritual 2: Learn the language

    Ritual 3: Practice


.. admonition:: cost of ideas

   You won't live long enough to learn more than a tiny fraction of all there is
   to know. Ideas have costs in the time it takes to learn them, the amount of
   maintenance required to remember them and the amount of effort it takes to
   apply them. Prefer ideas that have a high power-to-cost ratio.


Author's writing, explanation and choice of words are excellent.


----

`2014-02-07 Why programming is difficult - Joe Armstrong`_


.. admonition:: what makes programming difficult

   There are three other things that make programming difficult:

   * Fixing things that should not be broken
   * No time for learning things
   * Bad environment for programming

   Let's look at these things - these are all “time thieves“

.. admonition:: Google Casino

   Using the Google casino for bug fixing is terribly frustrating. I Google a bit
   and after a while find a posting where some poor unfortunate soul has
   encountered exactly the same problem that I have. My heart leaps for joy. My
   trembling fingers enter the magic spell that will remove the curse, and ...
   nothing. The problem remains.

The article is hilarious and very deep. I could sense Joe Armstrong's humility in this writing.

----

`Firefox Multicontainer Accounts`_

This is the equivalent to Google Chrome profiles that I was looking.

----

`Gears by Bartosz Ciechanowski`_

Very detailed, step-by-step explanation and interactive demo on how Gears work. I was wondering if the animation is
available via a javascript library. It seems author wrote both the js, css himself to write this article. He is a gem.



.. _Firefox Multicontainer Accounts: https://addons.mozilla.org/en-US/firefox/addon/multi-account-containers/

.. _Time safety is more important than memory safety: https://halestrom.net/darksleep/blog/036_timesafety/

.. _OpenSSH 8.2 released: https://lists.mindrot.org/pipermail/openssh-unix-announce/2020-February/000138.html

.. _Frank Ramsey - A Genius By All Tests for Genius: https://hnn.us/article/174250

.. _Thinking Of Mathematics — An Essay On Eyes-free Computing: http://emacspeak.sourceforge.net/raman/publications/thinking-of-math/thinking-of-math.html

.. _Humans should learn Maths: https://scattered-thoughts.net/writing/humans-should-learn-maths/

.. _2014-02-07 Why programming is difficult - Joe Armstrong: https://joearms.github.io/#2014-02-07%20Why%20programming%20is%20difficult

.. _Gears by Bartosz Ciechanowski: https://ciechanow.ski/gears/
