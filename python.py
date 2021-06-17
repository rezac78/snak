import turtle
import time
import random

delay=0.1
score=0
# map game
wn=turtle.Screen();
wn.title("reza python game")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

# head game
head=turtle.Turtle()
head.speed(0)
head.color("white")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction='stop'

# food game
food=turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

# pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player :" ,align="center",font=("Courier",24,"normal"))


# move join
segments=[]

# function
def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction!='up':
        head.direction='down'

def go_right():
    if head.direction!='left':
        head.direction='right'

def go_left():
    if head.direction!='right':
        head.direction='left'

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)

    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)

    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

# move game
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')


while True:
    wn.update()
    # game over
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        print("gameover")
        head.goto(0,0)
        head.direction='stop'

        # hide
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        score=0
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)


    # food eit  big
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

    # snak
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("black")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)
        score=score+1
        pen.clear()
        pen.write("player :{}".format(score) ,align="center",font=("Courier",24,"normal"))
    # join snak
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()
            score=0
            x=random.randint(-290,290)
            y=random.randint(-290,290)
            food.goto(x,y)


    time.sleep(delay)

wn.mainloop()