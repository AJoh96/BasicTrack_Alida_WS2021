import turtle

paper= turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red', 'blue', 'green', 'yellow', 'orange']

for element in range(12):
    #leonardo.color(colors[element % 5])
    leonardo.color(colors[element % len(colors)])
    if element % 2 ==0:
            leonardo.forward(100)
    else:
        leonardo.forward(50)
    leonardo.left(30)

paper.exitonclick()