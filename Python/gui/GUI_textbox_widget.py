import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("GUI add Label")

a_label = ttk.Label(win, text="A label")
a_label.grid(column=0, row=0)


def click_me():
    action.configure(text='Hello ' + name.get())

# Changing our Label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
action = ttk.Button(win, text="Click Me", command=click_me)
action.grid(column=1, row=0)



name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

actinon = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)



action.configure(state='disabled')
name_entered.focus()

win.mainloop()
