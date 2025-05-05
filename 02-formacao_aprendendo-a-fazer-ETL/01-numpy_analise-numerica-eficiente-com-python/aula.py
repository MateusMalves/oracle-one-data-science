# # Imports
#
import numpy as np
import os

# Load data
file_path = os.path.join(os.getcwd(), '02-formacao_aprendendo-a-fazer-ETL/data', 'apples_ts.csv') # Path relative to the root directory
data = np.loadtxt(file_path, delimiter=',', usecols=np.arange(1, 88))
print(data)
len(data)

# Array dimensions
data.ndim
data.size
data.shape

# Transpose
transposed_data = data.T
transposed_data

