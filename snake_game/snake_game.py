from snake import Snake
from turtle import Turtle, Screen
from snake_food import Food
from snake_scoreboard import ScoreBoard
import time
# Todo_1: screen setup and creating the snake body
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food =Food()
score = ScoreBoard()
# Controlling the snake with a key press
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



# Animating the snake segment on the screen

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
  
    # Detecting collision of head segment with food(distance between two instances)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    
  
    # Detecting collision. with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or  snake.head.ycor() >280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_over()


    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
















screen.exitonclick()