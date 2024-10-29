import tkinter as tk

# Function to update the expression in the entry field
def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the entry field
def button_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the final expression
def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Initialize window
window = tk.Tk()
window.geometry("400x500")
window.title("Calculator")

# Expression to store calculations
expression = ""

# StringVar to update entry field
input_text = tk.StringVar()

# Entry field for displaying the expression
input_frame = tk.Frame(window, width=400, height=50, bd=0)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for buttons
btns_frame = tk.Frame(window, width=400, height=450, bg="grey")
btns_frame.pack()

# First row
tk.Button(btns_frame, text="C", width=32, height=3, command=button_clear).grid(row=0, column=0, columnspan=3)
tk.Button(btns_frame, text="/", width=10, height=3, command=lambda: button_click("/")).grid(row=0, column=3)

# Second row
tk.Button(btns_frame, text="7", width=10, height=3, command=lambda: button_click(7)).grid(row=1, column=0)
tk.Button(btns_frame, text="8", width=10, height=3, command=lambda: button_click(8)).grid(row=1, column=1)
tk.Button(btns_frame, text="9", width=10, height=3, command=lambda: button_click(9)).grid(row=1, column=2)
tk.Button(btns_frame, text="*", width=10, height=3, command=lambda: button_click("*")).grid(row=1, column=3)

# Third row
tk.Button(btns_frame, text="4", width=10, height=3, command=lambda: button_click(4)).grid(row=2, column=0)
tk.Button(btns_frame, text="5", width=10, height=3, command=lambda: button_click(5)).grid(row=2, column=1)
tk.Button(btns_frame, text="6", width=10, height=3, command=lambda: button_click(6)).grid(row=2, column=2)
tk.Button(btns_frame, text="-", width=10, height=3, command=lambda: button_click("-")).grid(row=2, column=3)

# Fourth row
tk.Button(btns_frame, text="1", width=10, height=3, command=lambda: button_click(1)).grid(row=3, column=0)
tk.Button(btns_frame, text="2", width=10, height=3, command=lambda: button_click(2)).grid(row=3, column=1)
tk.Button(btns_frame, text="3", width=10, height=3, command=lambda: button_click(3)).grid(row=3, column=2)
tk.Button(btns_frame, text="+", width=10, height=3, command=lambda: button_click("+")).grid(row=3, column=3)

# Fifth row
tk.Button(btns_frame, text="0", width=21, height=3, command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2)
tk.Button(btns_frame, text=".", width=10, height=3, command=lambda: button_click(".")).grid(row=4, column=2)
tk.Button(btns_frame, text="=", width=10, height=3, command=button_equal).grid(row=4, column=3)

# Run the app
window.mainloop()
