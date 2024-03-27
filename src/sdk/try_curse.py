import curses

stdscr = curses.initscr()

curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

curses.noecho()

curses.cbreak()

stdscr.keypad(True)

curses.curs_set(0)

stdscr.clear()

def main2(stdscr):
    y, x = 1, 1
    
    while True:
        stdscr.clear() 
        height, width = 20, 30

        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    stdscr.addstr(i, j, '#', curses.color_pair(1))
                elif i == y and j == x:
                    stdscr.addstr(i, j, 'O', curses.color_pair(1))
        
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and y > 1:
            y -= 1
        elif key == curses.KEY_DOWN and y < height - 2:
            y += 1
        elif key == curses.KEY_LEFT and x > 1:
            x -= 1
        elif key == curses.KEY_RIGHT and x < width - 2:
            x += 1
        elif key == ord('q'):
            break

curses.wrapper(main2)
