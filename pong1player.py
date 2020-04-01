'''
Pong game, only one player
'''
import turtle

running = True
lost_games = 0
hit_counter = 0

# Create the screen
win = turtle.Screen()
win.title('Pong by @Josep')
win.bgcolor('blue')
win.setup(width=800, height=600)
win.tracer(0)
win.delay(2)

# Create paddle
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-360, 0)

# Create ball
ball = turtle.Turtle()
ball.shape('circle')
ball.speed(0)
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = 0.09

# write the score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Games Lost: {}  hits: {}  dx: {:.2f}  dy: {:.2f}'.
        format(lost_games, hit_counter, ball.dx, ball.dy),
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


def exit_game():
    global running
    running = False


# listen for events
win.onkeypress(paddle_a_up,'Up')
win.onkeypress(paddle_a_down,'Down')
win.onkeypress(exit_game,'q')
win.listen()

# main loop
while running:
    # This is to avoid an exception when the user closes the window.
    try:
        # movement of the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # change direction when hitting up o down limits
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        # change direction when hitting right limit
        if ball.xcor() > 390:
            ball.dx *= -1

        # when player fails, restart the ball at the center of the screen
        # initialize movement variables and counters
        if ball.xcor() < -390:
            ball.goto(0, 0)
            lost_games += 1
            ball.dx = 0.08
            ball.dy = 0.09
            hit_counter = 0
            pen.clear()
            # show the result at the top of the screen
            pen.write('Games Lost: {}  hits: {}  dx: {:.2f}  dy: {:.2f}'.
                    format(lost_games, hit_counter, ball.dx, ball.dy),
                    align='center', font=('arial', 20, 'normal'))

        # change direction when the ball hits the paddle and increase
        # counter, and speed every 5 hits
        if ball.xcor() < (paddle_a.xcor() + 10) and ball.ycor() < (paddle_a.ycor() + 50) and ball.ycor() > (paddle_a.ycor() - 50):
            ball.dx *= -1
            hit_counter += 1
            pen.clear()
            if hit_counter % 5 == 0:
                ball.dx += 0.02
                ball.dy += 0.02
            pen.write('Games Lost: {}  hits: {}  dx: {:.2f}  dy: {:.2f}'.
                    format(lost_games, hit_counter, ball.dx, ball.dy),
                    align='center', font=('arial', 20, 'normal'))

        win.update()
    except:
        break

