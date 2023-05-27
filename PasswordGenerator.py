import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    
    if length.isdigit():
        length = int(length)
        if length > 0:
            password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
            password_entry.delete(0, tk.END)
            password_entry.insert(tk.END, password)
        else:
            messagebox.showerror("Error", "Please enter a positive integer for password length.")
    else:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create and configure the widgets
length_label = tk.Label(window, text="Password Length:")
length_entry = tk.Entry(window, width=10)
generate_button = tk.Button(window, text="Generate", command=generate_password)
password_label = tk.Label(window, text="Generated Password:")
password_entry = tk.Entry(window, width=30)

# Position the widgets using grid layout
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)

# Run the main event loop
window.mainloop()
