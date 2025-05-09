# # Imports
#
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
from np_load_data import load_data


# # # Section of the course:
# 01. Conhecendo a biblioteca e nossos dados
# # #
try:
    data = load_data('apples_ts.csv', usecols=(1, 88))
except ValueError as e:
    print(e)

# Array dimensions
data.ndim
data.size
data.shape

# Transpose
transposed_data = data.T
transposed_data


# # # Section of the course:
# 02. Exploração dos dados
# # #

# Indexing
dates = transposed_data[:, 0]
dates
prices = transposed_data[:, 1:6]
prices

# Try to plot
# Will return a bug due to wrong type of dates
plt.figure()
plt.plot(dates, prices[:, 0])
plt.show()

# Fix: Naive way, without Pandas
dates = np.arange(1,88)
plt.figure()
plt.plot(dates, prices[:, 0])
plt.show()

# Cities indexes:
Moscow = prices[:, 0]
Kaliningrad = prices[:, 1]
Petersburg = prices[:, 2]
Krasnodar = prices[:, 3]
Ekaterinburg = prices[:, 4]
Moscow
Moscow.shape

Moscow_year1 = Moscow[0:12]
Moscow_year2 = Moscow[12:24]
Moscow_year3 = Moscow[24:36]
Moscow_year4 = Moscow[36:48]

# Plotting as subplots
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(np.arange(1,13),Moscow_year1)
axs[0,1].plot(np.arange(1,13),Moscow_year2)
axs[1,0].plot(np.arange(1,13),Moscow_year3)
axs[1,1].plot(np.arange(1,13),Moscow_year4)
plt.show()

# Plotting together
plt.plot(np.arange(1,13,1),Moscow_year1)
plt.plot(np.arange(1,13,1),Moscow_year2)
plt.plot(np.arange(1,13,1),Moscow_year3)
plt.plot(np.arange(1,13,1),Moscow_year4)
plt.legend(['ano1', 'ano2', 'ano3', 'ano4'])

# Np functions to check if two arrays are equal
Moscow_year1
Moscow_year2
np.array_equal(Moscow_year1, Moscow_year2)
np.allclose(Moscow_year1, Moscow_year2, 0.01)

# # # Study case:
# Testing Rtol
def test_rtol(a, b, rtol):
    allclose = np.allclose(a, b, rtol)
    difference = b - a
    tolerance = b * rtol
    print(f'\na = {a:.8f} || b = {b:.8f} || rtol = {rtol}')
    print('difference = b - a')
    print('tolerance = b * rtol')
    print('\n=> Result:')
    print(f'Tolerance = {tolerance:.8f}')
    print(f'Difference = {difference:.8f}')
    print(f'Allclose = {allclose}')

rtol1 = 0.1
a = 1
# 7 digits
b = 1.1111111
c = 1.1111112
# 8 digits
d = 1.11111111
e = 1.11111112
rtol2 = 0.9
f = 0.99
g = 0.53
h = 0.52
# Rtols of 0.1 captures any difference within the scope of up to 7 digits
test_rtol(a, b, rtol1) # Return True
test_rtol(a, c, rtol1) # Return False
# Loses track of +1 differences after the 8th digit - still captures +2 differences (i.e. a = 1.11111111 || b = 1.11111113 Returns False)
test_rtol(a, d, rtol1) # True
test_rtol(a, e, rtol1) # True

# Rtols of 0.9
# Very loose tolerance
test_rtol(a, g, rtol2) # Return True
test_rtol(f, g, rtol2)
test_rtol(a, h, rtol2) # Return False
test_rtol(f, h, rtol2)

# Rtols > 0.9 always return True for b > 1 > a
test_rtol(f, a, rtol2) # Parameter b = 1 || Parameter a < 1 # Return True
test_rtol(g, a, rtol2)
test_rtol(h, a, rtol2)

# Dealing with NaNs
plt.plot(dates, Kaliningrad) # There's inconsistency in the plot
Kaliningrad # Check for NaNs visually
np.isnan(Kaliningrad) # Returns an array of booleans
sum(np.isnan(Kaliningrad)) # Returns the count of NaNs

# Correcting the NaN throguh interpolation
(Kaliningrad[3]+Kaliningrad[5])/2 # Naive way
np.mean([Kaliningrad[3],Kaliningrad[5]]) # Better way
Kaliningrad[4] = np.mean([Kaliningrad[3],Kaliningrad[5]]) # Interpolate
plt.plot(dates, Kaliningrad) # Now it works correctly

# Comparing Moscow to Kaliningrad
np.mean(Moscow)
np.mean(Kaliningrad) # Moscow is more expensive


# # # Section of the course:
# 03. Operações entre arrays
# # #

# Linear regression
# 
# Calculating through guesses
# Guess
x = dates
y = 2*x + 80 # Guess

plt.plot(dates, Moscow)
plt.plot(x, y)

# Calculating the normalization
np.sqrt(np.sum(np.power(Moscow-y, 2)))
y = 0.52*x + 80 # Guess

np.linalg.norm(Moscow-y)

# Calculating through formula the angular coefficient
n = np.size(Moscow)
x = dates
y = Moscow

a = (n * np.sum(x*y) - np.sum(x)*np.sum(y))/(n*np.sum(x**2) - np.sum(x)**2)
a

# Calculating through formula the linear coefficient
b = np.mean(y) - a*np.mean(x)
b

y = a*x + b
np.linalg.norm(Moscow-y)

# More about regression
plt.plot(dates, Moscow)
plt.plot(x, y)
# Adding a marker to the line in a given x
plt.plot(41.5, 41.5*a+b, '*r')
# Estimating the future price
plt.plot(100, 100*a+b, '*r')

# # #
# 04. Números aleatórios
# # #

# Learning about random numbers
np.random.randint(low=40, high=100, size=100)
angular_coefs = np.random.uniform(low=0.10, high=0.90, size=100)
# Calculate the norm for each of the numbers
norm = np.array([])
for i in range(100):
    norm = np.append(norm, np.linalg.norm(Moscow-(angular_coefs[i]*x+b)))
print(norm)
# Find the minimum
min_value = np.min(norm)
print(min_value)
index = np.where(norm == min_value)
print(index)
print(angular_coefs[index][0])

# Functionalizing
def random_grid_search(
        x,
        y,
        linear_coef_low_high,
        angular_coef_low_high,
        norm=None,
        refinements=300,
        improve=True
        ):
    '''
    Calculates the linear regression of a given dataset based on random linear and angular coefficients.

    Parameters
    ----------
    `x` : array_like
        The x-axis data.
    `y` : array_like
        The y-axis data.
    `linear_coef_low_high` : tuple
        The guessed lower and upper bounds for the linear coefficient.
    `angular_coef_low_high` : tuple
        The guessed lower and upper bounds for the angular coefficient.
    `improve` : bool, optional. Default True.
        Whether to improve the regression or not.
    `refinements` : int, optional. Default 300.
        The number of refinements to perform when improving the regression.  
        Minimum value is 300.  
        Maximum value is 1000.  
        Values outside this range will be rounded to the nearest valid value.
    `norm` : float, optional. Default None.
        A guess of the norm of the regression. Can be provided in order to improve performace.  

        ***WARNING***:  
        Providing a lower value than the actual norm will lead to wrong results. If you are not sure, do not provide any guess.

    Returns
    -------
    `linear_coef` : float
        The linear coefficient of the regression.
    `angular_coef` : float
        The angular coefficient of the regression.
    `norm` : float
        The norm of the regression.
    '''
    refinements = 300 if refinements < 300 else refinements
    refinements = 1000 if refinements > 1000 else refinements
    iterate = True
    i = 0
    while iterate:
        linear_coefs = np.random.uniform(low=linear_coef_low_high[0], high=linear_coef_low_high[1], size=100)
        angular_coefs = np.random.uniform(low=angular_coef_low_high[0], high=angular_coef_low_high[1], size=100)

        norms = np.array([
            np.linalg.norm(y - (angular * x + linear))
            for angular in angular_coefs
            for linear in linear_coefs
        ])

        # Reshape norms to 2D (angular_coefs x linear_coefs)
        norms = norms.reshape(len(angular_coefs), len(linear_coefs))

        current_best_norm = np.min(norms)
        if norm is None or current_best_norm < norm:
            norm = current_best_norm
            i += 1
            iterate = True if i < 1000 else False
        else:
            iterate = False

    # Get index of best angular and linear
    i, j = np.unravel_index(np.argmin(norms), norms.shape)
    angular_coef = angular_coefs[i]
    linear_coef = linear_coefs[j]

    def improve_regression(x, y, norm, max_iter=refinements):
        print(f'Refinement {max_iter}')
        if max_iter == 0:
            return
        else:
            random_grid_search(x, y, linear_coef_low_high, angular_coef_low_high, norm, improve=False)
            return improve_regression(x, y, norm, max_iter - 1)

    if improve:
        improve_regression(x, y, norm)

    return angular_coef, linear_coef, norm

def test():
    angular_coef, linear_coef, norm = random_grid_search(
        dates,
        Moscow,
        linear_coef_low_high=(75, 85),
        angular_coef_low_high=(0.10, 0.90),
        refinements=500
        )
    print(f'a = {a} || b = {b} || norm = {np.linalg.norm(Moscow-y)}')
    print(f'Best angular coefficient: {angular_coef}')
    print(f'Best linear coefficient: {linear_coef}')
    print(f'Best norm: {norm}')

# # Reproductibility
# 
np.random.randint(low=40, high=100, size=100)

np.random.seed(84)
angular_coefs = np.random.uniform(low=0.10, high=0.90, size=100)
norm = np.array([])
for i in range(100):
    norm = np.append(norm, np.linalg.norm(Moscow-(angular_coefs[i]*x+b)))
print(angular_coefs)
print(norm)

# Homework: Applying numpy to improve performance
# Original function:
x = [0,1,2,3,4,5,6,7,8,9,10]
y = []

for i in x:
  y.append(i + 3 / 2)
print(y)

# Using numpy to approach the for loop
x = np.array(x)
y = np.array([])
for i in x:
    y = np.append(y, i + 3 / 2)
print(y)

#  Using built-in optimized np function to approach the for loop
x = np.array(x)
y = np.add(x, 3 / 2)
print(y)

