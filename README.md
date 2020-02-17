# game-theory-on-matrix

Final project for "Stochastic Simulation Method and Application".

This project is known as "基于记忆效应的空间囚徒困境中系统合作的演化" in Chinese.
The repo consists of all workflow for running simulation and generating
plots.

## 1v1 Simulation

Two agents game with each other with their own strategies. Output CSV-like
format with Python. Figures plotted with R language.

The design of this model is inspired by "Anderson, J. and Schooler, L. (1991). Reflections of the environment in memory. Psychological Science, 2(6):396."

## Matrix Simulation

Agents are occupied with their own position on a grid. They game with their
neighbours. In `matrix_result` folder, we use C++ to run this simulation.

The C++ program exports agent status in every epoch, and we use d3.js to
visualize the grid at any moment.

Design of this model is inspired by:

1. Wang J, Liu L N, Dong E Z, et al. An improved fitness evaluation mechanism with memory in spatial
prisoner's dilemma game on regular lattices[J]. Communications in Theoretical Physics, 2013, 59(3): 257.
2. Szabó G, Tőke C. Evolutionary prisoner’s dilemma game on a square lattice[J]. Physical Review E, 1998, 58(1): 69.

## License

The simulation program and the visualization program is licensed under MIT.
