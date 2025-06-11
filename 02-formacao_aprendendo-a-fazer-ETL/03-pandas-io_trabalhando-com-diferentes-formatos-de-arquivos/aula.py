# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #

# # Imports
#
import os
import sys
import re
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text

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

def optimize(df, categorical_columns):
    print(df.info())
    print(df.memory_usage(deep=True) / 1024 / 1024, 'MB')
    for column in categorical_columns:
        df[column] = df[column].astype('category')
    print(df.info())
    print(df.memory_usage(deep=True) / 1024 / 1024, 'MB')

categorical_columns = ['País', 'ISO 3166-1 alpha-3', 'Ano']
optimize(data_co2, categorical_columns)
optimize(per_capita, categorical_columns)
optimize(fonts, categorical_columns)

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
data_patients = pd.read_json(data_folder + 'pacientes.json')
data_patients

# Nested JSON
data_patients_2 = pd.read_json(data_folder + 'pacientes_2.json')
data_patients_2

# Normalizing JSON
df_normalized = pd.json_normalize(data_patients_2['Pacientes'])
df_normalized

# Writing JSON
df_normalized.to_json(outputs_folder + 'historico_pacientes_normalizado.json')
pd.read_json(outputs_folder + 'historico_pacientes_normalizado.json')

# # # Section of the course:
# 04. Lendo dados em HTML e XML
# # #

# HTML
data_html = pd.read_html('https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies')
data_html
type(data_html)
len(data_html)
top_movies = data_html[1]
top_movies

top_movies.to_html(outputs_folder + 'top_movies.html')
top_movies.to_csv(outputs_folder + 'top_movies_1998.csv', index=False)
pd.read_csv(outputs_folder + 'top_movies_1998.csv')

# XML
data_xml = pd.read_xml(data_folder + 'imdb_top_1000.xml')
data_xml.head(3)

data_xml.to_xml(outputs_folder + 'movies_imdb.xml')

# # # Section of the course:
# 05. Trabalhando com banco de dados
# # #

# Creating engine and loading data
engine = create_engine('sqlite:///:memory:')
data = pd.read_csv(data_folder + 'clientes_banco.csv')
data

# Writing to table
data.to_sql('customers', engine, index=False)
inspector = inspect(engine)
print(inspector.get_table_names())

# Reading from table
query = 'SELECT * FROM customers WHERE Categoria_de_renda = "Empregado"'
employed_customers = pd.read_sql(query, engine)
employed_customers

# Writing new table
employed_customers.to_sql('employed_customers', con=engine, index=False)

# Reading new table
pd.read_sql_table('employed_customers', engine)
pd.read_sql_table('employed_customers', engine, columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']) # Pandas syntax
pd.read_sql('SELECT ID_Cliente, Grau_escolaridade, Rendimento_anual FROM employed_customers', engine) # SQL syntax

# Updating table
pd.read_sql('SELECT * FROM customers', engine)
query = 'DELETE FROM customers WHERE ID_Cliente=5008804'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()

query = 'UPDATE customers SET Grau_escolaridade="Ensino superior" WHERE ID_Cliente=5008808'
with engine.connect() as conn:
    result = conn.execute(text(query))
    conn.commit()

pd.read_sql_table('customers', engine)