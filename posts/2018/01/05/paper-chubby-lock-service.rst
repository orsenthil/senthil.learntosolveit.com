.. title: Paper: Chubby Lock Service
.. slug: paper-chubby-lock-service
.. date: 2018-01-05 22:24:55 UTC-08:00
.. tags: papers-2018
.. category:
.. link:
.. description:
.. type: text


`The Chubby Lock Service for Loosely-Coupled Distributed Systems`_ is the internal distributed lock service that
Google uses. The paper shares the motivation and the design of the system. The focus is on a distributed lock, and
reliability given by paxos implementation. It seems that chubby is also used for the distributed DNS.

Open source Zookeeper project is modelled after this system.

.. _The Chubby Lock Service for Loosely-Coupled Distributed Systems: https://research.google.com/archive/chubby-osdi06.pdf
