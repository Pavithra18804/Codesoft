import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(username, length):
    # Generate random characters
    characters = string.ascii_letters + string.digits + string.punctuation
    password = username + ''.join(random.choices(characters, k=length - len(username)))
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def accept_action():
    username = username_entry.get()
    try:
        length = int(length_entry.get())
        if length < len(username):
            messagebox.showerror("Error", "Password length must be greater than username length.")
            return
        password = generate_password(username, length)
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

def reset_action():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_label.config(text="Generated Password: ")

def set_background_color():
    color = color_entry.get()
    if color:
        root.config(bg=color)

root = tk.Tk()
root.title("Password Generator")
root.config(bg="#E0b0FF")  # Set window background color to pink

# Set grid layout margins
root.grid_columnconfigure(0, weight=1, pad=10)
root.grid_columnconfigure(1, weight=1, pad=10)
root.grid_rowconfigure(0, weight=1, pad=10)
root.grid_rowconfigure(1, weight=1, pad=10)
root.grid_rowconfigure(2, weight=1, pad=10)
root.grid_rowconfigure(3, weight=1, pad=10)
root.grid_rowconfigure(4, weight=1, pad=10)
root.grid_rowconfigure(5, weight=1, pad=10)

tk.Label(root, text="Username:", bg="#C66668").grid(row=0, column=0, sticky="w", padx=10, pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password Length:", bg="#924DBF").grid(row=1, column=0, sticky="w", padx=10, pady=5)
length_entry = tk.Entry(root, width=30)
length_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Background Color (e.g., lightblue):", bg="#BDB76B").grid(row=2, column=0, sticky="w", padx=10, pady=5)
color_entry = tk.Entry(root, width=30)
color_entry.grid(row=2, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Generated Password: ", bg="#E9967A")
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

accept_button = tk.Button(root, text="Accept", bg="#DC143C", command=accept_action)
accept_button.grid(row=4, column=0, padx=10, pady=5)

reset_button = tk.Button(root, text="Reset", bg="#5F9EA0",  command=reset_action)
reset_button.grid(row=4, column=1, padx=10, pady=5)

color_button = tk.Button(root, text="Set Background Color", bg="#BC8F8F", command=set_background_color)
color_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()