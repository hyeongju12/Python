import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("GUI add Label")

ttk.Label(win, text="A label").grid(column=0, row=0)
win.mainloop()
