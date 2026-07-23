# Strong Password Generator (GUI)
# Simple Python Tkinter Application

import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Password Generator ---------------- #
def generate_password():
    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Please enter your name.")
        return

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{}?/"

    # Generate a strong random part
    random_part = (
        random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase)
        + random.choice(numbers)
        + random.choice(symbols)
    )

    remaining = ''.join(
        random.choice(letters + numbers + symbols)
        for _ in range(8)
    )

    password_list = list(random_part + remaining)
    random.shuffle(password_list)

    # Add first 3 letters of user's name
    password = name[:3].capitalize() + "".join(password_list)

    password_var.set(password)


# ---------------- Copy Password ---------------- #
def copy_password():
    password = password_var.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Success", "Password copied to clipboard! 📋")


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("🔐 Strong Password Generator")
root.geometry("500x300")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Strong Password Generator",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Enter Your Name:", font=("Arial", 12)).pack()

name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=8)

tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    command=generate_password,
    bg="green",
    fg="white",
).pack(pady=10)

password_var = tk.StringVar()

password_entry = tk.Entry(
    root,
    textvariable=password_var,
    width=35,
    font=("Consolas", 14),
    justify="center",
)
password_entry.pack(pady=10)

tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    command=copy_password,
    bg="blue",
    fg="white",
).pack(pady=5)

tk.Label(
    root,
    text="✔ Strong Password: Letters + Numbers + Symbols",
    font=("Arial", 10),
).pack(pady=15)

root.mainloop()