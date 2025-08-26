
# Enunciado do desafio:
'''
Para praticar os métodos aprendidos no decorrer dessa aula e também aprender novos, vamos realizar alguns tratamentos e seleções utilizando um arquivo csv diferente: alunos.csv.

Esse arquivo é o mesmo utilizado para resolução dos desafios da aula 1 e 3 e possui dados referentes a alunos de um curso superior. Com base nisso, solucione os problemas propostos abaixo utilizando os conhecimentos adquiridos até aqui.

1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.

2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras.

3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.
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

data_folder = cwd + '/data/02-formacao_aprendendo-a-fazer-ETL/02-pandas_conhecendo-a-biblioteca/'
data = load_data(data_folder + 'alunos.csv', is_pandas=True)

# 1) Os alunos participaram de uma atividade extracurricular e ganharam pontos extras. Esses pontos extras correspondem a 40% da nota atual de cada um deles. Com base nisso, crie uma coluna chamada "Pontos_extras" que contenha os pontos extras de cada aluno, ou seja, 40% da nota atual deles.
data['Pontos extras'] = data['Notas'] * 0.4
data

# 2) Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras.
data = data.assign(Notas_finais=data['Notas'] + data['Pontos extras'])
data

# 3) Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

# True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
# False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
data['Aprovado_final'] = data['Notas_finais'].apply(lambda x: True if x >= 6 else False)
data

# 4) Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.
data.query('Aprovado == False and Aprovado_final == True')