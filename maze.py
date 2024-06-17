from cells import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

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
        time.sleep(.05)