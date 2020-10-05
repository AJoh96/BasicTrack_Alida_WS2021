import turtle

#side = 20

window = turtle.Screen()
window.bgcolor("lightgreen")

def draw_square (animal, size):

    for _ in range (4):
        animal.forward(size)
        animal.left(90)

def draw_gap (animal,size):
    animal.stamp()
    animal.penup()
    animal.forward(50)
    animal.pendown()
    animal.stamp()

ali = turtle.Turtle()

for _ in range(4):
    draw_square(ali, 20)
    draw_gap(ali, 50)




window.mainloop()
