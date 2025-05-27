from game_of_life import GameBoard

def print_board(board_obj):
    """Prints the game board to the console."""
    print("\n" + "=" * (board_obj.cols * 2 + 1))
    for r in range(board_obj.rows):
        for c in range(board_obj.cols):
            print('X' if board_obj.get_cell(r, c) else '.', end=' ')
        print()
    print("=" * (board_obj.cols * 2 + 1))

def get_initial_pattern(board_obj):
    """Allows the user to set initial live cells by entering coordinates."""
    print("\n--- Set Initial Pattern ---")
    print("Enter coordinates of live cells one by one (e.g., 'row col').")
    print("Type 'done' when finished.")
    
    while True:
        try:
            user_input = input("Live cell (row col) or 'done': ").strip().lower()
            if user_input == 'done':
                break
            
            parts = user_input.split()
            if len(parts) != 2:
                raise ValueError("Please enter two numbers for row and column.")
            
            row, col = int(parts[0]), int(parts[1])
            
            if 0 <= row < board_obj.rows and 0 <= col < board_obj.cols:
                board_obj.set_cell(row, col, True)
                print(f"Cell ({row}, {col}) set to alive.")
                print_board(board_obj) # Show current state
            else:
                print(f"Coordinates ({row}, {col}) are out of bounds (Rows: 0-{board_obj.rows-1}, Cols: 0-{board_obj.cols-1}).")

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    """Main function to run the Game of Life application."""
    print("--- Conway's Game of Life ---")
    
    while True:
        try:
            rows = int(input("Enter number of rows for the board: "))
            cols = int(input("Enter number of columns for the board: "))
            if rows > 0 and cols > 0:
                break
            else:
                print("Rows and columns must be positive integers.")
        except ValueError:
            print("Invalid input. Please enter numbers for rows and columns.")

    game = GameBoard(rows, cols)
    get_initial_pattern(game)

    while True:
        print_board(game)
        action = input("Press Enter to see the next generation, 'r' to reset, or 'q' to quit: ").strip().lower()

        if action == 'q':
            print("Exiting Game of Life. Goodbye!")
            break
        elif action == 'r':
            print("Resetting board...")
            game = GameBoard(rows, cols) # Create a new empty board
            get_initial_pattern(game) # Ask for initial pattern again
        elif action == '':
            game.next_generation()
        else:
            print("Invalid action. Press Enter, 'r', or 'q'.")

if __name__ == '__main__':
    main()
