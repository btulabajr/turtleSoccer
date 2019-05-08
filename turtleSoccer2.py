# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
from pynput import keyboard
import sys

# This list will hold all currently-pressed keyboard inputs
keyList = list()
error = 'This game accepts alphanumerical keys, namely qweasd and uiojkl.'
# Initialize player select indices
ai, bi = 1, 1

def on_press(key):
    try:
        if key.char not in keyList:
            keyList.append(key.char)
    except AttributeError:
        print(error)

def on_release(key):
    global ai, bi
    try:
        if key.char in keyList:
            keyList.remove(key.char)
            # Button change rather than continuous
            if key.char == 'q': ai = playerIncrement(ai, -1)
            if key.char == 'e': ai = playerIncrement(ai, 1)
            if key.char == 'u': bi = playerIncrement(bi, -1)
            if key.char == 'o': bi = playerIncrement(bi, 1)
    except AttributeError:
        print(error)

# Blocking keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Field
turtle.clearscreen()
field = turtle.Screen()
field.bgpic("field.gif")
field.tracer(0)
# Graphic is 1200 x 800 pixels centered around 0,0
X, Y = 600, 400

# Team A
A = []
for index in range(3):
    A.append(turtle.Turtle())
    A[index].speed(0)
    playerA = "box-turtle.gif"
    field.addshape(playerA)
    A[index].shape(playerA)
    A[index].penup()
    if index == 1:
        A[index].goto(-X*0.3, 0)
    else:
        A[index].goto(-X*0.5, (-Y*0.5 + index*Y*0.5))

# Team B
B = []
for index in range(3):
    B.append(turtle.Turtle())
    B[index].speed(0)
    playerB = "sea-turtle.gif"
    field.addshape(playerB)
    B[index].shape(playerB)
    B[index].penup()
    if index == 1:
        B[index].goto(X*0.3, 0)
    else:
        B[index].goto(X*0.5, (-Y*0.5 + index*Y*0.5))

# Ball
ball = turtle.Turtle()
ball.speed(0)
image = "ball.gif"
field.addshape(image)
ball.shape(image)
ball.penup()
ball.setx(0)
ball.sety(0)
ball.dx = 0.5
ball.dy = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Selects player on either team in specified direction
def playerIncrement(player, direction):
    global ai, bi
    player += direction
    if player < 0: player = 2
    elif player > 2: player = 0
    return player

# Generic turtle movement speed
turtleSpeed = 1
# Score counters
scoreA, scoreB = 0, 0

allTurtles = A + B
allTurtles.append(ball)

# Main game loop
while scoreA < 3 and scoreB < 3:
    # if len(keyList) > 0: print(keyList)
    # print(ai, bi)
    field.update()

    # Move player A, diagonal is possible
    if 'w' in keyList: A[ai].sety( A[ai].ycor() + turtleSpeed )
    if 'a' in keyList: A[ai].setx( A[ai].xcor() - turtleSpeed )
    if 's' in keyList: A[ai].sety( A[ai].ycor() - turtleSpeed )
    if 'd' in keyList: A[ai].setx( A[ai].xcor() + turtleSpeed )

    # Move player B, diagonal is possible
    if 'i' in keyList: B[bi].sety( B[bi].ycor() + turtleSpeed )
    if 'j' in keyList: B[bi].setx( B[bi].xcor() - turtleSpeed )
    if 'k' in keyList: B[bi].sety( B[bi].ycor() - turtleSpeed )
    if 'l' in keyList: B[bi].setx( B[bi].xcor() + turtleSpeed )

    # Goal score condition
    if abs(ball.xcor()) > (X - 25) and abs(ball.ycor()) < 150:
        if ball.xcor() > 0: scoreA += 1
        else: scoreB += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bording checking
    #for objects in allTurtles:
