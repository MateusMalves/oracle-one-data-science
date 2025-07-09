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
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
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

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/05-classificacao_aprendendo-a-classificar-dados-com-ML/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Análise exploratória
# # #
data = load_data(f'{data_folder}marketing_investimento.csv', is_pandas=True)
data.info()

# Exploring uniques
def get_uniques(df, col):
    uniques = df[col].unique()
    uniques.sort()
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

plot_histogram(data, 'aderencia_investimento', 'Aderência ao investimento')
plot_histogram(data, 'estado_civil', 'Estado civil', color='aderencia_investimento')
plot_histogram(data, 'escolaridade', 'Escolaridade', color='aderencia_investimento')
plot_histogram(data, 'inadimplencia', 'Inadimplência', color='aderencia_investimento')
plot_histogram(data, 'fez_emprestimo', 'Fez Empréstimo', color='aderencia_investimento')

# Plotting numerics
def plot_boxplot(df, column, title, color=None):
    if color:
        return px.box(df, x=column, title=title, color=color).show()
    return px.box(df, x=column, title=title).show()

plot_boxplot(data, 'idade', 'Distribuição da Idade', color='aderencia_investimento')
plot_boxplot(data, 'saldo', 'Distribuição do Saldo', color='aderencia_investimento')
plot_boxplot(data, 'tempo_ult_contato', 'Distribuição do Tempo de Último Contato', color='aderencia_investimento')
plot_boxplot(data, 'numero_contatos', 'Distribuição do Número de Contatos', color='aderencia_investimento')

# # No inconsistencies found in the data


# # # Section of the course:
# 02. Transformação de dados
# # #

# Variables separation
x = data.drop(columns=['aderencia_investimento'], axis=1)
y = data['aderencia_investimento']

# Transforming explanatory variables
columns = x.columns

one_hot = make_column_transformer((
    OneHotEncoder(drop='if_binary'),
    ['estado_civil', 'escolaridade', 'inadimplencia', 'fez_emprestimo']
), remainder='passthrough', sparse_threshold=0)
x = one_hot.fit_transform(x)
one_hot.get_feature_names_out(columns)

pd.DataFrame(x, columns=one_hot.get_feature_names_out(columns)) # type: ignore

# Transforming target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


# # # Section of the course:
# 03. Ajustando modelos
# # #

# Splitting data
x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, random_state=5)

# Base Model: Dummy classifier
dummy = DummyClassifier()
dummy.fit(x_train, y_train)
dummy.score(x_test, y_test)

# Decision tree
# 
tree = DecisionTreeClassifier(random_state=5)
tree.fit(x_train, y_train)

# Predicting
tree.predict(x_test)

# Plotting
column_names = ['casado(a)', 'divorciado(a)', 'solteiro(a)', 'fundamental', 'médio', 'superior', 'indadimplencia', 'fez_emprestimo', 'idade', 'saldo', 'tempo_ult_contato', 'numero_contatos']
plt.figure(figsize=(15, 6))
plot_tree(tree, filled=True, class_names=['Não', 'Sim'], fontsize=1, feature_names=column_names)

# Scores
tree.score(x_test, y_test) # Test score
tree.score(x_train, y_train) # Train score: Overfitting

# Fixing...
tree = DecisionTreeClassifier(max_depth=3, random_state=5)
tree.fit(x_train, y_train)

# New scores
tree.score(x_test, y_test) # Test score
tree.score(x_train, y_train) # Train score: No overfitting

# Plotting
plt.figure(figsize=(15, 6))
plot_tree(tree, filled=True, class_names=['Não', 'Sim'], fontsize=7, feature_names=column_names)

# # # Section of the course:
# 04. Seleção de modelos
# # #