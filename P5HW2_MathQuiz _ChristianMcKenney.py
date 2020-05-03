# This program calculates addition and subtraction with random numbers
# 4/30/2020
# CTI-110 P5HW2 - Math Quiz
# Christian McKenney

#Step-1 Define the main and initialize the loop variable
#Step-2 Ask the user to enter a number from the menu
#Step-3 If the user enters the number 1, add the random numbers and
# display the addition problem

#Step-4 If the user enters the number 2, subtract the random numbers and
# display the subtraction problem

#Step-5 If the user enters 3, terminate the program


import random

def main():
    # The loop variable
    i = 0

    while i != 1:
        print('\nMAIN MENU\n')
        print('--------------------')
        print('1) Add Random Numbers')
        print('2) Subtract Random Numbers')
        print('3) Exit\n')

        # Ask the user to pick which option
        choice = int(input('Which would you like to do? '))


        if choice == 1:

                addRandom()

        elif choice == 2:

                subRandom()

        elif choice == 3:
            # The program will terminate
            print('The program will terminate')
            i = 1

        else:
            print('Not a valid option')


def addRandom():
    randomnum1 = random.randrange(1,300)
    randomnum2 = random.randrange(1,300)

    answer = randomnum1 + randomnum2

    print('  '+str(randomnum1)+'\n+ '+str(randomnum2))
   
    guess = int(input('\nWhat is the answer? '))

    if guess == answer:
        print('Congratulations! you got it correct!')

    elif guess != answer:
        print(answer)



def subRandom():
    randomnum1 = random.randrange(1,300)
    randomnum2 = random.randrange(1,300)

    answer = randomnum1 - randomnum2

    print('  '+str(randomnum1)+'\n- '+str(randomnum2))

    guess = int(input('\nWhat is the answer? '))

    if guess == answer:
        print('Congratulations! you got it correct!')

    elif guess != answer:
        print(answer)
    




main()
