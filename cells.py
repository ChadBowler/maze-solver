from graphics import Point, Line, BLACK, RED, GRAY

class Cell():
    def __init__(self, x1, y1, x2, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.tl_corner = Point(x1, y1)
        self.tr_corner = Point(x2, y1)
        self.bl_corner = Point(x1, y2)
        self.br_corner = Point(x2, y2)
        self.center_point = Point(((x2+x1)/2), ((y2+y1)/2))
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw_cell(self):
        if self.has_left_wall:
            left_wall = Line(self.tl_corner, self.bl_corner)
            self._win.draw_line(left_wall, BLACK) 
        if self.has_right_wall:
            right_wall = Line(self.tr_corner, self.br_corner)
            self._win.draw_line(right_wall, BLACK) 
        if self.has_top_wall:
            top_wall = Line(self.tl_corner, self.tr_corner)
            self._win.draw_line(top_wall, BLACK) 
        if self.has_bottom_wall:
            bottom_wall = Line(self.bl_corner, self.br_corner)
            self._win.draw_line(bottom_wall, BLACK)


    def draw_move(self, to_cell, undo=False):
        move_line = Line(self.center_point, to_cell.center_point)
        if not undo:
            self._win.draw_line(move_line, RED)
        else:
            self._win.draw_line(move_line, GRAY)