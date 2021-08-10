from turtle import *
import turtle
import random
import csv

points_x, points_y = [],[]

# Screen Config
ts = turtle.getscreen()
turtle.screensize(canvwidth=5000, canvheight=5000,
                  bg="black")
ts.tracer(False) #removing turtle animations

# Generates Solar Systems
def gen_system(xpos, ypos, count):
    s = turtle.Turtle() #init turtle
    for _ in range(count): #loop thru wanted solar system
        s.penup()
        s.setpos(xpos, ypos) #move turtle to the line
        s.right(random.randrange(0, 360)) #spin turtle in a random direction
        if random.randrange(0, 5) == 3: #chance to spawn far
            s.pencolor("blue")
            s.forward(random.randrange(101, 700)) #random distance
        else: #chance to spawn close
            s.pencolor("red")
            s.forward(random.randrange(10, 100)) #random distance
        s.pendown()
        s.forward(1) #spawn system
        points_x.append(int(s.xcor()))
        points_y.append(int(s.ycor()))

# Generates Galaxy Lines

# Recursive method that continues to draw lines based on the value of "start"
# Generates solar systems at the end of each line
def gen_galaxy_line(turt, start, stop, systems, multiplier=1):
    if start > stop: # Condition to stop recusive function
        gen_galaxy_line(turt, start - 1, stop, systems, multiplier)
        turt.forward((random.randrange(1, 9)/10+start)*multiplier) # Moves turtle forward a random yet increasing distance
        turt.right(random.randrange(3, 9)) #
        gen_system(int(turt.xcor()), int(turt.ycor()), systems)  # Generates solar systems
        
        return turt

# the shit
for angle in range(0, 360, 60):
    a = turtle.Turtle()
    a.right(angle) # turns turtle based on angle to set the initial angle
    first_section_length = random.randrange(25, 50) # varies the distance of the first segment of the spiral (before the split)

    a = gen_galaxy_line(a, first_section_length, 0, random.randrange(20, 30), 1) 
    b = a.clone()
    b.right(10)

    # Continues two new lines from the previous section to create a 'split' effect
    a = gen_galaxy_line(a, 75, first_section_length, random.randrange(20, 40), 2) # Uses 2x multiplier to make the split sections of the spiral have a wider radius
    b = gen_galaxy_line(b, 75, first_section_length, random.randrange(20, 40), 2)
    a.pencolor("white")
    b.pencolor("white")
    a.circle(10)
    b.circle(10)
    
print("Total Systems: ", len(points_x))
res = [points_x, points_y]

with open("points.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(res)

turtle.done()



