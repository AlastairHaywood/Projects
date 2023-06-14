
# #import libraries
import tkinter as tk
from tkinter import ttk

expression = ""

root = tk.Tk()

#base specs
root.geometry("")
root.resizable(0, 0)
root.title("Calculator")

input_value = ""
display_text = tk.StringVar()


def press(item):
    global input_value
    
    input_value = input_value + str(item)

    display_text.set(input_value)


def press_clear():
    global input_value

    input_value = ""

    display_text.set("")


def press_equal():
    global input_value
    try:
        result = str(eval(input_value))

        display_text.set(result)

        input_value = ""
    except:
        display_text.set("Error")
        input_value = ""


input_frame = ttk.Frame(root, width=312, height=50)
input_frame.pack(side = tk.TOP)

input_field = tk.Entry(input_frame, textvariable = display_text, width=50, justify = tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


buttons_frame = tk.Frame(root, width=300, height=250)
buttons_frame.pack()


clear_button = tk.Button(buttons_frame, text = "C", width=32, height=3, command = lambda: press_clear())
clear_button.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_button = tk.Button(buttons_frame, text = "/", width=10, height=3, command = lambda: press("/"))
divide_button.grid(row=0, column=3, padx=1, pady=1)


seven_button = tk.Button(buttons_frame, text = "7", width=10, height=3, command = lambda: press(7))
seven_button.grid(row=1, column=0, padx=1, pady=1)

eight_button = tk.Button(buttons_frame, text = "8", width=10, height=3, command = lambda: press(8))
eight_button.grid(row=1, column=1, padx=1, pady=1)

nine_button = tk.Button(buttons_frame, text = "9", width=10, height=3, command = lambda: press(9))
nine_button.grid(row=1, column=2, padx=1, pady=1)

multiply_button = tk.Button(buttons_frame, text = "*", width=10, height=3, command = lambda: press("*"))
multiply_button.grid(row=1, column=3, padx=1, pady=1)


four_button = tk.Button(buttons_frame, text = "4", width=10, height=3, command = lambda: press(4))
four_button.grid(row=2, column=0, padx=1, pady=1)

five_button = tk.Button(buttons_frame, text = "5", width=10, height=3, command = lambda: press(5))
five_button.grid(row=2, column=1, padx=1, pady=1)

six_button = tk.Button(buttons_frame, text = "6", width=10, height=3, command = lambda: press(6))
six_button.grid(row=2, column=2, padx=1, pady=1)

minus_button = tk.Button(buttons_frame, text = "-", width=10, height=3, command = lambda: press("-"))
minus_button.grid(row=2, column=3, padx=1, pady=1)


one_button = tk.Button(buttons_frame, text = "1", width=10, height=3, command = lambda: press(1))
one_button.grid(row=3, column=0, padx=1, pady=1)

two_button = tk.Button(buttons_frame, text = "2", width=10, height=3, command = lambda: press(2))
two_button.grid(row=3, column=1, padx=1, pady=1)

three_button = tk.Button(buttons_frame, text = "3", width=10, height=3, command = lambda: press(3))
three_button.grid(row=3, column=2, padx=1, pady=1)

plus_button = tk.Button(buttons_frame, text = "+", width=10, height=3, command = lambda: press("+"))
plus_button.grid(row=3, column=3, padx=1, pady=1)


zero_button = tk.Button(buttons_frame, text = "0", width=21, height=3, command = lambda: press(0))
zero_button.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

dot_button = tk.Button(buttons_frame, text = "-", width=10, height=3, command = lambda: press("-"))
dot_button.grid(row=4, column=2, padx=1, pady=1)

equal_button = tk.Button(buttons_frame, text = "=", width=10, height=3, command = lambda: press_equal())
equal_button.grid(row=4, column=3, padx=1, pady=1)

root.mainloop()