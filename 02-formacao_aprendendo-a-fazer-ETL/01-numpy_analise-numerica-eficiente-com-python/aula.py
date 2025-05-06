# # Imports
#
import os
import re
import numpy as np

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

# Indexing
dates = transposed_data[:, 0]
dates
prices = transposed_data[:, 1:6]
prices