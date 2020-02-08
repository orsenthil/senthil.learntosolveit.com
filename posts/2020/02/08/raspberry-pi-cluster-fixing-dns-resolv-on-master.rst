.. title: Raspberry Pi Cluster - Fixing DNS Resolv on Master
.. slug: raspberry-pi-cluster-fixing-dns-resolv-on-master
.. date: 2020-02-08 06:38:27 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I had setup a raspberry pi cluster, and suddenly the master became
non-operational. The cluster was able to see itself, but if I login to master
node, I noticed it was not able communicate externally.

The DNS Resolution for any site from master was failing.

Then I figured that Ubuntu had made some changes to resolve.conf protocol

Ubuntu requested users not to edit /etc/resolv.conf, and it's content on my
cluster was not something that I wanted.

I had setup pihole, and my devices had started to see the internet through
this. I noticed that Ubuntu since 18.04 had not set my router as the first
nameserver and thus after pi-hole experiment, my master node lost its
resolution capability

Fixing the Ubuntu DNS resolution was easy. I followed `this post from datawookie`_


1. resolvconf package was already installed.

2. Edit /etc/resolvconf/resolv.conf.d/head

::

   nameserver <pi-hole-server>
   nameserver 8.8.4.4
   nameserver 8.8.8.8

3. Restart the resolvconf server

::

   sudo service resolvconf restart

.. _`this post from datawookie`: https://datawookie.netlify.com/blog/2018/10/dns-on-ubuntu-18.04/

