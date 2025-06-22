# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #

# #
# Imports
import os
import sys
import re
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/02-formacao_aprendendo-a-fazer-ETL/01-numpy_analise-numerica-e-eficiente-com-python/'
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