from graphics import Window
from cells import Cell

def main():
    # Create new window with 1200 X 1200 dimensions
    win = Window(1200, 1200)
    # Example cell
    cells = [
        Cell(5, 5, 50, 50, win, True, True, True, False),
        Cell(50, 5, 100, 50, win, True, False, True, True),
        Cell(100, 5, 150, 50, win, True, True, False, True),
        Cell(150, 5, 200, 50, win, True, True, True, False),
        Cell(5, 50, 50, 100, win, True, True, False, True),
        Cell(5, 100, 50, 150, win, True, True, True, False),
        Cell(605, 755, 650, 800, win, True, False, True, True),
        Cell(650, 755, 700, 800, win, False, False, False, False),
        Cell(700, 755, 750, 800, win, False, True, False, True),
        Cell(750, 755, 800, 800, win, True, True, True, False)
    ]
    for cell in cells:
        cell.draw_cell()
    
    # draw_move example
    cells[0].draw_move(cells[1], False)
    cells[0].draw_move(cells[4], False)
    cells[-4].draw_move(cells[-3], True)

    # Example line draw
    # point_a = Point(50, 10)
    # point_b = Point(510, 110)
    # line = Line(point_a, point_b)
    # win.draw_line(line, "black")

    # continuously call redraw while program is running
    win.wait_for_close()

if __name__ == "__main__":
    main()