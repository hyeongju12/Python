from tkinter import *


def button_clicked():
    print("I got clicked")
    mile = str(int(input.get()) * 1.6)
    my_label.config(text=mile+'km')


window = Tk()
window.title("Mile To Kilometer")
window.minsize(width=300, height=200)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="Input mile")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)









window.mainloop()