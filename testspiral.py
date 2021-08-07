from turtle import *
import turtle
import random

points_x, points_y = [],[]

ts = turtle.getscreen()
turtle.screensize(canvwidth=5000, canvheight=5000,
                  bg="white")
ts.tracer(False)

def gen_system(xpos, ypos, count):
    s = turtle.Turtle()
    for _ in range(count):
        s.penup()
        s.setpos(xpos, ypos)
        s.right(random.randrange(0, 360))
        if random.randrange(0, 5) == 3:
            s.pencolor("blue")
            s.forward(random.randrange(101, 700))
        else:
            s.pencolor("red")
            s.forward(random.randrange(10, 100))
        s.pendown()
        s.circle(1)
        points_x.append(s.xcor())
        points_y.append(s.ycor())

def gen_galaxy_line(turt, start, stop, systems, spawn_chance, multiplier):
    if start > stop:
        gen_galaxy_line(turt, start - 1, stop, systems, spawn_chance, multiplier)
        turt.forward((random.randrange(1, 9)/10+start)*multiplier)
        turt.right(random.randrange(3, 9))
        if random.randrange(0, spawn_chance) == 0:
            gen_system(int(turt.xcor()), int(turt.ycor()), systems)
        
        return turt

for angle in range(0, 360, 60):
    a = turtle.Turtle()
    a.right(angle)
    first_section_length = random.randrange(30, 60)

    a = gen_galaxy_line(a, first_section_length, 0, 80, 5, 1)
    b = a.clone()
    b.right(10)

    gen_galaxy_line(a, 100, first_section_length, 80, 2, 2)
    gen_galaxy_line(b, 100, first_section_length, 80, 2, 2)
    
print("Total Systems: ", len(points_x))
res = [points_x, points_y]

import csv
with open("points.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(res)

turtle.done()



