from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="bet", prompt='Guess a color')
y_cor = [-60, -30, 0, 30, 60]
color = ['red', 'yellow', 'blue', 'green', 'brown']
turtle_list = []
game = True

for x in range(0, 5):
    tim = Turtle()
    tim.shape('turtle')
    tim.color(color[x])
    tim.penup()
    tim.goto(-230, y_cor[x])
    turtle_list.append(tim)

while game:
    for x in range(0, len(turtle_list)):
        turtle_list[x].forward(random.randint(0, 10))

        if turtle_list[x].pos() > (220, y_cor[x]):
            if bet == color[x]:
                print(f"you win, Color {color[x]} Won")
            else:
                print(f"you Lose, Color {color[x]} Won")
            game = False

screen.exitonclick()
