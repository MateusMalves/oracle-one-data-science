# # Imports
#
import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

# # Pandas I/O
# 
# Reading
data_folder = cwd + '/data/03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/'

data = load_data('03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/superstore_data.csv', is_pandas=True)
data_semicolon = load_data('03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/superstore_data_ponto_virgula.csv', delimiter=';', is_pandas=True)

data_first_lines = pd.read_csv(data_folder + 'superstore_data.csv', nrows=5)
data_first_lines

data_selection = pd.read_csv(data_folder + 'superstore_data.csv', usecols=['Id', 'Year_Birth', 'Income'])
data_selection

data_selection = pd.read_csv(data_folder + 'superstore_data.csv', usecols=[0, 1, 4])
data_selection

# Saving
data_selection.to_csv(data_folder + 'customers_market.csv')

customers_market = pd.read_csv(data_folder + 'customers_market.csv')
customers_market

# Fixing index
data_selection.to_csv(data_folder + 'customers_market.csv', index=False)

customers_market = pd.read_csv(data_folder + 'customers_market.csv')
customers_market