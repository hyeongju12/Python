# import smtplib
# my_email = "@.om"
# password = "!"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as conn:
# 	conn.starttls()
# 	conn.login(user=my_email, password=password)
# 	conn.sendmail(
# 		from_addr=my_email,
# 		to_addrs="hyeongju12@gmail.com",
# 		msg="Subject:Hello \n\n This is the body of my email"
# 	)
import pandas as pd
import datetime as dt
import random
import smtplib


def send_email(from_email, password, to_email, message):
	with smtplib.SMTP("smtp.gmail.com") as conn:
		conn.starttls()
		conn.login(user=from_email, password=password)
		conn.sendmail(
			from_addr = from_email,
			to_addrs = to_email,
			msg = 'Subject:Happy Birthday!\n\n' + message,
		)


def generate_msg(name):
	num = random.randint(1,3)
	with open(f'./letter_templates/letter_{num}.txt', 'r') as letters:
		msg = letters.read()
		msg = msg.replace('[NAME]', name)
	return msg


def check_birthday():
	cur = dt.datetime.now()
	month = cur.month
	day = cur.day
	return month, day


mem_list = pd.read_csv('birthdays.csv').to_dict()

for i in range(len(mem_list['name'])):
	mem_births = mem_list['month'][i], mem_list['day'][i]
	if check_birthday() == mem_births:
		from_email =  "___EMAIL_HERE____"
		password = "___PASSWORD_HERE___"
		to_email = mem_list['email'][i]
		message = generate_msg(mem_list['name'][i])
		try:
			send_email(from_email, password,to_email, message)
			print('메시지 전송 성공')
		except ConnectionError:
			print('메시지 전송 실패')
