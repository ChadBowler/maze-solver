from graphics import Window
from cells import Cell
from maze import Maze

def main():
    # Create new window with 1200 X 1200 dimensions
    win = Window(1200, 1200)
    
    # Example maze
    new_maze = Maze(150, 150, 10, 10, 50, 50, win)
    new_maze._create_cells()
    new_maze._break_entrance_and_exit()
    new_maze._break_walls_r(new_maze._cells[0][0])

    # continuously call redraw while program is running
    win.wait_for_close()

if __name__ == "__main__":
    main()