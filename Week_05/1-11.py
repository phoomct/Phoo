def question_1():
  import math as m
  print(m.pow(float(input()),2))
#question_1()

def question_2():
  print("%.2f"%(float(input()) / float(input())))
#question_2()

def question_3():
  print("%.2f"%((float(input()) - 32) * 5/9 ))
#question_3()

def question_4():
  print("%.2f"%((float(input()) * 1.8 ) + 32 ))
#question_4()

def question_5():
  import math as m
  print(m.pow( 2 - 2, 3 * 2 ))
  print(m.pow( 2 / 3 * 4, 4 ))
  print( 1 + 2 / 3 * 4 + 5 )
  print( 10 - 5 / 6)
  print(m.pow( 9 , 2 / 4 ))
#question_5()

def question_6():
  import math
  print(math.ceil((abs(-25.13))))
  print(math.floor(math.log2(25864)))
  print(math.sqrt(abs(math.tan(315))))
  print(math.sqrt(abs(math.sin(60))))
  print(math.sqrt(abs(math.cos(90))))
#question_6()

def question_7():
  data = float("{:.2f}".format(float(input())))
  data2 = float("{:.2f}".format(float(input())))
  print("%.2f" %((data2 - data) ** 2))
question_7()

def question_8():
  data1 = float("{:.2f}".format(float(input())))
  data2 = float("{:.2f}".format(float(input())))
  data3 = float("{:.2f}".format(float(input())))
  data4 = float("{:.2f}".format(float(input())))
  print("%.2f" %(data1 * data2 * data3 * data4 / data1 + data2 + data3 + data4))
#question_8()

def question_11_1():
  import math as m
  v = float(input("v = ")); c = float(input("c = ")); seta = float(input("θ = ")); psi = float(input("	Ψ = "))
  print(m.sqrt(1 - ((v ** 2) / (c ** 2))) / m.sin(seta + psi))
#question_11_1()

def question_11_2():
  x = float(input("x = ")) ; y = float(input("y = "))
  print(((x + (2 * y) - 7) ** 2) + ((2 * x) + y - 5) ** 2)
#question_11_2()