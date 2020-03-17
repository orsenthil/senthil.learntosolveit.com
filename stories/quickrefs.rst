.. title: Quick References
.. slug: quickrefs
.. date: 2020-02-19 08:48:19 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

.. class:: alert alert-primary float-md-left

.. contents::

These are some resources that augment me. This page serves a quick ref for resources and commands that I might need
find at some point in time in future. As a reader, you might find it useful too.

Nikola and Rst
--------------

* Inline Hyperlink

.. raw:: html

    <pre>
   `example <https://example.com>`_
    </pre>


Physical Libraries
------------------

* San Francisco Public Library https://sfpl.org
* Singapore Public Library
* Dublin Public Library
* San Ramon Public Library
* Georgia Tech Library
* `The Hindu Newspaper Reading with ProQuest <https://search-proquest-com.ezproxy.sfpl.org/>`_
* `Internet Archive <https://archive.org>`_

Memory Tools
------------

* Anki

Writing Tools
-------------

* Nikola

Development Tools
-----------------

* Jetbrains IntelliJ


PDF Utilities
-------------

Reduce the size of the PDF
..........................


::

   gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf


Unix Commands
-------------

Copy files to a single directory
................................

::

    find -type f -name *.pdf -exec cp -n {} books \;


Google Drive
------------

Using rclone to mount my google drive locally
.............................................


::

    rclone mount orsenthil-google-drive:Books orsenthil-google-drive

* `rclone reference`_

.. _rclone reference: https://www.ostechnix.com/how-to-mount-google-drive-locally-as-virtual-file-system-in-linux/
