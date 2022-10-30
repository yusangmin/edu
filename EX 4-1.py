# 4-1
print('나는' + str(12) +'개의 사과를 먹었다.')

# 4-2
print('apple' + 'grape')
print('apple' * 3)

# 4-3
_str = input("문자열을 입력하시오: ")
s = _str[0:2] + _str[-2:]
print(s)

# 4-4
s = input("문자열을 입력하시오: ")
s += "하는 중"
print(s)

# 4-5
_str_=input("기호를 입력하시오: ")
word=input("중간에 삽입할 문자열을 입력하시오: ")
s=_str_[:1] + word + _str_[1:]
print(s)

# 4-6
lista = [1, 2, 3, 4]
sum = 0
sum = lista[0] + lista[1] + lista[2] + lista[3]
print("리스트 = ", lista)
print("리스트 숫자들의 합 = ", sum)

4-7
import turtle
t = turtle.Turtle()
t.shape("turtle")

lista = [ ]
color = input("색상 #1을 입력하시오: ")
lista.append(color)
color = input("색상 #2을 입력하시오: ")
lista.append(color)
color = input("색상 #3을 입력하시오: ")
lista.append(color)

t.fillcolor(lista[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(100, 0)
t.down()
t.fillcolor(lista[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.goto(200, 0)
t.down()
t.fillcolor(lista[2])
t.begin_fill()
t.circle(50)
t.end_fill()
t._screen.exitonclick()   # 화면을 마우스로 클릭해야 종료되게 하는 부분

4-8
import turtle
t = turtle.Turtle()
t.shape("turtle")

lista = [ ]
lista.append(int(input("x1: ")))
lista.append(int(input("y1: ")))
lista.append(int(input("x2: ")))
lista.append(int(input("y2: ")))
lista.append(int(input("x3: ")))
lista.append(int(input("y3: ")))

t.goto(lista[0], lista[1])
t.goto(lista[2], lista[3])
t.goto(lista[4], lista[5])
t._screen.exitonclick()   # 화면을 마우스로 클릭해야 종료되게 하는 부분



# x y 축
# pip install matplotlib   ---> 데이터 분석을 위한 그래프를 그릴때 사용하는 라이브러리
import matplotlib.pyplot as plt

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

plt.plot(x, y)
plt.xticks(x, labels=['2010년', '2011년', '2012년', '2013년', '2014년', '2015년', '2016년', '2017년', '2018년', '2019년', '2020년', '2021년', '2022년'], rotation=45)
plt.yticks(y)
plt.show()