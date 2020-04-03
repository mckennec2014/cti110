# CTI-110
# P4HW1 - Expenses
# Christian McKenney
# 4/2/2020

#Step-1 Create starting variables
#Step-2 Create a while loop that asks the user to enter an expense
#Step-3 Check if the choice equals n if not continue the loop
#Step-4 After the loop show the user the information

# Initialize the variables
choice = ""
expenseNum = 0

# The amount the user starts with in the account
startAmount = int(input('Enter the starting amount: '))
amount = startAmount
 
while choice != "n":
    
    # Enter an expense
    expense = int(input('Enter expense: '))

    # Subtract expense from amount
    amount -= expense

    # Add to the number of expenses
    expenseNum +=1

    choice = input("Do you want to enter another expense? (y/n): ")

    if choice == "n":
        break

    elif choice == "y":
        expense = int(input('Enter expense: '))
        amount -= expense

        expenseNum +=1
        
        choice = input("Do you want to enter another expensse? (y/n): ")

    else:
        print("incorrect statment")


        
print('Amount in account before expense subtraction: $'+ str(startAmount))
print('Number of expenses entered: ' + str(expenseNum))
print('Amount in account after expense subtracted: $'+ str(amount))
