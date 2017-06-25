.. title: Runway - A distributed systems analysis tool by Salesforce
.. slug: runway-a-distributed-systems-analysis-tool-by-salesforce
.. date: 2016-12-29 17:10:06 UTC-08:00
.. tags: distributed systems, introduction,
.. category:
.. link:
.. description:
.. type: text

Diego Ongaro of Raft_ fame describes a tool that he has been working on at Salesforce. The tool http://runway.systems is
intended to help the designers of distributed systems. The idea is, folks designing distributed systems can encode their
encode their model, specify the states of the system, specify the invariant and run the simulations in the tool.

This tool will help in visualization and analysis of the distributed systems behavior under various conditions. Diego
states that such a system would have been really helpful to him when, if it was available, when he was writing Raft.

In this approachable presentation, he illustrates the tool using.

* A fictional, `too many bananas problem`_
* Simulating an `Elevator Control System`_
* Simulation of `Leader Election and Master Failures in Raft`_

.. youtube:: BAZHZG-8ayo
   :align: center



.. _too many bananas problem: https://github.com/salesforce/runway-model-toomanybananas
.. _Elevator Control System: https://en.wikipedia.org/wiki/Elevator_algorithm
.. _Leader Election and Master Failures in Raft: https://en.wikipedia.org/wiki/Raft_(computer_science)
.. _Raft: https://en.wikipedia.org/wiki/Raft_(computer_science)

