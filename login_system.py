import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x430+400+200")
root.title("Account Login")

login_password = {}


def register():

    geo = root.winfo_geometry()
    register_window = tk.Toplevel()
    register_window.geometry(geo)
    register_window.title('Register')

    root.withdraw()

    def fun():
        register_window.destroy()
        root.destroy()

    register_window.protocol('WM_DELETE_WINDOW', fun)

    r_l1 = tk.Label(register_window, text="Sign up - It's quick and easy.", font=(None, 20), borderwidth=2,
                    relief=tk.SOLID, padx=20, pady=20)
    r_l1.pack(pady=20)

    def signin():

        global login_password
        log = r_e1.get()
        passw = r_e2.get()
        if log in login_password:
            messagebox.showinfo(title='Sth went wrong', message='Login not available')
        else:
            login_password[log] = passw
            messagebox.showinfo(title='Success', message='Your account has been successfully created.')
            register_quit()

    def register_quit():
        root.geometry(register_window.winfo_geometry())
        root.deiconify()
        register_window.destroy()

    login = tk.StringVar()
    login.set('login')

    password = tk.StringVar()
    password.set('********')

    r_e1 = tk.Entry(register_window, textvariable=login, font=(None, 15), width=20)
    r_e1.pack(pady=(10, 20))

    r_e2 = tk.Entry(register_window, textvariable=password, font=(None, 15), width=20, show='*')
    r_e2.pack(pady=20)

    r_b1 = tk.Button(register_window, text="Register", font=(None, 15), width=20, height=2, borderwidth=2,
                     command=signin)
    r_b1.pack(pady=20)

    r_b2 = tk.Button(register_window,text="Quit", font=(None, 15), width=20, height=2, borderwidth=2,
                     command=register_quit)
    r_b2.pack()


def login():

    geo = root.winfo_geometry()
    login_window = tk.Toplevel()
    login_window.geometry(geo)
    login_window.title('Log in')

    root.withdraw()

    def fun():
        login_window.destroy()
        root.destroy()

    login_window.protocol('WM_DELETE_WINDOW', fun)

    r_l1 = tk.Label(login_window, text="Enter Login and password", font=(None, 20), borderwidth=2,
                    relief=tk.SOLID, padx=20, pady=20)
    r_l1.pack(pady=20)

    def log_in():

        global login_password
        log = l_e1.get()
        passw = l_e2.get()
        if log not in login_password or passw not in login_password.values():
            messagebox.showinfo(title='Sth went wrong', message='Wrong login or password')

        else:
            messagebox.showinfo(title='Success', message='You have successfully logged in')

            _geo = login_window.winfo_geometry()
            logged_window = tk.Toplevel()
            logged_window.geometry(_geo)
            login_window.withdraw()

            def fun():
                logged_window.destroy()
                root.destroy()

            logged_window.protocol('WM_DELETE_WINDOW', fun)

            def logged_quit():
                root.geometry(logged_window.winfo_geometry())
                root.deiconify()
                logged_window.destroy()

            l1_l1 = tk.Label(logged_window, text='Secret Area', font=(None, 20), width=20, borderwidth=2, relief=tk.SOLID,
                            padx=20, pady=20)
            l1_l1.pack(pady=10, padx=(0, 10) )

            l1_b1 = tk.Button(logged_window, text="Log out", font=(None, 15), width=20, height=2, borderwidth=2,
                             command=logged_quit)
            l1_b1.pack()

            # login_password[log] = passw
            # messagebox.showinfo(title='Success', message='Your account has been successfully created.')
            # register_quit()

    def login_quit():
        root.geometry(login_window.winfo_geometry())
        root.deiconify()
        login_window.destroy()

    login = tk.StringVar()
    login.set('login')

    password = tk.StringVar()
    password.set('********')

    l_e1 = tk.Entry(login_window, textvariable=login, font=(None, 15), width=20)
    l_e1.pack(pady=(10, 20))

    l_e2 = tk.Entry(login_window, textvariable=password, font=(None, 15), width=20, show='*')
    l_e2.pack(pady=20)

    l_b1 = tk.Button(login_window, text="Log in", font=(None, 15), width=20, height=2, borderwidth=2,
                     command=log_in)
    l_b1.pack(pady=20)

    l_b2 = tk.Button(login_window, text="Quit", font=(None, 15), width=20, height=2, borderwidth=2,
                     command=login_quit)
    l_b2.pack()


l1 = tk.Label(root, text='Log in or sign up', font=(None, 20), width=20, borderwidth=2, relief=tk.SOLID,
              padx=20, pady=20)
l1.pack(pady=10, padx=(0, 10) )

b1 = tk.Button(root, text="Login", font=(None, 15), width=20, height=2, borderwidth=2, command=login)
b1.pack(pady=20)

b2 = tk.Button(root, text="Register", font=(None, 15), width=20, height=2, borderwidth=2, command=register)
b2.pack(pady=20)

b3 = tk.Button(root, text="Quit", font=(None, 15), width=20, height=2, borderwidth=2, command=lambda: root.destroy())
b3.pack(pady=20)

root.mainloop()
