from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("dark.png")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

# listen for key events
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

playing = True
while playing:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food (using the turtle method: distance)
    if snake.head.distance(food) < 15:
        # reset food to new random location
        food.set_food()
        # add segment to snake
        snake.extend()
        # increase score
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        # stop game & write game over + show final score
        playing = False
        score.game_over()

    # Detect collision with tail
    # Q. How can we know if it collides with the tail?
    # A. If the head touches any segment that isn't the head segment
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            playing = False
            score.game_over()

screen.exitonclick()
