# # Imports
#
import os
import sys
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.style.core import context
import seaborn as sns

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

print(axs.flat)


# # # Section of the course:
# 03. Customizando com Matplotlib
# # #

def plotBrazil(color: str = ''):
    fig, ax = plt.subplots(figsize=(8, 4))
    if color == '':
        ax.plot(brazil.index, brazil['immigrants'], lw=3)
    else:
        ax.plot(brazil.index, brazil['immigrants'], lw=3, color=color)
    ax.set_title('Imigração de Brasileiros para o Canadá\n1980 - 2013', fontsize=18, loc='left')
    ax.set_xlabel('Ano', fontsize=14)
    ax.set_ylabel('Número de imigrantes', fontsize=14)
    ax.xaxis.set_tick_params(labelsize=12)
    ax.yaxis.set_tick_params(labelsize=12)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    plt.grid(linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig

plotBrazil()

# Altering styles
# 
print(plt.style.available)
IPython_default = plt.rcParams.copy()
plt.style.use('fivethirtyeight')
plt.rcParams.update(IPython_default)

# Using 'with' to alter the style once
with context('fivethirtyeight'):
  fig, ax = plt.subplots(figsize=(8, 4))
  ax.plot(brazil.index, brazil['immigrants'], lw=3)
  ax.set_title('Imigração do Brasil para o Canadá\n1980 a 2013', fontsize=20, loc='left')
  ax.set_ylabel('Número de imigrantes', fontsize=14)
  ax.set_xlabel('Ano', fontsize=14)
  ax.yaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_tick_params(labelsize=12)
  ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

# Altering colors
# 
plotBrazil(color='g')

df.head()
south_america = df.query('Região == "América do Sul"')
south_america.head()
south_america_sorted = south_america.sort_values(by='Total', ascending=True)

# Setting different colors for each country
# colors = ['royalblue', 'orange', 'forestgreen', 'orchid', 'purple', 'brown', 'slateblue', 'gray', 'olive', 'navy', 'teal', 'tomato']

# Highlighting Brazil
colors = []
for country in south_america_sorted.index:
    if country == 'Brasil':
        colors.append('green')
    else:
        colors.append('silver')

fig, ax = plt.subplots(figsize=(12, 5))
# ax.barh(south_america.index, south_america['Total'], color=colors) # Not sorted
ax.barh(south_america_sorted.index, south_america_sorted['Total'], color=colors)
ax.set_title('Imigração de sul americanos para o Canadá\n1980 - 2013\n\nBrasil é o 4o país com mais imigrantes', loc='left', fontsize=18)
ax.set_xlabel('Imigrantes', fontsize=14)
ax.set_ylabel('')
ax.xaxis.set_tick_params(labelsize=12)
ax.yaxis.set_tick_params(labelsize=12)

# Adding annotations
for i, v in enumerate(south_america_sorted['Total']):
    ax.text(v + 200, i, str(v), color='black', fontsize=10, ha='left', va='center')
ax.set_frame_on(False)
ax.get_xaxis().set_visible(False)
ax.tick_params(axis='both', which='both', length=0)

south_america_sorted['Total']

# Saving the graphs
print(fig.canvas.get_supported_filetypes())

fig.savefig(f'{outputs_folder}/south_america_immigration.png', transparent=False, dpi=300, bbox_inches='tight')
brazil_immigration = plotBrazil(color='g')
brazil_immigration.savefig(f'{outputs_folder}/brazil_immigration.png', transparent=False, dpi=300, bbox_inches='tight')


# # # Section of the course:
# 04. Conhecendo a biblioteca Seaborn
# # #

sns.set_theme()
top_10 = df.sort_values(by='Total', ascending=False).head(10)

sns.barplot(data=top_10, x=top_10.index, y='Total')
sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h')

# Personalizing views with Seaborn
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h')
ax.set(title='Top 10 países com mais imigrantes no Canadá\n1980 - 2013', xlabel='Imigrantes', ylabel='')
plt.show(ax)

fig, ax = plt.subplots(figsize=(8, 4))
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h')
ax.set_title('Top 10 países com mais imigrantes no Canadá\n1980 - 2013', fontsize=16, loc='left')
ax.set_xlabel('Imigrantes', fontsize=14)
ax.set_ylabel('')
plt.show()

# Altering colors using palettes
def generate_graph_palette(palette):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette=palette, hue=top_10.index, legend=False)
    ax.set_title('Top 10 países com mais imigrantes no Canadá\n1980 - 2013', fontsize=16, loc='left')
    ax.set_xlabel('Imigrantes', fontsize=14)
    ax.set_ylabel('')
    plt.show()

generate_graph_palette('Blues_r')
generate_graph_palette('rocket')
generate_graph_palette('coolwarm')
generate_graph_palette('tab10')

# Other examples
generate_graph_palette('Greens_r')
generate_graph_palette('Reds_r')
generate_graph_palette('Purples_r')
generate_graph_palette('Oranges_r')
generate_graph_palette('Set2')
generate_graph_palette('tab20')
generate_graph_palette('tab20b')

# Exploring themes
# 
# Styles: white, dark, whitegrid, darkgrid, ticks
sns.set_theme(style='ticks')
generate_graph_palette('tab10')

# Removing the frame
fig, ax = plt.subplots(figsize=(8, 4))
ax = sns.barplot(data=top_10, y=top_10.index, x='Total', orient='h', palette='tab10', hue=top_10.index, legend=False)
ax.set_title('Top 10 países com mais imigrantes no Canadá\n1980 - 2013', fontsize=18, loc='left')
ax.set_xlabel('Imigrantes', fontsize=14)
ax.set_ylabel('')
sns.despine()
plt.show()


# # # Section of the course:
# 05. Gráficos interativos com Plotly
# # #