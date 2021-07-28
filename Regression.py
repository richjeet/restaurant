# REGRESSION
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

# Initialize the lists for X and Y
sp = pd.read_csv('ScatterPlot.csv')
print(sp.head())
Food= sp['MonthlyExpenseFood']
Grocery= sp['MonthlyExpenseGrocery']

# Plot the data using scatter() method
plt.scatter(Food, Grocery, edgecolor= 'green', linewidth= 1, alpha= 0.75)
m, b = np.polyfit(Food, Grocery, 1)
plt.plot(Food, m*Food+b, color='red')
plt.title('Food & Grocery Expenses REGRESSION Pattern', fontdict={'fontname':'Comic Sans MS' , 'fontsize': 15})
plt.xlabel('Monthly Expenses on Food (in $)')
plt.ylabel('Monthly Expenses on Grocery (in $)')
plt.tight_layout()

# Show the plot
plt.show()