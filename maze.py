from cells import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        # seed to debug maze creation sequence
        if seed is not None:
            self.seed = random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                x1 = self._x1 + (i * self._cell_size_x)
                y1 = self._y1 + (j * self._cell_size_y)
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                new_cell = Cell(x1, y1, x2, y2, self._win, True, True, True, True)
                self._draw_cells(new_cell)
                col.append(new_cell)
            self._cells.append(col)

    def _draw_cells(self, cell):
        if self._win is None:
            return
        cell.draw_cell()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(.03)

    # sets the beginning and ending of the maze
    def _break_entrance_and_exit(self):
        entry_cell = self._cells[0][0]
        exit_cell = self._cells[-1][-1]
        entry_cell.has_top_wall = False
        self._draw_cells(entry_cell)
        exit_cell.has_bottom_wall = False
        self._draw_cells(exit_cell)

    # redrawing cells while making the maze
    def _remove_wall(self, current_cell, next_cell, direction):
        if direction == "above":
            current_cell.has_top_wall = False
            next_cell.has_bottom_wall = False
        elif direction == "left":
            current_cell.has_left_wall = False
            next_cell.has_right_wall = False
        elif direction == "below":
            current_cell.has_bottom_wall = False
            next_cell.has_top_wall = False
        elif direction == "right":
            current_cell.has_right_wall = False
            next_cell.has_left_wall = False
        self._draw_cells(current_cell)
        self._draw_cells(next_cell)

    def _break_walls_r(self, current_cell):
        # reverse engineer the column and row numbers
        col = ((current_cell.tl_corner.x - self._x1) // self._cell_size_x)
        row = ((current_cell.tl_corner.y - self._y1) // self._cell_size_y)
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            self._draw_cells(current_cell)
            return
        while True:
            # determine the possible directions we can move to open up the maze
            possibles = []
            if row-1 >= 0:
                above = (self._cells[col][row-1], "above")
                if not above[0].visited:
                    possibles.append(above)
            if col-1 >= 0:
                left = (self._cells[col-1][row], "left")
                if not left[0].visited:
                    possibles.append(left)
            if row+1 < self._num_rows:
                below = (self._cells[col][row+1], "below")
                if not below[0].visited:
                    possibles.append(below)
            if col+1 < self._num_cols:
                right = (self._cells[col+1][row], "right")
                if not right[0].visited:
                    possibles.append(right)
            if len(possibles) == 0:
                return
            else:
                next_direction = random.choice(possibles)
                self._remove_wall(current_cell, next_direction[0], next_direction[1])
                self._break_walls_r(next_direction[0])

    # resetting visited boolean after creating the maze so we can reuse it to traverse the maze
    def _reset_visited_cells(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_maze_r(self._cells[0][0])

    def _solve_maze_r(self, current_cell):
        self._animate()
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:
            return True
        # reverse engineer the column and row numbers
        col = ((current_cell.tl_corner.x - self._x1) // self._cell_size_x)
        row = ((current_cell.tl_corner.y - self._y1) // self._cell_size_y)
        # traversing possible directions to complete the maze
        possibles = []
        if row-1 >= 0:
            above = self._cells[col][row-1]
            if not above.visited and not current_cell.has_top_wall:
                possibles.append(above)
        if col-1 >= 0:
            left = self._cells[col-1][row]
            if not left.visited and not current_cell.has_left_wall:
                possibles.append(left)
        if row+1 < self._num_rows:
            below = self._cells[col][row+1]
            if not below.visited and not current_cell.has_bottom_wall:
                possibles.append(below)
        if col+1 < self._num_cols:
            right = self._cells[col+1][row]
            if not right.visited and not current_cell.has_right_wall:
                possibles.append(right)
        if len(possibles) > 0:
            for possible in possibles:
                current_cell.draw_move(possible)
                if self._solve_maze_r(possible):
                    return True
                current_cell.draw_move(possible, True)
        else:
            return False

