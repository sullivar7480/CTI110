"""
CTI 110
P_Turtle - Turtle Graphics
Raven Sullivan
9/26/23
Basic Turtle Graphics
"""
# set up the turtle
import turtle

t = turtle.Turtle() #create the turtle called 't'



#customize pen
t.pensize(5)
t.pencolor("lavender")

#method 1 - tank controls
#draw a 'R'
t.left(90)
t.forward(100)
t.right(25)
t.circle(-30, 240)
t.left(120)
t.forward(75)

#Draw a 'S'

t.penup()
t.left(90)
t.forward(100)
t.pendown()
t.right(30)
t.pencolor("LightSteelBlue")
t.circle(30, -240)
t.circle(30, 240)
t.circle(-30,240)


"""
t.left(90)
t.forward(50)
t.right(180)
t.forward(100)
"""



"""
#method 2 - goto
t.pencolor("lavender")
t.goto(0,0)
t.goto(100,200)
"""
