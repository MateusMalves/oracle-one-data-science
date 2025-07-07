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
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/05-classificacao_aprendendo-a-classificar-dados-com-ML/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Análise exploratória
# # #
data = load_data(f'{data_folder}marketing_investimento.csv', is_pandas=True)
data.info()

# Exploring uniques
def get_uniques(df, col):
    uniques = df[col].unique()
    uniques.sort()
    return uniques

columns = list(data.columns)
for col in columns:
    print(f'=> {col}:\n{get_uniques(data, col)}\n\n')

# Plotting categoricals
def plot_histogram(df, col, title, color=None):
    if color:
        return px.histogram(df, x=col, text_auto=True, title=title, color=color, barmode='group').show()
    else:
        return px.histogram(df, x=col, text_auto=True, title=title).show()

plot_histogram(data, 'aderencia_investimento', 'Aderência ao investimento')
plot_histogram(data, 'estado_civil', 'Estado civil', color='aderencia_investimento')
plot_histogram(data, 'escolaridade', 'Escolaridade', color='aderencia_investimento')
plot_histogram(data, 'inadimplencia', 'Inadimplência', color='aderencia_investimento')
plot_histogram(data, 'fez_emprestimo', 'Fez Empréstimo', color='aderencia_investimento')

# Plotting numerics
def plot_boxplot(df, column, title, color=None):
    if color:
        return px.box(df, x=column, title=title, color=color).show()
    return px.box(df, x=column, title=title).show()

plot_boxplot(data, 'idade', 'Distribuição da Idade', color='aderencia_investimento')
plot_boxplot(data, 'saldo', 'Distribuição do Saldo', color='aderencia_investimento')
plot_boxplot(data, 'tempo_ult_contato', 'Distribuição do Tempo de Último Contato', color='aderencia_investimento')
plot_boxplot(data, 'numero_contatos', 'Distribuição do Número de Contatos', color='aderencia_investimento')

# # No inconsistencies found in the data


# # # Section of the course:
# 02. Transformação de dados
# # #


# # # Section of the course:
# 03. Ajustando modelos
# # #


# # # Section of the course:
# 04. Seleção de modelos
# # #