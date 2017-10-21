.. title: Nuclear Gandhi in Civilization V
.. slug: nuclear-gandhi-in-civilization-v
.. date: 2017-10-21 11:44:00 UTC-07:00
.. tags: bugs
.. category: 
.. link: 
.. description: 
.. type: text

It seems like the developers of Civilization V once decided to store aggresiveness index of leaders in a unsigned int.
And Gandhi, as the most pacifist leader that he was, was assigned lowest number 1. Also, in the game play if a society adopted
democracy, the aggresiveness score was reduced by 2.

So, when Gandhi adopted democracy, his aggresiveness score became **1 - 2 = -1**, and as it was unsigned int, and it gained a very high value.

.. code-block:: c

    #include<stdio.h>

    int main(void) {
        unsigned int i;
        i = -1;
        printf("%x\n", i);
    }

.. code-block:: bash

    $ clang unsigned.c
    $ ./a.out
    4294967295

And thus Gandhi was ready to nuke whenever there is a conflict.


.. image:: https://i.kinja-img.com/gawker-media/image/upload/s--4uHRnRfT--/c_fit,fl_progressive,q_80,w_636/dnqxrzdmsdkud7fmsqyp.jpg

    