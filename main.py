from turtle import Screen, Turtle, textinput, tilt, xcor
from score import Scoreboard
from snake import Snake
from food import Food
from score import Scoreboard
import time
screen = Screen()
timy_the_turtle = Turtle()

screen.setup(width=600,height=500)
level = textinput("choose your level","enter which level you like easy,medium & hard").lower()
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
screen.update()    
game_is_on = True
while game_is_on:
    screen.update()
    if level == "easy":
        time.sleep(0.4)
    elif level == "medium":
        time.sleep(0.2)
    else:
        time.sleep(0.1)        
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or  snake.head.ycor()<-280:
        game_is_on = False     
        scoreboard.game_over()
    for segment in snake.segment:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()
       
screen.exitonclick()
