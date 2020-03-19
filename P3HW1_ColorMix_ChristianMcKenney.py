# CTI-110
# P3HW1 - Color Mixer
# Christian McKenney
# 3/17/2020


#Step-1 Enter the first primary color
#Step-2 Check if it's valid
#Step-3 Enter the second primary color
#Step-4 Check if it's valid
#Step-5 Check for combinations of colors and display that color


# Get user input
color1 = input('Enter the first primary color: ')


if color1 == "red" or color1 == "blue" or color1 == "yellow":
      color2 = input('Enter the second primary color: ')
      if color2 == "red" or color2 == "blue" or color2 == "yellow":
          if color1 == "red" and color2 == "blue": 
            print('These colors make purple')


          if color1 == "red" and color2 == "yellow":
            print('These colors make orange')


   
          if color1 == "blue" and color2 == "yellow":
            print('These colors make green')

      else:
          print('Invalid input')
else:
    print('Invalid input')




















    
