.. title: Computer Bugs - Roundoff Error and the Patriot Missile
.. slug: computer-bugs-roundoff-error-and-the-patriot-missile
.. date: 2017-07-17 09:09:13 UTC-07:00
.. tags: bugs
.. category:
.. link:
.. description:
.. type: text

0.10
----

* During the Gulf War in 1991, a U.S. Patriot missile failed to intercept an
* Iraqi Scud missile, and 28 Americans were killed.
* A later study determined that the problem was caused by the inaccuracy of the binary representation of 0.10.
* The Patriot incremented a counter once every 0.10 seconds.
* It multiplied the counter value by 0.10 to compute the actual time. However, the (24-bit) binary representation of 0.10 actually corresponds to 0.099999904632568359375, which is off by 0.000000095367431640625.
* This doesn’t seem like much, but after 100 hours the time ends up being off by 0.34 seconds—enough time for a Scud to travel 500 meters!
* Professor Skeel wrote a `short article`_ about this.

.. _short article: http://mate.uprh.edu/~pnegron/notas4061/patriot.htm
