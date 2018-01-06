.. title: Article: Making Applications scalable with load-balacing
.. slug: article-making-applications-scalable-with-load-balacing
.. date: 2018-01-04 19:14:30 UTC-08:00
.. tags: papers-2018
.. category:
.. link:
.. description:
.. type: text

This article titled, `"Making applications scalable with Load Balancing"`_
by the author of the famous software `HAProxy`_ introduces
the concept of load-balancing and talks about the need for load-balancing.

Definitions
-----------

*Scaling* - Since the power of any server is limited, a web application must be able to run on
multiple servers to accept an ever increasing number of users. this is called as scaling. when
application is running on internet, the site's maintainer has to find ways to spread the load
on several servers, either through internal mechanisms, external components or via re-design.

*Load Balancing* - Load Balancing is the ability make several
servers participate in the same service and do the same work.

*High Availability* - The ability to maintain unaffected service during
any previous number of simultaneous failures is called high availability.

The point is, *load balancing* and *high availability* are different.

The article focuses the different load-balancing options, gives details on Layer 3/4 load balancer, Layer 7 load
balancer and where those are used.

.. image::  https://dl.dropbox.com/s/qf9ksk6z56oamtk/scalable_architecture.png
   :align: center
   :height: 300
   :width: 450

.. _HAProxy: http://www.haproxy.org/
.. _"Making applications scalable with Load Balancing": http://wtarreau.blogspot.com/2006/11/making-applications-scalable-with-load.html




