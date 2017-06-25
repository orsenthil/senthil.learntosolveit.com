.. title: Who slides Wins
.. slug: who-slides-wins
.. date: 2017-02-15 09:22:07 UTC-08:00
.. tags: projects
.. category:
.. link:
.. description:
.. type: text

Few years ago, I wrote this n-puzzle using pygame for fun.  It was inspired from the
sliding block puzzle game that I had played as a kid, which had numerals in the front and
a picture of taj mahal in the back. The idea was to slide and fit the photo together.

https://github.com/orsenthil/who-slides-wins

**How to play**

1. Human plays first. Use Arrow Keys to Move and Fit the Picture.
2. Press Enter when Done.
3. Computer Plays and tries to beat you with less moves that you took.

It uses A* with Manhattan Distances to Solve the puzzle.

If you want to try it on your computer.

1. Install python2.7
2. Create a virtualenv.
3. pip install pygame
4. clone the git repo.
5. python run_game.py
