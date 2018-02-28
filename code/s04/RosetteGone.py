# RosetteGoneWild.py
import random
import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
t.width(3)
# Ask the user for the number of circles in their rosette, default to 6
listofcolors=[]

default_colors= turtle.textinput("Default colors", "Do you want to use the default colors (Y/N)?")

if default_colors=='Y':
    listofcolors=["green","blue","orange","purple","red","yellow"]
    numberofcolors=6
    
if default_colors=='N':
    numberofcolors= int(turtle.textinput("number of colors", " How many colors do you want"))
    for color in range (numberofcolors):
        tmpcolor= turtle.textinput("color", "What is the color #" + str(color+1))
        listofcolors.append(tmpcolor)                

number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your rosette?", 6))
#c1 = turtle.textinput("first color", "what is the first color ")
#c2 = turtle.textinput("second color","what is the second color ",)
    
for x in range(number_of_circles):
    r = random.randint(0,numberofcolors-1)
    t.pencolor(listofcolors[r])
    
    t.circle(100)
    r = random.randint(0,numberofcolors-1)
    t.pencolor(listofcolors[r])
    t.circle(50)
    t.left(360/number_of_circles)
    
