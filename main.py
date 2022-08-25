from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

colors = ['blue', 'green', 'black', 'pink', 'red', 'orange']

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

racing_turtles = []
race_on = False

y_axis = -100
for index in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.clone()
    new_turtle.backward(90)
    new_turtle.forward(100)
    new_turtle.color(colors[index])
    new_turtle.goto(x=-220, y=y_axis)
    racing_turtles.append(new_turtle)
    y_axis += 40

if user_bet:
    race_on = True


while race_on:
    for racer in racing_turtles:
        racer.forward(random.randint(0, 10))
        if racer.xcor() > 230:
            race_on = False
            winning_color = racer.pencolor()
            if winning_color == user_bet.lower():
                print(f"You won! The {winning_color} turtle has won!")