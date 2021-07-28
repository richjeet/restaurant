# PIE CHART
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the lists for X and Y
df = pd.read_csv('PieChart.csv')
print(df.head())
plt.rcParams['font.size'] = 11.0
Portal_data = df['OrderPortal']
PastOrder_data = df['PastMonthOrder']
colors = ["#555555", "#698b69", "#b8860b", "#8b4726"]
explode = (0.1, 0, 0, 0)

# Plot the data using pie() method
plt.pie(PastOrder_data, labels=Portal_data, explode= explode, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
plt.title(" Most Popular Online Portal for Food Delivery/Takeout", fontdict={'fontname':'Comic Sans MS' , 'fontsize': 15})

# Show the plot
plt.show()