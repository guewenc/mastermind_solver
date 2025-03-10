# Mastermind Solver

## Overview

A Python implementation of an automatic solver for the Mastermind game. This program generates a random secret code and uses a strategic elimination algorithm to find the solution.

## How it works

1. The program generates a random secret code of length 4 with numbers from 1 to 8
2. The solver uses a brute-force approach that:
   - Maintains a list of all possible code combinations
   - Makes guesses and receives feedback (black pegs for correct position, white pegs for correct number but wrong position)
   - Eliminates inconsistent guesses based on feedback history

## Usage

```
python run.py
```

The solver will display each attempt and the corresponding feedback until it finds the correct code.

## Parameters

- `CODE_LENGTH`: Length of the secret code (default: 4)
- `NUM_COLORS`: Number of possible values (default: 8)

These parameters can be modified to adjust the game difficulty.