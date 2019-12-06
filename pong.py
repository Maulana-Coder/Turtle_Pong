#############################################
# Simple A Pong Game                        #
# Python3                                   #
# Tested On Windows 10                      #
# Github : https://github.com/Maulana-Coder #
#############################################

import turtle

# Screen
wn = turtle.Screen()
wn.title("Pong - Maulana ID")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-400, -350)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
    border_pen.fd(800)
    border_pen.lt(90)
border_pen.hideturtle()

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
# Ball Speed
ball.dx = 1.5
ball.dy = -1.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 vs Player B: 0", align="center", font=("Courier", 20, "normal"))

# Function
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

def about():
    turtle.color("lime")
    turtle.speed(0)
    turtle.penup()
    turtle.write("Game Created \n     By \n Maulana ID",align="center", font=("Consolas", 20, "bold",))
    turtle.penup()
    turtle.hideturtle()
about()



# Keyboard Binding
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

#Game Main
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} vs Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} vs Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1





    

    






















    
