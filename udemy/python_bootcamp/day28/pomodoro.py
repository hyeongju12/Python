import threading
from tkinter import *
import datetime
from math import floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
TIMER = None

def reset_timer():
	global REPS
	REPS = 0
	window.after_cancel(TIMER)
	canvas.itemconfig(timer_text, text="00:00")
	timer.config(text="Timer")
	check_mark.config(text="")

def start_timer():
	global REPS
	REPS += 1

	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	if REPS % 8 == 0:
		count_down(long_break_sec)
		timer.config(text="break", fg=RED)
	elif REPS % 2 == 0:
		count_down(short_break_sec)
		timer.config(text="break", fg=PINK)
	else:
		count_down(work_sec)
		timer.config(text="work", fg=GREEN)


def count_down(count):

	count_min = floor(count / 60)
	count_sec = count % 60

	if int(count_sec) < 10:
		count_sec = f'0{count_sec}'

	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global TIMER
		TIMER = window.after(1000, count_down, count -1)
	else:
		start_timer()
		marks = ""
		work_sessions = floor(REPS/2)
		for _ in range(work_sessions):
			marks += "✅"
		check_mark.config(text=marks)

window = Tk()
window.title('Pomotoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image_path = PhotoImage(file="pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=image_path)
timer_text=canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.pack()
canvas.grid(column=1, row=1)

timer = Label(text="Timer", bg=YELLOW,  font=(FONT_NAME, 40, 'bold'), fg=GREEN)
timer.grid(column=1, row=0)

check_mark = Label(text='✅ ', font=10, bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=2)

start_bt = Button(text='start', command=start_timer)
start_bt.grid(column=0, row=2)

reset_bt = Button(text='reset', command=reset_timer)
reset_bt.grid(column=2, row=2)

window.mainloop()