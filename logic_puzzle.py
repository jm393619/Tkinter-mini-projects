import tkinter as tk
import numpy as np
from tkinter import messagebox


class Board:

    def __init__(self, n):
        self.board = np.zeros((10, 10))
        self.n = n
        self.fill_one()

    def fill_one(self):
        n = 0
        while n < self.n:
            a, b = np.random.randint(0, 10, 2)
            if not self.board[a][b]:

                self.board[a][b] = 1
                n += 1

    @staticmethod
    def fun(board):

        hor = []

        for i in board:
            k = 0
            hor_1 = []
            for j in i:
                if j:
                    k += 1
                elif k:
                    hor_1.append(str(k))
                    k = 0

            if k:
                hor_1.append(str(k))
            hor.append(hor_1)

        return hor

    def horizontal(self):
        return self.fun(self.board.T)

    def vertical(self):
        return self.fun(self.board)

    def __str__(self):

        return str(self.board)


class Game(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('Logic Puzzle')
        self.geometry("600x600+300+100")
        self.board = Board(67)

        # Create north frame
        self.frame_north = tk.Frame(border=3, relief=tk.SOLID)
        self.frame_north.grid(row=0, column=1, pady=(30, 0))
        self.horizontal = self.board.horizontal()

        for i, j in enumerate(self.horizontal):

            tk.Label(self.frame_north, borderwidth=3, width=5, pady=3, height=5, relief=tk.SOLID,
                     background='gray', text='\n'.join(j)).grid(row=0, column=i)

        self.button = tk.Button(text='CHECK', font=(None, 10), command=self.check)
        self.button.grid(row=0, column=0, pady=(30, 0), padx=(30, 0))

        # Create west frame
        self.frame_west = tk.Frame(border=3, relief=tk.SOLID)
        self.frame_west.grid(row=1, column=0, padx=(30, 0))
        self.vertical = self.board.vertical()

        for i, j in enumerate(self.vertical):
            tk.Label(self.frame_west, borderwidth=3, width=11, height=2, pady=3, relief=tk.SOLID,
                     background='gray', text=' '.join(j)).grid(row=i, column=0)

        # Create frame with labels
        self.frame_central = tk.Frame(border=3, relief=tk.SOLID)
        self.frame_central.grid(row=1, column=1)

        self.d = {}

        for i in range(10):
            for j in range(10):

                self.d[f"{i}-{j}"] = tk.Label(self.frame_central, borderwidth=3, width=5, pady=3, height=2,
                                              relief=tk.SOLID, background='#eceecc')
                self.d[f"{i}-{j}"].grid(row=i, column=j)

        # Central frame bindings
        self.bind("<Button-1>", self.left_click)
        self.bind("<Button-3>", self.right_click)

        # Create menu
        self.menu = tk.Menu()
        self.config(menu=self.menu)

        self.menu.add_command(label='New Game', command=self.new_game)

    def new_game(self):
        self.board = Board(67)
        self.horizontal = self.board.horizontal()
        self.vertical = self.board.vertical()
        for label in self.d.values():
            label.config(bg='#eceecc')

        for i, j in zip(self.frame_north.winfo_children(), self.horizontal):
            i.config(text='\n'.join(j))

        for i, j in zip(self.frame_west.winfo_children(), self.vertical):
            i.config(text=j)

    @staticmethod
    def left_click(e):

        d = {'#eceecc': '#2d2e26', '#2d2e26': '#eceecc'}

        if e.widget.winfo_parent() == '.!frame3':
            if e.widget['text'] == '':
                e.widget.config(bg=d[e.widget['bg']])

    @staticmethod
    def right_click(e):

        d = {'': 'X', 'X': ''}

        if e.widget.winfo_parent() == '.!frame3':
            if e.widget['bg'] == '#eceecc':
                e.widget.config(text=d[e.widget['text']])

    def check(self):
        for i, j in self.d.items():
            a, b = (int(x) for x in i.split('-'))

            if self.board.board[a][b] == 1 and j['bg'] != '#2d2e26':
                messagebox.showinfo(title='message', message='INCORRECT PATTERN')
                break
        else:
            messagebox.showinfo(title='message', message='CORRECT PATTERN')


if __name__ == '__main__':
    game = Game()
    game.mainloop()
