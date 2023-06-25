import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("450x280+300+100")
root.title("Bouncing ball")
a, b = -2, -2

canvas = tk.Canvas(root, width=400, height=210, bg='white')
canvas.pack(pady=(25, 0), padx=30)

rec = canvas.create_rectangle(200, 200, 300, 210, fill='black')


def motion(e):
    root.bind("<Button-1>", func=click)

    rec_coords = canvas.coords(rec)
    if e.x < rec_coords[0] or e.x > rec_coords[2]:
        return None
    else:
        canvas.coords(rec, e.x - c + d, rec_coords[1], e.x - c + f, rec_coords[3])


def click(e):
    global c, d, f
    c = e.x
    d = canvas.coords(rec)[0]
    f = canvas.coords(rec)[2]


def _move():

    global a, b
    if canvas.coords(ball)[0] < 0:
        # a += random.choice([1, 1, -1])
        # b += random.choice([1, 1, -1])
        a = -a

    elif canvas.coords(ball)[1] < 0:
        # a += random.choice([1, 1, -1])
        # b += random.choice([1, 1, -1])
        b = -b

    elif canvas.coords(ball)[2] > 390:
        # a += random.choice([1, 1, -1])
        # b += random.choice([1, 1, -1])
        a = -a

    elif canvas.coords(ball)[3] > 200:
        if canvas.coords(ball)[0] > canvas.coords(rec)[0] and canvas.coords(ball)[2] < canvas.coords(rec)[2]:
            # a += random.choice([1, 1, -1])
            # b += random.choice([1, 1, -1])
            b = -b
        else:
            messagebox.showinfo(title='Game over', message='Game over')
            return None

    canvas.move(ball, a, b)

    root.after(ms=4, func=_move)


root.bind("<Button-1>", func=click)
root.bind("<B1-Motion>", func=motion)

# Create ball
ball = canvas.create_oval(100, 150, 110, 160, fill='red')

root.after(ms=4, func=_move)

root.mainloop()
