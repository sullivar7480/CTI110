import turtle as t


def draw_R():
    t.penup()
    t.setpos(-200, 200)
    t.pendown()
    t.color("blue")
    t.pensize(3)
    
    t.circle(80, 180)
    t.left(90)
    t.forward(290)
    t.backward(110)
    t.left(45)
    t.forward(150)
    

# Function to draw the letter S
def draw_S():
    t.penup()
    t.setpos(250, 250)
    t.pendown()
    t.color("azure4")
    t.pensize(3)

    t.forward(30)
    t.backward(30)

    t.circle(-90, -185)
    t.circle(90, -250)
   
    

draw_R()


draw_S()

t.done()
