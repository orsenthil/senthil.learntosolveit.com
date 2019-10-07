.. title: Abstract Factory - Design Pattern Explanation
.. slug: abstract-factory-design-pattern-explanation
.. date: 2016-07-15 09:28:06 UTC-07:00
.. tags: java
.. description: Simple explanation of Abstract Factory Design Pattern in Java.
.. type: text
.. has_math: yes

Design patterns like "Decorator", "Singleton" are common and be easily
recognized. The "Builder" pattern is also recognizable whenever you use Java's
`StringBuilder` class.

Some patterns which are commonly used by frameworks are not easily recognizable
unless you are a framework author.  Recently, I spent time trying to recognize
and understand *Abstract Factory* design pattern.

In this post, we will look at "Abstract Factory" and explain it with an
example. I consulted multiple resources, and ultimately to gain confidence, I
had to rely upon `The Gang of Four`_ design patterns book.

This post is intended as refresher for a reader who has read the **Gang of
Four** chapter on Abstract Factory. This post presents an example which the
reader can relate to in the modern world.

Abstract Factory is a Factory for Factories. To understand this, you will first
have to understand the Factory Design pattern, which encapsulates creation of
objects. Factory pattern is recognized when instead of using `new SomeClass()`
we call `SomeClass.createObject()` static method. The advantage is `SomeClass`
is independent of your code, it could be supplied as a dependency from someone
else and you simply use the factory. The person controlling the factory can
modify the object creation process. 

For example, `SomeClass.createObject()` in version1, can be return `new
SomeClass(arg1)` and in version2, it can change to `return new SomeClass(arg1,
arg2)` with you as the caller, invoking the object creation entirely as
`SomeClass.createObject()` unaffected by the change made by the creator of
SomeClass.

Factory pattern is easy to understand. The next step comes in dealing with
Abstract Factory.

Intent
======

Abstract Factory provides an interface for creating families of related or
dependent objects without specifying the concrete classes.

Canonical Design
----------------

.. image:: https://dl.dropbox.com/s/3o1opat3zd7c569/Screenshot%202016-07-11%2023.04.02.png

Factory is a class that defers the instantiation of the object to the
subclass.Factory encapsulates the decision-making that figures out which
specific subclass to instantiate. There are three different kinds of Factory
patterns observable with respect to object instantiation.

**Simple Factory.**
    The client directly uses a static method of a subclass, to instantiate an object.

**Factory Pattern**
    The client uses a Factory class to create an object. A Factory, is a class that defers the instantiation of an
    object to the subclasses.Factory method creates only one product

**Abstract Factory**
   Abstract Factory is a constructional design pattern that is used to create a family of related products.

Abstract Factory is applicable when the

* System should be configured with one of multiple families of Products.
* The family of related product objects is designed to to used together and we need to enforce this constraint.

Design Problem 
==============

In this problem, we are trying to design a "Operating System Installer" for
Unix family of Operating Systems. We know there are two popular variants of
**Unix**, there popular operating system with **Linux kernel** and related
application stack, and there is **BSD** systems.

Each Operating System will consists of components like

1. Bootloader
2. Kernel
3. Shell
4. DisplayManager
5. WindowManager
6. Applications

The installer will have to abstract those components and help the client create an **Unix** operating system choice.

**Correspondence with Canonical Design**

.. image:: https://dl.dropbox.com/s/wmnawrv6h3rxx4u/Screenshot%202016-07-12%2002.15.48.png


Let's look at each of these in some detail.

Product Interfaces
------------------

Starting with products, these are:

* Bootloader
* Kernel
* Shell
* DisplayManager
* WindowManager
* BaseApplications

We will have **Interfaces** for the products.

.. listing::  java/abstractfactory/IBootLoader.java java

.. listing::  java/abstractfactory/IKernel.java java

.. listing::  java/abstractfactory/IShell.java java

.. listing::  java/abstractfactory/IDisplayManager.java java

.. listing::  java/abstractfactory/IWindowManager.java java

.. listing::  java/abstractfactory/IBaseApplications.java java

Concrete Products
-----------------

Each of these can create many difference concrete products. For the different
concrete products like

* Bootloader

  * BSDBootLoader
  * LinuxBootLoader

* Kernel

  * BSDKernel
  * Linux

* Shell

  * BASH
  * CShell

* DisplayManager

  * X11
  * WayLand

* WindowManager

  * Gnome
  * KDE

* BaseApplications

  * SystemVUnix
  * GNUApplications
  * ProprietaryApps

Let's denote these concrete products in code that can be instantiated.

.. listing::  java/abstractfactory/BSDBootLoader.java java

.. listing::  java/abstractfactory/BSDKernel.java java

.. listing::  java/abstractfactory/Bash.java java

.. listing::  java/abstractfactory/CShell.java java

.. listing::  java/abstractfactory/GNUApplications.java java

.. listing::  java/abstractfactory/Gnome.java java

.. listing::  java/abstractfactory/KDE.java java

.. listing::  java/abstractfactory/Linux.java java

.. listing::  java/abstractfactory/LinuxBootLoader.java java

.. listing::  java/abstractfactory/ProprietaryApps.java java

.. listing::  java/abstractfactory/SystemVUnix.java java

.. listing::  java/abstractfactory/WayLand.java java

.. listing::  java/abstractfactory/X11.java java


Factories
---------

The products are created by **Factories**

* BSDFactory
* LinuxFactory
* UbuntuFactory

.. listing::  java/abstractfactory/BSDFactory.java java

.. listing::  java/abstractfactory/LinuxFactory.java java

.. listing::  java/abstractfactory/UbuntuFactory.java java

Abstract Factory
----------------

The factories will implement an **abstraction** provided by the **Abstract Factory**

.. listing::  java/abstractfactory/IUnixFactory.java java


Client
------

The design is best understood from the view of the client  which uses the
**Abstract Factory**  to the create the products.

.. listing::  java/abstractfactory/OperatingSystem.java java

The execution looks like this.

.. code-block::

    Booting: LinuxBootLoader
    Loading: Linux
    Loading: Bash
    Installing: X11
    Installing: Gnome
    Installing: GNUApplications

    Booting: BSDBootLoader
    Loading: BSDKernel
    Loading: CShell
    Installing: X11
    Installing: KDE
    Installing: SystemVUnix

    Booting: LinuxBootLoader
    Loading: Linux
    Loading: Bash
    Installing: X11
    Installing: Gnome
    Installing: ProprietaryApps

Tabulated Correspondence
------------------------

Mapping of the code with various elements in the design helps us to appreciate this pattern.

.. image:: https://dl.dropbox.com/s/ahu9pj89qtt7pos/Screenshot%202016-07-27%2008.57.29.png

Hope this was useful. If you have any comments on this article, please add your
thoughts in the comments section of this article.

Thank you for reading!

.. target-notes::

.. _The Gang of Four: https://en.wikipedia.org/wiki/Design_Patterns
