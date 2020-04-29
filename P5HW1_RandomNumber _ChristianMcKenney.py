# This program is a guess the number game which loops until the answer is correct
# 4/28/2020
# CTI-110 P5HW1 - Random Number
# Christian McKenney

#Step-1 Initialize the loop variable 
#Step-2 Prompt the user to enter a number from the menu
#Step-3 If the user chooses to play the number game, create a random number
#Step-4 Check if the random number was too high or too low from what the user
# entered

import random

# The loop variable
i = 0

while i != 1:

    print('\nMAIN MENU\n')
    print('---------------------\n')
    print('1) Play Game')
    print('2) Exit')

    # Ask the user to pick which option
    choice = int(input(' Which would you like to do? '))

    if choice == 1:

        n = 0

        randomnum = random.randrange(1,100)


        while n != 1:

            # Ask the user to guess what the number is
            guess = int(input('\nGuess what the number is: '))


            # If the number the user entered was greater than the random number
            if guess > randomnum:
                print('Too high, try again.')

            # If the number the user entered was less than the random number
            elif guess < randomnum:
                print('Too low, try again.')

            # If the user guessed the correct number 
            elif guess == randomnum:
                print('Congratulations.')
                n = 1

    # The program will terminate
    elif choice == 2:
        print('The program will terminate.')
        i = 1

    else:
        print('Not valid option')

    
