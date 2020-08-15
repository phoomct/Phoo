from math import *
def question_1():
    print("{:.2f}".format(pi * (eval(input()) ** 2)))
#question_1()

def question_2():
    if eval(input())  < 0:
        print("Number < 0")
#question_2()

def question_3():
    if eval(input()) > 5000:
        print("100")
    else:
        print("10")
#question_3()

def question_4():
    data = eval(input())
    if data >= 80:
        print("High")
    elif data < 80 and data >= 50:
        print("Medium")
    else:
        print("Low")
#question_4()

def question_5():
    data = input()
    if data == "a":
        print("Grade A")
    elif data == "b":
        print("Grade B")
    elif data == "c":
        print("Grade C")
    elif data == "d":
        print("Grade D")
    else:
        print("Grade F")
question_5()

def question_6():
    data = input("รายชื่อเหล่าน้ สิ่งใดเป็นชื่อของสัตว์ 1) เก้าอี้ 2)เเมว 3)รถถัง 4)กางเกง\n")
    if data == "2":
        print("true")
    else:
        print("false")
#question_6()

def question_7():
    data1 = eval(input())
    data2 = eval(input())
    if data1 > data2:
        print(data1)
    else:
        print(data2)
#question_7()

def question_8():
    data = eval(input())
    if data >= 50:
        data = data ** 2
    else:
        data = data * 3
    print(data)
#question_8()

def question_9():
    data = eval(input())
    if data >= 80:
        data = "A"
    elif data < 80 and data >= 70:
        data = "B"
    elif data < 70 and data >= 60:
        data = "C"
    elif data < 60 and data >= 50:
        data = "D"
    else:
        data = "F"
    print(data)
#question_9()

def question_10():
    bank = 5000.50
    num = input()
    data = eval(input())
    if num == "1":
        bank = bank + data
    elif num == "2":
        bank = bank - data
    print(bank)
#question_10()

