import turtle


aung = turtle.clone()
aung.speed(0)
aung.color('#ff0000')

for i in range(10):
    aung.forward(20)
    aung.circle(100, 180)
    aung.left(40)
    aung.color('#00ff00')
for i in range(10):
    aung.forward(20)
    aung.circle(100, 180)
    aung.left(40)
    aung.color('#0000ff')




turtle.mainloop()