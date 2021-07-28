# BOX PLOT
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('default')

# Initialize the lists for X and Y
box = pd.read_csv('BoxPlot.csv', sep=',',na_values='.')
print(box.head(3))

# Plot the data using boxplot() method
boxes = box.boxplot(column=['MonthlyExpenses'], by='DietType',figsize=(5,7), grid=True)
plt.title("Diet Type Comparison", fontdict={'fontname':'Comic Sans MS' , 'fontsize': 15})
plt.ylabel('Monthly Expenses')

# Show the plot
plt.show()