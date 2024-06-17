from tkinter import Tk, BOTH, Canvas

RED="red"
GREEN="green"
BLACK="black"
WHITE="white"
line_width = 2

class Window():
    def __init__(self, height=1200, width=1200):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # Initially set to fullscreen
        self.__root.attributes("-zoomed", True)
        # Binding keys to exit and enter fullscreen mode
        self.__root.bind("<F11>", lambda event: self.__root.attributes("-fullscreen",
                                    not self.__root.attributes("-fullscreen")))
        self.__root.bind("<Escape>", lambda event: self.__root.attributes("-fullscreen", False))
        # Set up canvas
        self.__canvas = Canvas(self.__root, bg=WHITE, height="800", width="800")
        self.__canvas.pack()
        self.__running = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line = line.draw(self.__canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color=BLACK):
        self.fill_color = fill_color
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill=fill_color, width=line_width)

class Cell():
    def __init__(self, x1, y1, x2, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw_cell(self):
        tl_corner = Point(self._x1, self._y1)
        tr_corner = Point(self._x2, self._y1)
        bl_corner = Point(self._x1, self._y2)
        br_corner = Point(self._x2, self._y2)
        
        if self.has_left_wall:
            left_wall = Line(tl_corner, bl_corner)
            self._win.draw_line(left_wall, BLACK) 
        if self.has_right_wall:
            right_wall = Line(tr_corner, br_corner)
            self._win.draw_line(right_wall, BLACK) 
        if self.has_top_wall:
            top_wall = Line(tl_corner, tr_corner)
            self._win.draw_line(top_wall, BLACK) 
        if self.has_bottom_wall:
            bottom_wall = Line(bl_corner, br_corner)
            self._win.draw_line(bottom_wall, BLACK)
        