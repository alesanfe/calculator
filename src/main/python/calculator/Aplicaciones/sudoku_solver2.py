from tkinter import Tk, Frame, Entry, Button, StringVar, Label, RAISED


class SudokuSolver:
    def __init__(self):
        self.converter = {"": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        self.number_vars = []
        self.sudoku = Tk()
        self.sudoku.resizable(False, False)
        self.sudoku.title("Sudoku Solver")

        self.miFrame = Frame(self.sudoku)
        self.miFrame.pack()

        # General settings
        for row in range(1, 10):  # Extending to Row 10
            self.number_vars.append([])
            for column in range(1, 12):
                self.configure_elements(row, column)
                if column == 4 or column == 8:
                    self.create_separator_line(row)
        print(len(self.number_vars[0]))
        # Add separator lines for Row 4
        self.create_separator_line(4, is_horizontal=True)
        # Add separator lines for Row 5
        self.create_separator_line(5, is_horizontal=True)
        # Add separator lines for Row 6
        self.create_separator_line(6, is_horizontal=True)
        # Add separator lines for Row 7
        self.create_separator_line(7, is_horizontal=True)
        # Add separator lines for Row 8
        self.create_separator_line(8, is_horizontal=True)
        # Add separator lines for Row 9
        self.create_separator_line(9, is_horizontal=True)
        # Add separator lines for Row 10
        self.create_separator_line(10, is_horizontal=True)

        self.configure_solve_button()

    def configure_elements(self, row, column):
        font_type = "Calculator"
        font_size = 30
        border_type = RAISED
        border_size = 0
        padx_value = 1
        pady_value = 1
        sticky_position = "nsew"
        background_color = "black"
        font_color = "white"
        justify_position = "center"
        width_value = 2

        number_var = StringVar()
        screen = Entry(self.miFrame, textvariable=number_var, font=(font_type, font_size),
                       relief=border_type, borderwidth=border_size)
        screen.grid(row=row, column=column, padx=padx_value, pady=pady_value, sticky=sticky_position)
        screen.config(background=background_color, fg=font_color, justify=justify_position, width=width_value)

        print(number_var)
        self.number_vars[row - 1].append(number_var)

    def create_separator_line(self, row, is_horizontal=False):
        if is_horizontal:
            line = Label(self.miFrame, text="---------")
            line.grid(row=row, column=1, columnspan=12, sticky="e", padx=1, pady=1)
        else:
            for column in range(1, 12):
                line = Label(self.miFrame, text="|")
                line.grid(row=row, column=column, sticky="e", padx=1, pady=1)

    def configure_solve_button(self):
        button = Button(self.miFrame, text="SOLVE", width=4, command=self.solve_sudoku)
        button.grid(row=12, column=5, columnspan=3, sticky="nsew")

    def solve_sudoku(self):
        malla = self.make_grid()
        print(malla)
        self.solve(malla)
        self.update_grid(malla)

    def make_grid(self):
        lista = [[self.converter[self.get_screen_value(row, col)] for col in range(1, 10)] for row in range(1, 10)]
        return lista

    def get_screen_value(self, row, col):
        print(self.number_vars[row][col])
        return self.number_vars[row][col].get()

    def update_grid(self, malla):
        for row in range(1, 10):
            for col in range(1, 10):
                self.number_vars[row][col].set(str(malla[row - 1][col - 1]))

    def solve(self, malla):
        for y in range(9):
            for x in range(9):
                if malla[y][x] == 0:
                    for number in range(1, 10):
                        if self.is_possible(x, y, number, malla):
                            malla[y][x] = number
                            self.solve(malla)
                            malla[y][x] = 0
                    return

    def is_possible(self, x, y, number, malla):
        # Check row.
        for pos_x in range(9):
            if malla[y][pos_x] == number:
                return False
        # Check column.
        for pos_y in range(9):
            if malla[pos_y][x] == number:
                return False
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        # Check square.
        for y_pos in range(3):
            for x_pos in range(3):
                if malla[y0 + y_pos][x0 + x_pos] == number:
                    return False
        return True


if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
    sudoku_solver.sudoku.mainloop()

if __name__ == "__main__":
    sudoku_solver = SudokuSolver()
    sudoku_solver.sudoku.mainloop()
