import turtle
from keyboardInputs.py import *

screen = turtle.Screen()

image = "soccerBall.gif"

screen.addshape(image)
turtle.shape(image)

screen.bgcolor("lightblue")

moveSpeed = 10

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Key Inputs: ', keyList, align="center", font=("Courier", 24, "normal"))

# these defs control the movement of our "turtle"
def forward():
  turtle.sety(turtle.ycor()+moveSpeed)

def backward():
  turtle.sety(turtle.ycor()-moveSpeed)

def right():
  turtle.setx(turtle.xcor()+moveSpeed)

def left():
  turtle.setx(turtle.xcor()-moveSpeed)

turtle.penup()
turtle.speed(0)
turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")

screen.listen()

turtle.mainloop()
print(keyList)

pen.clear()
pen.write('Key Inputs: ', keyList, align="center", font=("Courier", 24, "normal"))