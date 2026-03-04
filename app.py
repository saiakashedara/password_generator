import tkinter as tk
from logic import generate_password


def generate():

    length = int(length_entry.get())

    numbers = numbers_var.get()
    symbols = symbols_var.get()

    password = generate_password(length, numbers, symbols)

    result_var.set(password)


root = tk.Tk()
root.title("Password Generator")


tk.Label(root, text="Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack()

numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate).pack()

result_var = tk.StringVar()

tk.Label(root, textvariable=result_var).pack()

root.mainloop()