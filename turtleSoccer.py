# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
from pynput import keyboard
import math

# This list will hold all currently-pressed keyboard inputs
keyList = list()
# Error is commented out to make the .exe
# error = 'This game accepts alphanumerical keys, namely qweasd and uiojkl.'

# When keys are pressed
def on_press(key):
    try:
        # If the key is alphanumerical and not in the list already
        if key.char not in keyList:
            keyList.append(key.char)
    # Print error statement if not alphanumerical
    except AttributeError:
        # print(error)
        pass

# When keys are released
def on_release(key):
    # Need to define that ai and bi are global to operate in this function
    global ai, bi
    try:
        if key.char in keyList:
            keyList.remove(key.char)
            # Button change rather than continuous for player selection
            if key.char == 'q': ai = playerIncrement(ai, -1)
            if key.char == 'e': ai = playerIncrement(ai, 1)
            if key.char == 'u': bi = playerIncrement(bi, -1)
            if key.char == 'o': bi = playerIncrement(bi, 1)
    except AttributeError:
        # print(error)
        pass

# Blocking keyboard listener, create listener thread
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Field
turtle.clearscreen()
field = turtle.Screen()
field.bgpic("field.gif")
field.tracer(0)
# Graphic is 1200 x 800 pixels centered around 0,0
# Scale: 10 pixels = 1 meter
X, Y = 600, 400
# These variables represent the scale of the goal box
xMult = 0.63
yMult = 0.59
# Offset is a value greater than any turtle can reasonably travel in one turn
offset = 10
# Radius of ball and players
R = 25
# Initialize field display as correct size
field.setup(2*X + offset, 2*Y + offset)

# Team A (Netherlands)
A = []
# Create index to hold all players on team A
for index in range(3):
    A.append(turtle.Turtle())
    A[index].speed(0)
    playerA = "playerA.gif"
    field.addshape(playerA)
    A[index].shape(playerA)
    # Make sure players don't have tracking line
    A[index].penup()
    # Place players in starting formation
    if index == 1:
        A[index].goto(-X*0.3, 0)
    else:
        A[index].goto(-X*0.5, (-Y*0.5 + index*Y*0.5))

# Team B (France)
B = []
for index in range(3):
    B.append(turtle.Turtle())
    B[index].speed(0)
    playerB = "playerB.gif"
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
ball.goto(0,0)
# Motor vector speed variables
ball.dx, ball.dy = 0, 0
ball.speed = 0
ball.minSpeed, ball.maxSpeed = 0.5, 3

# Pen
# Used to keep track of score
font = ("Courier", 100, "bold")
pen = turtle.Turtle()
pen.shape("square")
# Initialize team A score
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(-X*0.5, Y*0.7)
pen.write("0", align = "center", font=font)
# Initialize team B score
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(X*0.5, Y*0.7)
pen.write("0", align = "center", font=font)

# Initialize player select indices
ai, bi = 1, 1

# Selects player on either team in specified direction
def playerIncrement(player, direction):
    # Need to define that ai and bi are global to operate in this function
    global ai, bi
    player += direction
    # Wrap around if outside index
    if player < 0: player = 2
    elif player > 2: player = 0
    # Return new value for ai or bi
    return player

# Generic turtle movement speed
turtleSpeed = 1
# Score counters
scoreA, scoreB = 0, 0
oldScoreTotal = 0
# Change this for longer games
maxScore = 3

# Make list with all turtle objects to reduce code length
allTurtles = A + B
allTurtles.append(ball)

# Initialize variable to monitor collisions for ball slowdown
collisionIndex = 0

# MAIN GAME LOOP
while scoreA < maxScore and scoreB < maxScore:
    
    # Make sure pesky player A2 is in position!
    if oldScoreTotal != scoreA + scoreB:
        A[2].goto(-X*0.5, Y*0.5)
    oldScoreTotal = scoreA + scoreB

    # Highlight selected turtle
    aX, aY = A[ai].xcor(), A[ai].ycor()
    bX, bY = B[bi].xcor(), B[bi].ycor()    

    # Make sure all objects update every cycle
    field.update()

    # Move player A
    if 'w' in keyList: A[ai].sety( A[ai].ycor() + turtleSpeed )
    if 'a' in keyList: A[ai].setx( A[ai].xcor() - turtleSpeed )
    if 's' in keyList: A[ai].sety( A[ai].ycor() - turtleSpeed )
    if 'd' in keyList: A[ai].setx( A[ai].xcor() + turtleSpeed )

    # Move player B
    if 'i' in keyList: B[bi].sety( B[bi].ycor() + turtleSpeed )
    if 'j' in keyList: B[bi].setx( B[bi].xcor() - turtleSpeed )
    if 'k' in keyList: B[bi].sety( B[bi].ycor() - turtleSpeed )
    if 'l' in keyList: B[bi].setx( B[bi].xcor() + turtleSpeed )

    # Reset ball to middle and players to original positions (Foos!)
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

    # Get ball position before entering the enormous for loop below
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
                    # Reset ball
                    ball.goto(0, 0)
                    ball.speed = 0

                    # Reset players
                    ai, bi = 1, 1
                    for index in range(3):
                        if index == 1:
                            A[index].goto(-X*0.3, 0)
                            B[index].goto(X*0.3, 0)
                        else:
                            A[index].goto(-X*0.5, (-Y*0.5 + index*Y*0.5))
                            B[index].goto(X*0.5, (-Y*0.5 + index*Y*0.5))

                    # Update score        
                    pen.clear()
                    if xPos > 0: scoreA += 1
                    else: scoreB += 1
                    # Write score for team A
                    pen.color("orange")
                    pen.penup()
                    pen.hideturtle()
                    pen.goto(-X*0.5, Y*0.7)
                    pen.write(scoreA, align = "center", font=font)
                    # Write score for team B
                    pen.color("blue")
                    pen.penup()
                    pen.hideturtle()
                    pen.goto(X*0.5, Y*0.7)
                    pen.write(scoreB, align = "center", font=font)

                # If no goal is scored, bounce off goal line    
                else: ball.dx *= -1

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
                # Go to specified position
                allTurtles[index].goto(xSet, ySet)

            # Handle collisions between players and ball
            if allTurtles[index].distance(ball) < 2*R:
                # Make sure ball wasn't hit previously
                if collisionIndex > offset:    
                    # Give ball max speed
                    ball.speed = ball.maxSpeed
                    # Reset collision index for ball slowdown
                    collisionIndex = 0
                    # Find player positions
                    xPlayer = allTurtles[index].xcor()
                    yPlayer = allTurtles[index].ycor()
                    # Get x and y distance between player and ball
                    xDiff = xBall - xPlayer
                    yDiff = yBall - yPlayer
                    # Get angle between player and ball in radians
                    contactAngle = math.atan2(yDiff, xDiff)
                    # Set ball speed based off this contact angle
                    ball.dx = ball.speed*math.cos(contactAngle)
                    ball.dy = ball.speed*math.sin(contactAngle)

            # Implement slowdown if no recent collision
            else:
                previousAngle = math.atan2(ball.dy, ball.dx)
                ball.dx = ball.speed*math.sin(previousAngle)
                ball.dy = ball.speed*math.cos(previousAngle)

    # Update collision index
    collisionIndex += 1
    # Start to slow down if no recent collision and above minimum speed
    if collisionIndex > offset and ball.speed > ball.minSpeed:
        ball.speed -= 0.01

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
