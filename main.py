from turtle import Screen, Turtle
from paddle import Paddle

scr = Screen()
scr.bgcolor("black")
scr.setup(width=800, height=600)
scr.title("Pong")
scr.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

scr.listen()
scr.onkeypress(r_paddle.go_up, "Up")
scr.onkeypress(r_paddle.go_down, "Down")

scr.onkeypress(l_paddle.go_up, "w")
scr.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    scr.update()


scr.exitonclick()