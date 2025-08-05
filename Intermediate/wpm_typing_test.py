import curses
import time
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\n", curses.A_BOLD)
    stdscr.addstr("Press any key to begin...")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    target_text = "The quick brown fox jumps over the lazy dog."
    current_text = []
    
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None

        if key in ('\n', '\r'):
            break  

        if key:
            if ord(key) == 27: 
                break

            if key in ('KEY_BACKSPACE', '\b', '\x7f'):
                if current_text:
                    current_text.pop()
            elif len(current_text) < len(target_text):
                current_text.append(key)

        stdscr.clear()
        stdscr.addstr("Type the following:\n", curses.A_UNDERLINE)
        stdscr.addstr(target_text + "\n\n")

        for i, char in enumerate(current_text):
            correct_char = target_text[i]
            if char == correct_char:
                stdscr.addstr(char, curses.color_pair(1))
            else:
                stdscr.addstr(char, curses.color_pair(2))

      
        time_elapsed = max(time.time() - start_time, 1) 
        num_chars = len(current_text)
        wpm = (num_chars / 5) / (time_elapsed / 60)

        stdscr.addstr(6, 0, f"\nWPM: {wpm:.2f}", curses.color_pair(3))
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)   
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK) 

    start_screen(stdscr)
    wpm_test(stdscr)
    stdscr.addstr("\n\nPress any key to exit...")
    stdscr.nodelay(False)
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
