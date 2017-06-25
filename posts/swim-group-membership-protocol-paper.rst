.. title: SWIM - Group Membership protocol paper
.. slug: swim-group-membership-protocol-paper
.. date: 2017-01-12 20:54:20 UTC-08:00
.. tags: papers, computer science
.. category:
.. link:
.. description:
.. type: text

For my computer science paper reading, I picked up a paper called `SWIM - Scalable Weakly-consistent Infection style Process Group Membership Protocol`_, which I bookmarked a while ago.

I must have come across this while taking the distributed systems course by `Indranil Gupta`_ in Coursera.
This paper is interesting, approachable and tries to solve the problem of membership updates in distributed systems.

The primary motivation of this seems that heartbeat based member update seem not scalable, so they innovate on providing an alternate mechanism that can utilized for membership updates in a group.

The basic protocol uses the random-probing based failure detector protocol of and disseminates membership updates via
network multicast.

The core innovative concepts include:

* Epidemic style membership broadcast.
* Suspicion-based failure detector protocol.

In turn these provide:

* Constant message load (bandwidth) per member regardless of the number of members in the group
* Constant time to first-detection of a faulty process regardless of the number of members in the group
* Low false-positive failure detection rate

This seems to be a popular paper, and there are many implementations available in the web. I think, I must bookmarked this paper as suggestion to myself that these are interesting projects (in python) to attempt.



.. _Indranil Gupta: http://indy.cs.illinois.edu/

.. _SWIM - Scalable Weakly-consistent Infection style Process Group Membership Protocol: https://www.cs.cornell.edu/~asdas/research/dsn02-swim.pdf
