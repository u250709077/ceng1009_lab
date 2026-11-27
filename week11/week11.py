# def fizz_buzz(n):
#     for i in range (1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizz_buzz(16)
#
from functools import total_ordering


# def digit_sum(n):
#     total = 0
#     while n> 0 :
#         total= total + n % 10
#         n = n // 10
#         print(n)
#     return total
# print(digit_sum(1234))

# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result +s[i].upper()
#         else:
#             result = result + s[i].lower()
#     return result
# print(alternate_case("Hello World"))
# import turtle
# wn=turtle.Screen()
# t=turtle.Turtle()
# t.pensize(3)
# wn.bgcolor("lightgreen")
# color=["red","yellow","blue"]
# def draw_polygon(t,sides,length):
#     for i in range (sides):
#         t.fd(length)
#         t.left(360/sides)
#
# for i in range (3):
#     t.penup()
#     t.goto(-150+i*120,0)
#     t.pendown()
#     t.color(color[i])
#     draw_polygon(t,i+3,60,)
#
# wn.exitonclick()
# import turtle
# wn=turtle.Screen()
# t=turtle.Turtle()
# wn.bgcolor("lightgreen")
# colors=["red","blue","red","blue","red"]
#
# def filled_square(t,size,color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# for i in range (5):
#     t.penup()
#     t.goto(165+i*50,-25)
#     t.pendown()
#     filled_square(t,50,colors[i])
# import turtle
# wn=turtle.Screen()
# t=turtle.Turtle()
# wn.bgcolor("lightgreen")
# t.pensize(2)
#
# def draw_square(t,size):
#     for i in range(4):
#         t.fd(size)
#         t.left(90)
#
# for i in range(12):
#     draw_square(t,80)
#     t.left(30)

# import turtle
# wn=turtle.Screen()
# t=turtle.Turtle()
# wn.bgcolor("lightgreen")
# size=40
# def draw_square(t,size,filled):
#     if filled:
#         t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     if filled:
#         t.end_fill()
#
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120+col*size,120+row*size)
#         t.pendown()
#         draw_square(t,size,(row+col)%2==0)
# wn.exitonclick()
#





