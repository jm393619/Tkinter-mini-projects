import tkinter as tk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400+300+200")
        self.title("Gravity simulator")

        self.v_x_0 = 0.1
        self.v_y_0 = -0.2
        self.t = 10
        self.g = 0.002

        self.canvas = tk.Canvas(self, width=350, height=350, background='gray')
        self.canvas.pack(pady=20, padx=20)

        self.r1 = self.canvas.create_oval(150, 100, 160, 110, fill='black')

        self.mouse = None

        self.looper(self.v_x_0, self.v_y_0)

        self.bind("<Button-1>", self.fun)
        self.bind("<ButtonRelease-1>", self.fun)

    def fun(self, event):
        self.mouse = event.type == '4'

    def looper(self, v_x_0, v_y_0):

        coord = self.canvas.coords(self.r1)
        if coord[3] >= 350 or coord[1] <= 0:
            v_y_0 = - v_y_0
        if coord[2] >= 350 or coord[0] <= 0:
            v_x_0 = - v_x_0

        if self.mouse:
            # v_y_0 = - abs(self.v_y_0)
            v_y_0 = - abs(v_y_0)
            self.mouse = None

        self.canvas.move(self.r1, v_x_0 * self.t, v_y_0 * self.t)

        v_y_0 += 0.5 * self.g * self.t

        self.after(self.t, lambda: self.looper(v_x_0, v_y_0))


if __name__ == "__main__":
    root = Root()
    root.mainloop()
