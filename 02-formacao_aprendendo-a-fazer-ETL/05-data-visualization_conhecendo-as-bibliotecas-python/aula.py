# # Imports
#
import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

# # # Section of the course:
# 02. Criando figuras com Matplotlib
# # #

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(brazil.index, brazil['immigrants'])
ax.set_title('Imigração de Brasileiros para o Canadá\n1980 - 2013')
ax.set_xlabel('Ano')
ax.set_ylabel('Número de imigrantes')
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

# Creating subplots in one direction
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
axs[0].plot(brazil.index, brazil['immigrants'])
axs[0].set_title('Imigração de Brasileiros para o Canadá\n1980 - 2013')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Número de imigrantes')
axs[0].xaxis.set_major_locator(ticker.MultipleLocator(5))
axs[0].grid()

axs[1].boxplot(brazil['immigrants'])
axs[1].set_title('Boxplot da imigração de Brasileiros para o Canadá\n1980 - 2013')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número de imigrantes')
axs[1].grid()

brazil.describe()

# Creating subplots in two directions
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Imigração de sul americanos para o Canadá\n1980 - 2013')

axs[0, 0].plot(df.loc['Brasil'].loc[years])
axs[0, 0].set_title('Brasil')

axs[0, 1].plot(df.loc['Colômbia'].loc[years])
axs[0, 1].set_title('Colômbia')

axs[1, 0].plot(df.loc['Argentina'].loc[years])
axs[1, 0].set_title('Argentina')

axs[1, 1].plot(df.loc['Peru'].loc[years])
axs[1, 1].set_title('Peru')

for ax in axs.flat:
    ax.set(xlabel='Ano', ylabel='Imigrantes')
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1000))

ymin = 0
ymax = 7000
for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)
    ax.grid()

# # # Section of the course:
# 03. Customizando com Matplotlib
# # #


# # # Section of the course:
# 04. Conhecendo a biblioteca Seaborn
# # #


# # # Section of the course:
# 05. Gráficos interativos com Plotly
# # #