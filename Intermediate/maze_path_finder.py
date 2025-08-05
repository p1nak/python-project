import curses
import queue
from curses import wrapper
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", "#", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", " ", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"]
]



def print_maze(maze, stdscr, path=[]):
    Blue = curses.color_pair(1)
    Red = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", Red)
            else:
                stdscr.addstr(i, j * 2, value, Blue)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_neighbors(maze, row, col):
    neighbors = []
    rows, cols = len(maze), len(maze[0])

    if row > 0:
        neighbors.append((row - 1, col))  # up
    if row + 1 < rows:
        neighbors.append((row + 1, col))  # down
    if col > 0:
        neighbors.append((row, col - 1))  # left
    if col + 1 < cols:
        neighbors.append((row, col + 1))  # right

    return neighbors

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(0.1)

        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            visited.add(neighbor)
            q.put((neighbor, path + [neighbor]))

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
