from turtle import *

#Declare variables
sides = int(input("Enter number of sides:"))
size = int(input("Enter size number:"))
angle = 360/sides
color = input("Enter pen color:")
fill = input("Enter fill color:")

#Show how many sides and the angle of each side
print ("sides:", sides, "angle:", angle)

#Begin filling shape
fillcolor(fill)
begin_fill()

#Move and repeat for the given number of sides
for sides in range(sides):
    pencolor(color)
    forward(size)
    right(angle)

#Stop filling shape
end_fill()
exitonclick()
