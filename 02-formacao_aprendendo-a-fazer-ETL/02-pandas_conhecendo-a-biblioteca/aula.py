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


# # # Section of the course:
# 01. Conhecendo a base de dados
# # #

# Importing data
data = load_data('aluguel.csv', delimiter=';', is_pandas=True)
data
data.head()
data.head(10)
data.tail()
type(data)

# Data caracteristics
data.shape
data.columns
data.dtypes
data.info()
data['Tipo']
data[['Quartos', 'Valor']]

# # # Section of the course:
# 02. Análise exploratória de dados
# # #

# General mean
data['Valor'].mean()

# Specific means
data.groupby('Tipo').mean(numeric_only=True)
data.groupby('Tipo')['Valor'].mean()
data.groupby('Tipo')['Valor'].mean().sort_values()
df_price_type = data.groupby('Tipo')['Valor'].mean().sort_values()

# Plotting
df_price_type.plot(kind='barh', figsize=(14, 10), color='purple')

# Removing commercial properties
# 
data.Tipo.unique()
commercial_properties = ['Conjunto Comercial/Sala', 'Prédio Inteiro', 'Loja/Salão', 'Galpão/Depósito/Armazém', 'Casa Comercial', 'Terreno Padrão', 'Loja Shopping/ Ct Comercial', 'Box/Garagem', 'Chácara', 'Loteamento/Condomínio', 'Sítio', 'Pousada/Chalé', 'Hotel', 'Indústria']

data.query('@commercial_properties in Tipo')
data.query('@commercial_properties not in Tipo')

df = data.query('@commercial_properties not in Tipo')
df.head()
df.Tipo.unique()

# Plotting
df_price_type = df.groupby('Tipo')['Valor'].mean().sort_values()
df_price_type.plot(kind='barh', figsize=(14, 10), color='purple')

# Percentage of property types
# 
df.Tipo.unique()
df.Tipo.value_counts()
df_type_percentage = df.Tipo.value_counts(normalize=True).to_frame().sort_values(by='Tipo', ascending=False)

# Plotting
df_type_percentage.plot(kind='bar', figsize=(14, 10), color='green', xlabel='Tipo', ylabel='Porcentagem')

# Select only apartments
df = df.query('Tipo == "Apartamento"')
df