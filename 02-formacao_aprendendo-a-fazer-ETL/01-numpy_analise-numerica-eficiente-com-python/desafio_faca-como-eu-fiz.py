# Import
import numpy as np
import os

# Load data
file_path = os.path.join(os.getcwd(), '02-formacao_aprendendo-a-fazer-ETL/data', 'citrus.csv') # Path relative to the root directory
data = np.loadtxt(file_path, delimiter=',', skiprows=1, usecols=np.arange(1, 6))
transposed_data = data.T
data[0]
transposed_data[0]
data.shape