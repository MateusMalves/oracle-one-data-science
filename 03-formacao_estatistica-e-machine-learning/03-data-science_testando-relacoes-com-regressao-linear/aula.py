# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import os
import sys
import re
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data
from label_plots import label_plot

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/03-data-science_testando-relacoes-com-regressao-linear'
outputs_folder = data_folder + 'outputs/'

# # # Section of the course:
# 01. Ajustando uma reta
# # #

data = load_data(f'{data_folder}/Preços_de_casas.csv', is_pandas=True)
data.drop(columns = "Id", inplace=True)

corr = data.corr()
corr['preco_de_venda']

# Mão na massa: Plotting a correlation heatmap
# 
def plot_corr_heatmap(corr):
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Configure a matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Generate heatmap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .5})

plot_corr_heatmap(corr)

# Plotting a dispersion plot
plt.scatter(data['area_primeiro_andar'], data['preco_de_venda'])
plt.axline(xy1=(66,250000), xy2=(190,1700000), color='red')
label_plot(title='Relation Price vs Area', xlabel='Area 1st floor', ylabel='Price')

# Obtaining the best line
px.scatter(data, x='area_primeiro_andar', y='preco_de_venda', trendline_color_override='red', trendline='ols')

# # # Section of the course:
# 02. Explicando a reta
# # #



# # # Section of the course:
# 03. Adicionando outros fatores
# # #

# # # Section of the course:
# 04. Precificando as casas
# # #

# # # Section of the course:
# 05. Investigando nosso modelo
# # #