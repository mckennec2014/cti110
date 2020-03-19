# CTI-110
# P3HW2 - BasicMath
# Christian McKenney 
# 3/19/2020

#Step-1 Enter both of the numbers
#Step-2 Enter a number between 1-4 on the menu
#Step-3 Add both of the numbers to get the sum
#Step-4 Multiply both of the numbers to get the product
#Step-5 Subtract both of the numbers to get the difference
#Step-6 Exit the program

# First number
num1 = int(input('What is the first number? '))

# Second number
num2 = int(input('What is the second number? '))


print('----------MENU-----------')

print('1) Add Numbers')
print('2) Multiply Numbers')
print('3) Subtract Numbers')
print('4) Exit')

print('-------------------------')

choice = int(input('Which would you like to do? '))


# Add and get the sum of the numbers
if choice == 1:
    sum = num1 + num2
    print("The sum of the numbers:", sum)

# Multiply and get the product of the numbers   
elif choice == 2:
    product = num1 * num2
    print("The product of the numbers:", product)

# Subtract and get the difference of the numbers
elif choice == 3:
    difference = num1 - num2
    print("The difference of the numbers:", difference)

    
# Exit the program
elif choice == 4:
    print('The program will terminate')

else:
    print('Not a valid number')
