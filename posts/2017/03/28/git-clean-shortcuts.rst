.. title: Git Clean Shortcuts
.. slug: git-clean-shortcuts
.. date: 2017-03-28 09:59:08 UTC-07:00
.. tags: devprod
.. category: software
.. link:
.. description: Useful git-clean shortcuts
.. type: text

I added these git clean short-cut aliases to my config.

::

    [alias]
       cls = clean -x -n -e *.iml -e .idea
       cl = clean -x -f -e *.iml -e .idea

Often, I would mistakenly delete my IntelliJ idea files and I will loose the various customizations I had done. This
setup will prevent the mishap from happening again.
