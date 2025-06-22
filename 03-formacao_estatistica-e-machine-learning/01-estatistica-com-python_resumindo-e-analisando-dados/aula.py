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

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/01-estatistica-com-python_resumindo-e-analisando-dados'
outputs_folder = data_folder + 'outputs/'

# # # Section of the course:
# 01. Entendendo os dados 
# # #

# Importing the dataset
data = load_data(data_folder + '/vendas_ecommerce.csv', is_pandas=True)

# Treatment of data
data.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
categorical_columns = ['sexo', 'regiao_cliente', 'categoria_produto']
for column in categorical_columns:
    data[column] = data[column].astype('category')

# Investigating data types
categories = data['categoria_produto'].value_counts().reset_index()
plt.barh(categories['categoria_produto'], categories['count'])

# Manipulating ordinal qualitative data
sorted(data['avaliacao'].unique())
data['avaliacao_indicador'] = pd.Categorical(
    data['avaliacao'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)

evaluation_labels = {
    1: 'Péssimo',
    2: 'Ruim',
    3: 'Regular',
    4: 'Bom',
    5: 'Ótimo'
}
data['avaliacao_indicador'] = data['avaliacao_indicador'].map(evaluation_labels)
df_unique = data[['avaliacao', 'avaliacao_indicador']].drop_duplicates()

# Different discrete and continuous variables
data['quantidade'].unique()
print(f'We have sold from {min(data["quantidade"])} to {max(data["quantidade"])} units of products per registry.')

data['total_compra'].unique()
print(f'We have sold from {min(data["total_compra"]):,.2f} to {max(data["total_compra"]):,.2f} units of products per registry.')

data.sort_values(by='total_compra')

# # # Section of the course:
# 02. Identificando o perfil do público
# # #

# # # Section of the course:
# 03. Analisando a tendência dos dados
# # #

# # # Section of the course:
# 04. Investigando os dados dos funcionários
# # #

# # # Section of the course:
# 05. Analisando as variações dos dados
# # #