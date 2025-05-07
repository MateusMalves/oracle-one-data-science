import os
import sys
import re

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(f'{cwd}/02-formacao_aprendendo-a-fazer-ETL')
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data
    

data = load_data('citrus.csv', usecols=(1, 6), skiprows=1)