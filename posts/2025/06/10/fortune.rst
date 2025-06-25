.. title: fortune
.. slug: fortune
.. date: 2025-06-10 21:36:11 UTC-07:00
.. tags: browserextension, python, javascript
.. category: 
.. link: https://github.com/orsenthil/fortune
.. description: A minimalist browser extension that displays a new quote in the browser tab.
.. type: text
.. devto: true

A minimalist browser extension that displays a new quote in the browser tab. For example, when you open a new tab, you will see quotes like this:

----

*"And this is aviation; I give it to the world."*  - *Louis Mouillard, French Inventor/Aeronaut (1834-1897)*

*"We were on the point of abandoning our work when the book of Mouillard fell into our hands, and we continued with the results you know."* - *Wilbur Wright, American Inventor/Aviator (1867-1921)*

---- 

This extension is named after popular Unix Program {{% wikipedia article="Fortune_(Unix)" %}}, a command line utility which displays quotes in the shell. The browser with tabs is a modern shell interface of the computer. And this is the fortune program for the browser.

Technical Details
-----------------

I developed this with Python hosted on Google App Engine, and the client side written using Javascript as a browser addon. In the backend there is a database where I keep the quote and author in a table. There is API call that returns the quote and the author in the JSON format. To call the API visit http://quotes-1271.appspot.com/json . This is an unauthenticated API as it read-only GET call, and cannot change the state of the system.

The client side is entirely handled by Javascript, and it displays the quote using simple {{% wikipedia article="Document_Object_Model" %}} manipulation.

Get the extension directly from the webstore
--------------------------------------------

* `Google Chrome Extension <https://chromewebstore.google.com/detail/fortune/kmcoofcbagjmlfbkoopfohngcnfnaakb>`_
* `Firefox Addons <https://addons.mozilla.org/en-US/firefox/addon/fortune-browser-extension/>`_


Screenshot
----------

.. image:: https://i.imgur.com/qLlqW7t.png
   :alt: screenshot

Video Demo
----------

.. image:: http://img.youtube.com/vi/3S8b3eROxUY/0.jpg
   :target: http://www.youtube.com/watch?v=3S8b3eROxUY
   :alt: Demo
