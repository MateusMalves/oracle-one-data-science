import os
import sys
import re
import numpy as np
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/01-numpy_analise-numerica-e-eficiente-com-python/'
data = load_data(data_folder + 'citrus.csv', usecols=(1, 6), skiprows=1)

# Generate the arrays
diameter_orange = data[:5000, 0]
weight_orange = data[:5000, 1]
diameter_grapefruit = data[5000:, 0]
weight_grapefruit = data[5000:, 1]

# # Plotting
# 

# Using subplots
fig, axs = plt.subplots(1, 2)
axs[0].plot(diameter_orange, weight_orange)
axs[0].set_title('Orange')
axs[1].plot(diameter_grapefruit, weight_grapefruit)
axs[1].set_title('Grapefruit')
plt.xlabel('Diameter')
plt.ylabel('Weight')
plt.show()

# Using a single plot
plt.plot(diameter_orange, weight_orange)
plt.plot(diameter_grapefruit, weight_grapefruit)
plt.xlabel('Diameter')
plt.ylabel('Weight')
plt.legend(['Orange', 'Grapefruit'])

def linear_regression(x, y):
    n = np.size(x)
    a = (n * np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2)
    b = np.mean(y) - a*np.mean(x)
    return a, b

def predict(x, a, b):
    y = a*x + b
    return y

a_orange, b_orange = linear_regression(diameter_orange, weight_orange)
a_grapefruit, b_grapefruit = linear_regression(diameter_grapefruit, weight_grapefruit)

predicted_weight_orange = predict(diameter_orange, a_orange, b_orange)
predicted_weight_grapefruit = predict(diameter_grapefruit, a_grapefruit, b_grapefruit)

# Checking the norm
print(f'Norm of orange: {np.linalg.norm(weight_orange - predicted_weight_orange):.2f}')
print(f'Norm of grapefruit: {np.linalg.norm(weight_grapefruit - predicted_weight_grapefruit):.2f}')

# Plotting the data
plt.plot(diameter_orange, weight_orange)
plt.plot(diameter_orange, predicted_weight_orange)
plt.plot(diameter_grapefruit, weight_grapefruit)
plt.plot(diameter_grapefruit, predicted_weight_grapefruit)