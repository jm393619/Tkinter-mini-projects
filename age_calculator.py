import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

root = tk.Tk()
root.geometry("330x400")
root.title('Age Calculator')
root.configure(bg='#c9f187')

# frame1
f1 = tk.Frame(root, bg='#c9f187')
f1.grid(row=0, column=0)

f1.columnconfigure(0, weight=1)
f1.columnconfigure(1, weight=1)
f1.columnconfigure(2, weight=3)


def _set(x):

    exec(f"e{x}.delete(0, tk.END)")
    exec(f"e{x}.insert(tk.END, int(s{x}.get()))")


l1 = tk.Label(f1, text='When were you born?', bg='#c9f187', font=(None, 20), width=18, borderwidth=0)
l1.grid(row=0, column=0, sticky=tk.NW, padx=(10, 0), pady=(10, 0), columnspan=3)

# Year
l2 = tk.Label(f1, text='Year', bg='#c9f187', font=(None, 13), width=5, borderwidth=0, relief=tk.SOLID)
l2.grid(row=1, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

year = tk.IntVar()

s1 = ttk.Scale(f1, from_=1900, to=datetime.date.today().year, variable=year, length=130, command=lambda x: _set(1))
s1.grid(row=1, column=2)

e1 = tk.Entry(f1, font=(None, 13), width=5, borderwidth=1, relief=tk.SOLID)
e1.grid(row=1, column=1, padx=(0, 0), pady=(10, 0), sticky=tk.W)

# Month
l2 = tk.Label(f1, text='Month', bg='#c9f187', font=(None, 13), width=5, borderwidth=0,  relief=tk.SOLID)
l2.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

month = tk.IntVar()

s2 = ttk.Scale(f1, from_=1, to=12, variable=month, length=130, command=lambda x: _set(2))
s2.grid(row=2, column=2)

e2 = tk.Entry(f1, font=(None, 13), width=5, borderwidth=1, relief=tk.SOLID)
e2.grid(row=2, column=1, padx=(0, 0), pady=(10, 0), sticky=tk.W)


# Day
l2 = tk.Label(f1, text='Day', bg='#c9f187', font=(None, 13), width=5, borderwidth=0,  relief=tk.SOLID)
l2.grid(row=3, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

e3 = tk.Entry(f1, font=(None, 13), width=5, borderwidth=1, relief=tk.SOLID)
e3.grid(row=3, column=1, padx=(0, 0), pady=(10, 0), sticky=tk.W)

day = tk.IntVar()

s3 = ttk.Scale(f1, from_=1, to=31, variable=day, length=130, command=lambda x: _set(3))
s3.grid(row=3, column=2)


def calc():

    try:

        _year = int(e1.get())
        _month = int(e2.get())
        _day = int(e3.get())
        birth_date = datetime.date(year=_year, month=_month, day=_day)
        curr_date = datetime.date.today()
        birth_this_year = datetime.date(year=curr_date.year, month=_month, day=_day)

        if curr_date < birth_this_year:

            year_age = birth_this_year.year - birth_date.year - 1
            day_age = abs(datetime.date(curr_date.year + 1, curr_date.month, curr_date.day) - birth_this_year).days
        elif curr_date < birth_this_year:
            ...

        else:
            year_age = birth_this_year.year - birth_date.year

            day_age = abs(curr_date - birth_this_year).days


        _delta = abs(birth_date - curr_date)
        f2l2 = tk.Label(f2, text=f"{year_age}, {day_age}", font=(None, 13))
        f2l2.grid(row=1, column=0, padx=(50, 0), pady=(10, 0), sticky=tk. NS)
    except ValueError:
        messagebox.showerror(title='Sth went wrong', message='Wrong date. Correct the data.')
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)


# Calculate button
cal = tk.Button(root, text='Calculate your age', bg='#c9f187', font=(None, 13), command=calc)
cal.grid(row = 1, column=0, padx=(15, 0), pady=(15, 0), sticky=tk.NS)

# frame 2
f2 = tk.Frame(root, bg='#c9f187')
f2.grid(row=2, column=0, sticky=tk.NW)

f2l1 = tk.Label(f2, text="Your age", font=(None, 20), bg='#c9f187')
f2l1.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

root.mainloop()