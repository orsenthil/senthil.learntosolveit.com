.. title: Cheatsheet
.. slug: cheatsheet
.. date: 2020-02-19 08:48:19 UTC-08:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text

Cheatsheet
==========


Reduce the size of the PDF
--------------------------

.. raw:: bash

   gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf

