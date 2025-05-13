# Import
import os
import sys
import re

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/01-numpy_analise-numerica-e-eficiente-com-python/'

# Load data
data = load_data(data_folder + 'citrus.csv', usecols=(1, 6), skiprows=1)
transposed_data = data.T
transposed_data[0]
transposed_data.shape