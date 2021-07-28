# REGRESSION
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

# Initialize the lists for X and Y
Zahra = pd.read_csv('ND.csv')
print(Zahra.head())
Food= Zahra['COSTOFFOOD']
Beverage= Zahra['BeverageDessertCost']

# Plot the data using scatter() method
plt.scatter(Food, Beverage, edgecolor= 'blue', linewidth= 1, alpha= 0.75)

m, b = np.polyfit(Food, Beverage, 1)
plt.plot(Food, m*Food+b, color='red')
plt.title('Food & Beverage Expenses REGRESSION Pattern', fontdict={'fontname':'Comic Sans MS' , 'fontsize': 15})
plt.xlabel('Expenses on Food (in $)')
plt.ylabel('Expenses on Beverage & Dessert (in $)')
plt.tight_layout()

# Show the plot
plt.show()