import tkinter as tk
import tkinter.messagebox as mbox
import random


class Pong(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pong")
        self.geometry("600x400+300+200")

        # Create canvas
        self.can_width, self.can_height = 500, 300
        self.canvas = tk.Canvas(self, background='white', width=self.can_width, height=self.can_height)
        self.canvas.pack(pady=40)
        self.canvas.focus_set()

        # Create paddles
        self.p1 = self.create_paddle(0, 120)
        self.p2 = self.create_paddle(490, 120)

        # Create rectangles
        self.r1 = self.canvas.create_rectangle(200, 100, 300, 103, fill='brown')
        self.r2 = self.canvas.create_rectangle(200, 200, 300, 203, fill='brown')

        # Bind
        self.keys = dict.fromkeys(('w', 's', 'Up', 'Down'))
        self.bind("<KeyPress>", self.move_paddle)
        self.bind("<KeyRelease>", self.move_paddle)

        self.looper()

        # Create Ball
        x_0, y_0 = 350, random.randint(50, 250)
        self.ball = self.canvas.create_oval(x_0, y_0, x_0+10, y_0+10, fill='orange')

        # Move ball
        self.ball_move()

    def create_paddle(self, x_0, y_0):
        return self.canvas.create_rectangle(x_0, y_0, x_0+10, y_0+70, fill='black')

    def move_paddle(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = event.type == '2'

    def looper(self):
        if self.keys['w']:
            self.canvas.move(self.p1, 0, -10)
        if self.keys['s']:
            self.canvas.move(self.p1, 0, 10)
        if self.keys['Up']:
            self.canvas.move(self.p2, 0, -10)
        if self.keys['Down']:
            self.canvas.move(self.p2, 0, 10)

        self.after(50, self.looper)

    def ball_move(self, x=-10, y=10):

        coord = self.canvas.coords(self.ball)
        coord_p1 = self.canvas.coords(self.p1)
        coord_p2 = self.canvas.coords(self.p2)

        coll = self.canvas.find_overlapping(*coord)

        if coord[1] <= 0:
            y = -y

        if coord[3] >= self.can_height:
            y = -y

        if coord[0] <= 10:
            if coord[1] >= coord_p1[1] and coord[3] <= coord_p1[3]:
                x = -x
            else:
                self.keys = dict.fromkeys(('w', 's', 'Up', 'Down'))
                mbox.showinfo(title='Game over', message='You have lost')
                return None

        if coord[0] >= self.can_width-20:
            if coord[1] >= coord_p2[1] and coord[3] <= coord_p2[3]:
                x = -x
            else:
                self.keys = dict.fromkeys(('w', 's', 'Up', 'Down'))
                mbox.showinfo(title='Game over', message='You have lost')
                return None

        for i in coll:
            if i in (self.r1, self.r2):
                y = -y

        self.canvas.move(self.ball, x, y)

        self.after(50, lambda: self.ball_move(x, y))


if __name__ == "__main__":

    pong = Pong()
    pong.mainloop()
