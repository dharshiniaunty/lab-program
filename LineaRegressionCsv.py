import numpy as np
import csv 
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Salary_dataset.csv')
x=df['YearsExperience'].values
y=df['Salary'].values

def single_linear(x, y):
    if len(x) != len(y):
        raise ValueError("The lengths of x and y must be the same.")
    n = len(x)  
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator = sum((x[i] - mean_x) ** 2 for i in range(n))
    b1 = numerator / denominator
    b0 = mean_y - b1 * mean_x
    return b0, b1

def plot(x, y, b0, b1):
    plt.scatter(x, y, color = "m",marker = "o", s = 30)
    plt.xlabel('x')
    plt.ylabel('y')
  
intercept, slope = single_linear(x, y)
print(f"Intercept (b0): {intercept}")
print(f"Slope (b1): {slope}")
x1 = float(input("Enter x value: "))
y_pred = intercept + slope * x1
print (y_pred)
plot(x,y,intercept,slope)
plt.scatter(x1, y_pred, color = "g",marker = "*", s = 160)
plt.show()
