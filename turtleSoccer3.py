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

# Player Paddle A
A1 = turtle.Turtle()
A1.speed(0)
image1 = "soccerplayer_scaled.gif"
field.addshape(image1)
A1.shape(image1)
A1.penup()
A1.goto(-350, 0)

# Player Paddle B
B1 = turtle.Turtle()
B1.speed(0)
image2 = "soccerplayer2_scaled.gif"
field.addshape(image2)
B1.shape(image2)
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

def A1_left():
    x = A1.xcor()
    x -= 20
    A1.setx(x)

def A1_right():
    x = A1.xcor()
    x += 20
    A1.setx(x)

def A1_down():
    y = A1.ycor()
    y -= 20
    A1.sety(y)

def B1_up():
    y = B1.ycor()
    y += 20
    B1.sety(y)

def B1_left():
    x = B1.xcor()
    x -= 20
    B1.setx(x)

def B1_right():
    x = B1.xcor()
    x += 20
    B1.setx(x)

def B1_down():
    y = B1.ycor()
    y -= 20
    B1.sety(y)

# Keyboard bindings
field.listen()
field.onkeypress(A1_up, "w")
field.onkeypress(A1_left, "a")
field.onkeypress(A1_right, "d")
field.onkeypress(A1_down, "s")
field.onkeypress(B1_up, "Up")
field.onkeypress(B1_left, "Left")
field.onkeypress(B1_right, "Right")
field.onkeypress(B1_down, "Down")

# Hit Check
hitcheckA = 0
hitcheckB = 0

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
    if turtle.xcor() > 500:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        A1.goto(-350, 0)
        B1.goto(350, 0)
        turtle.goto(0, 0)
        turtle.dx *= -1

    elif turtle.xcor() < -500:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        A1.goto(-350, 0)
        B1.goto(350, 0)
        turtle.goto(0, 0)
        turtle.dx *= -1

    # Player Paddle and ball collisions
    # On first hit, dy does not change, but dy is flipped for each consecutive hit after the first
    if turtle.xcor() < A1.xcor() + 50 and turtle.xcor() > A1.xcor() - 50 and turtle.ycor() < A1.ycor() + 100 and turtle.ycor() > A1.ycor() - 100:
        if hitcheckA == 1:    
            turtle.dx = 0.2
            turtle.dy *= -1
        else:
            turtle.dx = 0.2
            hitcheckA = 1
            hitcheckB = 0
        
        # Could add the below sound but causes ball lag: slows down loop and so ball changes position less quickly, so ball appears to move slowly    
        #os.system("afplay bounce.wav&")
    
    elif turtle.xcor() < B1.xcor() + 50 and turtle.xcor() > B1.xcor() - 50 and turtle.ycor() < B1.ycor() + 100 and turtle.ycor() > B1.ycor() - 100:
        if hitcheckB == 1:    
            turtle.dx = -0.2
            turtle.dy *= -1
        else:
            turtle.dx = -0.2
            hitcheckB = 1
            hitcheckA = 0
        # Could add the below sound but causes ball lag: slows down loop and so ball changes position less quickly, so ball appears to move slowly
        #os.system("afplay bounce.wav&")
    
