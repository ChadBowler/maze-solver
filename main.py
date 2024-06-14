from graphics import Window, Point, Line

def main():
    # Create new window with 1200 X 1200 dimensions
    win = Window(1200, 1200)
    # Example line draw
    point_a = Point(50, 10)
    point_b = Point(510, 110)
    line = Line(point_a, point_b)
    win.draw_line(line, "green")
    # continuously call redraw while program is running
    win.wait_for_close()

if __name__ == "__main__":
    main()