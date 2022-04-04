class QuizBrain:
	def __init__(self, q_list):
		self.question_number = 0
		self.question_list = q_list
		self.user_point = 0

	def still_has_question(self):
		return self.question_number < len(self.question_list)

	def next_question(self):
		current_question = self.question_list[self.question_number]
		user_answer = input(f'{self.question_number + 1}. {current_question.text} (True/False) : ')
		self.question_number += 1
		self.check_answer(user_answer, current_question.answer)
		# if qs == self.question_list[self.question_number].answer or qs == 't':
		# 	print("문제를 맞췄습니다.")
		# elif qs != self.question_list['start'].answer or qs == 'f':
		# 	print("문제를 틀렸습니다.")

	def check_answer(self, user_answer, correct_answer):
		if user_answer.lower() == correct_answer.lower():
			print("You got it right")
			self.user_point += 1
		else:
			print("That's wrong.")
		print(f"Correct answer was : {correct_answer}")
		print(f"Your current score is : {self.user_point}/{self.question_number}")
		print("\n")