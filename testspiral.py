from tkinter import *
from turtle import *
import turtle
import random

tot = 0

angles = []
i = 0
while i < 360:
    angles.append(i)
    i += 60

ts = turtle.getscreen()
turtle.screensize(canvwidth=5000, canvheight=5000,
                  bg="white")

systurtle = turtle.Turtle()
systurtle.pencolor("red")
def gen_system(xpos, ypos, times):
    for _ in range(times):
        systurtle.penup()
        systurtle.setpos(xpos, ypos)
        if random.randrange(0, 5) == 3:
            systurtle.pencolor("blue")
            systurtle.forward(random.randrange(101, 700))
        else:
            systurtle.pencolor("red")
            systurtle.forward(random.randrange(10, 100))
        print(systurtle.xcor(), systurtle.ycor())
        systurtle.pendown()
        systurtle.right(random.randrange(0, 360))
        systurtle.circle(1)

for x in angles:
    a = turtle.Turtle()
    a.right(x)
    dev = random.randrange(20, 40) 
    atotang = 0
    for i in range(dev):
        a.forward(random.randrange(1, 9)/10+i)
        tempang = random.randrange(3, 9)
        a.right(tempang)
        atotang += tempang
        if random.randrange(0, 5) == 3:
            gen_system(int(a.xcor()), int(a.ycor()), 80)
            tot+=80

    b = turtle.Turtle()
    b.penup()
    b.setpos(int(a.xcor()), int(a.ycor()))
    b.pendown()
    b.right(x + atotang + 10)
    btotang = 0
    for i in range(dev, 50):
        a.forward(random.randrange(1, 9)/10+2*i)
        a.right(random.randrange(3, 9))
        b.forward(random.randrange(1, 9)/10+2*i)
        tempang = random.randrange(3, 9)
        b.right(tempang)
        btotang += tempang
        if random.randrange(0, 3) == 2:
                gen_system(int(b.xcor()), int(b.ycor()), 40)
                tot+=40
        if random.randrange(0, 3) == 2:
                gen_system(int(a.xcor()), int(a.ycor()), 40)
                tot+=40
        if random.randrange(0, 25) == 5:
            c = turtle.Turtle()
            c.penup()
            c.setpos(int(b.xcor()), int(b.ycor()))
            c.pendown()
            c.right(x + btotang + atotang + 20)
            for ij in range(10):
                c.forward(random.randrange(1, 9)/10+4*i)
                tempang = random.randrange(3, 9)
                c.right(tempang)
                gen_system(int(c.xcor()), int(c.ycor()), 80)
                tot+=80

ts.getcanvas().postscript(file="duck.eps")
turtle.done()

print(tot)