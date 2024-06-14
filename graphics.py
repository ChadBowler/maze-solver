from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, height=1200, width=1200):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.attributes("-fullscreen", True)
        self.__root.bind("<F11>", lambda event: self.__root.attributes("-fullscreen",
                                    not self.__root.attributes("-fullscreen")))
        self.__root.bind("<Escape>", lambda event: self.__root.attributes("-fullscreen", False))
        self.canvas = Canvas(self.__root, bg="red", height="800", width="800")
        self.canvas.pack()
        self.running = False
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False