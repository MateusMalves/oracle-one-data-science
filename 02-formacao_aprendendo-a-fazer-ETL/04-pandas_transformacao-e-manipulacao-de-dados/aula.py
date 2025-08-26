
# # Imports
#
import os
import sys
import re
import numpy as np
import pandas as pd

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)

data_folder = cwd + '/data/02-formacao_aprendendo-a-fazer-ETL/04-pandas_transformacao-e-manipulacao-de-dados/'
outputs_folder = data_folder + 'outputs/'

# # Pandas: transformação e manipulação de dados
# 

# # # Section of the course:
# 01. Entendendo o problema

data = pd.read_json(data_folder + 'dados_hospedagem.json')
data = pd.json_normalize(data['info_moveis'].tolist())
data.head()

# # # Section of the course:
# 02. Dados numéricos

# Extracting from the lists
columns = list(data.columns)
print(columns)
data = data.explode(columns[3:])
data.reset_index(drop=True, inplace=True)
data.head()

# Converting numeric data
data.info()
data['max_hospedes'] = data['max_hospedes'].astype(np.int64)

col_numeric = ['quantidade_banheiros', 'quantidade_camas', 'quantidade_quartos']
data[col_numeric] = data[col_numeric].astype(np.int64)

data['avaliacao_geral'] = data['avaliacao_geral'].astype(np.float64)
data.info()

# Numbers in strings
data['preco']
data['preco'] = data['preco'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
data['preco'] = data['preco'].astype(np.float64)

# Transforming multiple columns
data[['taxa_deposito', 'taxa_limpeza']] = data[['taxa_deposito', 'taxa_limpeza']].map(lambda x: x.replace('$', '').replace(',', '').strip()).astype(np.float64)
data.head()

# Extra: Categorical
data['modelo_cama'].unique()
data['modelo_cama'] = data['modelo_cama'].astype('category')

# # # Section of the course:
# 03. Dados textuais

data['descricao_local'] = data['descricao_local'].str.lower()
data.head()

# Simple tokenization
# 

# Removing characters using regex
data['descricao_local'][3169] # Checking an arbitrary random sample
data['descricao_local'] = data['descricao_local'].str.replace(r'[^a-zA-Z0-9\-\']', ' ', regex=True)

# Removing unnecessary hifens
data['descricao_local'] = data['descricao_local'].str.replace(r'(?<!\w)-(?!\w)', ' ', regex=True)
data['descricao_local']

# Cleaning amenities column
data['comodidades'] = data['comodidades'].str.replace(r'[\{|}|\"]', '', regex=True)
data['comodidades']

# Tokenizing
data['descricao_local'] = data['descricao_local'].str.split()
data['comodidades'] = data['comodidades'].str.split(',')
data.head()

# Desafio: faça você mesmo
# 
data['descricao_vizinhanca'].unique()
data['descricao_vizinhanca'] = data['descricao_vizinhanca'].str.lower()
data['descricao_vizinhanca'] = data['descricao_vizinhanca'].str.replace(r'[^a-zA-Z0-9\-\']', ' ', regex=True).str.strip()
data['descricao_vizinhanca'] = data['descricao_vizinhanca'].str.replace(r'(?<!\w)-(?!\w)', ' ', regex=True)
data['descricao_vizinhanca'] = data['descricao_vizinhanca'].str.replace(r'^\s*$', '', regex=True)
data['descricao_vizinhanca'] = data['descricao_vizinhanca'].str.split()
data.head()

# # # Section of the course:
# 04. Dados de tempo

# Transforming date data
data_furniture = pd.read_json(data_folder + 'moveis_disponiveis.json')
data_furniture.head()
data_furniture.info()

data_furniture['data'] = pd.to_datetime(data_furniture['data'])

# Manipulating temporal data
months = data_furniture['data'].dt.strftime('%Y-%m')
subset = data_furniture.groupby(months)['vaga_disponivel'].sum()
subset.head()

# Desafio: faça você mesmo
data_furniture.info()
data_furniture['preco'].fillna(0.0, inplace=True)
data_furniture['preco'] = data_furniture['preco'].str.replace('$', '').str.replace(',', '').str.strip()
data_furniture['preco'] = data_furniture['preco'].astype(np.float64)
data_furniture.info()