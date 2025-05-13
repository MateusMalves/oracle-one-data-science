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

data_folder = cwd + '/data/03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/'
outputs_folder = data_folder + 'outputs/'

# # Pandas I/O
# 

# # # Section of the course:
# 01. Fazendo leitura de arquivos csv
# # #


# Reading
data = load_data('03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/superstore_data.csv', is_pandas=True)
data_semicolon = load_data('03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/superstore_data_ponto_virgula.csv', delimiter=';', is_pandas=True)

data_first_lines = pd.read_csv(data_folder + 'superstore_data.csv', nrows=5)
data_first_lines

data_selection = pd.read_csv(data_folder + 'superstore_data.csv', usecols=['Id', 'Year_Birth', 'Income'])
data_selection

data_selection = pd.read_csv(data_folder + 'superstore_data.csv', usecols=[0, 1, 4])
data_selection

# Saving
data_selection.to_csv(data_folder + 'customers_market.csv')

customers_market = pd.read_csv(data_folder + 'customers_market.csv')
customers_market

# Fixing index
data_selection.to_csv(data_folder + 'customers_market.csv', index=False)

customers_market = pd.read_csv(data_folder + 'customers_market.csv')
customers_market

# # # Section of the course:
# 02. Utilizando planilhas
# # #

# Reading
pd.ExcelFile(data_folder + 'emissoes_CO2.xlsx').sheet_names
data_co2 = pd.read_excel(data_folder + 'emissoes_CO2.xlsx')
per_capita = pd.read_excel(data_folder + 'emissoes_CO2.xlsx', sheet_name='emissoes_percapita')
fonts = pd.read_excel(data_folder + 'emissoes_CO2.xlsx', sheet_name='fontes')
data_co2.head()
per_capita.head()
fonts.head()

def optimize(df):
    print(df.info())
    print(df.memory_usage(deep=True) / 1024 / 1024, 'MB')
    df['País'] = df['País'].astype('category')
    df['ISO 3166-1 alpha-3'] = df['ISO 3166-1 alpha-3'].astype('category')
    df['Ano'] = df['Ano'].astype('category')
    print(df.info())
    print(df.memory_usage(deep=True) / 1024 / 1024, 'MB')

optimize(data_co2)
optimize(per_capita)
optimize(fonts)

# Using intervals
interval = pd.read_excel(data_folder + 'emissoes_CO2.xlsx', usecols="A:D")
interval

interval_2 = pd.read_excel(data_folder + 'emissoes_CO2.xlsx', usecols="A:D", nrows=10)
interval

# Writing excel file
per_capita.to_excel(data_folder + '/outputs/emissoes_co2_percapita.xlsx')
pd.read_excel(data_folder + '/outputs/emissoes_co2_percapita.xlsx')

# Using Google Sheets
sheet_id = '1SU6Ur1-OZSWRVYzqGnLmOBQGU5l9gVsz'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'
data_co2_sheets = pd.read_csv(url)
data_co2_sheets.head()

# Selecting specific sheets
sheet_name = 'emissoes_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
per_capita_sheets = pd.read_csv(url_percapita)
per_capita_sheets.head()

sheet_name_fonts = 'fontes'
url_fonts = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name_fonts}'
fonts_sheets = pd.read_csv(url_fonts)
fonts_sheets.head()

# # # Section of the course:
# 03. Manipulando arquivos JSON
# # #


# # # Section of the course:
# 04. Lendo dados em HTML e XML
# # #


# # # Section of the course:
# 05. Trabalhando com banco de dados
# # #