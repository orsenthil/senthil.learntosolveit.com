<!--
.. title: Games - AisleRiot Zebra
.. slug: games-aisleriot-zebra
.. date: 2025-11-08 21:40:39 UTC-08:00
.. tags: games
.. category: 100games2025
.. link: 
.. description: 
.. type: text
.. devto: true
-->

It has become very easy to learn new things. In these series of blog poss, I will be sharing #100games2025, I will be sharing about 100 different new games I have learned in 2025.


The [Zebra](https://help.gnome.org/users/aisleriot/stable/Zebra.html.en) variant of AisleRiot / [Klondike](https://en.wikipedia.org/wiki/Klondike_(solitaire)) game is played with two decks. The top row has the two decks to arrange. The player has to arrange the cards with opposite colors. Like Black and Red go alternate on top of each. The bottom is same as solitaire, but in the zebra variant, the top row is arranged alternately. When a slot in the bottom row, called tableau has an empty slot, it is automatically filled in with the latest in the waste pile or from the stock pile.


![](/2025/11/aiselriot-zebra.png)

Source Code of Gnome AisleRiot

[https://gitlab.gnome.org/GNOME/aisleriot/](https://gitlab.gnome.org/GNOME/aisleriot/-/tree/master?ref_type=heads)

The program is written in Guile [Scheme](https://exercism.org/tracks/scheme). The games are written declaratively, as in the variant rules and handlers are defined, and AisleRiot Framework handles the rendering, input and the game loop.


