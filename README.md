# Conway's Game of Life - Pygame Edition

This project is a Python implementation of Conway's Game of Life, featuring an interactive graphical interface built with Pygame.

## Features

*   Interactive graphical interface using Pygame.
*   Visual grid where cells can be toggled live/dead with mouse clicks (when paused).
*   Customizable board size (determined by screen and cell size settings in `app.py`).
*   Controls for starting, pausing, and stepping through generations.
*   Ability to reset the board to draw new patterns.
*   Adjustable simulation speed (Frames Per Second - FPS).
*   Real-time display of the current FPS.

## Files

*   `game_of_life.py`: Contains the core logic for the Game of Life (unchanged).
*   `app.py`: Provides the Pygame-based graphical user interface, event handling, and simulation controls.
*   `requirements.txt`: Lists project dependencies (Pygame).

## Prerequisites

*   **Python 3.x**
*   **Pygame**: You can install it by running:
    ```bash
    pip install pygame
    ```
    Alternatively, if you have the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Ensure Python and Pygame are installed** (see Prerequisites).
2.  **Save/clone the project files** (`game_of_life.py`, `app.py`, `requirements.txt`) into the same directory.
3.  **Open a terminal or command prompt**.
4.  **Navigate to the directory** where you saved the files. For example:
    ```bash
    cd path/to/your/game_of_life_directory
    ```
5.  **Run the application**:
    ```bash
    python app.py
    ```

## Interface and Controls

*   **Grid**: The main area displays the grid of cells. Live cells are typically shown in one color (e.g., green), and dead cells in another (e.g., white).
*   **Mouse Interaction**:
    *   When the simulation is **paused** (initially, or after clicking "Pause" or "Reset"), you can click on any cell in the grid to toggle its state (live to dead, or dead to live).
*   **Control Buttons** (located in a panel below the grid):
    *   **Start**: Begins or resumes the simulation. Cells will evolve according to Conway's rules at the current FPS.
    *   **Pause**: Pauses the simulation. This allows you to examine the current state or edit the pattern by clicking on cells.
    *   **Next**: When the simulation is paused, clicking "Next" advances the game by a single generation.
    *   **Reset**: Clears the entire grid (all cells become dead) and pauses the simulation. You can then draw a new initial pattern.
    *   **FPS -**: Decreases the simulation speed (reduces FPS).
    *   **FPS +**: Increases the simulation speed (increases FPS).
*   **FPS Display**: The current target Frames Per Second for the simulation is displayed near the FPS control buttons.

## Game Rules (Conway's Game of Life)

1.  **Underpopulation**: Any live cell with fewer than two live neighbours dies.
2.  **Survival**: Any live cell with two or three live neighbours lives on to the next generation.
3.  **Overpopulation**: Any live cell with more than three live neighbours dies.
4.  **Reproduction**: Any dead cell with exactly three live neighbours becomes a live cell.
