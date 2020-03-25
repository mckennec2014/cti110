# CTI-110
# P3LAB - Debugging
# Christian McKenney 
# 3/24/2020

#Step-1 Give score a variable and define the score
#Step-2 Initialize score A-D
#Step-3 Compare the scores
#Step-4 Display your grade

score = int(input('What is the score? '))
            
A_score = 90
B_score = 80
C_score = 70
D_score = 60

if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')
