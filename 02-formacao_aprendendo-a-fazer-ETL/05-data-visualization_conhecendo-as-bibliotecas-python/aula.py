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

data_folder = cwd + '/data/05-data-visualization_conhecendo-as-bibliotecas-python/'
outputs_folder = data_folder + 'outputs/'

# # Data Visualization: criando gráficos com as bibliotecas Python
# 

# # # Section of the course:
# 01. Conhecendo a biblioteca Matplotlib
# # #


# # # Section of the course:
# 02. Criando figuras com Matplotlib
# # #


# # # Section of the course:
# 03. Customizando com Matplotlib
# # #


# # # Section of the course:
# 04. Conhecendo a biblioteca Seaborn
# # #


# # # Section of the course:
# 05. Gráficos interativos com Plotly
# # #