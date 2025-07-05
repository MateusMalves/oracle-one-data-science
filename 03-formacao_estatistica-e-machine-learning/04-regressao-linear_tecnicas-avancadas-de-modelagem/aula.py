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

# Behaviour of the Dependent Variable (Y)
sns.set_palette('Accent')
sns.set_style('darkgrid')

plt.figure(figsize=(20, 5))
sns.boxplot(data=data, x='Valor', orient='h', width=0.3)
label_plot(title='Valor', xlabel='Reais', fontsizes='large')
plot_central_tendency(column=data['Valor'])

# Frequency distribution
plt.figure(figsize=(20, 6))
sns.histplot(list(data['Valor']), kde=True, color='green')
label_plot(title='Distribuição de Frequências', xlabel='Preço dos Imóveis (R$)', fontsizes='large')
plot_central_tendency(column=data['Valor'])

# Dispersion between variables
plt.suptitle('Dispersão entre variáveis', fontsize=20, y=1.05)
sns.pairplot(data=data, y_vars='Valor', x_vars=['Area', 'Dist_Praia', 'Dist_Farmacia'], height=5, kind='reg')


# # # Section of the course:
# 03. Transformação de variáveis
# # #

np.log(1) # Returns 0
np.log(0) # Returns -inf

def add_log(data: pd.DataFrame, columns_with_zeros: list[str])-> None:
    columns = list(data.columns)
    for column in columns:
        if not column in columns_with_zeros:
            data[f'log_{column}'] = np.log(data[column])
        else:
            data[f'log_{column}'] = np.log(data[column] + 1)

add_log(data, columns_with_zeros=['Dist_Praia', 'Dist_Farmacia'])
data.head()

plt.figure(figsize=(20, 6))
sns.histplot(list(data['log_Valor']), kde=True, color='green')
label_plot(title='Distribuição de Frequências', xlabel='log do Preço dos Imóveis', fontsizes='large')
plot_central_tendency(column=data['log_Valor'])


# Verifying linear relation
sns.pairplot(data=data, y_vars='log_Valor', x_vars=['log_Area', 'log_Dist_Praia', 'log_Dist_Farmacia'], height=5, kind='reg')


# # # Section of the course:
# 04. Regressão linear com Statsmodels
# # #


# # # Section of the course:
# 05. Regressão linear com Scikit-learn
# # #