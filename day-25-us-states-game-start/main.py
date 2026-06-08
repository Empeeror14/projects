import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Games")
image = "/Users/victoriamadedor/Desktop/Stan's projects/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)

player = turtle.Turtle()
player.hideturtle()
player.penup()

# with open("/Users/victoriamadedor/Desktop/Stan's projects/day-25-us-states-game-start/50_states.csv") as data:
#     all_states = data.readlines()
#     print(all_states)

data = pandas.read_csv("/Users/victoriamadedor/Desktop/Stan's projects/day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    if not answer_state:
        break
    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("/Users/victoriamadedor/Desktop/Stan's projects/day-25-us-states-game-start/states_to_learn.csv")
        break
    elif answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        player.hideturtle()
        player.penup()
        state_data = data[data.state == answer_state]
        player.goto(state_data.x.item(), state_data.y.item())
        player.write(state_data.state.item())
        
turtle.mainloop()