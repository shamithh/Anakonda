import turtle
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
#screen setup
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Anakonda")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

#movement setup
screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#food appearence
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#wall collision
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
#tail collision
    for fragment in snake.fragments:
        if fragment == snake.head:
            pass
        elif snake.head.distance(fragment) < 10:
            scoreboard.reset()
            snake.reset()

























screen.exitonclick()