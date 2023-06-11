import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

root = tk.Tk()
root.geometry("300x300+400+200")
root.title("Math flashcards")
choice = 'Addition'


def game():

    aux_d = {'Addition': '+', 'Subtraction': '-', 'Multiplication': '*'}

    geo = root.winfo_geometry()
    game_window = tk.Toplevel()
    game_window.geometry(geo)
    root.withdraw()

    def fun():
        game_window.destroy()
        root.destroy()
    game_window.protocol('WM_DELETE_WINDOW', fun)

    def _quit():
        root.geometry(game_window.winfo_geometry())
        root.deiconify()
        game_window.destroy()

    def flashcard():

        nonlocal g_l, a, b, g_e1

        try:
            ans = int(g_e1.get())
        except ValueError:
            messagebox.showinfo(title='Sth went wrong', message='Please, enter your answer')
            return None

        if ans != eval(f"a {aux_d[choice]} b"):
            messagebox.showerror(title='Sth went wrong', message='Bad answer')
            g_e1.delete(0, tk.END)
            return None
        g_e1.delete(0, tk.END)
        a = random.randint(0, 20)
        b = random.randint(0, 20)

        g_l.grid_forget()
        g_l = tk.Label(game_window, text=f'{a} {aux_d[choice]} {b}', font=(None, 20), borderwidth=2, relief=tk.GROOVE, pady=10, padx=10,
                       width=6, height=2)
        g_l.grid(row=0, column=0, padx=90, pady=10)

    a = random.randint(0, 20)
    b = random.randint(0, 20)

    g_l = tk.Label(game_window, text=f'{a} {aux_d[choice]} {b}', font=(None, 20), borderwidth=2, relief=tk.GROOVE, pady=10, padx=10,
                   width=6, height=2)
    g_l.grid(row=0, column=0, padx=90, pady=10)

    g_e1 = tk.Entry(game_window, font=(None, 15), width=5)
    g_e1.grid(row=1, column=0, padx=90, pady=10)

    g_w0 = tk.Button(game_window, font=(None, 15), text='Submit', width=8, command=flashcard)
    g_w0.grid(row=2, column=0, padx=90, pady=10)

    g_w1 = tk.Button(game_window, font=(None, 15), text='Quit', width=8, command=_quit)
    g_w1.grid(row=3, column=0, padx=90, pady=10)


def settings():

    geo = root.winfo_geometry()
    setting_window = tk.Toplevel()
    setting_window.geometry(geo)
    root.withdraw()

    def fun():
        setting_window.destroy()
        root.destroy()
    setting_window.protocol('WM_DELETE_WINDOW', fun)

    def _quit():
        root.geometry(setting_window.winfo_geometry())
        root.deiconify()
        setting_window.destroy()

    s_l = tk.Label(setting_window, text='Settings', font=(None, 20), borderwidth=2, relief=tk.GROOVE, pady=10, padx=10)
    s_l.pack(padx=10, pady=10)

    options = ['Addition', 'Subtraction', 'Multiplication']

    s_cb1 = ttk.Combobox(setting_window, values=options)
    s_cb1.pack(padx=10, pady=10)
    s_cb1.set(choice)

    def fun1(_):
        global choice
        choice = s_cb1.get()

    s_cb1.bind("<<ComboboxSelected>>", fun1)

    s_w0 = tk.Button(setting_window, text='Quit', font=(None, 15), command=_quit)
    s_w0.pack(padx=10, pady=10)


curr_value = tk.StringVar()

root_w0 = tk.Label(root, text="Math flashcards app", font=(None, 20), borderwidth=2, relief=tk.GROOVE,
                   pady=10, padx=10)
root_w1 = tk.Button(root, text='New Game', font=(None, 15), pady=5, padx=5, width=10, command=game)
root_w2 = tk.Button(root, text='Settings', font=(None, 15), pady=5, padx=5, width=10, command=settings)
root_w3 = tk.Button(root, text='Quit', font=(None, 15), pady=5, padx=5, width=10, command=lambda: root.destroy())

for i in range(4):
    exec(f"root_w{i}.pack(pady=10, padx=10)")

root.mainloop()
