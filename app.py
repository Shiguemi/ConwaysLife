import pygame
from game_of_life import GameBoard # Keep this import

# --- Pygame Setup ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800  # Can be adjusted
SCREEN_HEIGHT = 600 # Can be adjusted
CELL_SIZE = 20      # Adjust for visual preference

# Adjust GRID_HEIGHT for UI area
UI_AREA_HEIGHT = 60 # Height for the button panel
EFFECTIVE_GRID_HEIGHT_PIXELS = SCREEN_HEIGHT - UI_AREA_HEIGHT
# Ensure GRID_HEIGHT is positive
GRID_HEIGHT = max(1, EFFECTIVE_GRID_HEIGHT_PIXELS // CELL_SIZE) 
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE # Width remains the same

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200) # For grid lines
GREEN = (0, 255, 0)   # For live cells (example)
BUTTON_COLOR = (180, 180, 180)
BUTTON_TEXT_COLOR = BLACK

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Game of Life - Pygame")

# Initialize font
pygame.font.init() # Ensure font module is initialized
UI_FONT_SIZE = 22
ui_font = pygame.font.SysFont('arial', UI_FONT_SIZE)

# --- UI Button Helper ---
def draw_button(surface, text, rect, button_color, text_color, font):
    pygame.draw.rect(surface, button_color, rect)
    pygame.draw.rect(surface, BLACK, rect, 2) # Border
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    surface.blit(text_surface, text_rect)

# --- Game Variables ---
# board will be initialized in main_pygame

def draw_grid(surface, board_obj):
    """Draws the grid and cells onto the Pygame surface."""
    # Iterate only up to GRID_HEIGHT to avoid drawing over UI area
    for r in range(min(board_obj.rows, GRID_HEIGHT)): 
        for c in range(board_obj.cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if board_obj.get_cell(r, c):
                pygame.draw.rect(surface, GREEN, rect)
            else:
                pygame.draw.rect(surface, WHITE, rect)
            pygame.draw.rect(surface, GRAY, rect, 1)

# --- Main Game Loop ---
def main_pygame():
    running = True
    clock = pygame.time.Clock()
    
    # Initialize GameBoard with the new GRID_HEIGHT
    board = GameBoard(GRID_HEIGHT, GRID_WIDTH) 

    simulation_paused = True
    simulation_running = False # Tracks if simulation has started at least once

    # Define button rects
    button_width = 100
    button_height = 40
    button_y = SCREEN_HEIGHT - UI_AREA_HEIGHT + (UI_AREA_HEIGHT - button_height) // 2 # Center buttons in UI area

    start_button_rect = pygame.Rect(10, button_y, button_width, button_height)
    pause_button_rect = pygame.Rect(start_button_rect.right + 10, button_y, button_width, button_height)
    next_button_rect = pygame.Rect(pause_button_rect.right + 10, button_y, button_width, button_height)
    reset_button_rect = pygame.Rect(next_button_rect.right + 10, button_y, button_width, button_height)

    # FPS control variables
    MIN_FPS = 1
    MAX_FPS = 60 # Max FPS as per current subtask
    DEFAULT_FPS = 10
    current_fps = DEFAULT_FPS
    fps_step = 1

    # FPS button rects (smaller buttons)
    fps_button_width = 50 # Smaller width for FPS buttons
    speed_down_button_rect = pygame.Rect(reset_button_rect.right + 20, button_y, fps_button_width, button_height)
    speed_up_button_rect = pygame.Rect(speed_down_button_rect.right + 10, button_y, fps_button_width, button_height)
    
    # Check if SCREEN_WIDTH needs adjustment
    required_width = speed_up_button_rect.right + 10
    if SCREEN_WIDTH < required_width:
        # This is a simple print for the subtask, actual screen resize would be more involved
        # if done after pygame.display.set_mode has already been called.
        # For this exercise, we'll assume initial SCREEN_WIDTH is large enough or
        # this print serves as a note for manual adjustment later if needed.
        print(f"INFO: Consider increasing SCREEN_WIDTH to at least {required_width} to fit all UI elements.")
        # To properly resize, one would need to handle screen re-initialization carefully.
        # global SCREEN_WIDTH, screen 
        # SCREEN_WIDTH = required_width
        # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while running:
        mouse_pos = pygame.mouse.get_pos() # Get mouse pos once per frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    clicked_on_button = False
                    if start_button_rect.collidepoint(mouse_pos):
                        simulation_paused = False
                        simulation_running = True
                        clicked_on_button = True
                    elif pause_button_rect.collidepoint(mouse_pos):
                        simulation_paused = True
                        clicked_on_button = True
                    elif next_button_rect.collidepoint(mouse_pos):
                        if simulation_paused and simulation_running:
                            board.next_generation()
                        clicked_on_button = True
                    elif reset_button_rect.collidepoint(mouse_pos):
                        board = GameBoard(GRID_HEIGHT, GRID_WIDTH) # Re-initialize board
                        simulation_paused = True
                        simulation_running = False
                        clicked_on_button = True
                    elif speed_down_button_rect.collidepoint(mouse_pos):
                        current_fps = max(MIN_FPS, current_fps - fps_step)
                        clicked_on_button = True
                        # print(f"FPS: {current_fps}") # For debugging
                    elif speed_up_button_rect.collidepoint(mouse_pos):
                        current_fps = min(MAX_FPS, current_fps + fps_step)
                        clicked_on_button = True
                        # print(f"FPS: {current_fps}") # For debugging

                    if not clicked_on_button and simulation_paused:
                        # Only toggle cells if paused and no button was clicked
                        clicked_col = mouse_pos[0] // CELL_SIZE
                        clicked_row = mouse_pos[1] // CELL_SIZE
                        
                        # Ensure click is within the drawable grid area, not on UI panel
                        if 0 <= clicked_row < GRID_HEIGHT and 0 <= clicked_col < GRID_WIDTH:
                             # Check if the click is above the UI area
                            if mouse_pos[1] < (SCREEN_HEIGHT - UI_AREA_HEIGHT):
                                current_state = board.get_cell(clicked_row, clicked_col)
                                board.set_cell(clicked_row, clicked_col, not current_state)

        if not simulation_paused and simulation_running:
            board.next_generation()
        
        screen.fill(WHITE) # Fill screen first
        draw_grid(screen, board) # Draw the current state of the grid

        # Draw UI panel background
        pygame.draw.rect(screen, (220, 220, 220), (0, SCREEN_HEIGHT - UI_AREA_HEIGHT, SCREEN_WIDTH, UI_AREA_HEIGHT))

        # Draw buttons
        draw_button(screen, "Start", start_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)
        draw_button(screen, "Pause", pause_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)
        draw_button(screen, "Next", next_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)
        draw_button(screen, "Reset", reset_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)
        
        draw_button(screen, "-", speed_down_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)
        draw_button(screen, "+", speed_up_button_rect, BUTTON_COLOR, BUTTON_TEXT_COLOR, ui_font)

        # Display current FPS
        fps_text = f"FPS: {current_fps}"
        fps_surface = ui_font.render(fps_text, True, BLACK)
        # Position FPS text above the FPS buttons or in a suitable place
        fps_text_x = (speed_down_button_rect.left + speed_up_button_rect.right) // 2
        fps_text_y = speed_down_button_rect.top - (UI_FONT_SIZE // 2) - 5 # 5 pixels padding above
        fps_rect = fps_surface.get_rect(center=(fps_text_x, fps_text_y))
        screen.blit(fps_surface, fps_rect)
        
        pygame.display.flip() # Update the full display
        clock.tick(current_fps) # Use the variable current_fps

    pygame.quit()

if __name__ == '__main__':
    # This will eventually call main_pygame()
    main_pygame() # Now run the Pygame app
