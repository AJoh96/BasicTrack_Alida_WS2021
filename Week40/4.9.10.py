import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
finn = turtle.Turtle()
finn.color('blue')


def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)


for _ in range(5):
    draw_star(finn, 100)
    finn.penup()
    finn.forward(300)
    finn.right(144)
    finn.pendown()

window.mainloop()
