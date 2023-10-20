  import tkinter as tk
from tkinter import ttk
import math

# Create a function to update the display when a button is clicked
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Create a function to perform calculations
def calculate():
    current = entry.get()
    try:
        result = eval(current)  # Use eval to calculate the expression
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a function to calculate square root
def square_root():
    current = entry.get()
    try:
        result = math.sqrt(float(current))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a function to calculate percentage
def percentage():
    current = entry.get()
    try:
        result = eval(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a function to clear the display
def clear():
    entry.delete(0, tk.END)

# Create a function to perform backspace
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

# Create the main window
root = tk.Tk()
root.title("Calculator by Dhruvz")

# Create an entry field for input with a sleek style
style = ttk.Style()
style.configure("TEntry", font=('Arial', 18))
entry = ttk.Entry(root, style="TEntry")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

# Create calculator buttons with a modern appearance
button_style = ttk.Style()
button_style.configure("TButton", font=('Arial', 14))
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    ttk.Button(root, text=button_text, style="TButton", command=lambda text=button_text: button_click(text) if text != '=' else calculate() if text == '=' else clear()).grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create additional calculator buttons for square root, percentage, and backspace
ttk.Button(root, text='√', style="TButton", command=square_root).grid(row=1, column=4, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
ttk.Button(root, text='%', style="TButton", command=percentage).grid(row=2, column=4, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
ttk.Button(root, text='C', style="TButton", command=clear).grid(row=3, column=4, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")
ttk.Button(root, text='⌫', style="TButton", command=backspace).grid(row=4, column=4, padx=5, pady=5, ipadx=5, ipady=5, sticky="nsew")

# Configure rows and columns to expand with the window
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter main loop
root.mainloop()
