import turtle
import pandas


screen = turtle.Screen()

screen.title("US state game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
data = pandas.read_csv("50_states.csv")

t = turtle.Turtle()
t.hideturtle()
t.penup()



all_states = []
all_states.extend(data["state"].values)

missing_states = []

input_answer = screen.textinput(title="Guess The State", prompt="What's another state's name?")
capitalized_answer = input_answer.capitalize()


guessed_states =[]
score = 0
while len(guessed_states) < 50:
    capitalized_answer = screen.textinput(title="Guess The State", prompt="What's another state's name?").title()

    if capitalized_answer is None: 
        game_on = False
        break
    
    if capitalized_answer == "Exit":
        for states in all_states:
            if states not in guessed_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if capitalized_answer in data["state"].values:
        score += 1
        
        guessed_states.append(capitalized_answer)

        state_row = data[data["state"] == capitalized_answer]
        x_value = int(state_row["x"].values[0])
        y_value = int(state_row["y"].values[0])
        

        t.goto(x_value, y_value)
        t.pendown()
        t.write(capitalized_answer, font=("Arial", 5, "bold"))
        t.penup()


        






screen.exitonclick()

