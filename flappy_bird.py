import tkinter as tk
from random import randint


class Game(tk.Tk):

    def __init__(self):
        super().__init__()

        self.geometry("900x500+200+100")
        self.title('Flappy Bird')

        # Create canvas
        self.canvas = tk.Canvas(background='gray', width=850, height=450, borderwidth=0, highlightthickness=0)
        self.canvas.pack(pady=25, padx=5)

        # Create Bird
        self.bird = self.canvas.create_rectangle(200, 200, 220, 220, fill='black')

        # Bird cinematic quantities
        self.g = 0.002
        self.t = 20
        self.v_0 = 0
        self.out = False
        self.fly = True

        # Create Obstacles number 1
        self.o_c_1 = (850, 0, 900, randint(0, 400))  # Obstacle coordinates
        self.obs_up_1 = self.canvas.create_rectangle(*self.o_c_1, fill='green')
        self.obs_down_1 = self.canvas.create_rectangle(self.o_c_1[0], self.o_c_1[3]+150, self.o_c_1[2], 450, fill='green')

        # Create Obstacles number 2
        self.o_c_2 = (1300, 0, 1350, randint(0, 400))  # Obstacle coordinates
        self.obs_up_2 = self.canvas.create_rectangle(*self.o_c_2, fill='red')
        self.obs_down_2 = self.canvas.create_rectangle(self.o_c_2[0], self.o_c_2[3]+150, self.o_c_2[2], 450, fill='red')

        # Loop
        self.bind("<space>", self.velocity_reflection)
        self.bird_fly()
        self.obs_move()

    def velocity_reflection(self, e):
        self.v_0 = -0.35
        if self.out:
            self.canvas.coords(self.bird, 200, 414, 220, 434)
            self.out = False
            self.bird_fly()

    def bird_fly(self):

        coord = self.canvas.coords(self.bird)

        if not self.fly:
            return None

        if coord[3] >= 435:
            self.out = True
            return None

        self.canvas.move(self.bird, 0, self.v_0 * self.t + 0.5*self.g * self.t**2)

        self.v_0 += self.g * self.t

        self.after(self.t, self.bird_fly)

    def obs_move(self):

        coord_1 = self.canvas.coords(self.obs_up_1)
        coord_2 = self.canvas.coords(self.obs_up_2)

        if self.check_collision():
            self.fly = False
            return None

        if coord_1[2] <= 0:
            self.o_c_1 = (850, 0, 900, randint(0, 300))
            self.canvas.coords(self.obs_up_1, *self.o_c_1)
            self.canvas.coords(self.obs_down_1, self.o_c_1[0], self.o_c_1[3]+150, self.o_c_1[2], 450)

        self.canvas.move(self.obs_up_1, -10, 0)
        self.canvas.move(self.obs_down_1, -10, 0)

        if coord_2[2] <= 0:
            self.o_c_2 = (850, 0, 900, randint(0, 300))
            self.canvas.coords(self.obs_up_2, *self.o_c_2)
            self.canvas.coords(self.obs_down_2, self.o_c_2[0], self.o_c_2[3]+150, self.o_c_2[2], 450)

        self.canvas.move(self.obs_up_2, -10, 0)
        self.canvas.move(self.obs_down_2, -10, 0)

        self.after(50, self.obs_move)

    def check_collision(self):
        coord = self.canvas.coords(self.bird)

        coll = self.canvas.find_overlapping(*coord)

        if len(coll) != 1:
            return True
        else:
            return False


if __name__ == '__main__':
    game = Game()
    game.mainloop()
