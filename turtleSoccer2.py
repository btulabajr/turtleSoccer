# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
import os

#turtle.clearscreen()

field = turtle.Screen()
field.bgpic("field.gif")
field.tracer(0)

# Score
score_a = 0
score_b = 0

# Team A
# for player in range(3):
#     playerA(player) = turtle.Turtle()
#     playerA(player).speed(0)
#     playerA(player).shape("circle")
#     playerA(player).color("white")
#     playerA(player).shapesize(st)
A1 = turtle.Turtle()
A1.speed(0)
A1.shape("square")
A1.color("white")
A1.shapesize(stretch_wid=5,stretch_len=1)
A1.penup()
A1.goto(-350, 0)

# Paddle B
B1 = turtle.Turtle()
B1.speed(0)
B1.shape("square")
B1.color("white")
B1.shapesize(stretch_wid=5,stretch_len=1)
B1.penup()
B1.goto(350, 0)

# Ball
image = "ball.gif"
field.addshape(image)
turtle.shape(image)
turtle.penup()

turtle.setx(0)
turtle.sety(0)
turtle.dx = 0.2
turtle.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def A1_up():
    y = A1.ycor()
    y += 20
    A1.sety(y)

def A1_down():
    y = A1.ycor()
    y -= 20
    A1.sety(y)

def B1_up():
    y = B1.ycor()
    y += 20
    B1.sety(y)

def B1_down():
    y = B1.ycor()
    y -= 20
    B1.sety(y)

# Keyboard bindings
field.listen()
field.onkeypress(A1_up, "w")
field.onkeypress(A1_down, "s")
field.onkeypress(B1_up, "Up")
field.onkeypress(B1_down, "Down")

# Main game loop
while True:
    field.update()
    
    # Move the ball
    turtle.setx(turtle.xcor() + turtle.dx)
    turtle.sety(turtle.ycor() + turtle.dy)

    # Border checking

    # Top and bottom
    if turtle.ycor() > 290:
        turtle.sety(290)
        turtle.dy *= -1
        os.system("afplay bounce.wav&")
    
    elif turtle.ycor() < -290:
        turtle.sety(-290)
        turtle.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if turtle.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, 0)
        turtle.dx *= -1

    elif turtle.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        turtle.goto(0, 0)
        turtle.dx *= -1

    # Paddle and ball collisions
    if turtle.xcor() < -340 and turtle.ycor() < A1.ycor() + 50 and turtle.ycor() > A1.ycor() - 50:
        turtle.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif turtle.xcor() > 340 and turtle.ycor() < B1.ycor() + 50 and turtle.ycor() > B1.ycor() - 50:
        turtle.dx *= -1
        os.system("afplay bounce.wav&")
    