import tkinter
from tkinter import *
import pandas as pd
import random

DATA = pd.read_csv('french_words.csv')
current_card = {}
to_learn = {}

try:
	data = pd.read_csv('french_words.csv')
except FileNotFoundError:
	original_data = pd.read_csv("french_words.csv")
	print(original_data)
	to_learn = original_data.to_dict(orient='records')
else:
	to_learn = data.to_dict(orient='records')


def next_card():
	global  current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	canvas.itemconfig(card_title, text="French", fill='black')
	canvas.itemconfig(card_word_text, text=current_card["French"], fill='black')
	canvas.itemconfig(card_background, image=card_front_img)
	flip_timer = window.after(3000, func=flip_card)


def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word_text, text=current_card["English"], fill="white")
	canvas.itemconfig(card_background, image=card_back_img)


def is_known():
	to_learn.remove(current_card)
	print(len(to_learn))
	data = pd.DataFrame(to_learn)
	data.to_csv("words_to_learn.csv", index=False)
	next_card()

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Dictionary')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800)
front_img=tkinter.PhotoImage(file='card_front.png')
canvas.create_image(400, 263, image=front_img)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file='card_back.png')
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, "italic"))
card_word_text = canvas.create_text(400, 263, text='Word', font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

o_btn_image = PhotoImage(file='right.png')
o_btn = Button(height=50, width=50, image=o_btn_image, highlightthickness=0,
			   command=next_card)
o_btn.grid(row=1, column=1)

x_btn_image = PhotoImage(file='wrong.png')
x_btn = Button(height=50, width=50, image=x_btn_image, highlightthickness=0,
			   command=is_known)
x_btn.grid(row=1, column=0)

next_card()

window.mainloop()