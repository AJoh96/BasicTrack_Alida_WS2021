import turtle


def draw_square(animal, size):

    for _ in range(6):
        animal.forward(size)
        animal.left(90)


screen = turtle.Screen()
nick = turtle.Turtle()

#for _ in range(60):
#    draw_square(nick, 100)
#    nick.left(6)

for index in range(60):
    draw_square(nick, index * 5)
    nick.left(6)

screen.exitonclick()

