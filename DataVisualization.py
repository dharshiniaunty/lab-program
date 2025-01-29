import matplotlib.pyplot as plt
import pandas as pd

# Reading the tips.csv file
data = pd.read_csv('beauty.csv')

# initializing the data
x = data['PRODUCT']
y = data['SALES']

# plotting the data
plt.bar(x, y)

# Adding title to the plot
plt.title("Beauty Products")

# Adding label on the y-axis
plt.ylabel('SALES')

# Adding label on the x-axis
plt.xlabel('PRODUCT')

plt.show()
