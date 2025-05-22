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

data_folder = cwd + '/data/04-pandas_transformacao-e-manipulacao-de-dados/'
outputs_folder = data_folder + 'outputs/'

# # Pandas: transformação e manipulação de dados
# 

# # # Section of the course:
# 01. Entendendo o problema
# # #

# # # Section of the course:
# 02. Dados numéricos
# # #

# # # Section of the course:
# 03. Dados textuais
# # #

# # # Section of the course:
# 04. Dados de tempo
# # #