# Enunciado do desafio:
'''
Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos, vamos realizar algumas análises utilizando um arquivo csv diferente: alunos.csv.

1) Importe o arquivo alunos.csv e armazene seu conteúdo em um DataFrame Pandas.

2) Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

3) Confira a quantidade de linhas e colunas desse DataFrame.

4) Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.

Extra: Calcule algumas estatísticas descritivas básicas dos dados do DataFrame (média, desvio padrão, etc). Dica: pesquise pelo método describe.
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

# 1) Import the file alunos.csv and store its content in a Pandas DataFrame.
data = load_data('02-pandas_conhecendo-a-biblioteca/alunos.csv', is_pandas=True)
# 2) Visualize the first 7 rows of the DataFrame and the last 5.
data.head(7)
data.tail(5)
# 3) Check the number of rows and columns in this DataFrame.
data.shape
# 4) Explore the columns of the DataFrame and analyze the types of data in each column.
data.info()

# Extra: Calculate some basic descriptive statistics of the data in the DataFrame (mean, standard deviation, etc). Hint: search for the describe method.
data.describe()