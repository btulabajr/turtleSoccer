# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
import os

turtle.clearscreen()

field = turtle.Screen()
field.bgpic("field.gif")
field.tracer(0)

# Score
score_a = 0
score_b = 0

A = []

# Team A
for index in range(3):
    A.append(turtle.Turtle())
    A[index].speed(0)
    A[index].shape("circle")
    A[index].color("red")
    A[index].shapesize(stretch_wid=2.5,stretch_len=2.5)
    A[index].penup()
    if index == 1:
        A[index].goto(-200, 0)
    else:
        A[index].goto(-300, (-200 + index*200))

# Team B
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
    y = A[1].ycor()
    y += 20
    A[1].sety(y)

def A1_down():
    y = A[1].ycor()
    y -= 20
    A[1].sety(y)

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
while scoreA < 5 and scoreB < 5:
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
    if turtle.xcor() < -340 and turtle.ycor() < A[1].ycor() + 50 and turtle.ycor() > A[1].ycor() - 50:
        turtle.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif turtle.xcor() > 340 and turtle.ycor() < B1.ycor() + 50 and turtle.ycor() > B1.ycor() - 50:
        turtle.dx *= -1
        os.system("afplay bounce.wav&")
    
