from turtle import *                                            # เอาไว้ใช้ข้อ 5 #
from statistics import *                                    # เอาไว้ใช้ข้อ 10 #

def question_01(num):
    return(sum([i for i in num if i > 2]))             # หาผลรวมของ list นี้ (ถ้าตัวเลขมากกว่า 2 ค่อยเอาไปบวก) 
print(question_01((1,2,3,5,6,1,3,4,5,6,1)))


def question_02(num):
    return(sum([int(i) for i in num]))                  # หาผลรวมของ list นี้   
#print(question_02([1,2,'3','4','5']))
    
def question_03(num):
    num.append(5)                                        #เพิ่ม 5 เข้าไปใน  list  จะกลายเป็น[1,2,3,5]
    num.remove(2)                                        # เอา 2 ออกจาก list จะกลายเป็น[1,3,5]
    num[0] = 2                                                # เปลียน list ตำเเหน่งที่ 0 จาก 1 เป็น 2 [2,3,5]
    return num
#print(question_03([1,2,3]))


def question_04():
    total_score = []                                               #สร้างไว้เพื่อเก็บคะเเนน
    while True:
        name, score = input().split(" ")                  # เเยกชื่อกับคะเเนน
        if name == "-1" or score == "-1":                 # ถ้า ชื่อ หรือ คะเเนน = -1
            break
        else:
            total_score.append(float(score))          # เอาคะเเนนเก็บไว้ใน list
    return(sum(total_score)/len(total_score))   # หาค่าเฉลียของคะเเนน
#print(question_04())

def question_05():
    while True:
        x, y = input().split(",")                                     #เเยก x กับ  y
        if x == "-1" and y == "-1":                                 # ถ้า x เเละ y = -1
            break                                                   
        else:
            penup()                                         
            goto(int(x),int(y))                                        #ไปที่ x, y
            pendown()
            circle(100)
#question_05()

def question_06():
    matrix = [input() for i in range(0,4)]                   #สร้าง list
    for i in range(0,2):                                              # วนลูปจำนวนเเถวเเนวนอน
        for j in range(0,2):                                          # วนลูปจำนวนเเถวตั้ง
            print(matrix[0], end="|")                             # print list ตำเเหน่งที่ 0
            matrix.remove(matrix[0])                          # เอา list ตำเเหน่งที่ 0 ออก
        print()
#question_06()

def question_07(num):
    matrix = [input() for x in range(num ** 2)]         #สร้าง list
    for i in range(num):                                            # วนลูปจำนวนเเถวเเนวนอน
        for j in range(num):                                        # วนลูปจำนวนเเถวตั้ง
            print(matrix[0], end="|")                            # print list ตำเเหน่งที่ 0
            matrix.remove(matrix[0])                         # เอา list ตำเเหน่งที่ 0 ออก
        print()
#uestion_07(int(input()))

def question_08(num):
    return(max(num), min(num))                        #print ค่า มากสุด, ค่าน้อยสุด
#print(question_08([int(input()) for i in range(int(input()))]))
    
def question_09(num):
    return(sorted(num),sorted(num,reverse = True))      # เรียงเลขน้อยไปมาก, เรียงจากมากไปน้อย
#print(question_09([int(input()) for i in range(int(input()))]))

def question_10(num):
    return(mode(num), median(num), mean(num))     # print mode, median, mean
#print(question_10([int(input()) for i in range(int(input()))]))

def question_11(num):
    if int(input()) in num:                           #ถ้า  input มันอยู่ใน list
        return("พบ")                                             
    else:
        return("ไม่พบ")                                                  
#print(question_11([int(input()) for i in range(int(input()))]))

