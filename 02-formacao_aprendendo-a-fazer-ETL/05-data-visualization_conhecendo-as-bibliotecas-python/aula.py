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

data_folder = cwd + '/data/05-data-visualization_conhecendo-as-bibliotecas-python/'
outputs_folder = data_folder + 'outputs/'

# # Data Visualization: criando gráficos com as bibliotecas Python
# 

# # # Section of the course:
# 01. Conhecendo a biblioteca Matplotlib
# # #

df = load_data(f'{data_folder}/imigrantes_canada.csv', is_pandas=True)
df.info()

df.set_index('País', inplace=True)
years = list(map(str, range(1980, 2014)))
brazil = df.loc[['Brasil'], years]
brazil = brazil.T
brazil.rename(columns={'Brasil': 'immigrants'}, inplace=True)
brazil.columns.name = 'year'

plt.figure(figsize=(8, 4))
plt.plot(brazil.index, brazil['immigrants'])
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.yticks([500, 1000, 1500, 2000, 2500, 3000])
plt.title('Imigração de Brasileiros para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')

# Change index label from "Pais" to "year'


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