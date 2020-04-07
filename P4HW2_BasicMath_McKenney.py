# CTI-110
# P4HW2 - BasicMath
# Christian McKenney 
# 4/7/2020

#Step-1 Enter both of the numbers
#Step-2 Initialize the loop variable 
#Step-3 Create a while loop that will loop displaying a menu, asking the user
# to enter a number between 1-4, doing the calcuations based on the number
# entered, and if the user enters the number 5 display an error message and
# repeat the loop

#Step-4 Exit the program


# First number
num1 = int(input('What is the first number? '))

# Second number
num2 = int(input('What is the second number? '))

# Initialize the loop variable
terminate = 0


while terminate != 1:

    print('\n----------MENU-----------')

    print('1) Add Numbers')
    print('2) Multiply Numbers')
    print('3) Subtract Numbers')
    print('4) Exit')

    print('-------------------------\n')

    choice = int(input('Which would you like to do? '))


    # Add the numbers, display the numbers entered, and show the sum
    if choice == 1:
        sum = num1 + num2
        print("The first number entered:", num1)
        print("The second number entered:", num2)
        print("The sum of the numbers:", sum)
        
    # Multiply the numbers, display the numbers entered, and show the product
    elif choice == 2:
        product = num1 * num2
        print("The first number entered:", num1)
        print("The second number entered:", num2)
        print("The product of the numbers:", product)

    # Subtract the numbers, display the numbers entered, and show the difference
    elif choice == 3:
        difference = num1 - num2
        print("The first number entered:", num1)
        print("The second number entered:", num2)
        print("The difference of the numbers:", difference)

        
    # Exit the program
    elif choice == 4:
        print('The program will terminate')
        
        # Close the program
        terminate = 1

    else:
        print('Not a valid number')

