# CTI-110
# P3T1- Areas of Rectangles
# Christian McKenney
# 3/12/2020

# Get the dimensions of rectangle 1
l1 = int(input('Enter the length of rectangle 1: '))
w1 = int(input('Enter the width of rectangle 1: '))


# Get the dimensions of rectangle 2
l2 = int(input('Enter the length of rectangle 2: '))
w2 = int(input('Enter the width of rectangle 2: '))

# Calculate the areas of the rectangles
area1 = l1 * w1
area2 = l2 * w2

# Determine which has the greater area
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
