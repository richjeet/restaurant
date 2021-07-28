# SCATTER PLOT
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Initialize the lists for X and Y
sp = pd.read_csv('ScatterPlot.csv')
print(sp.head())
Food= sp['MonthlyExpenseFood']
Grocery= sp['MonthlyExpenseGrocery']
ratio = sp['Ratio']

# Plot the data using scatter() method
plt.scatter(Food, Grocery, c= ratio, cmap= 'rainbow', edgecolor= 'black', linewidth= 1, alpha= 0.75)
plt.xscale('log')
plt.yscale('log')
cbar = plt.colorbar()
cbar.set_label('Food/Grocery Ratio')
plt.title('Food & Grocery Expenses Pattern', fontdict={'fontname':'Comic Sans MS' , 'fontsize': 15})
plt.xlabel('Monthly Expenses on Food (in $)')
plt.ylabel('Monthly Expenses on Grocery (in $)')
plt.tight_layout()

# Show the plot
plt.show()