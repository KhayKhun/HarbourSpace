import turtle

# global config
turtle.shape('turtle')
turtle.speed(0)

# A
a = turtle.clone()
a.color('#FF0000')

a.penup()
a.backward(100)
a.pendown()
a.left(120)
a.forward(180)
a.left(120)
a.forward(180)
a.penup()
a.backward(90)
a.pendown()
a.left(120)
a.forward(90)


# B
b = turtle.clone()
b.color('#0000FF', '#0000FF')

b.begin_fill()
b.forward(50)
b.circle(50, 180)
b.right(180)
b.circle(50, 180)
b.forward(50)
b.left(90)
b.forward(200)
b.end_fill()
# C

c = turtle.clone()
c.color('#00FF00')
c.penup()
c.forward(300)
c.pendown()
c.circle(100, -180)



turtle.mainloop()