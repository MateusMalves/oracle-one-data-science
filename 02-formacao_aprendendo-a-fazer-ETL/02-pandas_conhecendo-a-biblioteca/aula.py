# # Imports
#
import os
import sys
import re
import pandas as pd

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data


# # # Section of the course:
# 01. Conhecendo a base de dados
# # #

# Importing data
data = load_data('aluguel.csv', delimiter=';', is_pandas=True)
data
data.head()
data.head(10)
data.tail()
type(data)