import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
finn = turtle.Turtle()
finn.color('blue')

for x in range(100):
    finn.forward(x * 5)
    finn.right(90)
    #finn.right(89)




window.mainloop()
