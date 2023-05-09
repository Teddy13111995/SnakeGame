from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision between snake and food
    if snake.turtles[0].distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -280 or snake.turtles[0].ycor() > 280 or \
            snake.turtles[0].ycor() < -280:
        scoreboard.reset_game()
        snake.reset()
    # detect collision of head with tail
    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            scoreboard.reset_game()
            snake.reset()
my_screen.exitonclick()
