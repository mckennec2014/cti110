# CTI-110
# P4T1b - Initials
# Christian McKenney
# 3/26/2020

#Step-1 Display the turtle, change the pensize, and change the pencolor
#Step-2 Pick the penup, move the turtle to get into position, put the pendown,
# and draw the letter C

#Step-3 Pick the penup, move the turtle to get into position, put the pendown,
# and draw the letter M


# To show turtle
import turtle
turtle.showturtle()

# Change the pensize and the pencolor
turtle.pensize(5)
turtle.pencolor("orange")


# To get into position for drawing letter C
turtle.penup()
turtle.forward(40)
turtle.left(90)
turtle.forward(50)
turtle.left(45)
turtle.pendown()

# Letter C
for i in (1,2,3,4,5,6):
    turtle.forward(20)
    turtle.left(45)
    turtle.forward(30)

# To get into position for drawing letter M
turtle.penup()
turtle.right(45)
turtle.right(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(40)
turtle.pendown()

# Letter M
turtle.left(70)
turtle.forward(130)
turtle.right(140)
turtle.forward(130)
turtle.left(140)
turtle.forward(130)
turtle.right(140)
turtle.forward(130)


