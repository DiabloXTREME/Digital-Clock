import datetime as dt
import time
import turtle
import random

# Screen
screen = turtle.Screen()
screen.clear()
screen.bgcolor("black")
screen.screensize(800, 800)
screen.colormode(255)

# Circle Turtle
circle = turtle.Turtle()
circle.speed(0)
circle.pensize(10)
circle.pencolor("white")
circle.penup()
circle.goto(0, -350)
circle.pendown()
circle.circle(350)
circle.hideturtle()

# Time turtle

minTurtle = turtle.Turtle()
secTurtle = turtle.Turtle()
hourTurtle = turtle.Turtle()

minTurtle.pensize(10)
secTurtle.pensize(10)
hourTurtle.pensize(10)

minTurtle.hideturtle()
secTurtle.hideturtle()
hourTurtle.hideturtle()

minTurtle.speed(0)
secTurtle.speed(0)
hourTurtle.speed(0)

minTurtle.color("orange")
secTurtle.color("red")
hourTurtle.color("yellow")

# Ticks Turtle
ticks = turtle.Turtle()
ticks.penup()
ticks.pensize(17)
tick_angle = 0
ticks.speed(0)
ticks.hideturtle()
# Ticks
for i in range(12):
    ticks.color(random.randint(0, 100), random.randint(100, 200), random.randint(0, 255))
    ticks.penup()
    ticks.goto(0, 0)
    ticks.setheading(0 + tick_angle)
    ticks.forward(301)
    ticks.pendown()
    ticks.forward(43)
    tick_angle += 30

# Test Turtle
# tester = turtle.Turtle()
# tester.hideturtle()
# tester.pensize(10)
# tester.color("blue")
# tester.goto(0,0)
# tester.forward(1000)
# tester.goto(0,0)
# tester.setheading(90)
# tester.color("green")
# tester.forward(1000)
# tester.goto(0,0)
# tester.setheading(-90)
# tester.color("pink")
# tester.forward(1000)
# tester.goto(0,0)

# Previous Times
previousHour = -1
previousMinute = -1
while True:

    # Mini Circle
    circle.pensize(50)
    circle.pencolor((random.randint(0, 150), random.randint(10, 150), random.randint(100, 255)))
    circle.penup()
    circle.goto(0, 0)
    circle.pendown()
    circle.circle(1)

    # Time
    minutes = int(dt.datetime.now().minute)
    seconds = int(dt.datetime.now().second)
    hours = int(dt.datetime.now().strftime("%I"))

    # Angles
    secondsAngle = 90 - seconds * 6
    minutesAngle = 90 - minutes * 6
    hoursAngle = 90 - hours * 30

    # Hands
    if previousMinute != minutes or minutesAngle == secondsAngle or minutesAngle == hoursAngle:
        minTurtle.penup()
        minTurtle.goto(0, 0)
        minTurtle.setheading(minutesAngle)
        minTurtle.pendown()
        minTurtle.forward(250)

    secTurtle.penup()
    secTurtle.goto(0, 0)
    secTurtle.setheading(secondsAngle)
    secTurtle.pendown()
    secTurtle.forward(275)
    if previousHour != hours or hoursAngle == minutesAngle or hoursAngle == secondsAngle:
        hourTurtle.penup()
        hourTurtle.goto(0, 0)
        hourTurtle.setheading(hoursAngle)
        hourTurtle.pendown()
        hourTurtle.forward(200)

    # Clear and Pause
    time.sleep(1)
    if previousHour != hours:
        hourTurtle.clear()
        previousHour = hours
    if previousMinute != minutes:
        minTurtle.clear()
        previousMinute = minutes
    secTurtle.clear()

    # Circle Redraw
    circle.pensize(10)
    circle.pencolor((random.randint(0, 150), random.randint(10, 150), random.randint(100, 255)))
    circle.penup()
    circle.goto(0, -350)
    circle.pendown()
    circle.circle(350)
