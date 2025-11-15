<!--
.. title: Games: achilles-1
.. slug: games-achilles-1
.. date: 2025-11-15 06:01:18 UTC-08:00
.. tags: games
.. category: 100games2025
.. link: 
.. description: 
.. type: text
.. devto: true
-->

Achilles is a simulation, not really a game. In Achilles, the world is given an X coordinate, Z coordinate, number of food items and number of organisms.
The organisms are not given any objective. But they have functions like they have vision, and learning systems powered by neural networks.
Food spawns randomly across the world. Food decays if it is left alone.
When the organisms see food in proximity, they eat the food. When the organisms see each other, if they are similar, they mate. If there is enough strength and difference, they can attack each other.

And the world evolves!

Here is a screenshot of the evolution

![](https://senthil.learntosolveit.com/2025/11/achilles-1.png)

Here is the attack in progress.

![](https://senthil.learntosolveit.com/2025/11/eat.png)

The program is written in C++ and uses OpenGL to display the world. The package that is present in many Linux operating systems does not behave the way we want. I had to check out the source code, and fix the bugs in the program.

The source of the maintained version lives in GitHub here: [https://github.com/orsenthil/achilles-1](https://github.com/orsenthil/achilles-1); there is [a lifetime worth of learning concepts](https://github.com/orsenthil/achilles-1/blob/main/LEARNING_RESOURCES.md) used by this simple program.