import tkinter as tk
from tkinter import messagebox
from random import choice


class Game:
    def __init__(self, a=10, b=20):
        self.a = a
        self.b = b
        self.board = self.create_board(self.a, self.b)

    @staticmethod
    def create_board(a, b):

        to_ret = [[0 for _ in range(a)] for _ in range(b)]
        to_ret.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        return to_ret

    def show_board(self):
        for i in self.board:
            print(i)
        print('-'*30)

    @staticmethod
    def check_row(lst):
        if lst == [1]*10:
            return True
        else:
            return False

    def delete_row(self):
        for i in range(self.b-1, -1, -1):
            if self.check_row(self.board[i]):
                for j in range(i, 0, -1):
                    for k in range(self.a):
                        self.board[j][k] = self.board[j-1][k]


class Board(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x570+400+50")
        self.title('Tetris')

        self.game = Game()
        self.main_board = self.game.board
        self.color_bg = '#C0C0C0'

        self.frame = tk.Frame(borderwidth=1, relief=tk.SOLID)
        self.frame.pack(pady=10)

        self.labels = self.create_fields()
        self.positions = {y: x for x, y in self.labels.items()}

        self.shape1 = ((0, -1), (0, 0), (0, 1), (0, 2))
        self.shape2 = ((0, -1), (0, 0), (1, 0), (0, 1))
        self.shape3 = ((0, 0), (0, 1), (1, 0), (1, 1))
        self.shape4 = ((0, -1), (0, 0), (0, 1), (1, 1))
        self.shape5 = ((1, -1), (0, -1), (0, 0), (0, 1))
        self.shape6 = ((1, -1), (1, 0), (0, 0), (0, 1))
        self.shape7 = ((0, -1), (0, 0), (1, 0), (1, 1))

        self.shapes = [self.shape1, self.shape2, self.shape3, self.shape4, self.shape5, self.shape6, self.shape7]
        self.shape = -1
        self.orient = -1
        self.end = False
        self.fast = False

        self.x = 0
        self.y = 5

        self.rect = self.create_shape(self.x, self.y)

        self.bind("<KeyPress>", self.move_shape)
        self.bind("<KeyRelease>", self.release)

        self.fall_shape()

        # self.menu = tk.Menu()
        # self.config(menu=self.menu)
        # self.menu.add_command(label='New Game', command=...)

    def create_fields(self):

        d = {}

        for i in range(self.game.b):
            for j in range(self.game.a):

                d[f"{i}-{j}"] = tk.Label(self.frame, text='  ', font=(None, 15), width=2, height=1,  borderwidth=1,
                                         relief=tk.SOLID, bg=self.color_bg)
                d[f"{i}-{j}"].grid(row=i, column=j)

        return d

    def release(self, e):

        if e.keysym == 'Down':
            self.fast = False

    def create_shape(self, x, y):
        self.x = x
        self.y = y
        shape = choice(self.shapes)
        self.shape = self.shapes.index(shape)
        self.orient = 0
        to_ret = []

        for i, j in shape:
            self.labels[f"{x+i}-{y+j}"].configure(bg='green')
            to_ret.append((x+i, y+j))

        self.check_end(to_ret)

        return to_ret

    def move_shape(self, e):

        d = {'Left': -1, 'Right': 1, 'Up': 0, 'Down': 0}

        if self.end:
            d['Left'] = 0
            d['Right'] = 0

        if e.keysym not in d:
            return None

        elif e.keysym == 'Up':

            self.rotate_shape()
            return None

        elif e.keysym == 'Down':

            self.fast = True
            return None

        try:
            if not self.check_shape(0, 1):
                d['Right'] = 0

            if not self.check_shape(0, -1):
                d['Left'] = 0
        except IndexError:
            pass

        self.color(self.color_bg)

        new_rect = []

        for i, j in self.rect:

            k = j + d[e.keysym]
            new_rect.append((i, k))

        for i, j in new_rect:
            if j in (-1, 10):
                self.color('green')
                return None

        for i, j in new_rect:
            self.labels[f"{i}-{j}"].config(bg='green')

        self.y += d[e.keysym]
        self.rect = sorted(new_rect, key=lambda x: x[-1])

    def color(self, col):
        for i, j in self.rect:
            self.labels[f"{i}-{j}"].config(bg=col)

    def fall_shape(self):

        if self.end:
            messagebox.showinfo(message='Game Over')
            return None

        if not self.check_shape(1, 0):
            for i, j in self.rect:
                self.main_board[i][j] = 1
            self.delete_line()
            self.rect = self.create_shape(0, 4)
        else:

            self.color(self.color_bg)
            new_rect = []
            for i, j in self.rect:
                k = i + 1
                self.x = k
                new_rect.append((k, j))
                self.labels[f"{k}-{j}"].config(bg='green')

            self.rect = new_rect

        self.after(70 if self.fast else 500, self.fall_shape)

    def check_shape(self, a, b):

        f = True

        for i, j in self.rect:
            if self.main_board[i+a][j+b] == 1:
                f = False

        return f

    def check_rotate(self, x, y, lst):

        f = True

        for i, j in lst:
            if y + j > 9 or y+j < 0 or self.main_board[x + i][y + j] == 1:
                f = False

        return f

    def delete_line(self):
        for i in range(self.game.b-1, -1, -1):
            if self.main_board[i] == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                self.main_board[i] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                for j in range(i, 0, -1):
                    for k in range(10):
                        self.labels[f"{j}-{k}"].config(bg=self.labels[f"{j-1}-{k}"]['bg'])
                        self.main_board[j][k] = self.main_board[j-1][k]
                self.delete_line()

    def check_end(self, x):
        f = False

        for i, j in x:
            if self.main_board[i][j] == 1:
                f = True

        self.end = f
        return f

    def rotate_shape(self):

        x, y = self.x, self.y

        if x == 0:
            return None

        if not self.check_shape(1, 0):
            return None

        orient = (self.orient + 1) % 4
        shape = self.shape

        orientations = {0: {0: ((0, -1), (0, 0), (0, 1), (0, 2)), 1: ((-1, 0), (0, 0), (1, 0), (2, 0)),
                            2: ((0, -2), (0, -1), (0, 0), (0, 1)), 3: ((-2, 0), (-1, 0), (0, 0), (1, 0))},
                        1: {0: ((0, -1), (0, 0), (1, 0), (0, 1)), 1: ((-1, 0), (0, 0), (0, -1), (1, 0)),
                            2: ((0, -1), (0, 0), (-1, 0), (0, 1)), 3: ((-1, 0), (0, 0), (0, 1), (1, 0))},
                        2: {0: ((0, 0), (0, 1), (1, 0), (1, 1)), 1: ((0, 0), (0, 1), (1, 0), (1, 1)),
                            2: ((0, 0), (0, 1), (1, 0), (1, 1)), 3: ((0, 0), (0, 1), (1, 0), (1, 1))},
                        3: {0: ((0, -1), (0, 0), (0, 1), (1, 1)), 1: ((-1, 0), (0, 0), (1, 0), (1, -1)),
                            2: ((0, 1), (0, 0), (0, -1), (-1, -1)), 3: ((1, 0), (0, 0), (-1, 0), (-1, 1))},
                        4: {0: ((1, -1), (0, -1), (0, 0), (0, 1)), 1: ((-1, -1), (-1, 0), (0, 0), (1, 0)),
                            2: ((-1, 1), (0, 1), (0, 0), (0, -1)), 3: ((1, 1), (1, 0), (0, 0), (-1, 0))},
                        5: {0: ((1, -1), (1, 0), (0, 0), (0, 1)), 1: ((-1, -1), (0, -1), (0, 0), (1, 0)),
                            2: ((-1, 1), (-1, 0), (0, 0), (0, -1)), 3: ((1, 1), (0, 1), (0, 0), (-1, 0))},
                        6: {0: ((0, -1), (0, 0), (1, 0), (1, 1)), 1: ((-1, 0), (0, 0), (0, -1), (1, -1)),
                            2: ((0, 1), (0, 0), (-1, 0), (-1, -1)), 3: ((1, 0), (0, 0), (0, 1), (-1, 1))}
                        }

        if not self.check_rotate(self.x, self.y, orientations[shape][orient]):
            return None

        self.orient = orient

        new_rect = []

        self.color(self.color_bg)

        for i, j in orientations[shape][orient]:
            new_rect.append((x+i, y+j))
            self.labels[f"{x+i}-{y+j}"].config(bg='green')

        self.rect = new_rect


if __name__ == "__main__":

    board = Board()
    board.mainloop()
