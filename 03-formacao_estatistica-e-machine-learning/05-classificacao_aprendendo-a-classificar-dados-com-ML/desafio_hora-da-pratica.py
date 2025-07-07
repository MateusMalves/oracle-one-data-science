# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# Case aula 1
# Enunciado do desafio
'''
1 - A primeira etapa em um projeto de Machine Learning é a obtenção de dados. A partir dessa obtenção, podemos fazer a leitura dos dados para se construir um modelo. Como tarefa inicial, faça a leitura da base de dados e verifique a presença de dados nulos. Além disso, remova a coluna 'id_cliente', uma vez que esse tipo de informação única para cada linha não é útil para uso em modelos de machine learning.

2 - Após a leitura dos dados, é importante conhecer os dados, checando inconsistências e entendendo o comportamento de cada uma das colunas. Nesta tarefa, faça uma análise exploratória utilizando gráficos para as variáveis categóricas da base de dados, incluindo a variável alvo churn. Para essas variáveis, pode ser utilizado gráficos de barras para fazer a contagem das categorias e fazer um agrupamento por cores de acordo com as categorias da variável alvo.

3 - Depois de explorar as variáveis categóricas, chegou a vez das variáveis numéricas. Construa gráficos de distribuição como boxplots ou histogramas para analisar o comportamento dos valores numéricos e checar se existem valores inconsistentes.
'''

# #
# Imports
import os
import sys
import re
import plotly.express as px

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/05-classificacao_aprendendo-a-classificar-dados-com-ML'
outputs_folder = data_folder + 'outputs/'

# Import data
data = load_data(f'{data_folder}/churn.csv', is_pandas=True)
data.drop(columns=['id_cliente'], inplace=True)
data.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
data.info()

# Fix categorical columns
data['tem_cartao_credito'] = data['tem_cartao_credito'].astype('category')
data['membro_ativo'] = data['membro_ativo'].astype('category')

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

plot_histogram(data, 'churn', 'Histograma do Churn')
columns_categorical = [col for col in columns if data[col].dtype == 'object' or data[col].dtype.name == 'category']
for col in columns_categorical:
    plot_histogram(data, col, f'Histogram: {col}', 'churn')

# Plotting numerics
def plot_boxplot(df, column, title, color=None):
    if color:
        return px.box(df, x=column, title=title, color=color).show()
    return px.box(df, x=column, title=title).show()

columns_numerics = [col for col in columns if data[col].dtype != 'object' and col != 'churn' and data[col].dtype.name != 'category']
for col in columns_numerics:
    plot_boxplot(data, col, f'Boxplot: {col}', 'churn')