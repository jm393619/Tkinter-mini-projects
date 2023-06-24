import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser

root = tk.Tk()
root.geometry("600x550+300+100")
root.title("Paint")

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=2)
root.columnconfigure(index=2, weight=8)

# Canvas widget
canvas = tk.Canvas(root, width=500, height=300, bg='white')
canvas.grid(row=0, column=0, pady=20, padx=20, columnspan=3)

_size = tk.IntVar()

size_frame = tk.LabelFrame(root, text='Size')
size_frame.grid(row=1, column=0, pady=10, padx=50, sticky=tk.NW)

size_value = tk.Label(size_frame, text=f"{1}")


def size_val_fun(e):
    global size_value
    size_value.config(text=f"{int(size_scale.get())}")


size_scale = ttk.Scale(size_frame, from_=15, to=1, orient='vertical', command=size_val_fun, value=1)
size_scale.pack(padx=10)
size_value.pack(pady=4)


def draw(e):
    global size_scale
    canvas.create_line(e.x-1, e.y-1, e.x+1, e.y+1, capstyle=tk.ROUND, width=int(size_scale.get()),
                       fill=lab_color['bg'])


canvas.bind("<B1-Motion>", draw)
canvas.bind("<Button-1>", draw)


def set_color(e):
    global lab_color  # erase_var
    lab_color.config(bg=e.widget['bg'])


# frame with colors
color_frame = tk.LabelFrame(root, text='Color')
color_frame.grid(row=1, column=1, sticky=tk.NW, pady=10)

color_frame.focus()

lab_color = tk.Label(color_frame, bg='black', width=3, height=1)
lab_color.grid(row=0, column=0, columnspan=2, sticky=tk.NS, pady=(2, 4))

col_lab1 = tk.Label(color_frame, bg='blue', width=5, height=2, borderwidth=1)
col_lab1.grid(row=1, column=0)

col_lab2 = tk.Label(color_frame, bg='red', width=5, height=2, borderwidth=1)
col_lab2.grid(row=1, column=1)

col_lab3 = tk.Label(color_frame, bg='black', width=5, height=2, borderwidth=1)
col_lab3.grid(row=2, column=0)

col_lab4 = tk.Label(color_frame, bg='yellow', width=5, height=2, borderwidth=1)
col_lab4.grid(row=2, column=1)

col_lab5 = tk.Label(color_frame, bg='green', width=5, height=2, borderwidth=1)
col_lab5.grid(row=3, column=0)

col_lab6 = tk.Label(color_frame, bg='orange', width=5, height=2, borderwidth=1)
col_lab6.grid(row=3, column=1)

col_lab1.bind("<Button-1>", set_color)
col_lab2.bind("<Button-1>", set_color)
col_lab3.bind("<Button-1>", set_color)
col_lab4.bind("<Button-1>", set_color)
col_lab5.bind("<Button-1>", set_color)
col_lab6.bind("<Button-1>", set_color)


# Frame with options
def _clear():
    canvas.delete('all')
    canvas.config(bg='white')


def erase():
    global lab_color
    lab_color.config(bg='white')


def canvas_color():
    canvas.config(bg=lab_color['bg'])


def color():
    brush_color = colorchooser.askcolor()[1]
    lab_color.config(bg=str(brush_color))


def save():
    ...


option_frame = tk.LabelFrame(root, text='Options', pady=5, padx=5)
option_frame.grid(row=1, column=2, sticky=tk.NW, pady=10, padx=10)

clear_but = tk.Button(option_frame, text='Clear', width=6, command=_clear)
clear_but.grid(row=0, column=0)

eraser_but = tk.Button(option_frame, text='Eraser', width=6, command=erase)
eraser_but.grid(row=1, column=0)

save_but = tk.Button(option_frame, text='Color', width=6, command=color)
save_but.grid(row=2, column=0)

canvas_but = tk.Button(option_frame, text='Canvas', width=6, command=canvas_color)
canvas_but.grid(row=3, column=0)

save_but = tk.Button(option_frame, text='Save', width=6, command=save)
save_but.grid(row=4, column=0)

root.mainloop()
