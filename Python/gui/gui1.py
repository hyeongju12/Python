import tkinter as tk

# TK class Instance 생성
win = tk.Tk()

# Add a Title
win.title("Python First GUI")

# Disable Resizing the GUI
# x축, y축 사이즈 변경 불가
win.resizable(True, False)

# Start GuI
win.mainloop()
