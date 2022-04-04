from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = question_data[0]['results']
quest_lists = []
if __name__ == '__main__':
	for question in question_bank:
		text = question['question']
		answer = question['correct_answer']
		text = question['question']
		answer = question['correct_answer']
		quest_lists.append(Question(text, answer))

	quiz = QuizBrain(quest_lists)

	while quiz.still_has_question():
		quiz.next_question()

print("You're completed the quiz")
print(f'Your final score was : {quiz.user_point}/{len(question_bank)}')