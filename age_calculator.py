import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime


class Age:

    curr_date = datetime.date.today()

    def __init__(self, _year, _month, _day):
        self.birth_day = datetime.date(_year, _month, _day)
        self.this_year_birthday = datetime.date(self.curr_date.year, _month, _day)
        self.next_year_birthday = datetime.date(self.curr_date.year + 1, _month, _day)
        self.last_year_birthday = datetime.date(self.curr_date.year - 1, _month, _day)

    def get_days_age(self):
        return (self.curr_date - self.birth_day).days

    def get_age(self):

        if self.curr_date < self.this_year_birthday:
            years = self.curr_date.year - self.birth_day.year - 1
            days = (self.curr_date - self.last_year_birthday).days

        elif self.curr_date == self.this_year_birthday:
            years = self.curr_date.year - self.birth_day.year
            days = 0

        else:
            years = self.curr_date.year - self.birth_day.year
            days = (self.curr_date - self.this_year_birthday).days

        return years, days

    def get_days_to_birthday(self):

        if self.curr_date < self.this_year_birthday:

            days = (self.this_year_birthday - self.curr_date).days

        else:

            days = (self.next_year_birthday - self.curr_date).days

        return days


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

    global f2l2, f2l4

    f2l2.grid_forget()
    f2l4.grid_forget()

    try:

        if int(e1.get()) > 2023:
            messagebox.showinfo(title='Sth went wrong', message='Correct the year')
            e1.delete(0, tk.END)

        date = Age(int(e1.get()), int(e2.get()), int(e3.get()))

        res = date.get_age()

        f2l2 = tk.Label(f2, text=f"{res[0]} years and {res[1]} days" if res[1] else f"{res[0]} years",
                        font=(None, 13), bg='#c9f187')
        f2l2.grid(row=1, column=0, padx=(50, 0), pady=(10, 0), sticky=tk. NS)

        f2l4 = tk.Label(f2, text=f"{date.get_days_to_birthday()} days", font=(None, 13), bg='#c9f187')
        f2l4.grid(row=3, column=0, padx=(50, 0), pady=(10, 0), sticky=tk. NS)
    except ValueError:
        f2l2 = tk.Label(f2, text='', font=(None, 13))
        f2l2.grid(row=1, column=0, padx=(50, 0), pady=(10, 0), sticky=tk.NS)
        messagebox.showerror(title='Sth went wrong', message='Wrong date. Correct the data.')
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)


# Calculate button
cal = tk.Button(root, text='Calculate your age', bg='#c9f187', font=(None, 13), command=calc)
cal.grid(row=1, column=0, padx=(15, 0), pady=(15, 0), sticky=tk.NS)

# frame 2
f2 = tk.Frame(root, bg='#c9f187')
f2.grid(row=2, column=0, sticky=tk.NW)

f2l1 = tk.Label(f2, text="Your age", font=(None, 20), bg='#c9f187')
f2l1.grid(row=0, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

f2l2 = tk.Label(f2, text='', font=(None, 13))
f2l2.grid(row=1, column=0, padx=(50, 0), pady=(10, 0), sticky=tk.NS)

f2l3 = tk.Label(f2, text=f"Birthday in", font=(None, 20), bg='#c9f187')
f2l3.grid(row=2, column=0, padx=(15, 0), pady=(10, 0), sticky=tk.NW)

f2l4 = tk.Label(f2)

root.mainloop()
