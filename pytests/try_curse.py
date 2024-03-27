import curses

# Initialize the screen
stdscr = curses.initscr()

# Start colors in curses
curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

# Specifies whether to echo input
curses.noecho()

# React to keys instantly, without requiring the Enter key to be pressed
curses.cbreak()

# Enable keypad mode
stdscr.keypad(True)

# Hide the cursor
curses.curs_set(0)

# Clear screen
stdscr.clear()

# This function will draw a 10x10 frame and allow the user to move a cursor within it
def main2(stdscr):
    # Initialize the cursor position
    y, x = 1, 1
    
    while True:
        stdscr.clear()  # Clear the screen
        height, width = 10, 10  # Frame dimensions

        # Draw the frame
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    stdscr.addstr(i, j, '#', curses.color_pair(1))
                elif i == y and j == x:
                    stdscr.addstr(i, j, 'O', curses.color_pair(1))  # Draw the cursor
        
        # Refresh the screen
        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Move the cursor based on the key pressed
        if key == curses.KEY_UP and y > 1:
            y -= 1
        elif key == curses.KEY_DOWN and y < height - 2:
            y += 1
        elif key == curses.KEY_LEFT and x > 1:
            x -= 1
        elif key == curses.KEY_RIGHT and x < width - 2:
            x += 1
        elif key == ord('q'):  # Quit if 'q' is pressed
            break

# Wrap the main function to clean up properly
curses.wrapper(main2)
