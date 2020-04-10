# This program uses nested loops to print multiple number signs to create
# a triangle.

# 4/9/2020
# CTI-110 P4HW3 - Nested Loops
# Christian McKenney

#Step-1 Create a nested loop that sets the range for the vertical line and
# prints the first part of the triangle, the (vertical line).

#Step-2 Create another nested loop that sets the spaces for the range and
# prints the second part of the triangle, the (diagnol line).

# The range for the vertical line
for row in range( 6 ):
    
    # The vertical straight line
    print( "#", end="", sep="")
    
    # The diagnol line
    for spaces in range( row ):
        print( " ", end="", sep="")
    print( "#", sep="" )

