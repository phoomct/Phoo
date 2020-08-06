def question_1():
    PR = "I love KMUTNB"
    print(PR)
question_1()

def question_2():
    print("KOR ma di KUB\nONE TO ONE\nI get grade F\nElection Cheat in TH")
question_2()

def question_3(a):
    for i in range(1, a + 1):
        print("|",end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print("  " * (a - i),end="|")
        print()
question_3(3)

def question_4(a):
    b = a
    for i in range(0, a):
       print("|",end=" ")
       print("  " * i,end="")
       for j in range(b,0,-1):
           print("* ",end="")
       print("" * (a - i),end="|")
       print()
       b -= 1
question_4(3)

def question_5():
    a = "'10/2 = 5'"+'\n"21 - 20 = 1"' + "\n\who" + "\gre " + "\You"
    print(a.replace("g","a"))
question_5()

def question_6():
    print("ไอ้อ่วนพูดว่า" + '"เเก่ตายเเน่น"' + "\n" + "ไอ้ผอมบอกว่า" + "'เเน่จริงกลับใหม่'")
question_6()

def question_7():
    price = 500
    sale = price * (5/100)
    new_price = price - sale
    print("ราคา = %d"%price)
    print("ส่วนที่ลด = %d"%sale)
    print("ราคาที่ลดเเล้ว = %d"%new_price)
question_7()

def question_8():
    total = 0
    for i in range (1,7):
        data = eval(input())
        total = total + data
    print(total)
question_8()

def question_9():
    total = 0
    for i in range(1,4):
        data = eval(input())
        total = total + (data * data)
    print(total)
question_9()

def question_10():
    total = 0
    for i in range (1,6):
        data = eval(input())
        total = total + data
    print(total/5)
question_10()

def question_11():
    text = ""
    for i in range(1,4):
        data = input()
        text = text + data
    print(text)
question_11()

def question_12():
    a = 10
    b = 5
    #print(a/c) #name error
    c = 10
    #d * 10 #name error
    #y = d + 10 #name error
    r = 5
    #print(d) #name error
    # print(r) #syntax error
    #print(d) #name error
    print(a)
question_12()

def question_13():
    a = 0
    b = 4
    c = "3"
    #print(4/c) #Type error
    #print(b/a) # zero Division Error
    print(c * a)
    a = 7
    xxx = a
    c = b
    print( b + c )
    #a * b = d # syntax error
question_13()

def question_14():
    a = 10
    b = 0
    a = b
    r = a
    t = "I likes GUN"
    #a | b = 15 #syntax error
    #a / c = 1 #syntax error
    #4 + 6 = r #syntax error
    print(r)
    a + 10 * 4
    #print(5/a) #Zero Division Error
    a = b;
    c = 5.5
    print(c,a+b)
    print(c+a+b)
    #print(c+a+"") #Type error
    #print(t+a+b+r) #Type error
question_14()

def question_16():
    a = 20; b = 30
    #a + 25 = a #Syntax error
    x = "25"
    #print(a+b+x) #type error
    d = 15
    g = 25
    _f = 5
    d = a/b
    #a5 = a+f #name error
    #is = a +Z2 + 25 #Syntax error
question_16()

def question_17():
    #a = 20;b = 30; in = 10 #Syntax error
    #a + 25 = a #Syntax error
    x = "250"
    #print(250 + x) #type error
    o = 25
    #E * pin = 50 #Syntax error
    d = 150 / o
    #print(af+"KAk") #Name error
question_17()

