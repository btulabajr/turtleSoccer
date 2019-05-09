# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
from pynput import keyboard
import math

# This list will hold all currently-pressed keyboard inputs
keyList = list()
error = 'This game accepts alphanumerical keys, namely qweasd and uiojkl.'

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
# Radius of ball and players
R = 25

# Team A
A = []
for index in range(3):
    A.append(turtle.Turtle())
    A[index].speed(0)
    playerA = "red.gif"
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
    playerB = "blue.gif"
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
# Motor vector speed variables
ball.dx, ball.dy = 0, 0
ball.speed = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Initialize player select indices
ai, bi = 1, 1

# Selects player on either team in specified direction
def playerIncrement(player, direction):
    global ai, bi
    player += direction
    if player < 0: player = 2
    elif player > 2: player = 0
    return player

# Generic turtle movement speed
turtleSpeed = 1
# Score indexs
scoreA, scoreB = 0, 0

allTurtles = A + B
allTurtles.append(ball)

collisionIndex = 0

# Main game loop
while scoreA < 5 and scoreB < 5:
    # Make sure all objects update every cycle
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

    # Reset ball to middle if spacebar is hit (Foos!)
    if 'g' in keyList:
        for index in range(3):
            if index == 1:
                A[index].goto(-X*0.3, 0)
                B[index].goto(X*0.3, 0)
            else:
                A[index].goto(-X*0.5, (-Y*0.5 + index*Y*0.5))
                B[index].goto(X*0.5, (-Y*0.5 + index*Y*0.5))
        ball.goto(0, 0)
        ball.speed = 0

    # Get ball position before entering this enormous for loop
    xBall = ball.xcor()
    yBall = ball.ycor()

    # Border checking
    for index in range(7):
        # Get position of current turtle
        yPos = allTurtles[index].ycor()
        xPos = allTurtles[index].xcor()
        
        # Keep players and ball between sidelines
        if abs(yPos) > Y-R:
            # First six objects are turtle players
            if index < 6:
                if yPos > 0: ySet = Y-R
                else: ySet = -(Y-R)
                allTurtles[index].sety(ySet)
            # Last one is the ball
            else: ball.dy *= -1
        
        # Keep players and ball between sidelines, also monitor goals
        if abs(xPos) > X-R:
            # Look at players
            if index < 6:
                if xPos > 0: xSet = X-R
                else: xSet = -(X-R)
                allTurtles[index].setx(xSet)
            # Look at ball
            else:
                # If goal is scored
                if abs(yPos) < 150:
                    if yPos < 0: scoreA += 1
                    else: scoreB += 1
                    ball.goto(0, 0)
                    ball.speed = 0
                    pen.clear()
                    # Update score
                    pen.write("Player A: {}  Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
                    ai, bi = 1, 1
                    for index in range(3):
                        if index == 1:
                            A[index].goto(-X*0.3, 0)
                            B[index].goto(X*0.3, 0)
                        else:
                            A[index].goto(-X*0.5, (-Y*0.5 + index*Y*0.5))
                            B[index].goto(X*0.5, (-Y*0.5 + index*Y*0.5))
                else: ball.dx *= -1

        # These variables are the scale of the goal box on the field graphic
        xMult = 0.63
        yMult = 0.59
        offset = 10
        # Just look at players for the following functions
        if index < 6:
            # Keep players outside of goal box
            if abs(xPos) > X*xMult and abs(yPos) < Y*yMult:
                # If within back end of goal box, move to side
                if abs(xPos) > X*xMult + offset:
                    if yPos > 0: ySet = Y*yMult
                    else: ySet = -(Y*yMult)
                else: ySet = yPos
                # If within middle section of goal box, move to front
                if abs(yPos) < Y*yMult - offset:
                    if xPos > 0: xSet = X*xMult
                    else: xSet = -(X*xMult)
                else: xSet = xPos
                allTurtles[index].goto(xSet, ySet)

            # Handle collisions between players and ball
            if allTurtles[index].distance(ball) < 2*R:
                # Give ball max speed
                ball.speed = 2
                # Reset collision index for ball slowdown
                collisionIndex = 0
                xPlayer = allTurtles[index].xcor()
                yPlayer = allTurtles[index].ycor()
                # Get x and y distance between player and ball
                xDiff = xBall - xPlayer
                yDiff = yBall - yPlayer
                # Get angle between player and ball in radians
                contactAngle = math.atan2(yDiff, xDiff)
                # Set ball speed based off this contact angle
                ball.dx = ball.speed*math.sin(contactAngle)
                ball.dy = ball.speed*math.cos(contactAngle)
            else:
                # Implement slow down if no collision
                previousAngle = math.atan2(ball.dy, ball.dx)
                ball.dx = ball.speed*math.sin(previousAngle)
                ball.dy = ball.speed*math.cos(previousAngle)

    # Update collision
    collisionIndex += 1
    # Start to slow down 
    if collisionIndex > 100 and ball.speed > 0.4:
        ball.speed -= 0.005

    # Move the ball (eventually implement slowdown too)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
