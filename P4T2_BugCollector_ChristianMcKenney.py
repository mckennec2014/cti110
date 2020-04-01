# This program asks the user to enter the number of bugs collected on different
# days and gives the total.

# CTI-110 P4T2 - Bug Collector
# Christian McKenney
# 4/1/2020

#Step-1 Initialize the variable.
#Step-2 Create a for loop that keeps asking the user to enter the number of bugs
#Step-3 Add bugs to total.
#Step-4 Display the total bugs.

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 6):
  print('Enter the bugs collected on day', day)
  bugs = int(input())
  total += bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
  
  
