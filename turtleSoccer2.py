# TURTLE SOCCER
# ME 369P Final
# Mission ImpROSible

import turtle
from pynput import keyboard

# This list will hold all currently-pressed keyboard inputs
keyList = list()
error = 'This game accepts alphanumerical keys, namely qweasd and uiojkl.'
# Initialize player select indices
# global ai, bi
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
            if key.char == 'q': ai = playerIncrement(ai, -1)
            if key.char == 'e': ai = playerIncrement(ai, 1)
            if key.char == 'u': bi = playerIncrement(bi, -1)
            if key.char == 'o': bi = playerIncrement(bi, 1)
    except AttributeError:
        print(error)

# Blocking keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

oldKeyList = keyList

# Non-blocking keyboard listener
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()



turtle.clearscreen()
field = turtle.Screen()
field.bgpic("field.gif")
field.tracer(0)

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
        A[index].goto(-200, 0)
    else:
        A[index].goto(-300, (-200 + index*200))

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
        B[index].goto(200, 0)
    else:
        B[index].goto(300, (-200 + index*200))

# Ball
ball = turtle.Turtle()
ball.speed(0)
image = "ball.gif"
field.addshape(image)
ball.shape(image)
ball.penup()
ball.setx(0)
ball.sety(0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def playerIncrement(player, direction):
    global ai, bi
    player += direction
    if player < 0: player = 2
    elif player > 2: player = 0
    return player


# Generic turtle movement speed
turtleSpeed = 1
# Score counters
scoreA = scoreB = 0

# Main game loop
while scoreA < 3 and scoreB < 3:
    # if len(keyList) > 0: print(keyList)
    print(ai, bi)
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
    
    # if 'q' in oldKeyList:
    #     if 'q' not in keyList:
    #         print('yeet!')
    # if key == 'q': ai = playerIncrement(ai, -1)
    # if key == 'e': ai = playerIncrement(ai, 1)
    # if key == 'u': bi = playerIncrement(bi, -1)
    # if key == 'o': bi = playerIncrement(bi, 1)

    oldKeyList = keyList
    # Change player selection
    # if 'q' in keyList: ai -= 1
    # if 'e' in keyList: ai += 1
    # if 'u' in keyList: bi -= 1
    # if 'o' in keyList: bi += 1
    # if 'q' in oldKeyList and 'q' not in keyList:
    #     if ai > 0: ai -= 1
    #     else: ai = 2 
    # if key == 'e':
    #     if ai < 2: ai += 1
    #     else: ai = 0
    # if key == 'u':
    #     if bi > 0: bi -= 1
    #     else: bi = 2 
    # if key == 'o':
    #     if bi < 2: bi += 1
    #     else: bi = 0
    # if ai < 0: ai = 0
    # elif ai > 2: ai = 2
    # if bi < 0: bi = 0
    # elif bi > 2: bi = 2


# Movement Functions



    
#     # Move the ball
#     ball.setx(ball.xcor() + ball.dx)
#     ball.sety(ball.ycor() + ball.dy)


#     # Border checking

#     # Top and bottom
#     if turtle.ycor() > 290:
#         turtle.sety(290)
#         turtle.dy *= -1
#         os.system("afplay bounce.wav&")
    
#     elif turtle.ycor() < -290:
#         turtle.sety(-290)
#         turtle.dy *= -1
#         os.system("afplay bounce.wav&")

#     # Left and right
#     if turtle.xcor() > 350:
#         score_a += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#         turtle.goto(0, 0)
#         turtle.dx *= -1

#     elif turtle.xcor() < -350:
#         score_b += 1
#         pen.clear()
#         pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
#         turtle.goto(0, 0)
#         turtle.dx *= -1

#     # Paddle and ball collisions
#     if turtle.xcor() < -340 and turtle.ycor() < A[1].ycor() + 50 and turtle.ycor() > A[1].ycor() - 50:
#         turtle.dx *= -1 
#         os.system("afplay bounce.wav&")
    
#     elif turtle.xcor() > 340 and turtle.ycor() < B1.ycor() + 50 and turtle.ycor() > B1.ycor() - 50:
#         turtle.dx *= -1
#         os.system("afplay bounce.wav&")
