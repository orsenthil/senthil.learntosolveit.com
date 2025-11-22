<!--
.. title: Games: Hitori
.. slug: games-hitori
.. date: 2025-11-22 06:24:26 UTC-08:00
.. tags: games
.. category: 100games2025
.. link: 
.. description: 
.. type: text
.. devto: true
-->

Hitori is a Japanese logic puzzle played on a grid of numbers. The objective is to eliminate numbers so that no row or column contains duplicate numbers, all shaded cells are isolated (not touching horizontally or vertically), and unshaded cells create a single connected group, that is you can you move from one unshaded cell to another unshaded cell following the path vertically or horizontally.

Here’s how a typical Hitori puzzle appears:

![Hitori puzzle grid](https://senthil.learntosolveit.com/2025/11/hitori.png)

**How to Play:**

- Shade cells to eliminate duplicate numbers from each row and column.
- Shaded (black) cells cannot be adjacent to each other vertically or horizontally.
- All non-shaded (white) cells must be connected.

The source code of this project is here [https://gitlab.gnome.org/GNOME/hitori](https://gitlab.gnome.org/GNOME/hitori) and the architecture is explained [here](https://gitlab.gnome.org/orsenthil/hitori/-/blob/main/architecture.md).
