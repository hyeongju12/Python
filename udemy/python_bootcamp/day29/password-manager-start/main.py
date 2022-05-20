from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
	password_symbols = [random.choice(symbols ) for _ in range(random.randint(2, 4))]
	password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

	password_list = password_letters + password_symbols + password_numbers
	random.shuffle(password_list)

	password = ''.join(password_list)
	password_entry.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_data = {website : {
		"email": email,
		"password": password,
	}}

	if len(website) == 0 and len(password) == 0:
		messagebox.showinfo(title='Check your Inputs', message='정보를 입력해주세요.')
	else:
		is_ok = messagebox.askokcancel(title='Confirm', message=f'website : {website}\nemail : {email}\npassword: {password}\n')
		if is_ok:
			try:
				with open('data.json', 'r') as file:
					data = json.load(file)
			except FileNotFoundError:
				with open('data.json', 'w') as file:
					json.dumps(new_data, file, indent=4)
			else:
				data.update(new_data)

				with open('data.json', 'a') as file:
					json.dump(new_data, file, indent=4)
					print("save data")
			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)


def find_password():
	key = search_entry.get()
	with open('data.json', 'r') as passwords:
		data = json.load(passwords)
		try:
			messagebox.showinfo(title='Check your Inputs', message=f'{data[key]}')
		except KeyError:
			messagebox.showerror(title='Check your Inputs', message=f'{data[key]} not in data.json')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Generator')

image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.pack()
canvas.grid(column=1, row=0)

search_label = Label(text='search :')
search_label.grid(row=1, column=2)
website_label = Label(text='webstite :')
website_label.grid(row=2, column=0)
user_label = Label(text='user :')
user_label.grid(row=3, column=0)
password_label = Label(text='password :')
password_label.grid(row=4, column=0)

search_entry = Entry(width=36)
search_entry.grid(row=1, column=1, columnspan=2)
website_entry = Entry(width=36)
website_entry.grid(row=2, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=3, column=1, columnspan=2)
email_entry.insert(0, "hyeongju@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=4, column=1)

generate_password_button = Button(text='Generate Password', command=gen_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=3, rowspan=2)


window.mainloop()