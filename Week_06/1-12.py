from turtle import *
def triangle():
    pendown()
    pensize(5)
    forward(200)
    goto(50,150)
    goto(-100,0)
    goto(0,0)
    done()
#triangle()

def rectangle():
    forward(200)
    left(90)
    forward(100)
    left(90)
    forward(200)
    left(90)
    forward(100)
#rectangle()

def diamond():
    right(45)
    for i in range(0,4):
        forward(100)
        right(90)
#diamond()

def two_circle():
    circle(100)
    penup()
    forward(100)
    pendown()
    circle(100)
#two_circle()

def circle_but_user_input():
    penup()
    x1 = int(input())
    y1 = int(input())
    radius = int(input())
    goto(x1 , y1 )
    dot(10,"blue")
    goto(x1 , y1 - radius)
    pendown()
    circle(radius)
    done()
#circle_but_user_input()

def circle_but_fill():
    penup()
    color("black","blue")
    x1 = int(input())
    y1 = int(input())
    radius = int(input())
    goto(x1 , y1 )
    dot(10,"blue")
    goto(x1 , y1 - radius)
    begin_fill()
    pendown()
    circle(radius)
    end_fill()
    done()
#circle_but_fill()

def three_color():
    pencolor("red")
    circle(100)
    penup()
    forward(100)
    pendown()
    pencolor("blue")
    circle(100)
    penup()
    backward(50)
    right(90)
    forward(100)
    left(90)
    pencolor("yellow")
    pendown()
    circle(100)
    done()
#three_color()

def square_from_input():
    penup()
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    goto(x1,y1)
    pendown()
    forward(x2 - x1)
    left(90)
    forward(y2 - y1)
    left(90)
    forward(y2 - y1)
    left(90)
    forward(y2 - y1)
    left(90)
    goto(x1,y1)
    done()
#square_from_input()

def olympic():
    penup()
    goto(-300,0)
    pensize(10)
    ###########
    pencolor("blue")
    pendown()
    circle(100)
    penup()
    ###########
    pencolor("yellow")
    pendown()
    right(90)
    circle(100)
    penup()
    left(90)
    ###########
    forward(220)
    color("white")
    begin_fill()
    pencolor("black")
    pendown()
    circle(100)
    end_fill()
    penup()
    ###########
    forward(220)
    begin_fill()
    pencolor("Red")
    pendown()
    circle(100)
    penup()
    ###########
    left(90)
    pencolor("Green")
    pendown()
    circle(100)
    done()
#olympic()

def stop_sign():
    backward(50)
    right(90)
    pensize(10)
    pencolor("black")
    forward(150)
    penup()
    goto(0,0)
    left(90)
    begin_fill()
    color("Black","Red")
    pendown()
    pensize(5)
    for i in range(0,6):
        left(60)
        forward(100)
    end_fill()
    penup()
    backward(50)
    left(90)
    forward(60)
    right(90)
    color("white")
    write("STOP",True,align="center",font=("Arial",40,"normal"))
    done()
#stop_sign()


def star():
    speed(100)
    penup()
    goto(-200,0)
    left(60)
    color("black","white")
    begin_fill()
    pendown()
    forward(150)
    dot(10,"blue")
    right(120)
    forward(150)
    dot(10,"blue")
    left(-120)
    forward(150)
    dot(10,"blue")
    end_fill()
    penup()
    right(90)
    forward(90)

    begin_fill()
    pendown()
    right(90)
    dot(10,"blue")
    forward(150)
    dot(10,"blue")
    right(120)
    forward(150)
    dot(10,"blue")
    right(120)
    forward(150)
    dot(10,"blue")
    end_fill()

    right(120)
    forward(53)
    pencolor("white")
    forward(44)
    penup()
    forward(53)
    right(120)
    pensize(5)
    forward(56)
    pendown()
    forward(44)
    penup()
    forward(50)
    right(120)
    forward(50)
    pendown()
    forward(44)
    done()
#star()

def heart():
    penup()
    goto(-200,100)
    left(60)
    pendown()
    forward(50)
    dot(10,"blue")
    right(120)
    forward(50)
    dot(10,"blue")
    left(120)
    forward(50)
    dot(10,"blue")
    right(120)
    forward(50)
    dot(10,"blue")
    left(120)
    forward(50)
    dot(10,"blue")
    right(120)
    forward(50)
    dot(10,"blue")
    left(120)
    forward(50)
    dot(10,"blue")
    right(120)
    forward(50)
    dot(10,"blue")
    right(60)
    forward(100)
    dot(10,"blue")
    right(120)
    forward(100)
    left(120)
    forward(100)
    dot(10,"blue")
    right(120)
    forward(100)
    dot(10,"blue")
    done()
#heart()




