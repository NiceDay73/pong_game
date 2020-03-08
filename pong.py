'''
Pong game
'''
import turtle

win = turtle.Screen()
win.title('Pong by @Josep')
win.bgcolor('blue')
win.setup(width=800, height=600)
win.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(360, 0)

# ball
ball = turtle.Turtle()
ball.shape('square')
ball.speed(0)
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.08

# write the score
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: {}  Player B: {}'.format(score_a, score_b),
    align='center', font=('arial', 20, 'normal'))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y > 240:
        y = 240
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y < -240:
        y = -240
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y > 240:
        y = 240
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y < -240:
        y = -240
    paddle_b.sety(y)


# listen for events
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')
win.listen()

# main loop
running = True
while running:
    # This is to avoid an exception when the user closes the window.
    try:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            score_a += 1
            pen.clear()
            pen.write('Player A: {}  Player B: {}'.format(score_a, score_b),
                align='center', font=('arial', 20, 'normal'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            score_b += 1
            pen.clear()
            pen.write('Player A: {}  Player B: {}'.format(score_a, score_b),
                align='center', font=('arial', 20, 'normal'))

        if ball.xcor() > (paddle_b.xcor() - 10) and ball.ycor() < (paddle_b.ycor() + 50) and ball.ycor() > (paddle_b.ycor() - 50):
           ball.dx *= -1

        if ball.xcor() < (paddle_a.xcor() + 10) and ball.ycor() < (paddle_a.ycor() + 50) and ball.ycor() > (paddle_a.ycor() - 50):
            ball.dx *= -1

        win.update()
    except:
        break
