# circlespiral1.py

import turtle
t = turtle.Pen()
turtle.bgcolor("blue")
t.speed(0)
sides = eval(input( ' Enter a number of sides between 2 and 10: ' ))
colors = ["silver", "black", "orange", "purple", "grey", "white", "pink", "lightblue", "green", "red"]
for x in range(360):
    t.pencolor( colors[ x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
    t.left(90)
  
    
