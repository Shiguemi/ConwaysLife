class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[False for _ in range(cols)] for _ in range(rows)]

    def set_cell(self, row, col, alive):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.board[row][col] = alive
        else:
            # Optionally, handle out-of-bounds error or ignore
            print(f"Warning: Cell ({row}, {col}) is out of bounds.")

    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.board[row][col]
        return False # Cells outside the grid are considered dead

    def count_live_neighbors(self, row, col):
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue # Skip the cell itself
                
                neighbor_row, neighbor_col = row + i, col + j
                if self.get_cell(neighbor_row, neighbor_col):
                    live_neighbors += 1
        return live_neighbors

    def next_generation(self):
        new_board_state = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                live_neighbors = self.count_live_neighbors(r, c)
                current_cell_alive = self.get_cell(r, c)

                if current_cell_alive:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_board_state[r][c] = False # Dies
                    else:
                        new_board_state[r][c] = True # Survives
                else:
                    if live_neighbors == 3:
                        new_board_state[r][c] = True # Becomes alive
                    else:
                        new_board_state[r][c] = False # Stays dead
        self.board = new_board_state

if __name__ == '__main__':
    # Basic test
    board = GameBoard(5, 5)

    # Blinker pattern
    board.set_cell(2, 1, True)
    board.set_cell(2, 2, True)
    board.set_cell(2, 3, True)

    def print_board_simple(b):
        for r in range(b.rows):
            for c in range(b.cols):
                print('X' if b.get_cell(r, c) else '.', end=' ')
            print()
        print("-" * (b.cols * 2))

    print("Generation 0:")
    print_board_simple(board)

    board.next_generation()
    print("Generation 1:")
    print_board_simple(board)

    board.next_generation()
    print("Generation 2:")
    print_board_simple(board)
