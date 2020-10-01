import turtle

window = turtle.Screen()
ali = turtle.Turtle()

#Equal. triangle

for _ in range(3):
    ali.forward(50)
    ali.left(120)

#square
for _ in range(4):
    ali.forward(50)
    ali.left(90)

#Heyagon
for _ in range(6):
    ali.forward(100)
    ali.left(60)

window.exitonclick()

