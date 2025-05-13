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

data_folder = cwd + '/data/02-pandas_conhecendo-a-biblioteca/'
outputs_folder = data_folder + 'outputs/'

# # # Section of the course:
# 01. Conhecendo a base de dados
# # #

# Importing data
data = load_data(data_folder + 'aluguel.csv', delimiter=';', is_pandas=True)
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
df_type_percentage.rename(columns={'proportion': 'Porcentagem'}, inplace=True)

# Plotting
df_type_percentage.plot(kind='bar', figsize=(14, 10), color='green', xlabel='Tipo', ylabel='Porcentagem')

# Select only apartments
df = df.query('Tipo == "Apartamento"')
df

# # # Section of the course:
# 03. Tratando e filtrando os dados
# # #

# Treating NaNs
df.isnull()
df.isnull().sum()

# Replace NaNs with 0
df.fillna(0)
df = df.fillna(0)
df.isnull().sum()

# Remove outliers
df.query('Valor == 0 | Condominio == 0').index
registers_to_remove = df.query('Valor == 0 | Condominio == 0').index
df.drop(registers_to_remove, axis=0, inplace=True)
df.query('Valor == 0 | Condominio == 0')

df.head()
df.Tipo.unique()
df.drop('Tipo', axis=1, inplace=True)
df.head()

# Applying filters
df.query('"Quartos" == 1 | "Valor" < 1200')
selection_1 = df['Quartos'] == 1
df[selection_1]
selection_2 = df['Valor'] < 1200
df[selection_2]

final_selection = (selection_1 & selection_2)
df[final_selection]

df1 = df[final_selection]

selection = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
selection
df[selection]

df2 = df[selection]
df2

# Saving the data
df.to_csv(outputs_folder + 'data_apartments.csv', sep=';', index= False)
pd.read_csv(outputs_folder + 'data_apartments.csv', sep=';')

# Challenge: Save the filtered data
df1.to_csv(outputs_folder + 'data_apartments_filtered_1.csv', sep=';', index= False)
df2.to_csv(outputs_folder + 'data_apartments_filtered_2.csv', sep=';', index= False)
pd.read_csv(outputs_folder + 'data_apartments_filtered_1.csv', sep=';')
pd.read_csv(outputs_folder + 'data_apartments_filtered_2.csv', sep=';')

# # # Section of the course:
# 04. Manipulando os dados
# # #

# Creating numerical columns
data2 = load_data(data_folder + 'aluguel.csv', delimiter=';', is_pandas=True)
data2['Valor_por_mes'] = data2['Valor'] + data2['Condominio']
data2['Valor_por_ano'] = data2['Valor_por_mes'] * 12 + data2['IPTU']
data2

# Creating a categorical column
data2['Descricao'] = data2['Tipo'] + ' em ' + data2['Bairro'] + ' com ' + data2['Quartos'].astype(str) + ' quarto(s) e ' + data2['Vagas'].astype(str) + ' vaga(s) de garagem.'
data2

# Creating a binary column
data2['Possui_suite'] = data['Suites'].apply(lambda x: "Sim" if x > 0 else "Não")
data2

# Save the data
data2.to_csv(outputs_folder + 'complete_data.csv', sep=';', index= False)
pd.read_csv(outputs_folder + 'complete_data.csv', sep=';')