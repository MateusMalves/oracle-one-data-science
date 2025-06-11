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

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/06-IA-aplicada-a-data-science/'
outputs_folder = data_folder + 'outputs/'

data_customers = load_data(data_folder + 'zoop_clientes.csv', is_pandas=True)
data_sales = load_data(data_folder + 'zoop_vendas.csv', is_pandas=True)

data_customers.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
data_customers['cidade'] = data_customers['cidade'].astype('category')
data_customers['uf'] = data_customers['uf'].astype('category')
data_customers['regiao'] = data_customers['regiao'].astype('category')
data_customers['sexo'] = data_customers['sexo'].astype('category')
data_customers['cashback'] = data_customers['cashback'].apply(lambda x: True if x == 'Sim' else False)

data_sales.rename(columns={'preco_unitario': 'preco'}, inplace=True)
data_sales['data'] = pd.to_datetime(data_sales['data'])
data_sales['categoria'] = data_sales['categoria'].astype('category')
data_sales['metodo_pagamento'] = data_sales['metodo_pagamento'].astype('category')


# Use GPT to generate a explore the data (portuguese outputs)
# 
# Expore data_customers DataFrame

# Exibir as primeiras linhas para ter uma visão geral dos dados
data_customers.head()

# Verificar o tamanho do DataFrame (número de linhas e colunas)
data_customers.shape

# Verificar os tipos de dados e valores nulos
data_customers.info()

# Obter estatísticas descritivas para colunas numéricas
data_customers.describe()

# Contagem de valores únicos por coluna categórica
data_customers['sexo'].value_counts()
data_customers['regiao'].value_counts()
data_customers['uf'].value_counts()
data_customers['cidade'].nunique()

# Verificar distribuição de idade
data_customers['idade'].describe()

# Verificar média de avaliação da compra
data_customers['avaliacao_compra'].mean()

# Verificar quantos participam do programa de cashback
data_customers['cashback'].value_counts(normalize=True)

# Verificar a quantidade de data_customers por faixa etária
bins = [0, 17, 25, 35, 45, 60, 100]
labels = ['0-17', '18-25', '26-35', '36-45', '46-60', '60+']
data_customers['faixa_etaria'] = pd.cut(data_customers['idade'], bins=bins, labels=labels)
data_customers['faixa_etaria'].value_counts().sort_index()

# Avaliação média por sexo
data_customers.groupby('sexo')['avaliacao_compra'].mean()

# Avaliação média por participação no cashback
data_customers.groupby('cashback')['avaliacao_compra'].mean()