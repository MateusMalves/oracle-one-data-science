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


data_customers.describe()