import tkinter as tk

root = tk.Tk()
root.geometry("350x200")
root.title('Converter')

def convert():
    try:
        temp_f = int(entry1.get())
    except:
        temp_f = 0

    temp_c = round((temp_f-32) / 1.8, 2)

    label4 = tk.Label(frame1, text=f'{temp_c}')
    label4.grid(row=1, column=1)


def convert2():
    try:
        temp_c = int(entry2.get())
    except:
        temp_c = 0

    temp_f = round((temp_c*1.8)+32, 2)

    label7 = tk.Label(frame1, text=f'{temp_f}')
    label7.grid(row=3, column=1)

# Menu
main_menu = tk.Menu(root)
root.config(menu=main_menu)

file_menu = tk.Menu(main_menu)
main_menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New', command=lambda: ...)
file_menu.add_command(label='Open', command=lambda: ...)
file_menu.add_separator()
file_menu.add_command(label='Close', command=lambda: ...)

edit_menu = tk.Menu(main_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)

edit_menu.add_command(label='Cut', command=lambda: ...)
edit_menu.add_command(label='Copy', command=lambda: ...)

paste_menu = tk.Menu(edit_menu)
edit_menu.add_cascade(label='Paste', menu=paste_menu)

paste_menu.add_command(label='Paste', command=lambda: ...)
paste_menu.add_command(label='Paste From History', command=lambda: ...)
paste_menu.add_command(label='Paste as Plain Text', command=lambda: ...)

edit_menu.add_command(label='Delete', command=lambda: ...)

# Frame1
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, padx=(10,0), pady=(10,0))

label1 = tk.Label(frame1, text='Fahrenheit', padx=15, pady=10)
label1.grid(row=0, column=0)

entry1 = tk.Entry(frame1, width=20)
entry1.grid(row=0, column=1)

label2 = tk.Label(frame1, text='Celsjusz', padx=15, pady=10)
label2.grid(row=1, column=0, sticky=tk.W)

label3 = tk.Label(frame1)
label3.grid(row=1, column=1, sticky=tk.W)

label5 = tk.Label(frame1, text='Celsjusz', padx=15, pady=10)
label5.grid(row=2, column=0, sticky=tk.W)

entry2 = tk.Entry(frame1, width=20)
entry2.grid(row=2, column=1)

label6 = tk.Label(frame1, text='Fahrenheit', padx=15, pady=10)
label6.grid(row=3, column=0, sticky=tk.W)

# Frame2

frame2 = tk.Frame(root)
frame2.grid(row=0, column=1, sticky=tk.N, pady=(10,0))

button1 = tk.Button(frame2, text='Convert', padx=10, command=convert)
button1.grid(row=0, column=0, padx=20, pady=6, sticky=tk.N)

button1 = tk.Button(frame2, text='Convert', padx=10, command=convert2)
button1.grid(row=1, column=0, padx=20, pady=50)

root.mainloop()