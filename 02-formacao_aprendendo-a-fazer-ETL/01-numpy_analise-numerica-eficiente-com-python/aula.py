# # Imports
#
import os
import re
import numpy as np
import matplotlib.pyplot as plt


# # # Section of the course:
# 01. Conhecendo a biblioteca e nossos dados
# # #

# # Load data
def load_data(filename):
    # Format paths to access from both the root directory and '/02-formacao_aprendendo-a-fazer-ETL/01-numpy_analise-numerica-eficiente-com-python'
    cwd = os.getcwd()
    if not bool(re.search(r'\d-', cwd)):
        # From root
        datasets_folder = cwd
        datasets_folder += '/02-formacao_aprendendo-a-fazer-ETL/data'   
    else:
        # From '/02-formacao_aprendendo-a-fazer-ETL/01-numpy_analise-numerica-eficiente-com-python'
        datasets_folder = os.path.dirname(cwd)
        datasets_folder += '/data'

    file_path = os.path.join(datasets_folder, filename) # Path relative to the root directory
    data = np.loadtxt(file_path, delimiter=',', usecols=np.arange(1, 88))
    print(data[0])
    print('length =', len(data))

    return data

data = load_data('apples_ts.csv')

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


# # #
# 04. Números aleatórios
# # #
