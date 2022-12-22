from turtle import Turtle
starting_postion = [(0,0),(-20,0),(-40,0)]
move_distance = 20 

up = 90
down = 270
left = 180
right = 0



class Snake:
    def __init__(self):
        self.segment = []
        self.creat_snake()
        self.head = self.segment[0]
    def creat_snake(self):
        for postion in starting_postion:
           self.add_segment(postion)
    def add_segment(self,postion):
            timy_the_turtle = Turtle("square")
            timy_the_turtle.speed("fastest")
            timy_the_turtle.penup()
   
            timy_the_turtle.goto(postion)
    
    
            timy_the_turtle.color("blue")
            self.segment.append(timy_the_turtle)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg_num in range(len(self.segment)-1 ,0,-1):
            new_x = self.segment[seg_num-1].xcor()
            new_y = self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(new_x,new_y)
        self.segment[0].forward(move_distance)  
    def up(self):
        if self.head.heading()!= down:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!= up:
            self.head.setheading(down)   
    def left(self):
        if self.head.heading()!= right:
           self.head.setheading(left) 
    def right(self):
        if self.head.heading()!= left:
            self.head.setheading(right)     