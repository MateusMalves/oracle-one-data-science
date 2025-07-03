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
import matplotlib.pyplot as plt
import plotly.express as px

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data
from plot_utils import label_plot, plot_central_tendency

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/04-regressao-linear_tecnicas-avancadas-de-modelagem/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Análises Preliminares
# # #
data = load_data(f'{data_folder}dataset.csv', is_pandas=True, delimiter=';')
data.head()

# Descriptive analysis
# 
# Descriptive statistics
data.describe().round(2)

# Correlation analysis
corr = data.corr().round(4)
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)


# # # Section of the course:
# 02. Análises gráficas
# # #


# # # Section of the course:
# 03. Transformação de variáveis
# # #


# # # Section of the course:
# 04. Regressão linear com Statsmodels
# # #


# # # Section of the course:
# 05. Regressão linear com Scikit-learn
# # #