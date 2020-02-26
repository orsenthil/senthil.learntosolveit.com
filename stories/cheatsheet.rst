.. title: Cheatsheet
.. slug: cheatsheet
.. date: 2020-02-19 08:48:19 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Reduce the size of the PDF
--------------------------

::

   gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf


Copy files to a single directory
--------------------------------

::

    find -type f -name *.pdf -exec cp -n {} books \;


Using rclone to mount my google drive locally
---------------------------------------------

::

    rclone mount orsenthil-google-drive:Books orsenthil-google-drive

* `rclone reference`_

.. _rclone reference: https://www.ostechnix.com/how-to-mount-google-drive-locally-as-virtual-file-system-in-linux/