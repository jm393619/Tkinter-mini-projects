import tkinter as tk
import random
from tkinter import messagebox


d = {}
for i1 in range(1, 5):
    for j1 in range(1, 5):

        d[f"{i1}{j1}"] = [f"{i1-1}{j1}", f"{i1+1}{j1}", f"{i1}{j1-1}", f"{i1}{j1+1}"]


class Game(tk.Tk):
    pady = 2
    width=4
    height = 2
    font=(None, 30)

    def __init__(self):
        super().__init__()
        self.geometry('420x420+400+100')
        self.title("Puzzle")

        # Create frame
        self.frame = tk.Frame(borderwidth=1, relief=tk.SOLID)
        self.frame.pack(pady=10)

        # Create menu with reset
        self.menu = tk.Menu()
        self.config(menu=self.menu)

        self.menu.add_command(label='Reset', command=self.mix)

        self.labels = {}
        self.positions = {}

        self.create_labels()
        self.mix()

        self.bind("<Button-1>", self.click)

    def create_labels(self):
        k = 1
        for i in range(1, 4):
            for j in range(1, 5):
                self.positions[f"{i}{j}"] = tk.Label(self.frame, text=f"{k}", borderwidth=2, relief=tk.SOLID,
                                                     width=Game.width, height=Game.height, font=Game.font,
                                                     pady=Game.pady)
                self.positions[f"{i}{j}"].grid(row=i, column=j)
                k += 1

        self.positions["41"] = tk.Label(self.frame, text=f"13", borderwidth=2, relief=tk.SOLID,
                                                     width=Game.width, height=Game.height, font=Game.font,
                                                     pady=Game.pady)
        self.positions["41"].grid(row=4, column=1)

        self.positions["42"] = tk.Label(self.frame, text=f"14", borderwidth=2, relief=tk.SOLID,
                                                     width=Game.width, height=Game.height, font=Game.font,
                                                     pady=Game.pady)
        self.positions["42"].grid(row=4, column=2)

        self.positions["43"] = tk.Label(self.frame, text="15", borderwidth=2, relief=tk.SOLID,
                                                     width=Game.width, height=Game.height, font=Game.font,
                                                     pady=Game.pady)
        self.positions["43"].grid(row=4, column=3)

        self.positions["44"] = tk.Label(self.frame, text="  ", borderwidth=2, relief=tk.SOLID,
                                                     width=Game.width, height=Game.height, font=Game.font,
                                                     pady=Game.pady)
        self.positions["44"].grid(row=4, column=4)
        self.None_label = self.positions["44"]

        self.win_configuration = self.positions.copy()

        self.labels = {x: y for y, x in self.positions.items()}

    def mix(self):

        lst = self.frame.winfo_children()
        random.shuffle(lst)

        for a, b in zip(self.positions, lst):
            self.positions[a] = b
            self.labels[b] = a
            self.positions[a].grid(row=a[0], column=a[1])

    def click(self, e):

        try:
            for y in d[self.labels[e.widget]]:
                try:
                    if self.positions[y]['text'] == '  ':
                        info1 = self.None_label.grid_info()
                        info2 = e.widget.grid_info()

                        e.widget.grid(row=info1['row'], column=info1['column'])
                        self.None_label.grid(row=info2['row'], column=info2['column'])
                        self.positions[f"{info2['row']}{info2['column']}"] = self.None_label
                        self.positions[f"{info1['row']}{info1['column']}"] = e.widget

                        self.labels[e.widget] = f"{info1['row']}{info1['column']}"
                        self.labels[self.None_label] = f"{info2['row']}{info2['column']}"

                    if self.positions == self.win_configuration:
                        messagebox.showinfo(title='Game over', message='You have won')
                        break

                except KeyError:
                    pass
        except KeyError:
            pass


if __name__ == "__main__":

    game = Game()
    game.mainloop()
