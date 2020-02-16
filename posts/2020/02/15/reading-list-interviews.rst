.. title: Reading List: Interviews
.. slug: reading-list-interviews
.. date: 2020-02-15 07:53:43 UTC-08:00
.. tags: distributed systems, interviews
.. category: reading
.. link: 
.. description: 
.. type: text


`The Horrifically Dystopian World of Software Engineering Interviews`_

.. admonition:: job search

    I could go on bemoaning the many disappointing experiences I had on this
    slog of a job search. There were many of them. 23 interviews and I didn’t
    get a single offer. I have always sought to be completely honest and humble
    with myself and others about my abilities.

I had a similar experience after getting fired from twitter. I attend 20-30 interviews and I managed to clear one.
The experience frustrated me to no end.

My personal experience at Square interview was one of humiliation. I was escorted out after the 1st round as I could
not write code.


.. admonition:: cottage industry

   There is a cottage industry springing up around passing interviews - All of
   this algorithm challenge hubub started with popular companies like Google.
   There were several engineers who worked at these popular tech companies that
   saw an opportunity to make a few bucks be offering prep material. There were
   two influential books written on the subject: Cracking the Coding Interview and
   Elements of Programming Interviews. Both of these books offer guided interview
   preparation material. The problem is that the industry got a hold of these
   books and tailored their interviews to the book’s material.

This is real. So many start-ups help you prepare for the interview.

.. admonition:: Acceptance

   Complaining about it wont do any good.  - Sooner or later I’m going to have to
   get another job. Even if I don’t like the methodology, I am going to have to go
   through the loop again.

The final conclusions makes it a balanced article, in my opinion.

There is no good way to find the right candidates. These interviews of-course help test if the candidate can code,
has prepared for the interview and is taking the process seriously. I am with this process until we find a better one.


----

`ZooKeeper- Wait-free coordination for Internet-scale systems`_

By Patrick Hunt and Mahadev Konar of Yahoo! Grid and Flavio P. Junqueira and Benjamin Reed of Yahoo! Research


.. admonition:: wait-free

   Our system,  Zookeeper,hence implements an API that manipulates
   simple wait-free data objects organized hierarchically as in file systems.

.. admonition:: Linearizable writes

   With ZooKeeper, we are able to implement all coordination primitives that our applications require, even though
   only writes are linearizable.

.. admonition:: Ordering Gaurantees

   ZooKeeper has two basic ordering guarantees. 
   
   Linearizable writes: All requests that update the state of  ZooKeeper  are
   serializable  and  respect precedence. 
   
   FIFO client order: All requests from a given client are executed  in the
   order  that  they  were  sent  by  the client.


The important design of the Zookeeper was in the Client API used by the clients, server is a well defined architecture.

I used Zookeeper for the Packer service, which is a service to manage artifacts on Aurora scheduler (on Mesos)  at
twitter. ZK was used along with hadoop for storing package metadata. This was overkill for simple operation, and it
was decided migrate the service from ZK to a relational database like MySQL.

I had worked on the client of this service in python and also wrote certain parts the migration client in java.

-----

Byzantine Fault Tolerance
--------------------------

Zookeeper is not Byzantine Fault Tolerant. Author say for the production uses they have have not observed the failure
that could have been prevented by *then* proposed systems to make Zookeeper Byzantine Fault Tolerant.

.. youtube:: dfsRQyYXOsQ

.. _The Horrifically Dystopian World of Software Engineering Interviews: https://www.jarednelsen.dev/posts/The-horrifically-dystopian-world-of-software-engineering-interviews

.. _ZooKeeper- Wait-free coordination for Internet-scale systems: https://www.usenix.org/legacy/event/usenix10/tech/full_papers/Hunt.pdf


-----

Chubby
------

`The Chubby lock service for loosely-coupled distributed systems`_ By Mike Burrows, Google Inc

.. admonition:: intended use

   It is intended for use within a loosely-coupled distributed system consisting
   of moderately large numbers of small machines connected by a high-speed
   network. For example, a Chubby instance (also known as a Chubby cell) might
   serve ten thousand 4-processor machines connected by 1Gbit/s Ethernet. Most
   Chubby cells are confined to a single data centre or machine room, though we do
   run at least one Chubby cell whose replicas are separated by thousands of
   kilometres.

.. admonition:: backup

   Every few hours, the master of each Chubby cell writes a snapshot of its
   database to a GFS file server in a different building. The use of a
   separate building ensures both that the backup will survive building damage,
   and that the backups introduce no cyclic dependencies in the system; a GFS cell
   in the same building potentially might rely on the Chubby cell for electing its
   master.

.. _The Chubby lock service for loosely-coupled distributed systems:  https://static.googleusercontent.com/media/research.google.com/en//archive/chubby-osdi06.pdf
