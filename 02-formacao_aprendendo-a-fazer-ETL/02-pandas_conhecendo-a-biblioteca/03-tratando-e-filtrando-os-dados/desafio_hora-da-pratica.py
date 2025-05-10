# Enunciado do desafio:
'''
Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos, vamos realizar alguns tratamentos e seleções utilizando um arquivo csv diferente: alunos.csv.

Esse arquivo é o mesmo utilizado para resolução dos desafios da aula 1 e possui dados referentes a alunos de um curso superior.

Com base nisso, solucione os problemas propostos abaixo utilizando os conhecimentos adquiridos até aqui.

1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.

2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.

3) Aplique um filtro que selecione apenas os alunos que foram aprovados.

4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".

Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.
'''

# # Imports
#
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

data = load_data('alunos.csv', is_pandas=True)

# 1) Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.
data.isnull().sum()
data.fillna(0, inplace=True)  # Preenchendo os valores nulos com 0
data.isnull().sum()

# 2) Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.
data = data.query('Nome != "Alice" & Nome != "Carlos"').reset_index(drop=True)
data

# 3) Aplique um filtro que selecione apenas os alunos que foram aprovados.
approved = data.query('Aprovado == True')

# 4) Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".
approved.to_csv('alunos_aprovados.csv', index=False)
pd.read_csv('alunos_aprovados.csv', delimiter=',', encoding='utf-8')

# Extra: Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.
data.replace(7.0, 8.0, inplace=True)
data