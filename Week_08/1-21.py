from turtle import *
from random import *
def question_01():
    total = 0
    for i in range (int(input()), int(input()) + 1):
            total += i
    print(total)
#question_01()

def question_02():
    pensize(10)
    for i in range(0,3):
        pendown()
        if i == 0:
            pencolor("Red")
        elif i == 1:
            pencolor("Green")
        else:
            pencolor("Blue")
        circle(100)
        penup()
        forward(150)
    done()
#question_02()

def question_03():
    pensize(10)
    penup()
    goto(-200,0)
    pendown()
    for i in range(0,2):
        if i == 0:
            pencolor("Blue")
        if i == 1:
            pencolor("Black")
        pendown()
        circle(100)
        right(90)
        if i == 0:
            pencolor("Yellow")
        if i == 1:
            pencolor("Green")
        circle(100)
        left(90)
        penup()
        forward(200)
    pendown()
    pencolor("Red")
    circle(100)
    done()
#question_03()

def question_04():
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
#question_04()

def question_05():
    penup()
    goto(-200,100)
    pendown()
    for k in range(0,2):
        for j in range(0,4):
            right(45)
            for i in range(0,4):
                pendown()
                forward(40)
                left(90)
            left(45)
            penup()
            forward(100)
        goto(-200,0)
#question_05()

def question_06():
    for j in range(0,4):
        penup()
        goto(randrange(-300,300),randrange(-300,300))
        right(45)
        square = randrange(50,250)
        for i in range(0,4):
            pendown()
            forward(square)
            left(90)
        penup()
        left(45)
#question_06()

def question_07():
    for i in range(0,int(input())+ 1):
        for j in range(1,i+1):
            print(j,end="|")
        print()
#question_07()

def question_08():
    for i in range(int(input()),0,-1):
        for j in range(1,i+1):
            print(j,end="|")
        print()
#question_08()

def question_09():
    a = int(input())
    b = a
    for i in range (1,a + 1):
        print(" " * ( b  *2),end="")
        b -= 1
        for j in range (1,i+1):
            print(j,end="|")
        print()
#question_09()

def question_10():
    a = int(input())
    b = a - 1
    for i in range (a,0,-1):
        print(" " * ((a - b) * 2),end="")
        b -= 1
        for j in range(1, i + 1):
            print(j,end="|")
        print()
#question_10()

def question_11():
    print([x for x in range(1,151,2)])
#question_11()

def question_12():
    print([x for x in range(200,451,2)])
#question_12()

def question_13():
    for i in range(1,13):
      print(i * 31)
#question_13()

def question_14():
    for i in range(1,13):
      print(i * 7)
#question_14()

#def question_15():
############################
############################

def question_16():
    total = 0
    for i in range(0, 10):
        total =+ float(input())
    print(total/10)
#question_16()

def question_17():
    data = input()
    for i in range(0,len(data)-1):
        print(data[i],end=",")
    print(data[len(data)-1])
#question_17()

def question_18():
    number = []
    for i in range(0,5):
        number.append(float(input()))
    print(min(number))
    print(max(number))
#question_18()

def question_19():
    data = int(input())
    for i in range(2,data):
        if data % i == 0:
            print("ไม่ใช่จำนวนเฉพาะ")
            break
    else:
        print("จำนวนเฉพาะ")
#question_19()

def question_20():
    number = []
    remainder = []
    for i in range(0,4):
        number.append(int(input()))
    for i in range(1,max(number)):
        if int(number[0]) % i == 0 and int(number[1]) % i == 0 and  int(number[2]) % i == 0 and int(number[3]) % i == 0:
            remainder.append(i)
    print(max(remainder))
#question_20()

def question_21():
    number = []
    for i in range(0,4):
        number.append(int(input()))
    total = number[0] * number[1] * number[2] * number[3]
    for i in range(1,total):
        if total % i == 0 and i % number[0] == 0 and i % number[1] == 0 and i % number[2] == 0 and i % number[3] == 0:
            print(i)
            break
#question_21()
