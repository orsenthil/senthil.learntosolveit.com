<!--
.. title: Games- Amoebax
.. slug: games-amoebax
.. date: 2025-11-09 08:16:13 UTC-08:00
.. tags: games
.. category: 100games2025 
.. link: 
.. description: 
.. type: text
.. devto: true
-->

Amoebax is a falling puzzle game, tetris like game. The player has to arrange a group of four.

![](https://senthil.learntosolveit.com/2025/11/amoebax.png)

You have to arrange the falling tiles into groups of four. It has a two player game mechanics too, where in, while you try to ensure that you dont crash to the top, when you remove the paired blocks, you send it to your opponent. You win when your opponent's game is full.

The opponent is usually an AI. The game is written in C++, and uses libraries like [SDL](https://en.wikipedia.org/wiki/Simple_DirectMedia_Layer), zlib, ogg and vorbis.

The source code here is [https://gitlab.com/perita/amoebax/](https://gitlab.com/perita/amoebax/), there is an [emscripten](https://en.wikipedia.org/wiki/Emscripten) port of the game [https://peritasoft.com/amoebax/index.html](https://peritasoft.com/amoebax/index.html) which can be played online by the author, Jordi Frita. 

When examining the source code, it is written in modular C++ and uses multiple game design concepts like state design pattern to manage different game states, singleton for creating an instance of the game, factory to create ai players, strategy to implement player behaviors, template for customizable steps, observer for communication, and RAII for dealing with sound and image resources.