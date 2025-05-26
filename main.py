import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

scr.listen()
scr.onkeypress(r_paddle.go_up, "Up")
scr.onkeypress(r_paddle.go_down, "Down")

scr.onkeypress(l_paddle.go_up, "w")
scr.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    ball.move()
    if ball.detect_wall_collision():
        ball.y *= -1

    if (
            (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(l_paddle) and ball.xcor() < -320)
    ): ball.x *= -1

    if ball.xcor() > 380:
        score.update_scoreboard()
        ball.reset_position()


    if ball.xcor() < -380:
        score.update_scoreboard()
        ball.reset_position()



scr.exitonclick()



