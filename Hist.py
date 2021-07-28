# HISTOGRAM
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the lists for X and Y
His= pd.read_csv('Pytho.csv')
print(His.head(3))
bins = [10,20,30,40,50,60,70,80]

# Plot the data using hist() method
plt.hist(His.DeliveryTime, bins=bins, color='#006666')
plt.xticks(bins)
plt.ylabel("Number of People")
plt.xlabel("Delivery Time")
plt.title('Acceptable Delivery Time by people when ordering Food online')

# Show the plot
plt.show()