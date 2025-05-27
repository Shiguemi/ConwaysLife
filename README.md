# Conway's Game of Life - Python Console Application

This project is a Python console-based implementation of Conway's Game of Life, an interactive cellular automaton devised by the British mathematician John Horton Conway.

## Features

*   Interactive console interface.
*   Customizable board size (rows and columns).
*   User-defined initial patterns by specifying live cell coordinates.
*   Step-by-step generation advancement.
*   Option to reset the board with a new pattern.
*   Basic error handling for user inputs.

## Files

*   `game_of_life.py`: Contains the core logic for the Game of Life, including the `GameBoard` class which manages the state of the cells and the rules for transitioning between generations.
*   `app.py`: Provides the console-based user interface for interacting with the game. It handles user input for board setup, displaying the board, and controlling the simulation.

## How to Run

1.  **Ensure you have Python installed** on your system (version 3.x recommended).
2.  **Save the files**: Make sure you have `game_of_life.py` and `app.py` in the same directory.
3.  **Open a terminal or command prompt**.
4.  **Navigate to the directory** where you saved the files. For example:
    ```bash
    cd path/to/your/game_of_life_directory
    ```
5.  **Run the application** using the following command:
    ```bash
    python app.py
    ```
6.  **Follow the on-screen prompts**:
    *   Enter the desired number of rows and columns for the game board.
    *   Input the coordinates (row and column, space-separated) of the initial live cells. Type `done` when you have finished setting up the pattern.
    *   Press `Enter` to advance to the next generation.
    *   Type `r` and press `Enter` to reset the board and set a new initial pattern.
    *   Type `q` and press `Enter` to quit the application.

## Game Rules (Conway's Game of Life)

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1.  **Underpopulation**: Any live cell with fewer than two live neighbours dies.
2.  **Survival**: Any live cell with two or three live neighbours lives on to the next generation.
3.  **Overpopulation**: Any live cell with more than three live neighbours dies.
4.  **Reproduction**: Any dead cell with exactly three live neighbours becomes a live cell.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously. The rules continue to be applied repeatedly to create further generations.
