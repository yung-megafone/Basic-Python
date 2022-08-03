# Simple Pong in Python 3
import turtle
import os

wn = turtle.Screen()
wn.title("Pong by yung_megafone")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
l_score = 0
r_score = 0

# Left Paddle
l_paddle = turtle.Turtle()
l_paddle.speed(0)
l_paddle.shape("square")
l_paddle.color("white")
l_paddle.shapesize(stretch_wid=5, stretch_len=1)
l_paddle.penup()
l_paddle.goto(-350, 0)

# Right Paddle
r_paddle = turtle.Turtle()
r_paddle.speed(0)
r_paddle.shape("square")
r_paddle.color("white")
r_paddle.shapesize(stretch_wid=5, stretch_len=1)
r_paddle.penup()
r_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.025
ball.dy = 0.025

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 | Player B: 0", align="center", font=("Courier", 24, "normal"))

### Functions ###
# Left Paddle Up
def l_paddle_up():
    y = l_paddle.ycor()
    y += 20
    l_paddle.sety(y)

# Left Paddle Down
def l_paddle_down():
    y = l_paddle.ycor()
    y -= 20
    l_paddle.sety(y)

# Right Paddle Up
def r_paddle_up():
    y = r_paddle.ycor()
    y += 20
    r_paddle.sety(y)

# Right Paddle Down
def r_paddle_down():
    y = r_paddle.ycor()
    y -= 20
    r_paddle.sety(y)

# Keybinds
wn.listen()
wn.onkeypress(l_paddle_up, "w")
wn.onkeypress(l_paddle_down, "s")
wn.onkeypress(r_paddle_up, "Up")
wn.onkeypress(r_paddle_down, "Down")


# Main loop
while True:
    wn.update() # Update the display

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for tje top / bottom borders and reflect
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("mpg123 bounce.wav&")


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("mpg123 bounce.wav&")

    # Chack for the left / right borders and reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        l_score += 1
        ball.dx *= -1
        os.system("mpg123 bonce.wav&")
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(l_score, r_score), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        r_score += 1
        ball.dx *= -1
        os.system("mpg123 bonce.wav&")
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(l_score, r_score), align="center", font=("Courier", 24, "normal"))

    
    # Paddle Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() - 40)):
        ball.setx(340)
        ball.dx *= -1
        os.system("mpg123 bounce.wav&")


    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() - 40)):
        ball.setx(-340)
        ball.dx *= -1
        os.system("mpg123 bounce.wav&")