# TicTacToe - Minimax AI 

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)
![GitHub stars](https://img.shields.io/github/stars/HTANV/TicTacToe-Minimax?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/HTANV/TicTacToe-Minimax?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/HTANV/TicTacToe-Minimax?style=for-the-badge)

---

## Overview

**TicTacToe-Minimax** is a Python implementation of the classic Tic Tac Toe game featuring an unbeatable **Minimax AI**.  
The bot evaluates all possible moves using the **Minimax algorithm** and chooses the optimal play to either win or draw.  

This project is a lightweight educational example for learning:
- Minimax decision-making
- Game AI logic
- Recursive algorithms
- Turn-based game implementation in Python

---

## Features

- Fully playable **Tic Tac Toe** game in console
- Human vs AI (Player is 'O', AI is 'X')
- **Minimax AI** ensures the bot never loses
- Detects **wins, draws**, and prevents invalid moves
- Simple **3x3 grid UI** in the console
- Dynamic input validation and user prompts

---

## How It Works

1. **Game Grid**: Represented as a dictionary with positions 1-9
2. **Player Input**: Human selects positions to place 'O'
3. **Computer AI**: Uses **Minimax function** to determine optimal move
4. **Winner Check**: Checks horizontal, vertical, and diagonal lines
5. **Draw Detection**: Game ends if all spaces are filled with no winner
6. **Recursive Minimax**: Explores all possible moves, maximizing AI's outcome while minimizing the player's chance to win

---

## How to Run

1. **Clone the repository**

```bash
git clone https://github.com/HTANV/TicTacToe-Minimax.git
cd TicTacToe-Minimax
````

2. **Run the game using Python 3.x**

```bash
python TicTacToe-Minimax.py
```

3. **Gameplay Instructions**

* The computer goes first ('X')
* Enter positions 1-9 to place your mark ('O')
* Grid layout:

```
1 || 2 || 3
===========
4 || 5 || 6
===========
7 || 8 || 9
```

* The game announces **winner or draw** automatically

---

## Minimax Algorithm (AI)

The **Minimax algorithm** is a recursive decision-making method:

* **Maximizing Player**: AI ('X') tries to get the highest score
* **Minimizing Player**: Human ('O') tries to reduce AI's score
* Evaluates all possible moves until terminal states (win, lose, draw)
* Chooses the optimal move to **never lose**

---

## Requirements

* Python 3.x
* No additional packages required

> This project runs entirely in the console

---

## Notes

* The AI is **unbeatable** using Minimax logic
* Designed for learning and demonstration of **game AI**
* Single file project — easy to modify or extend
* Can be extended for GUI using **Tkinter, PyGame, or Unity Python integrations**

---

## Contributing

Contributions welcome:

* Add GUI front-end
* Enhance AI with Alpha-Beta pruning
* Add multiple difficulty levels
* Expand grid size for NxN TicTacToe variants

---


**Play Tic Tac Toe, beat the Minimax AI if you can!**
