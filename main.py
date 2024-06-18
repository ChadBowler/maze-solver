from graphics import Window
from maze import Maze

def main():
    # Create new window with 1200 X 1200 dimensions
    win = Window(1200, 1200)
    
    # Example maze
    maze = Maze(150, 150, 10, 10, 50, 50, win)
    maze._create_cells()
    maze._break_entrance_and_exit()
    maze._break_walls_r(maze._cells[0][0])
    maze._reset_visited_cells()
    maze.solve()

    # continuously call redraw while program is running
    win.wait_for_close()

if __name__ == "__main__":
    main()