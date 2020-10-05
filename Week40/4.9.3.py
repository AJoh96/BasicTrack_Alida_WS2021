import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()

def draw_poly (t, n, sz):

    for _ in range(n):
        t.forward(sz)
        t.left(45)

draw_poly(tess, 8, 50)


window.mainloop()
