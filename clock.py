import tkinter as tk
from tkinter import ttk
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("330x150+450+150")
        self.title("Clock")

        # Create menu
        self.menu = tk.Menu()
        self.config(menu=self.menu)
        self.menu.add_command(label='clock', command=self.clock)
        self.menu.add_command(label='stopwatch', command=self.stopwatch, )
        self.menu.add_command(label='timer', command=self.timer)

        # Variables
        self.clock_var = tk.StringVar()
        self.stopwatch_var = tk.IntVar(value=0)
        self.stopwatch_sec = tk.IntVar(value=0)
        self.stopwatch_min = tk.IntVar(value=0)
        self.stopwatch_hr = tk.IntVar(value=0)
        self.timer_min = tk.IntVar(value=1)
        self.timer_sec = tk.IntVar(value=0)

        self.clock_check = tk.IntVar(value=1)
        self.stopwatch_check = tk.IntVar(value=0)
        self.timer_check = tk.IntVar(value=0)

        # Frame with clock
        self.clock_frame = tk.Frame()
        self.clock_label = tk.Label(self.clock_frame, textvariable=self.clock_var, font=(None, 60),
                                    bg='brown', fg='white')
        self.clock_label.pack(pady=(20, 0))

        # Frame with stopwatch
        self.stopwatch_frame = tk.Frame()
        self.stopwatch_label = tk.Label(self.stopwatch_frame, font=(None, 40),
                                        text=f"{self.stopwatch_min.get()} min: {self.stopwatch_sec.get()} s")
        self.stopwatch_label.grid(row=0, column=0, columnspan=2)

        self.start_stop_button = ttk.Button(self.stopwatch_frame, text="Start", command=self.stopwatch_start_stop)
        self.start_stop_button.grid(row=1, column=0)

        self.reset_button = ttk.Button(self.stopwatch_frame, text="Reset", command=self.stopwatch_reset)
        self.reset_button.grid(row=1, column=1)

        # Frame with timer
        self.timer_frame = tk.Frame()
        self.timer_label = tk.Label(self.timer_frame, font=(None, 40), width=10,
                                    text=f"{self.timer_min.get()} min {self.timer_sec.get()} s")
        self.timer_label.grid(row=0, column=0, columnspan=3)
        self.timer_label.pack_propagate(False)

        self.scale_min = ttk.Scale(self.timer_frame, variable=self.timer_min, from_=0, to=30, command=self.set_min,
                                   length=200)
        self.scale_min.grid(row=1, column=0)

        self.scale_sec = ttk.Scale(self.timer_frame, variable=self.timer_sec, from_=0, to=60, command=self.set_sec,
                                   length=200)
        self.scale_sec.grid(row=2, column=0)

        self.timer_start = ttk.Button(self.timer_frame, text='start', command=self.start_timer)
        self.timer_start.grid(row=1, column=2, pady=(10, 0))

        self.timer_reset = ttk.Button(self.timer_frame, text='reset', command=self.reset_timer)
        self.timer_reset.grid(row=2, column=2, pady=(10, 0))

        self.clock()

    def clock(self):
        self.close()
        self.clock_frame.pack(pady=0)
        self.clock_check.set(1)

        def update_clock():
            if not self.clock_check.get():
                return None

            self.clock_var.set(time.ctime().split()[3])
            self.after(ms=1000, func=update_clock)

        update_clock()

    def stopwatch(self):
        self.close()
        self.stopwatch_frame.pack()

        def update_stopwatch():
            if not self.stopwatch_check.get():
                return None

            # _sec, _min, _hr = self.stopwatch_sec.get(), self.stopwatch_min.get(), self.stopwatch_hr.get()

            self.stopwatch_sec.set(self.stopwatch_sec.get()+1)

            if self.stopwatch_sec.get() == 60:
                self.stopwatch_min.set(self.stopwatch_min.get()+1)
                self.stopwatch_sec.set(0)

            self.stopwatch_label.config(text=f"{self.stopwatch_min.get()} min: {self.stopwatch_sec.get()} s")
            self.after(ms=1000, func=update_stopwatch)

        update_stopwatch()

    def timer(self):
        self.close()
        self.timer_frame.pack()
        self.timer_check.set(1)

    def close(self):
        self.clock_frame.pack_forget()
        self.stopwatch_frame.pack_forget()
        self.timer_frame.pack_forget()
        self.clock_check.set(0)
        self.timer_check.set(0)

        # self.stopwatch_check.set(0)

    def stopwatch_start_stop(self):
        d = {'Stop': 'Start', 'Start': "Stop"}
        self.stopwatch_check.set((self.stopwatch_check.get()+1) % 2)
        self.start_stop_button.config(text=d[self.start_stop_button['text']])
        self.stopwatch()

    def stopwatch_reset(self):
        self.stopwatch_check.set(0)
        self.stopwatch_sec.set(0)
        self.stopwatch_min.set(0)
        self.stopwatch_label.config(text=f"{self.stopwatch_min.get()} min: {self.stopwatch_sec.get()} s")

    def start_timer(self):

        self.timer_check.set(1)

        self.timer_start.config(state='disabled')

        self.scale_min.config(state='disabled')
        self.scale_sec.config(state='disabled')

        def update_timer():
            if self.timer_min.get() == 0 and self.timer_sec.get() == 0:
                return None

            if not self.timer_check.get():
                return None

            if self.timer_sec.get() == 0:
                self.timer_min.set(self.timer_min.get()-1)
                self.timer_sec.set(60)

            self.timer_sec.set(self.timer_sec.get()-1)

            self.timer_label.config(text=f"{self.timer_min.get()} min {self.timer_sec.get()} s")
            self.after(ms=1000, func=update_timer)

        update_timer()

    def set_min(self, x):
        self.timer_min.set(int(float(x)))
        self.upload_timer_label()

    def set_sec(self, x):
        self.timer_sec.set(int(float(x)))
        self.upload_timer_label()

    def upload_timer_label(self):
        self.timer_label.config(text=f"{self.timer_min.get()} min {self.timer_sec.get()} s")

    def reset_timer(self):
        self.timer_check.set(0)
        self.set_min(1)
        self.set_sec(0)
        self.upload_timer_label()
        self.timer_start.config(state='normal')
        self.scale_min.config(state='normal')
        self.scale_sec.config(state='normal')


app = App()
app.mainloop()
