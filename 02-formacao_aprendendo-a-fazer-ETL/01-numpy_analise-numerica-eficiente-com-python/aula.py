# # Imports
#
import numpy as np
import os

# Load data
file_path = os.path.join(os.getcwd(), '02-formacao_aprendendo-a-fazer-ETL/01-numpy_analise-numerica-eficiente-com-python/data', 'apples_ts.csv') # Path relative to the root directory
data = np.loadtxt(file_path, delimiter=',', skiprows=1, usecols=np.arange(1, 87))
print(data)
len(data)