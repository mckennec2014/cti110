# This program calculates the predicted sales.
# 2/20/2020
# CTI-110 P2T1 - Sales Prediction
# Christian McKenney

# Gets the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculates the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Displays the profit.
print('The profit is $', format(profit, ',.2f'))
