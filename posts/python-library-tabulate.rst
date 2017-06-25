.. title: Python Library: tabulate
.. slug: python-library-tabulate
.. date: 2016-08-20 22:52:19 UTC-07:00
.. tags: python
.. category:
.. link:
.. description:
.. type: text

I prefer to use Restructured Text for my posts, but drawing tables in Restructured text has always been tricky for me.
Getting the columns right, drawing and aligning the bar characters is a frustrating exercise for me.

The best to draw tables is to then generate it. I've tried ascii art table maker and I have not been very impressed or
successful with it.

I tried a python library called tabulate_ which can be used to print the table in restructed text format.
The table could easily be constructed using python data structures like list.

Here is an example table of Graph applications, which shows the concept graphs, their vertices and edges.

===================  ============================  ===========================
graph                vertex                        edge
===================  ============================  ===========================
communication        telephone, computer           fiber optic cable
circuit              gate, register, processor     wire
mechanical           joint                         rod, beam, spring
financial            stock, currency               transactions
transportation       street intersection, airport  highway, airway route
internet             class C network               connection
game                 board position                legal move
social relationship  person, actor                 friendship, movie cast
neural network       neuron                        synapse
protein network      protein                       protein-protein interaction
molecule             atom                          bond
===================  ============================  ===========================

This table was generated using this python program.


.. listing:: python/tabulate_example.py python


I landed upon tabulate when another python library by name PTable_ did not provide a restructured text specific formatting. If you just prefer ASCII tables, then that's a convenient library as well.


.. target-notes::

.. _tabulate: https://bitbucket.org/astanin/python-tabulate
.. _PTable: https://ptable.readthedocs.io/en/latest/tutorial.html
