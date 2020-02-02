.. title: Kubernetes Cluster Using Raspberry Pi
.. slug: kubernetes-cluster-using-raspberry-pi
.. date: 2020-02-02 13:11:53 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

I setup a kubernetes cluster using Raspberry pi. It was much easier than I had imagined.

.. image:: https://i.imgur.com/GlSDW8O.png
   :width: 640
   :height: 480


I used a Raspberry 4 for the master, and an agent. And I used two Raspberry B for two agents.

.. image:: https://i.imgur.com/kCB1tq0.png
   :width: 640
   :height: 480


I setup using `mhausenblas tutorial`_, which uses `k3s`_ for setting up of kubernetes on raspberry pis.
I used `k3sup`_ tool for installation of packages, which worked well.

My overall goal ran into some challenges.

* I was not able to setup the kubernetes dashboard via helm package, and I had to use instructions from github.
* I was not able to setup minecraft using the available helm package: https://github.com/itzg/docker-minecraft-server/issues/433
* I used k3sup to install packages, but I do not know how to uninstall the package using k3sup https://github.com/alexellis/k3sup/issues/179

Givem all these, I still have the my local kubernetes cluster up and running and I am excited about the possiblities
of using kubernetes on raspberry pis.


.. _`mhausenblas tutorial`: https://mhausenblas.info/kube-rpi/
.. _k3s: https://k3s.io/
.. _k3sup: https://github.com/alexellis/k3sup



