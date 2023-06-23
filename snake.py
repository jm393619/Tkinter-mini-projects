import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("369x400+400+100")
root.title("Snake")

canvas = tk.Canvas(root, width=300, height=300, bg='white')
canvas.grid(row=1, column=0, padx=30)

head = canvas.create_oval(200, 200, 210, 210, fill='black')

_snake = [head]
positions = [canvas.coords(head)]
dict_aux = {1: (0, -10), 2: (10, 0), 3: (0, 10), 4: (-10, 0)}


def _move():
    coord = canvas.coords(head)

    for i in _snake:
        positions.append(canvas.coords(i))

    if coord[0] <= 0 or coord[1] <= 0 or coord[2] >= 300 or coord[3] >= 300:
        messagebox.showinfo(title='Game over', message='Game over')
        return None

    for k in range(len(_snake)-1, 0, -1):
        canvas.coords(_snake[k], *canvas.coords(_snake[k - 1]))

    if (c[0] - c[1]) % 2:
        canvas.move(head, *dict_aux[c[0]])
    else:
        canvas.move(head, *dict_aux[c[1]])

    if canvas.coords(head) == canvas.coords(apple_1):
        canvas.delete(apple_1)
        apple()

        _snake.append(canvas.create_oval(-20, -20, -10, -10, fill='red'))
        positions.append(canvas.coords(_snake[-1]))
        label1.config(text=f"Score: {len(_snake)}")

    if canvas.coords(head) in positions:
        messagebox.showinfo(title='Game over', message='Game over')
        return None

    positions.clear()

    canvas.after(ms=100, func=_move)


def direction(x):
    global c
    c0, c1 = c
    c0, c1 = x if x != c0 else c0, c0 if x != c0 else c1
    c = (c0, c1)


def apple():

    global apple_1
    while True:
        x = random.randint(200, 2800) // 10
        y = random.randint(200, 2800) // 10

        x -= x % 10
        y -= y % 10

        if [x, y, x+10, y+10] not in positions:
            break

    apple_1 = canvas.create_oval(x, y, x+10, y+10, fill='green', outline='green')


canvas.after(ms=100, func=_move)
apple_1 = canvas.create_oval(-10, -10, -5, -5)
apple()

c = [1, 1]
root.bind("<Up>", func=lambda x: direction(1))
root.bind("<Right>", func=lambda x: direction(2))
root.bind("<Down>", func=lambda x: direction(3))
root.bind("<Left>", func=lambda x: direction(4))

label1 = tk.Label(root, text="Score: 1", font=(None, 15))
label1.grid(row=0, column=0, sticky=tk.NW, pady=10, padx=30)

root.mainloop()
