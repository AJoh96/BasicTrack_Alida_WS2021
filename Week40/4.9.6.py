import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
finn = turtle.Turtle()
finn.color('blue')

def draw_poly (t, n, sz):
    angle = 360/n
    for _ in range(n):
        t.forward(sz)
        t.left(angle)

def draw_equitriangle (t, sz):
    draw_poly(t, 3, sz)

draw_equitriangle(finn, 50)


window.mainloop()
