# Enunciado do desafio:
'''
O time de ML chegou com algumas demandas de última hora para resolvermos nesse momento da análise exploratória. Essas demandas são:

1) Calcular a média de quartos por apartamento;

2) Conferir quantos bairros únicos existem na nossa base de dados;

3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas;

4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
'''

# # Imports
#
import os
import sys
import re

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data = load_data('aluguel.csv', delimiter=';', is_pandas=True)

# 1) Calcular a média de quartos por apartamento
data_apartments = data.query('Tipo == "Apartamento"')
data_apartments['Quartos'].mean()

# 2) Conferir quantos bairros únicos existem na nossa base de dados
data_apartments['Bairro'].nunique()

# 3) Analisar quais bairros possuem a média de valor de aluguel mais elevadas
rent_values = data_apartments.groupby('Bairro')['Valor'].mean().sort_values(ascending=False)

# 4) Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.
top_5_bairros = rent_values.head(5)
top_5_bairros.plot(kind='barh', figsize=(14, 10), color='purple')
# Plot with higher first
top_5_bairros[::-1].plot(kind='barh', figsize=(14, 10), xlabel='Aluguel', color='purple', title='Top 5 bairros com maiores valores de aluguel')