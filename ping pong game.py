#Screen Shape 
import turtle
win = turtle.Screen()
win.title("Ping Pong")
win.setup(width=600, height=600)
win.bgcolor("white")
win.tracer(0)

#1st madrab --> mdrb1
mdrb1 = turtle.Turtle()
mdrb1.color("blue")
mdrb1.penup()
mdrb1.speed(0)
mdrb1.shapesize(stretch_wid=5, stretch_len=1)
mdrb1.shape("square")
mdrb1.goto(-250, 0)

#2nd madrab --> mdrb2
mdrb2 = turtle.Turtle()
mdrb2.shape("square")
mdrb2.shapesize(stretch_wid=5, stretch_len=1)
mdrb2.color("red")
mdrb2.speed(0)
mdrb2.penup()
mdrb2.goto(250, 0)


# ball --> ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


# score variables
score1 = 0
score2 = 0


# Score display for Player 1
score_display1 = turtle.Turtle()
score_display1.speed(0)
score_display1.color("blue")
score_display1.penup()
score_display1.hideturtle()
score_display1.goto(-200, 260)
score_display1.write("Player 1: 0", align="center", font=("Arial", 18, "bold"))

# Score display for Player 2
score_display2 = turtle.Turtle()
score_display2.speed(0)
score_display2.color("red")
score_display2.penup()
score_display2.hideturtle()
score_display2.goto(200, 260)
score_display2.write("Player 2: 0", align="center", font=("Arial", 18, "bold"))


# movement elmadareb
def mdrb1_up():
    y = mdrb1.ycor()
    if y < 250:
        y += 20
        mdrb1.sety(y)


def mdrb1_down():
    y = mdrb1.ycor()
    if y > -250:
        y -= 20
        mdrb1.sety(y)


def mdrb2_up():
    y = mdrb2.ycor()
    if y < 250:
        y += 20
        mdrb2.sety(y)


def mdrb2_down():
    y = mdrb2.ycor()
    if y > -250:
        y -= 20
        mdrb2.sety(y)

win.listen()
win.onkeypress(mdrb1_up, 'w')
win.onkeypress(mdrb1_down, 's')
win.onkeypress(mdrb2_up, 'Up')
win.onkeypress(mdrb2_down, 'Down')

# main game function
while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 290:
        score2 -= 1
        ball.goto(0, 0)
        ball.setx(290)
        ball.dx *= -1
        score_display1.clear()
        score_display2.clear()
        score_display1.write(f"Player 1: {score1}", align="center", font=("Arial", 18, "bold"))
        score_display2.write(f"Player 2: {score2}", align="center", font=("Arial", 18, "bold"))

    if ball.xcor() < -290:
        score1 -= 1
        ball.goto(0, 0)
        ball.setx(-290)
        ball.dx *= -1
        score_display1.clear()
        score_display2.clear()
        score_display1.write(f"Player 1: {score1}", align="center", font=("Arial", 18, "bold"))
        score_display2.write(f"Player 2: {score2}", align="center", font=("Arial", 18, "bold"))

    if (240 <= ball.xcor() <= 250) and (mdrb2.ycor() - 55 < ball.ycor() < mdrb2.ycor() + 55) and ball.dx > 0:
        ball.setx(240)
        ball.dx *= -1.1
        ball.dy *= 1.1
        score2 += 1
        score_display1.clear()
        score_display2.clear()
        score_display1.write(f"Player 1: {score1}", align="center", font=("Arial", 18, "bold"))
        score_display2.write(f"Player 2: {score2}", align="center", font=("Arial", 18, "bold"))

    if (-250 <= ball.xcor() <= -240) and (mdrb1.ycor() - 55 < ball.ycor() < mdrb1.ycor() + 55) and ball.dx < 0:
        ball.setx(-240)
        ball.dx *= -1.1
        ball.dy *= 1.1
        score1 += 1
        score_display1.clear()
        score_display2.clear()
        score_display1.write(f"Player 1: {score1}", align="center", font=("Arial", 18, "bold"))
        score_display2.write(f"Player 2: {score2}", align="center", font=("Arial", 18, "bold"))

    if score1 >= 5 or score2 <= -5:
        ball.dx = 0
        ball.dy = 0
        winner_display = turtle.Turtle()
        winner_display.speed(0)
        winner_display.color("blue")
        winner_display.penup()
        winner_display.hideturtle()
        winner_display.goto(0, 0)
        winner_display.write("Congratulations Player 1 Wins!", align="center", font=("Arial", 20, "bold"))

    elif score2 >= 5 or score1 <= -5:
        ball.dx = 0
        ball.dy = 0
        winner_display = turtle.Turtle()
        winner_display.speed(0)
        winner_display.color("red")
        winner_display.penup()
        winner_display.hideturtle()
        winner_display.goto(0, 0)
        winner_display.write("Congratulations Player 2 Wins!", align="center", font=("Arial", 20, "bold"))
