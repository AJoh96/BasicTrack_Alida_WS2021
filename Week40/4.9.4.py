import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
finn = turtle.Turtle()
finn.color('blue')

angel = 360/21

def square (t, size):
    for _ in range(4):
        t.forward(50)
        t.left(90)

for x in range(21):
    finn.left(angel)
    square(finn, 50)




window.mainloop()
