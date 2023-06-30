import tkinter as tk
from random import choice, randint

root = tk.Tk()
root.geometry("600x500+200+100")
root.title('Arkanoid')

canvas_width = 500
canvas_height = 400

# Create canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack(pady=30)

# Possible colors of bricks
colors = ('black', 'red', 'orange', 'blue', 'gray', 'yellow', 'pink', 'purple', 'green')

# Create bricks
pos_xi = 0 # Initial position of brick
pos_yi = 0
for i in range(20):
    for i in range(10):
        canvas.create_rectangle(pos_xi, pos_yi, pos_xi+50, pos_yi+10, fill=choice(colors))
        pos_xi += 50
    pos_xi = 0
    pos_yi += 10


x_0 = randint(30, canvas_width-30)
ball = canvas.create_oval(x_0, 350, x_0+10, 360)

x, y = -5, -5  # Initial direction of the ball

# Previous coordinates of the ball (with respect to current coordinates)
pb_pos = canvas.coords(ball)


# Create function which controls movement of the ball
def _move():
    global x, y, pb_pos

    cord_ball = canvas.coords(ball)

    coll = canvas.find_overlapping(*canvas.coords(ball))

    if cord_ball[0] <= 0 or cord_ball[2] >= canvas_width:
        x = -x
    if cord_ball[1] <= 0 or cord_ball[3] >= canvas_height:
        y = -y

    for i in coll:
        if canvas.coords(ball)[3] >= canvas_height and paddle not in coll:
            return None
        if i in (ball, paddle):
            continue

        i_x1, i_y1, i_x2, i_y2 = canvas.coords(i)
        b_x1, b_y1, b_x2, b_y2 = canvas.coords(ball)
        p_x1, p_y1, p_x2, p_y2 = pb_pos

        cond1 = (i_x1 == b_x2 and i_y1 == b_y2) and (p_x2 < i_x1 and p_y2 < i_y1)
        cond2 = (i_x2 == b_x1 and i_y1 == b_y2) and (p_x1 > i_x2 and p_y2 < i_y1)
        cond3 = (i_x2 == b_x1 and i_y2 == b_y1) and (p_y1 > i_y2 and p_x1 > i_x2)
        cond4 = (i_x1 == b_x2 and i_y2 == b_y1) and (p_x2 < i_x1 and p_y1 > i_y2)

        if cond1 or cond2 or cond3 or cond4:
            x, y = -x, -y
            canvas.delete(i)
        elif (i_x1 == b_x2 and i_y1 == b_y2) or (i_x2 == b_x1 and i_y1 == b_y2) \
                or (i_x2 == b_x1 and i_y2 == b_y1) or (i_x1 == b_x2 and i_y2 == b_y1):
            pass
        elif i_x1 == b_x2 or i_x2 == b_x1:
            x = -x
            canvas.delete(i)
        elif i_y1 == b_y2 or i_y2 == b_y1:
            y = -y
            canvas.delete(i)

    pb_pos = canvas.coords(ball)
    canvas.move(ball, x, y)

    root.after(ms=10, func=_move)


root.after(ms=2, func=_move)

# Creare paddle
paddle = canvas.create_rectangle(300, canvas_height-10, 420, canvas_height, fill='black')


def paddle_move(e):
    # root.bind("<Button-1>", func=click)

    paddle_coords = canvas.coords(paddle)
    if e.x < paddle_coords[0] or e.x > paddle_coords[2]:
        return None
    else:
        canvas.coords(paddle, e.x - c + d, paddle_coords[1], e.x - c + f, paddle_coords[3])


def click(e):
    global c, d, f
    c = e.x
    d = canvas.coords(paddle)[0]
    f = canvas.coords(paddle)[2]


c = d = f = 0
root.bind("<B1-Motion>", func=paddle_move)
root.bind("<Button-1>", click)

root.mainloop()