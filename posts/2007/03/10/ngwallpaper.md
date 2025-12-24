.. title: ngwallpaper
.. slug: ngwallpaper
.. date: 2007-03-10 03:35:00
.. tags: python, wallpaper, national geographic, desktop
.. category: Projects
.. description: A Python script that fetches and sets the National Geographic photo of the day as desktop wallpaper

I started using Google Code project hosting for the **ngwallpaper** project.
This Python script fetches the wallpaper of the day from the {{% wikipedia article="National Geographic" %}}
website and sets it as your desktop wallpaper.

It currently works on Windows by leveraging Python for Windows Extensions, (using the `SETDESKTOPWALLPAPER` attribute from a Windows API call).

Future improvements include:
1. Making it platform-agnostic (support for Windows, Linux, and Mac).
2. Refactoring the code for better structure.
3. Implementing the program as a service or scheduled task.
4. Fixing the issue where the wallpaper resets after a few hours on Windows.
