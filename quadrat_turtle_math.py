import turtle
turtle.color('CornflowerBlue', 'CornflowerBlue')

side_length = input("side length: ")
radius_incircle = sidelength * 1.9626

for a in range(5):

    for m in range(18):
        turtle.left(20)

        for i in range(4):
            turtle.forward(side_length)
            turtle.right(90)

    turtle.penup()
    turtle.left(72)
    turtle.forward(radius_incircle)
    turtle.pendown()

turtle.exitonclick()

#Liste der Farben: http://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
