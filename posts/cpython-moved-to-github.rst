.. title: CPython moved to Github
.. slug: cpython-moved-to-github
.. date: 2017-02-20 07:09:24 UTC-08:00
.. tags: python
.. category:
.. link:
.. description:
.. type: text

CPython project moved it's source code hosting from self-hosted mercurial repository, at hg.python.org to Git
version control system hosted at Github. The new location of python project is http://www.github.com/python/cpython

This is second big version control migration that is happening since I got involved. The first one was when
we moved from svn to mercurial. Branches were sub-optimal in svn and we used svn-merge.py to merge across
branches. Mercurial helped there and everyone got used to a distributed version control written in python,
mercurial. It was interesting for me personally to compare mercurial with the other popular DVCS, git.

Over the years, Github has become popular place for developers to host their
projects. They have constantly improved their service offering. Many python
developers, got used to git version control system and found it's utility value too.

Two years ago, it was decided that Python will move to Git and Github. The `effort was led by
Bret Cannon`_  assisted by number of other developers and the migration happened on Feb 10, 2017.

I helped with the migration too and helped with providing tool around converting the hg to git, using the facilities
available from hg-git mercurial plugin.

We made use hg-git, and wrote some conversions scripts that could get us to the converted repo as we wanted.

1) https://github.com/orsenthil/cpython-hg-to-git
2) https://bitbucket.org/orsenthil/hg-git

Now that the migration is done, we are getting ourselves familiar to the new workflow.

.. _effort was led by Bret Cannon: https://paper.dropbox.com/doc/CPython-workflow-changes-mx1k8G6M0rg5JLy80F1r6
