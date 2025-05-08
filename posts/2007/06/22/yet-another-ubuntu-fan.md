.. title: Yet another Ubuntu Fan
.. slug: yet-another-ubuntu-fan
.. date: 2007-06-22 21:17:00
.. tags: ubuntu, linux, package-management, software-installation
.. category: Linux
.. description: My experience with Ubuntu's package management system and how I solved proxy authentication issues.

I was almost about to give up on {{% wikipedia article="Ubuntu" %}}, because after I installed the Fiesty, I was not able to download the packages from Repositories due to some proxy authentication issue. Tried various things for a week and when could not go any step further, I had thought let me get back to Fedora and was thinking about how new users of Linux will be feeling when they dont get support on what they need to get wishes satisfied with Linux. In my case, it was a particular distribution.

After a week, I setup my box again and wanted to give a final try. Instead of going to {{% wikipedia article="Synaptic (software)" %}} and meddling with Repository sources, I thought let me try Add/Remove application to Install software and see what happens.

The basic install of ubuntu (from the CD) did not have things which a regular Linux user would desire. Well, what the heck, gvim was not there! Browsing through the software list I checked {{% wikipedia article="Emacs" %}} 21 for Installation and pressed Apply. Something interesting started to happen. It started downloading automatically from http://archive.ubuntu.com/ubuntu/dists/feisty/main/

I felt a kind of relief that I will be able to spend more time with ubuntu now.

There is a tricky bug with Ubuntu package manager, I think. The following was my setup with package installation from repos worked.

1) {{% wikipedia article="Firefox" %}} configured with proxy and proxy authentication details.
2) Gnome Network Preferences, Proxy NOT configured.
3) Without adding any repos, archive.ubuntu.com which is kind of a default repo is only working thing.

If I configure, Gnome Network Preferences with proxy details, the package manager fails with Proxy Authentication message.

The following tests might help.

1) Without Firefox Proxy, try with package manager.
2) Test Gnome Network Preferences for other applications. {{% wikipedia article="Epiphany (web browser)" %}} can be used.
3) Try other repositories.

I shall try that and figure out the exact issue.

Now that I was able to configure the package manager, I got a wealth of neatly arranged package to choose from and Install. The Installation procedure was totally homogeneous. Neat, easy is what I can say of Ubuntu. Hey, you might hear those two words from many of the Ubuntu users, but you will appreciate only when you "feel" it.

Even [Picassa](http://picasa.google.com/linux/download.html) download in deb format was handled properly by gnome deb package installer. I had never used deb and always thought deb format is difficult than rpm.

I had transfered my camera shot movies of Bungee jump to Ubuntu machine, first surprised to see the thumbnail of avi file and next [{{% wikipedia article="Totem (media player)" %}} player played that avi](http://orsenthil.blogspot.com/2005/10/tried-new-default-apps-with-linux.html) file. I felt wow!. Because, its first time Totem player had worked for me (apart from the live cd demo)

Then I spent looking at all the interesting programs that default, multiverse, and universe repositories could offer. There are tons of python language packages to install directly from the repos.

But the sweetest of all surprises came, when I thought let me search for [rapple](http://rapple.sourceforge.net/) and [nanoblogger](http://nanoblogger.sourceforge.net/). I know, there were debian maintainers for these to two projects. But it was really nice, to see a the project I have contributed to as being listed from the repository and choosing them to install it!
