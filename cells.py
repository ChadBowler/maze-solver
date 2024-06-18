from graphics import Point, Line, BLACK, RED, GRAY, WHITE

class Cell():
    def __init__(self, x1, y1, x2, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True, visited=False):
        self.tl_corner = Point(x1, y1)
        self.tr_corner = Point(x2, y1)
        self.bl_corner = Point(x1, y2)
        self.br_corner = Point(x2, y2)
        self.center_point = Point(((x2+x1)/2), ((y2+y1)/2))
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

    def draw_cell(self):
        left_wall = Line(self.tl_corner, self.bl_corner)
        right_wall = Line(self.tr_corner, self.br_corner)
        top_wall = Line(self.tl_corner, self.tr_corner)
        bottom_wall = Line(self.bl_corner, self.br_corner)
        if self.has_left_wall:
            self._win.draw_line(left_wall, BLACK) 
        else:
            self._win.draw_line(left_wall, WHITE)
        if self.has_right_wall:
            self._win.draw_line(right_wall, BLACK)
        else:
            self._win.draw_line(right_wall, WHITE) 
        if self.has_top_wall:
            self._win.draw_line(top_wall, BLACK)
        else:
            self._win.draw_line(top_wall, WHITE)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, BLACK)
        else:
            self._win.draw_line(bottom_wall, WHITE)


    def draw_move(self, to_cell, undo=False):
        move_line = Line(self.center_point, to_cell.center_point)
        if not undo:
            self._win.draw_line(move_line, RED)
        else:
            self._win.draw_line(move_line, GRAY)