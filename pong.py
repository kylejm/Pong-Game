# Kyle Massie Pong Game Using Turtle
import turtle

#Window Setup
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_l = 0
score_r = 0

#Identities 

#Paddle A
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.color("white")
paddle_l.penup()
paddle_l.goto(-350, 0)

#Paddle B
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.color("white")
paddle_r.penup()
paddle_r.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.75
ball.dy = 0.75


# Functions
def paddle_l_up():
    y = paddle_l.ycor()
    y += 30
    paddle_l.sety(y)
def paddle_l_down():
    y = paddle_l.ycor()
    y -= 30
    paddle_l.sety(y)
def paddle_r_up():
    y = paddle_r.ycor()
    y += 30
    paddle_r.sety(y)
def paddle_r_down():
    y = paddle_r.ycor()
    y -= 30
    paddle_r.sety(y)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

# Key Binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")


# Main Game Loop
while True:
    wn.update()

    # Move the ball
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
        ball.goto(0,0)
        ball.dx *= -1
        score_l += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_l, score_r), align="center", font=("Courier",24,"normal"))


    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_r += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_l, score_r), align="center", font=("Courier",24,"normal"))

    # Paddle and ball collisons 
    if ball.xcor() < -340 and ball.ycor() < paddle_l.ycor() + 50 and ball.ycor() > paddle_l.ycor() - 50:
        ball.dx *= -1 
       
    elif ball.xcor() > 340 and ball.ycor() < paddle_r.ycor() + 50 and ball.ycor() > paddle_r.ycor() - 50:
        ball.dx *= -1
      
    