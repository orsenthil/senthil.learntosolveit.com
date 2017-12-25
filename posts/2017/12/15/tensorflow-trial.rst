.. title: Tensorflow trial
.. slug: tensorflow-trial
.. date: 2017-12-15 06:34:25 UTC-08:00
.. tags: tutorials
.. category:
.. link:
.. description:
.. type: text

Followed this `digitalocean tutorial on Tensorflow`_ to try an image classification on my computer.

Tried with a Robot image first.

.. image:: https://www.robotshop.com/media/catalog/product/cache/15/image/900x900/9df78eab33525d08d6e5fb8d27136e95/e/z/ez-robot-jd-humanoid-robot.jpg
   :height: 400
   :width: 300


It couldn't recognize it that well.

.. code-block:: console

    $ python classify_image.py --image_file ez-robot-jd-humanoid-robot.jpg 2>/dev/null
    whistle (score = 0.05857)
    tripod (score = 0.03762)
    microphone, mike (score = 0.03662)
    radio, wireless (score = 0.01969)
    spotlight, spot (score = 0.01623)

But, eureka for Cats!


.. image:: https://www.petmd.com/sites/default/files/what-does-it-mean-when-cat-wags-tail.jpg
   :height: 400
   :width: 300


.. code-block:: console


    $ python classify_image.py --image_file what-does-it-mean-when-cat-wags-tail.jpg 2>/dev/null
    tabby, tabby cat (score = 0.51155)
    Egyptian cat (score = 0.36965)
    tiger cat (score = 0.06952)
    lynx, catamount (score = 0.00368)
    doormat, welcome mat (score = 0.00064)




.. _digitalocean tutorial on Tensorflow: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-tensorflow-on-ubuntu-16-04
