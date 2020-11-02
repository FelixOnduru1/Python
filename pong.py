# Imports the library needed
import turtle 
import winsound
# Describes the specifications of the background(Title, color, and screen size)
# wn.tracer prevents it from updating. 
wn = turtle.Screen()
wn.title("Pong by TheOnduru")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
winsound.PlaySound("start.wav", winsound.SND_ASYNC)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")  
paddle_a.shapesize(stretch_wid = 5, stretch_len =1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")  
paddle_b.shapesize(stretch_wid = 5, stretch_len =1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")  
ball.penup()
ball.goto(0,0)

# Movement of paddles and making the controls happen through the keyboard
# Paddle A up and down movement
def paddle_a_up ():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
def paddle_a_down ():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#Paddle B up and down movement    
def paddle_b_up ():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
def paddle_b_down ():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Ball Movement
ball.dx = 0.2
ball.dy = 0.2

#Scoring
scoring_a = 0
scoring_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
# Creates the game loop and wn.update makes sure that everytime the loop runs it updates the string
while True:
    wn.update()
    #Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Scoring
    if ball.xcor()> 390:
        ball.goto(0,0)
        ball.dx *= -1 
        scoring_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoring_a, scoring_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
    if ball.xcor()< -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoring_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoring_a, scoring_b), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("score.wav", winsound.SND_ASYNC)
    #Bouncing on borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor()<paddle_b.ycor() + 40) and (ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *=(-1)
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor()<paddle_a.ycor() + 40) and (ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=(-1)
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
            


