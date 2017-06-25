.. title: Deep Learner Playing Breakout
.. slug: deep-learner-playing-breakout
.. date: 2017-01-24 21:36:55 UTC-08:00
.. tags: research, computer science
.. category:
.. link:
.. description:
.. type: text

Let's first watch this video

.. youtube:: qINUIONARkE
   :align: center


In this video, I just gave the program a game and it learned to play by itself. No, I did
not code the player, that would have been so traditional. Here the player, the computer, the
program, actually learns to play by itself by just playing the game! It does not need me.

I recorded this video for experiencing how a Deep learning algorithm actually works. And as you
can notice, it works amazingly! Deep learning is subset Artificial Intelligence that tries to show
"intelligent behavior" by using something similar to (neural networks) human brains wiring.
It uses mathematics, that we think, human brains internally use to exhibit rational thinking.

The results of these have been amazing. From beating go games (`Thanks For Ruining Another
Game Forever, Computers`_) , to making self-driving cars a possibility. The above video
should give some idea that self-driving cars can learn about hurdles and try to navigate by itself.

**How to setup your system for Deep Learning Experiment ?**

I wish, you will be excited to replicate this experiment. If you are interested, here is how I setup.

1. Rent a GPU Instance from AWS or Azure. Right now, we need GPUS. They are very costly, but the deep learning frameworks
are not optimized for CPUs. I spent multiple weeks of uptime on CPU without any results. Go for GPU. AWS Has it.

2. Setup `Ubuntu 14.04 with proper NVIDIA`_ drivers.

3. Install X11 and Window Manager. It wont be fun otherwise.

::

   sudo apt-get install xubuntu-desktop xfce

4. Setup viewing your powerful "Cloud Desktop" using nomachine_.
Apparently, that's the best way I could setup remote graphic viewing.

5. Clone the `DeepMind-Atari-Deep-Q-Learner`_ code.

6. Install the dependencies.

::

   ./install_dependencies.sh

7. And, as my son will say. *Here you go!*

::

   ./run_gpu breakout

You can exit nomachine with the program running, and constantly come
back to monitor your computer trying to learn to play a game by itself.


.. _DeepMind-Atari-Deep-Q-Learner: https://github.com/kuz/DeepMind-Atari-Deep-Q-Learner
.. _Ubuntu 14.04 with proper NVIDIA: http://tleyden.github.io/blog/2014/10/25/cuda-6-dot-5-on-aws-gpu-instance-running-ubuntu-14-dot-04/
.. _nomachine: https://www.nomachine.com/
.. _Thanks For Ruining Another Game Forever, Computers: https://blog.codinghorror.com/thanks-for-ruining-another-game-forever-computers/
