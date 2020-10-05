import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
finn = turtle.Turtle()



def draw_square(animal, size):

    for _ in range(6):
        animal.forward(size)
        animal.left(90)

finn.speed(50)
start_point = (0,0)

for index in range(60):
    finn.color('blue')
    draw_square(finn, index * 5)
    finn.left(6)

finn.penup()
finn.pendown()
finn.setx(start_point[0])
finn.sety(start_point[0])

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)

for index in range(40):
    finn.color('red')
    draw_star(finn, index * 20)



window.mainloop()
