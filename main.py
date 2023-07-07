import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the numbers and results
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 0),
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, padx=20, pady=10,
                       command=lambda num=button_text: button_click(num))
    button.grid(row=row, column=column)

# Create operator buttons
operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("=", 4, 2),
    ("C", 4, 1),
]

for button_text, row, column in operators:
    button = tk.Button(window, text=button_text, padx=20, pady=10)
    button.grid(row=row, column=column)
    if button_text == "=":
        button.config(command=button_equal)
    elif button_text == "C":
        button.config(command=button_clear)
    else:
        button.config(command=lambda operator=button_text: button_click(operator))

# Run the main loop
window.mainloop()
