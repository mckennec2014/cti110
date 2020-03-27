# CTI-110
# P4T1a - Shapes
# Christian McKenney 
# 3/26/2020

#Step-1 Display the turtle and set the number of squares
#Step-2 Give side_unit a variable and give side_unit a number equal to
# how many spaces that the variable (s) will move

#Step-3 Set the forloop command
# and let the program draw the number of squares equal to the range of
# 1, the number of squares + 1)

#Step-4 Everytime the loop will loop the increments are increased making the
# squares bigger

# To show the turtle
import turtle
turtle.showturtle()

# Number of squares
num_squares = 100

# The variable for side_unit and the number of spaces variable (s) will move
s = side_unit = 10

# Put the pendown
turtle.pendown()

# Draw the squares and increase the increments for every loop
for square in range(1, num_squares + 1):
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    turtle.left(90)
    turtle.forward(s)
    s = side_unit + 3 * square

# Return back to the base
    turtle.goto(0,0)


turtle.done()
