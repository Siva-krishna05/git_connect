'''import turtle
import math
import random
screen=turtle.Screen()
screen.bgcolor("black")
t=turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)
colors=['red','blue',"lime",'yellow','cyan','magenta','orange','pink','white']
for i in range(100):
    t.penup()
    t.goto(0,40)
    angle=i*(math.pi*2)/100
    x=16*(math.sin(angle)**3)*15
    y=(13*math.cos(angle)-5*math.cos(2*angle)-2*math.cos(3*angle)-math.cos(4*angle))*15
    c=random.choice(colors)
    t.color(c)
    t.pendown()
    t.goto(x,y)
    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)
        
turtle.done()
    '''
'''x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
'''

