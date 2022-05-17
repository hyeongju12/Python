from tkinter import *

window = Tk()
window.title('테스트')
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label.config(text="new text")


def button_clicked():
	my_label.config(text='text')
	if input.get():
		new_text = input.get()
		my_label.config(text=new_text)

#Enntry : 텍스트를 입력받는 객체

input = Entry(width=10)
input.pack()

button = Button(text='click', command=button_clicked)
button.pack(side='right')

window.mainloop()