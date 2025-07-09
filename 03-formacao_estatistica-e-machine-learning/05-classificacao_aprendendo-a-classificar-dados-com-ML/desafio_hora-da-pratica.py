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
1 - A primeira etapa em um projeto de Machine Learning é a obtenção de dados. A partir dessa obtenção, podemos fazer a leitura dos dados para se construir um modelo. Como tarefa inicial, faça a leitura da base de dados e verifique a presença de dados nulos. Além disso, remova a coluna 'id_cliente', uma vez que esse tipo de informação única para cada linha não é útil para uso em modelos de machine learning.

2 - Após a leitura dos dados, é importante conhecer os dados, checando inconsistências e entendendo o comportamento de cada uma das colunas. Nesta tarefa, faça uma análise exploratória utilizando gráficos para as variáveis categóricas da base de dados, incluindo a variável alvo churn. Para essas variáveis, pode ser utilizado gráficos de barras para fazer a contagem das categorias e fazer um agrupamento por cores de acordo com as categorias da variável alvo.

3 - Depois de explorar as variáveis categóricas, chegou a vez das variáveis numéricas. Construa gráficos de distribuição como boxplots ou histogramas para analisar o comportamento dos valores numéricos e checar se existem valores inconsistentes.
'''

# #
# Imports
import os
import sys
import re
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/05-classificacao_aprendendo-a-classificar-dados-com-ML'
outputs_folder = data_folder + 'outputs/'

# Import data
data = load_data(f'{data_folder}/churn.csv', is_pandas=True)
data.drop(columns=['id_cliente'], inplace=True)
data.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
data.info()

# Fix categorical columns
data['tem_cartao_credito'] = data['tem_cartao_credito'].astype('category')
data['membro_ativo'] = data['membro_ativo'].astype('category')

# Exploring uniques
def get_uniques(df, col):
    uniques = df[col].unique()
    return uniques

columns = list(data.columns)
for col in columns:
    print(f'=> {col}:\n{get_uniques(data, col)}\n\n')

# Plotting categoricals
def plot_histogram(df, col, title, color=None):
    if color:
        return px.histogram(df, x=col, text_auto=True, title=title, color=color, barmode='group').show()
    else:
        return px.histogram(df, x=col, text_auto=True, title=title).show()

plot_histogram(data, 'churn', 'Histograma do Churn')
columns_categorical = [col for col in columns if data[col].dtype == 'object' or data[col].dtype.name == 'category']
for col in columns_categorical:
    plot_histogram(data, col, f'Histogram: {col}', 'churn')

# Plotting numerics
def plot_boxplot(df, column, title, color=None):
    if color:
        return px.box(df, x=column, title=title, color=color).show()
    return px.box(df, x=column, title=title).show()

columns_numerics = [col for col in columns if data[col].dtype != 'object' and col != 'churn' and data[col].dtype.name != 'category']
for col in columns_numerics:
    plot_boxplot(data, col, f'Boxplot: {col}', 'churn')

# Case aula 2
# Enunciado do desafio
'''
1 - Para utilizar os dados nos algoritmos de Machine Learning, precisamos informar quais são as variáveis explicativas e qual é a variável alvo. Neste desafio, faça a separação da base de dados de churn entre as variáveis explicativas, armazenando em uma variável x e a variável alvo em y.
2 - Variáveis categóricas que estejam em formato de texto não podem ser utilizadas diretamente nos modelos de Machine Learning. Neste desafio, faça a transformação das variáveis categóricas para o formato numérico usando o OneHotEncoder, utilizando o parâmetro drop='if_binary' caso alguma variável tenha apenas 2 categorias.
3 - A variável alvo, como é do tipo categórica, também precisa passar por um tratamento similar às variáveis explicativas categóricas para que possa ser usada nos algoritmos. Nessa tarefa, utilize o método LabelEncoder para fazer a transformação da variável churn.
'''

x = data.drop(columns=['churn'])
y = data['churn']

# Transforming categorical variables
one_hot = make_column_transformer((
    OneHotEncoder(drop='if_binary'), columns_categorical
), remainder='passthrough', sparse_threshold=0)
x = one_hot.fit_transform(x)

one_hot.get_feature_names_out()
pd.DataFrame(x, columns=one_hot.get_feature_names_out()) # type: ignore

# Transforming target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


# Case aula 3
# Enunciado do desafio
'''
1 - A separação dos dados entre conjunto de treinamento e teste é essencial para compreender se um modelo está conseguindo aprender os padrões e generalizar para novos dados. Nesta tarefa, faça a divisão da base de dados entre treinamento e teste de forma estratificada.
2 - Um modelo de base é muito importante para definir um critério de comparação para modelos mais complexos. Nesta etapa, crie um modelo de base com o DummyClassifier e encontre a taxa de acerto com o método score.
3 - A árvore de decisão é um algoritmo que faz as classificações a partir de decisões simples tomadas a partir dos dados. Temos que tomar certo cuidado para não utilizar uma profundidade muito grande, porque isso pode provocar um sobreajuste do modelo aos dados de treinamento. Neste desafio, crie um modelo de árvore de decisão com o parâmetro max_depth=4, avalie o desempenho do modelo nos dados de teste e visualize as decisões da árvore usando o método plot_tree.
'''

# Splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42, stratify=y)

# Base model
base_model = DummyClassifier()
base_model.fit(x_train, y_train)
base_model.score(x_test, y_test)
base_model.score(x_train, y_train)

# Decision tree
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(x_train, y_train)
tree.score(x_test, y_test) # Good score 0.8552
tree.score(x_train, y_train) # Not overfitted: 0.8552

# Plotting
column_names = ['Alemanha', 'Espanha', 'França', 'Mulher', 'Tem Cartão', 'Membro Ativo', 'Score Crédito', 'Idade', 'Anos de Cliente', 'Saldo', 'Serviços Adquiridos', 'Salário Estimado']

plt.figure(figsize=(15, 6))
plot_tree(tree, filled=True, feature_names=column_names, fontsize=7, class_names=['Não', 'Sim'])