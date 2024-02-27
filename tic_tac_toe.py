import tkinter as tk
from tkinter import ttk
import random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('750x600+400+100')
        self.title('Tic Tac Toe')
        self.config(background='gray')

        self.frame = tk.Frame(height=3, width=10, background='red', borderwidth=1, relief=tk.SOLID)
        self.frame.grid(row=0, column=0, pady=50, padx=50, rowspan=2)

        s = ttk.Style()
        s.configure('Wild.TRadiobutton', background='gray', foreground='black')

        self.labels = {}
        for i in range(9):
            self.labels[i] = tk.Label(self.frame, borderwidth=1, relief=tk.SOLID, width=10, height=4, font=(None, 20),
                                      pady=15, background='#05e6ea')
            self.labels[i].grid(row=i//3, column=i % 3)

        self.label_frame = tk.LabelFrame(text='FIRST MOVE', bg='gray')
        self.label_frame.grid(row=0, column=1, sticky=tk.NW, pady=70)

        self.txt = tk.IntVar(value=1)

        self.radio_1 = ttk.Radiobutton(self.label_frame, text='YOU', style='Wild.TRadiobutton', variable=self.txt,
                                       value=1)
        self.radio_1.pack(anchor=tk.NW, pady=5, padx=5)

        self.radio_2 = ttk.Radiobutton(self.label_frame, text='AI', style='Wild.TRadiobutton', variable=self.txt,
                                       value=2)
        self.radio_2.pack(anchor=tk.NW, pady=5, padx=5)

        self.new_game = tk.Button(text='NEW GAME', command=self.new, background='gray', relief=tk.RAISED)
        self.new_game.grid(row=1, column=1, sticky=tk.NW)

        self.rowconfigure(1, weight=2)

        self.positions = {y: x for x, y in self.labels.items()}

        self.bind1 = self.bind('<Button-1>', self.click)

        self.game = Game()

    def new(self):
        self.game.board = '---------'
        self.bind1 = self.bind('<Button-1>', self.click)
        for i in self.frame.winfo_children():
            i['text'] = ''

        if self.txt.get() == 2:

            y = random.randint(0, 8)
            self.game.move(y, 'o')
            self.labels[y].config(text='O')

    def click(self, e):

        if self.game.game_over():
            self.unbind("<1>", self.bind1)
            return None

        if e.widget in self.frame.winfo_children() and e.widget['text'] == '':

            x = self.positions[e.widget]
            e.widget.config(text='X')
            self.game.move(x, 'x')
            if self.game.game_over():
                self.unbind("<1>", self.bind1)
                return None
            self.move_o()

    def move_o(self):
        if self.game.evaluate(self.game.board):
            return None
        y = self.game.best_move()
        self.game.move(y, 'o')
        self.labels[y].config(text='O')

    def is_end(self):
        return self.game.evaluate(self.game.board)

class Game:
    def __init__(self):
        self.board = '---------'

    def game_over(self):
        return self.board.count('-') == 0 or self.who_win(self.board, 'o') or self.who_win(self.board, 'x')

    def move(self, x, sign):
        self.board = self.board[:x] + sign + self.board[x+1:]

    @staticmethod
    def who_win(b, sign):
        if b[:3] == sign*3 or b[3:6] == sign*3 or b[6:] == sign*3:
            return True
        if b[0] == sign and b[3] == sign and b[6] == sign:
            return True
        if b[1] == sign and b[4] == sign and b[7] == sign:
            return True
        if b[2] == sign and b[5] == sign and b[8] == sign:
            return True
        if b[0] == sign and b[4] == sign and b[8] == sign:
            return True
        if b[2] == sign and b[4] == sign and b[6] == sign:
            return True
        else:
            return False

    def evaluate(self, board):
        b = board  # self.board
        if self.who_win(b, 'o'):
            return 10
        if self.who_win(b, 'x'):
            return -10

        return 0

    def best_move(self):

        optimal = -1
        best_value = -20
        for i, j in enumerate(self.board):

            if j == '-':

                value = self.minimax(self.board[:i] + 'o' + self.board[i+1:], 'o')

                if value > best_value:
                    best_value = value
                    optimal = i

        return optimal

    def minimax(self, board, sign):

        if self.evaluate(board) or board.count('-') == 0:
            return self.evaluate(board)

        else:

            if sign == 'x':
                best_value = -20
                for i, j in enumerate(board):

                    if j == '-':
                        value = self.minimax(board[:i] + 'o' + board[i + 1:], 'o')
                        best_value = max(best_value, value)

                return best_value

            else:
                best_value = 20
                for i, j in enumerate(board):

                    if j == '-':

                        value = self.minimax(board[:i] + 'x' + board[i + 1:], 'x')
                        best_value = min(best_value, value)

                return best_value


if __name__ == '__main__':
    app = App()
    app.mainloop()
