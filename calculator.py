import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("280x320")
root.title('Calculator')


def click(x): e1.insert(tk.END, x)


def equal():
    try:
        st = e1.get()
        e1.delete(0, 'end')
        e1.insert('end', round(eval(st), 6))
    except:
        messagebox.showinfo(title='Sth went wrong', message='SYNTAX ERROR')



e1 = tk.Entry(root, width=18, borderwidth=5, font=(None, 20), relief=tk.SUNKEN)
e1.grid(row=0, column=0, columnspan=4)

b7 = tk.Button(root, text='7', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('7'))
b7.grid(row=1, column=0, sticky=tk.W)

b8 = tk.Button(root, text='8', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('8'))
b8.grid(row=1, column=1, sticky=tk.W)

b9 = tk.Button(root, text='9', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('9'))
b9.grid(row=1, column=2, sticky=tk.W)

b4 = tk.Button(root, text='4', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('4'))
b4.grid(row=2, column=0, sticky=tk.W)

b5 = tk.Button(root, text='5', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('5'))
b5.grid(row=2, column=1, sticky=tk.W)

b6 = tk.Button(root, text='6', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('6'))
b6.grid(row=2, column=2, sticky=tk.W)

b1 = tk.Button(root, text='1', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('1'))
b1.grid(row=3, column=0, sticky=tk.W)

b2 = tk.Button(root, text='2', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('2'))
b2.grid(row=3, column=1, sticky=tk.W)

b3 = tk.Button(root, text='3', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('3'))
b3.grid(row=3, column=2, sticky=tk.W)

b_div = tk.Button(root, text='/', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('/'))
b_div.grid(row=4, column=3, sticky=tk.W)

b0 = tk.Button(root, text='0', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('0'))
b0.grid(row=4, column=1, sticky=tk.W)

bc = tk.Button(root, text='C', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: e1.delete(0, 'end'))
bc.grid(row=4, column=2, sticky=tk.W)

b_plus = tk.Button(root, text='+', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('+'))
b_plus.grid(row=1, column=3, sticky=tk.W)

b_minus = tk.Button(root, text='-', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('-'))
b_minus.grid(row=2, column=3, sticky=tk.W)

b_mul = tk.Button(root, text='*', borderwidth=3, width=2, font=(None, 25), padx=10, command=lambda: click('*'))
b_mul.grid(row=3, column=3, sticky=tk.W)

b_eq = tk.Button(root, text='=', borderwidth=3, width=2, font=(None, 25), padx=10, command=equal)
b_eq.grid(row=4, column=0, sticky=tk.W, padx=(1, 0))

root.mainloop()
