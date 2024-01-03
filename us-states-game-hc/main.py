# US States Interactive Game
# Author: Victoria Aroworade

import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess The States")

# create image and load in screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Upload CSV and set variables

states_data = pandas.read_csv("50_states.csv")
states = states_data["state"].to_list()
states_count = len(states)

user_answers = []

score = 0

while len(user_answers) < 50:

    answer_state = screen.textinput(f"States Correct {score}/50", prompt="What is another state's name").title()

    if answer_state == "Exit":

        states_to_learn = [state for state in states if state not in user_answers]
        states_to_learn_data = pandas.DataFrame(states_to_learn)
        states_to_learn_data.rename(columns={0: 'US States'}, inplace=True)
        states_to_learn_data.to_csv("states_to_learn.csv")
        break

    for state in states:
        if answer_state == state and answer_state not in user_answers:
            correct_row = states_data[states_data.state == f"{state}"]
            x_cor = int(correct_row.x.item())
            y_cor = int(correct_row.y.item())
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.setposition(x_cor, y_cor)
            t.write(f"{state}", font=("Arial", "10", "normal"))
            user_answers.append(state)
            score += 1


