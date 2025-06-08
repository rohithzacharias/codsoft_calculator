import customtkinter as ctk
import math
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Scientific Calculator")
app.geometry("420x650")
app.resizable(False, False)

expression = ""
display_var = ctk.StringVar()

def update_display(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear_display():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = eval(expression.replace("^", "**"))
        display_var.set(str(result))
        expression = str(result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression\n{e}")
        expression = ""

def apply_function(func, convert_to_radians=False):
    global expression
    try:
        value = eval(expression.replace("^", "**"))
        if convert_to_radians:
            value = math.radians(value)
        result = func(value)
        display_var.set(str(result))
        expression = str(result)
    except Exception as e:
        messagebox.showerror("Error", f"Function Error\n{e}")
        expression = ""

# Setup display
display = ctk.CTkEntry(app, textvariable=display_var, font=("Arial", 28), justify="right", height=60, width=400, corner_radius=10)
display.pack(pady=15, padx=10)

# Scientific button layout
sci_buttons = [
    ["sin", "cos", "tan", "√"],
    ["log", "ln", "π", "e"],
    ["x^2", "x^3", "x^y", "10^x"],
    ["1/x", "x!", "Deg", "%"]
]

sci_frame = ctk.CTkFrame(app)
sci_frame.pack(pady=5)

for row in sci_buttons:
    row_frame = ctk.CTkFrame(sci_frame)
    row_frame.pack()
    for btn in row:
        def make_action(b=btn):
            if b == "sin": return lambda: apply_function(math.sin, True)
            elif b == "cos": return lambda: apply_function(math.cos, True)
            elif b == "tan": return lambda: apply_function(math.tan, True)
            elif b == "sinh": return lambda: apply_function(math.sinh)
            elif b == "cosh": return lambda: apply_function(math.cosh)
            elif b == "tanh": return lambda: apply_function(math.tanh)
            elif b == "√": return lambda: apply_function(math.sqrt)
            elif b == "log": return lambda: apply_function(math.log10)
            elif b == "ln": return lambda: apply_function(math.log)
            elif b == "π": return lambda: update_display(math.pi)
            elif b == "e": return lambda: update_display(math.e)
            elif b == "x^2": return lambda: update_display("**2")
            elif b == "x^3": return lambda: update_display("**3")
            elif b == "x^y": return lambda: update_display("**")
            elif b == "10^x": return lambda: apply_function(lambda x: 10**x)
            elif b == "1/x": return lambda: apply_function(lambda x: 1/x)
            elif b == "x!": return lambda: apply_function(math.factorial)
            elif b == "Deg": return lambda: apply_function(math.degrees)
            elif b == "%": return lambda: update_display("/100")
            else: return lambda: update_display(b)

        ctk.CTkButton(row_frame, text=btn, font=("Arial", 16), width=90, height=40, command=make_action()).pack(side="left", padx=5, pady=5)

# Standard buttons
buttons = [
    ["C", "←", "(", ")"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

frame = ctk.CTkFrame(app)
frame.pack(pady=5)

for row in buttons:
    row_frame = ctk.CTkFrame(frame)
    row_frame.pack()
    for btn in row:
        def make_standard_action(b=btn):
            if b == "C": return clear_display
            elif b == "←": return backspace
            elif b == "=": return calculate
            else: return lambda: update_display(b)

        ctk.CTkButton(row_frame, text=btn, font=("Arial", 18), width=90, height=50, command=make_standard_action()).pack(side="left", padx=5, pady=5)

app.mainloop()