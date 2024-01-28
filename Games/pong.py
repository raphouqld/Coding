import turtle as t

p1_score=0
p2_score=0

#screen
wind=t.Screen()
wind.title("Pong Game by raphou.qld")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)

#left paddle
left=t.Turtle()
left.penup()
left.shape("square")
left.color("white")
left.shapesize(stretch_len=1, stretch_wid=5)
left.goto(-300,0)

#right paddle
right=left.clone()
right.penup()
right.goto(300,0)

#ball
ball=t.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0,0)
ballxdir=1.5
ballydir=1

#pen for score
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("P1 : {}     P2 : {}".format(p1_score,p2_score), align="center", font=("Courier",24,"normal"))

#functions to move
def leftup() :
    y=left.ycor()
    y+=60
    left.sety(y)

def leftdown() :
    y=left.ycor()
    y-=60
    left.sety(y)

def rightup() :
    y=right.ycor()
    y+=60
    right.sety(y)

def rightdown() :
    y=right.ycor()
    y-=60
    right.sety(y)

#assign keys
wind.listen()
wind.onkeypress(leftup,"z" or "Z")
wind.onkeypress(leftdown,"s" or "S")
wind.onkeypress(rightup,"Up")
wind.onkeypress(rightdown,"Down")

while True :
    wind.update()
    
    #moving ball
    ball.setx(ball.xcor()+ballxdir)
    ball.sety(ball.ycor()+ballydir)
    
    #up border
    if ball.ycor() > 290 :
        ball.sety(290)
        ballydir = ballydir*-1
    
    #down border
    if ball.ycor() < -290 :
        ball.sety(-290)
        ballydir = ballydir*-1
    
    #right border
    if ball.xcor() > 390 :
        ballxdir=1
        ballydir=0.5
        ballxdir = ballxdir*-1
        ball.goto(0,0)
        p1_score += 1
        pen.clear()
        pen.write("P1 : {}     P2 : {}".format(p1_score,p2_score), align="center", font=("Courier",24,"normal"))
    
    #left border
    if ball.xcor() < -390 :
        ballxdir=-1
        ballydir=0.5
        ballxdir = ballxdir*-1
        ball.goto(0,0)
        p2_score += 1
        pen.clear()
        pen.write("P1 : {}     P2 : {}".format(p1_score,p2_score), align="center", font=("Courier",24,"normal"))
    
    #collisions with the paddles :
    #right
    if (ball.xcor() > 290) and (ball.xcor() < 310) and (ball.ycor() > right.ycor() - 50) and  (ball.ycor() < right.ycor() + 50) :
        ballxdir = ballxdir * -1
        #add speed
        ballxdir *= 1.05
        ballydir *= 1.05
        
    #left
    if (ball.xcor() < -290 ) and (ball.xcor() > -310) and (ball.ycor() > left.ycor() - 50) and  (ball.ycor() < left.ycor() + 50) :
        ballxdir = ballxdir * -1
        #add speed
        ballxdir *= 1.05
        ballydir *= 1.05