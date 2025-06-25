# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# Case aula 1
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
import seaborn as sns

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/01-estatistica-com-python_resumindo-e-analisando-dados'
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


# Case aula 2
# Enunciado do desafio
'''
Case Aula 2:
Continuando a análise dos dados da PNAD de 2015, você precisa agora identificar o perfil das pessoas responsáveis pelo domicílio. Para isso, siga as instruções abaixo e reflita sobre os resultados encontrados:

Construa uma tabela de frequências das pessoas responsáveis pelo domicílio por Cat.Sexo. Adicione também uma coluna com esse valor em porcentagem: utilize a variável categórica com o sexo biológico que criamos no Mão na Massa da aula anterior, para construir esta tabela. Esteja atento(a) ao agrupamento dos dados e aos cálculos de frequência absoluta e relativa.

Construa uma tabela de frequências absolutas e outra de relativas cruzando as variáveis Cat.Sexo e Cat.Cor das pessoas responsáveis pelo domicílio. utilize as variáveis categórica com o sexo biológico e cor ou raça que criamos no Mão na Massa da aula anterior, para construir esta tabela. Leia as dicas no documento para criar uma tabela que considere a relação entre todos os cruzamentos dos dados para o cálculo da frequência relativa.

Construa uma tabela cruzada para calcular a Renda média das pessoas responsáveis pelo domicílio em relação ao Cat.Sexo e Cat.Cor. crie a tabela relacionando as duas variáveis categóricas que trabalhamos anteriormente juntamente a uma variável quantitativa, resumindo os dados pela média. Preste atenção na forma de agrupamento dos dados e cálculo da estatística descritiva requerida.
'''

data.head()
table_frequency_sex = data['Sexo'].value_counts().reset_index(name='Absolute Frequency')
table_frequency_sex['Relative Frequency'] = round(table_frequency_sex['Absolute Frequency'] / table_frequency_sex['Absolute Frequency'].sum() * 100, 2)

crosstable_absolute_sex_color = pd.crosstab(data['Sexo'], data['Cor'], margins=True)
crosstable_relative_sex_color = pd.crosstab(data['Sexo'], data['Cor'], margins=True, normalize='all') * 100

average_income_sex_color = round(pd.crosstab(data['Sexo'], data['Cor'], values=data['Renda'], aggfunc='mean'), 2)

# Case aula 3
# Enunciado do desafio
'''
Case Aula 3:
Continuando a análise dos dados da PNAD de 2015, você precisa agora analisar os dados das pessoas responsáveis pelo domicílio, focando na renda e explorando brevemente as variáveis das idades e alturas das pessoas observando o comportamento das medidas de tendência central nos dois casos. Para isso, siga as instruções abaixo e reflita sobre os resultados encontrados:

Calcule as medidas de tendência central (média, mediana e moda) para a variável Renda: calcule os valores e observe o que estes dados representam. Quais os valores mais frequentes? Eles condizem com a média ou estão aquém? Será que temos dados muito extremos?

Crie um gráfico de barras do Top 5 estados pela médias de Renda: Leia as dicas no documento para conseguir filtrar os dados dos estados com as maiores médias de renda e construa uma tabela e visual com esses dados.

Construa 3 tabelas cruzadas calculando a média, mediana e valores máximos de Renda relacionando as pessoas responsáveis por estado da Região Sudeste (UF) e por Cat.Sexo: filtre os dados pelos estados da Região Sudeste c("Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo") e crie uma tabela para cada medida requisitada. O que você encontrou aqui? Tem algum dado que te chamou atenção? Se quiser, crie um gráfico você mesmo ou com auxílio da IA para observar esses comportamentos.

Construa 2 histogramas com curva de densidade com os valores das colunas Altura e Idade de todas as pessoas responsáveis e compare as curvas obtidas com as suas MTCs: Crie para cada variável um histograma com curva de densidade e interprete o que a curva pode apontar. Utilize como suporte uma tabela com as medidas de tendência central verificando se o comportamento da curva esperado bate com os dados encontrados.
'''

data.head()
# Calculating the mean, median and mode of the 'Renda' column
mean_income = data['Renda'].mean()
median_income = data['Renda'].median()
mode_income = data['Renda'].mode()[0]
print(f'The mean of the "Renda" column is {mean_income}, the median is {median_income} and the mode is {mode_income}.')

income_by_state = data.groupby('UF')['Renda'].mean().sort_values(ascending=False).reset_index().head(5)
# Creating a bar chart of the top 5 states with the highest average income
plt.figure(figsize=(10, 6))
sns.barplot(x='UF', y='Renda', data=income_by_state)
plt.title('Top 5 States with Highest Average Income')
plt.xlabel('State')
plt.ylabel('Average Income')

for i, row in income_by_state.iterrows():
    plt.text(i, row['Renda'] + 10, round(row['Renda'], 2), ha='center', va='bottom') # type: ignore

# Creating a crosstab for the average, median and maximum income by state and sex
southeast_states = ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"]
df_southeast = data[data['UF'].isin(southeast_states)]
crosstable_average_income_sex = pd.crosstab(df_southeast['UF'], df_southeast['Sexo'], values=df_southeast['Renda'], aggfunc='mean')
crosstable_median_income_sex = pd.crosstab(df_southeast['UF'], df_southeast['Sexo'], values=df_southeast['Renda'], aggfunc='median')
crosstable_mode_income_sex = df_southeast.groupby(['UF', 'Sexo'])['Renda'].agg(lambda x: x.mode().iloc[0]).unstack()

# Plotting data for the average income by state and sex
def plot_crosstab(crosstab, title, xlabel):
    plt.figure(figsize=(10, 6))

    states = crosstab.index
    y_pos = range(len(states))

    plt.barh(y=y_pos, width=crosstab['Masculino'], color='blue', height=0.4, label='Homens', align='center')
    plt.barh(y=[p - 0.4 for p in y_pos], width=crosstab['Feminino'], color='red', height=0.4, label='Mulheres', align='center')

    # Ajustes visuais
    plt.yticks([p - 0.2 for p in y_pos], states)
    plt.xlabel(xlabel, fontsize=12)
    plt.title(title, fontsize=14)
    plt.legend()
    plt.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()

plot_crosstab(crosstable_average_income_sex, 'Average Income by State and Sex', 'Average Income')
plot_crosstab(crosstable_median_income_sex, 'Median Income by State and Sex', 'Median Income')
plot_crosstab(crosstable_mode_income_sex, 'Mode Income by State and Sex', 'Mode Income')

# Creating histograms with density curves for the 'Altura' and 'Idade' columns
def plot_histogram(x, title, xlabel, tendencies):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=x, kde=True, kde_kws={'bw_adjust':2}, color='blue', label=x, bins=30)

    plt.axvline(tendencies['average'], color="red", linestyle="--", label=f'Average: {tendencies['average']:.2f}')
    plt.axvline(tendencies['median'], color="green", linestyle="-.", label=f'Median: {tendencies['median']:.2f}')
    plt.axvline(tendencies['mode'], color="black", linestyle=":", label=f'Mode: {tendencies['mode']:.2f}')

    plt.title(title, fontsize=18, ha='center')
    plt.xlabel(xlabel, fontsize=14)
    plt.legend(title='', fontsize=12)

    # Validate
    print(f'Average: {tendencies['average']:.2f} || Median: {tendencies['median']:.2f} || Mode: {tendencies['mode']:.2f}')

tendencies_height = {
    'average': data['Altura'].mean(),
    'median': data['Altura'].median(),
    'mode': data['Altura'].mode()[0]
}

tendecies_age = {
    'average': data['Idade'].mean(),
    'median': data['Idade'].median(),
    'mode': data['Idade'].mode()[0]
}

plot_histogram('Altura', 'Height Distribution', 'Height', tendencies_height)
plot_histogram('Idade', 'Age Distribution', 'Age', tendecies_age)