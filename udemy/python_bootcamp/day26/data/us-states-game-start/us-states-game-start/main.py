import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
print(all_states)

guessed_states = []

while len(guessed_states) < 50:
	answer_state = screen.textinput(title="Guess the state",prompt="What's another state's name")

	if answer_state == "Exit":
		missing_states = []
		for state in all_states:
			if state not in guessed_states:
				missing_states.append(state)
		new_data = pd.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break


	if answer_state in all_states:
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data[data.state == answer_state]
		guessed_states.append(answer_state)
		t.goto(float(state_data.x), float(state_data.y))
		t.write(answer_state)
		print(guessed_states)

screen.exitonclick()