import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("480x400")
root.title('BMI Calculator')
root.configure(bg='#505744')


def _set(x, y):
    exec(f'''
f{y}e1.delete(0, tk.END)
f{y}e1.insert(0, str(int({x})))
    ''')


def decr(x, y):

    curr_val = x.get()
    x.set(curr_val - 1)
    _set(weight.get(), y)
    exec(f"f{y}s1.set({x.get()})")


def incr(x, y):

    curr_val = x.get()
    x.set(curr_val + 1)
    _set(height.get(), y)
    exec(f"f{y}s1.set({x.get()})")


# frame 1
f1 = tk.Frame(root, borderwidth=2, relief=tk.RAISED, bg='#8f9780')
f1.grid(row=0, column=0, padx=(30, 0), pady=(15,0))

f1l1 = tk.Label(f1, text='Weight', font=(None, 15), bg='#8f9780')
f1l1.grid(row=0, column=0, sticky=tk.NW, padx=(63, 30), pady=(15, 0), columnspan=3)

f1e1 = tk.Entry(f1, font=(None, 15), width=5)
f1e1.grid(row=1, column=1, sticky=tk.NW, padx=(35, 15), pady=(15, 0), columnspan=3)

weight = tk.IntVar()

f1s1 = ttk.Scale(f1, variable=weight, from_=30, to=150, command=lambda x: _set(x, 1))
f1s1.grid(row=2, column=1, padx=(10, 0), pady=(15, 15))

f1b1 = tk.Button(f1, borderwidth=1, command=lambda: decr(weight, 1), width=2)
f1b1.grid(row=2, column=0, padx=(10, 0))

f1b2 = tk.Button(f1, borderwidth=1, command=lambda : incr(weight, 1), width=2)
f1b2.grid(row=2, column=2, padx=10)

# frame 2
f2 = tk.Frame(root, borderwidth=2, relief=tk.RAISED, bg='#8f9780')
f2.grid(row=0, column=1, padx=50, pady=(15, 0))

f2l1 = tk.Label(f2, text='Height', font=(None, 15), bg='#8f9780')
f2l1.grid(row=0, column=0, sticky=tk.NW, padx=(63, 30), pady=(15, 0), columnspan=3)

f2e1 = tk.Entry(f2, font=(None, 15), width=5)
f2e1.grid(row=1, column=1, sticky=tk.NW, padx=(35, 15), pady=(15, 0), columnspan=3)

height = tk.IntVar()

f2s1 = ttk.Scale(f2, variable=height, from_=100, to=220, command=lambda x: _set(x, 2))
f2s1.grid(row=2, column=1, padx=(10, 0), pady=(15, 15))

f2b1 = tk.Button(f2, borderwidth=1, command=lambda: decr(height, 2), width=2)
f2b1.grid(row=2, column=0, padx=(10, 0))

f2b2 = tk.Button(f2, borderwidth=1, command=lambda : incr(height, 2), width=2)
f2b2.grid(row=2, column=2, padx=10)


def calc():

    global label1

    try:
        _weight = float(f1e1.get())
        _height = float(f2e1.get())

        label1.grid_forget()

        bmi = round(_weight / (_height/100)**2, 2)

        if bmi < 18.5:
            res = 'Underweight'
        elif bmi < 25:
            res = 'Normal Weight'
        elif bmi < 30:
            res = 'Overweight'
        else:
            res = 'Obesity'

        label1 = tk.Label(root, text=f"{bmi}\n\n{res}", font=(None, 15), padx=10, pady=10, bg='#8f9780', width=14)
        label1.grid(row=2, column=0, padx=(15, 0), pady=(20, 0))
    except:
        messagebox.showinfo(title='Sth went wrong', message='Incorrect data')


# Calculate Button
button1 = tk.Button(root, text='Calculate BMI', font=(None, 20), borderwidth=2, command=calc, bg='#8f9780')
button1.grid(row=1, column=0, sticky=tk.NW, pady=(20, 0), padx=(140, 0), columnspan=2)

label1 = tk.Label(root, text='\n\n', font=(None, 15), padx=10, pady=10, bg='#8f9780', width=14)
label1.grid(row=2, column=0, padx=(15, 0), pady=(20, 0))

# frame 3
f3 = tk.Frame(root)
f3.grid(row=2, column=1, padx=(30, 0), pady=(20, 0), sticky=tk.NW)

f3l0 = tk.Label(f3, text='<18.5', font=(None, 15), width=8, borderwidth=1, relief=tk.SOLID, bg='#78a2fd')
f3l1 = tk.Label(f3, text='18.5 - 25', font=(None, 15), width=8, borderwidth=1, relief=tk.SOLID, bg='#b0f235')
f3l2 = tk.Label(f3, text='25 - 30', font=(None, 15), width=8, borderwidth=1, relief=tk.SOLID, bg='#e3990f')
f3l3 = tk.Label(f3, text='>30', font=(None, 15), width=8, borderwidth=1, relief=tk.SOLID, bg='#e81613')

f3l4 = tk.Label(f3, text='Underweight', font=(None, 15), width=11, borderwidth=1, relief=tk.SOLID, bg='#93b4fb')
f3l5 = tk.Label(f3, text='Normal', font=(None, 15), width=11, borderwidth=1, relief=tk.SOLID, bg='#d4f694')
f3l6 = tk.Label(f3, text='Overweight', font=(None, 15), width=11, borderwidth=1, relief=tk.SOLID, bg='#f5a511')
f3l7 = tk.Label(f3, text='Obesity', font=(None, 15), width=11, borderwidth=1, relief=tk.SOLID, bg='#f51815')

for i in range(4): exec(f"f3l{i}.grid(row={i}, column=0)")
for i in range(4, 8): exec(f"f3l{i}.grid(row={i-4}, column=1)")

root.mainloop()
