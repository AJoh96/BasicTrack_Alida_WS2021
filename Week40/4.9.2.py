import turtle

#side = 20 --> next slide +20

window = turtle.Screen()
window.bgcolor("lightgreen")

def draw_square (animal,size):
     animal.penup()
     animal.forward(10)
     animal.left(90)
     animal.forward(10)
     animal.right(90)
     animal.pendown()

     for _ in range(4):
         animal.forward(size)
         animal.left(90)

ali = turtle.Turtle()

for x in range(1, 6):
    draw_square(ali, x * 20)





window.mainloop()
