.. title: Virtualbox Networking Modes
.. slug: virtualbox-networking-modes
.. date: 2016-12-14 08:14:25 UTC-08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text

With Virtualbox you get different types of networking modes that can be useful for many purposes. This post is for
quick reference for the different virtualbox networking modes.


* Not Attached - Unplugged.

* NAT - You get a new IP, like connecting a computer, and you can browse inside. NAT stands for Network Address
  Translation, which means  that you will get a private IP inside the virtualbox (like a computer inside your home,
  office) and you are accessing the internet from host system.

* Bridged networking - The virtual machine attaches to your physical network card and exchanges packets directly,
  circumventing the host operating systems network stack.

* Internal Networking - Kind of software-based network which is visible to selected virtual machines. Not to
  applications running on the host or to the outside world.

* Host-only networking - Network containing host and the set of virtual machines, without the need for the hosts
  physical network interface. Instead a virtual network (similar to loopback interface) is created on the host,
  providing connectivity among virtual machines and the host.
