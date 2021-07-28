# BARPLOT
# Import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the lists for X and Y
data = pd.read_csv('BarPlot.csv')

df = pd.DataFrame(data)

print(df.head())

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.figure(figsize=(10,7))

# Plot the data using bar() method
plt.bar(X, Y, color='#996666')

plt.title('Food Preferences based on Religious Diversity', fontdict={'fontname':'Comic Sans MS', 'fontsize': 15})

plt.xlabel("Religion")
plt.ylabel("Number of Followers")

# Show the plot
plt.show()