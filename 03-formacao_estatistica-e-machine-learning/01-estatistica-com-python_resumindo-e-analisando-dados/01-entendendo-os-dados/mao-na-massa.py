# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #

# Enunciado do desafio
'''
Vamos aproveitar esse espaço para praticar tudo o que aprendemos durante a aula. Para isso, serão apresentados alguns problemas para que você possa aplicar os seus conhecimentos e explorar as suas habilidades. Para você responder a este e os próximos cases ao longo do curso, disponibilizamos o notebook Desafios.ipynb com os textos e orientações de cada problema.

Vamos colocar a mão na massa?

Análise da Pesquisa Nacional por Amostra de Domicílios - 2015
Utilizando os conhecimentos adquiridos ao longo do curso, você precisará realizar uma análise descritiva básica de um conjunto de dados retirados da Pesquisa Nacional por Amostra de Domicílios - 2015 do IBGE. Vamos dividir esse processo aula a aula de acordo com o que aprendemos no momento, respondendo às perguntas levantadas e interpretando os dados. Dentro do notebook você conseguirá entender sobre a base, quais dados foram levantados e o que eles representam.

Case Aula 01:
Neste primeiro momento, você está treinando para ser um cientista de dados e recebeu a demanda de investigar os dados da PNAD de 2015. A fim de testar as suas habilidades de análise de dados e os conceitos da estatística descritiva, siga as seguintes instruções:

Importe o dataset e armazene o conteúdo em um data.frame: no documento já consta a url, mas você precisa passar o arquivo .csv que está nela para uma variável.

Visualize o conteúdo do data.frame e leia as infos sobre os dados (linhas, colunas, tipos): Observe brevemente os dados usando as funções de leitura dos dados e visualize os tipos de dados.

Explore brevemente a variável UF e investigue quantos dados possuímos para cada estado: observe quantos valores distintos temos na variável, conte as ocorrências em cada caso e crie um gráfico de barras horizontal com esses dados.

Transforme as variáveis Sexo, Cor e Anos.de.Estudo em categorical e observe o resultado: crie colunas que tratam as variáveis categóricas nominais e ordinais de dados numéricos. Siga as instruções e dados trazidos no documento. Leia no final a nova tabela com os dados transformados.

Apresente em texto a menor e maior Renda da base de dados: Utilize a função print juntamente a formatação de dados f-string como explicada no documento para exibir estes dados.
'''

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

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning'
outputs_folder = data_folder + 'outputs/'

# Import data
data = load_data(data_folder + '/dados_desafio.csv', is_pandas=True)
data.info()

# UF study
data['UF'].unique()
df_uf = data['UF'].value_counts().reset_index()
plt.barh(df_uf['UF'], df_uf['count'])
plt.tight_layout()

categorical_columns = ['Sexo', 'Cor', 'Anos.de.Estudo']
for column in categorical_columns:
    data[column] = data[column].astype('category')
data.info()

# Defining variables
sex = {0: 'Masculino', 1: 'Feminino'}
color = {0:'Indígena', 2:'Branca', 4:'Preta', 6:'Amarela', 8:'Parda'}
years_of_study = {1:'Sem instrução e menos de 1 ano', 2:'1 ano', 3:'2 anos', 4:'3 anos', 5:'4 anos', 6:'5 anos',
    7:'6 anos', 8:'7 anos', 9:'8 anos', 10:'9 anos', 11:'10 anos', 12:'11 anos', 13:'12 anos',14:'13 anos',
    15:'14 anos', 16:'15 anos ou mais', 17:'Não determinados'
}
# Mapping variables
labels = [sex, color, years_of_study]
for x, y in zip(categorical_columns, labels):
    data[x] = data[x].map(y)

# Checking
data.info()
for column in categorical_columns:
    print(f'{data[column].value_counts()}\n\n')

# Printing min and max for 'Renda' in the database
print(f'The minimum value for "Renda" is {data["Renda"].min()} and the maximum value for "Renda" is {data["Renda"].max()}.')
data['Renda'].sort_values()