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
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/01-estatistica-com-python_resumindo-e-analisando-dados'
outputs_folder = data_folder + 'outputs/'

# # # Section of the course:
# 01. Entendendo os dados 
# # #

# Importing the dataset
data = load_data(data_folder + '/vendas_ecommerce.csv', is_pandas=True)

# Treatment of data
data.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
categorical_columns = ['sexo', 'regiao_cliente', 'categoria_produto']
for column in categorical_columns:
    data[column] = data[column].astype('category')

# Investigating data types
categories = data['categoria_produto'].value_counts().reset_index()
plt.barh(categories['categoria_produto'], categories['count'])

# Manipulating ordinal qualitative data
sorted(data['avaliacao'].unique())
data['avaliacao_indicador'] = pd.Categorical(
    data['avaliacao'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)

evaluation_labels = {
    1: 'Péssimo',
    2: 'Ruim',
    3: 'Regular',
    4: 'Bom',
    5: 'Ótimo'
}
data['avaliacao_indicador'] = data['avaliacao_indicador'].map(evaluation_labels)
df_unique = data[['avaliacao', 'avaliacao_indicador']].drop_duplicates()

# Different discrete and continuous variables
data['quantidade'].unique()
print(f'We have sold from {min(data["quantidade"])} to {max(data["quantidade"])} units of products per registry.')

data['total_compra'].unique()
print(f'We have sold from {min(data["total_compra"]):,.2f} to {max(data["total_compra"]):,.2f} units of products per registry.')

data.sort_values(by='total_compra')


# # # Section of the course:
# 02. Identificando o perfil do público
# # #

data.head()
# Absolute frequency
freq_evaluations = (data.groupby('avaliacao_indicador', observed=False)
                    .size()
                    .reset_index(name='absolute_frequency')
                    .sort_values(by='avaliacao_indicador', ascending=False))

# Relative frequency
freq_evaluations['relative_frequency'] = round(freq_evaluations['absolute_frequency'] / freq_evaluations['absolute_frequency'].sum() * 100, 2)
freq_evaluations.columns = ['Evaluation', 'Quantity', 'Percentage']

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(data=freq_evaluations, x='Evaluation', y='Quantity')

plt.title('Frequency of Evaluations Distribution', fontsize=16)
plt.xlabel('Evaluation', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

for index, row in freq_evaluations.iterrows():
    plt.text(index, row['Quantity'] + 500, f"{row['Quantity']} ({row['Percentage']:.1f}%)", # type: ignore
             ha='center', va='bottom', fontsize=12)

# Frequency distribution with 2 variables
table_region_evaluation = pd.crosstab(data['avaliacao_indicador'], data['regiao_cliente'])
table_region_relative_evaluation = round(pd.crosstab(data['avaliacao_indicador'], data['regiao_cliente'], normalize='columns') * 100, 2)

table_positive_evaluations_filtered = table_region_relative_evaluation[table_region_relative_evaluation.index.isin(['Ótimo', 'Bom'])]
result_positive = table_positive_evaluations_filtered.sum()

table_negative_evaluations_filtered = table_region_relative_evaluation[table_region_relative_evaluation.index.isin(['Ruim', 'Péssimo'])]
result_negative = table_negative_evaluations_filtered.sum()

# Crossing customers data
average_ticket_by_sex = round(pd.crosstab(data['sexo'], data['regiao_cliente'], data['total_compra'], aggfunc='mean'), 2)


# # # Section of the course:
# 03. Analisando a tendência dos dados
# # #

# Calculating the average of a variable
average_delivery = data['tempo_entrega'].mean()

average_delivery_category = data.groupby('categoria_produto')['tempo_entrega'].mean().reset_index().round(1)
average_delivery_category.columns = ['Category', 'Average Delivery']
average_delivery_category = average_delivery_category.sort_values(by='Average Delivery', ascending=False)

plt.figure(figsize=(8, 8))
sns.barplot(data=average_delivery_category, x='Average Delivery', y='Category', order=list(average_delivery_category['Category']))
plt.axvline(x=average_delivery, color='red', linestyle='--')

plt.xlabel('Average Delivery', fontsize=14)
plt.ylabel('Category', fontsize=14)
plt.title('Average Delivery by Category', fontsize=16)

# Applying median in the investigation
# Manual calculation
data_nordeste = data[(data['regiao_cliente'] == 'Nordeste') & (data['categoria_produto'] == 'Eletrônicos')]
data_nordeste = data_nordeste.sort_values(by='total_compra')

n = data_nordeste.shape[0]
mid_element = int(n / 2)
median = round((data_nordeste['total_compra'].iloc[mid_element - 1] + data_nordeste['total_compra'].iloc[mid_element]) / 2, 2)

# Built-in function
data_nordeste['total_compra'].median()

# Comparing mean vs median
mean_minus_median = data_nordeste['total_compra'].mean() - median

# Plotting
sns.histplot(list(data_nordeste['total_compra']), bins=30)

# Identifying the most frequent values
data['regiao_cliente'].value_counts()
data_filtered = data[data['categoria_produto'] == 'Livros']
data_filtered['quantidade'].mode()

# Understanding the relation between mean, median and mode
sns.histplot(data=data, bins=21, x='tempo_entrega', kde=True, kde_kws={'bw_adjust':3})
delivery_time_summary = {
    'mean': data['tempo_entrega'].mean(),
    'median': data['tempo_entrega'].median(),
    'mode': data['tempo_entrega'].mode()[0]
}

data_score_5 = data[data['avaliacao_indicador'] == 'Ótimo']
sns.histplot(data=data_score_5, bins=21, x='tempo_entrega', kde=True, kde_kws={'bw_adjust':3})
delivery_time_score_5_summary = {
    'mean': data_score_5['tempo_entrega'].mean(),
    'median': data_score_5['tempo_entrega'].median(),
    'mode': data_score_5['tempo_entrega'].mode()[0]
}


# # # Section of the course:
# 04. Investigando os dados dos funcionários
# # #

workers = load_data(f'{data_folder}/dados_funcionarios.csv', is_pandas=True)
workers.rename(columns={'sexo_biologico': 'sexo', 'nota_desempenho': 'desempenho'}, inplace=True)

# Applying Sturges' rule
n = workers.shape[0]
k = 1 + (10/3) * math.log10(n)
k = int(k)

# Creating the salary ranges
ranges = workers.copy()
ranges['faixa_salarial'] = pd.cut(workers['remuneracao'], bins=k, include_lowest=True)

# Plotting the histogram
table_frequencies = ranges.groupby('faixa_salarial', observed=False).size().reset_index(name='frequencia')
table_frequencies['porcentagem'] = (table_frequencies['frequencia'] / n) * 100

plt.figure(figsize=(15, 6))
sns.histplot(data=ranges, x='remuneracao')
sns.histplot(data=ranges, x='remuneracao', bins=k, kde=True)

# Evaluating salaries by separative measurements
quartiles = {
    'first_quartile': workers['remuneracao'].quantile(0.25),
    'second_quartile': workers['remuneracao'].quantile(0.50),
    'third_quartile': workers['remuneracao'].quantile(0.75)
}

plt.figure(figsize=(15, 6))
sns.histplot(binwidth=500, data=workers, x='remuneracao')
plt.axvline(quartiles['first_quartile'], color='red', linestyle='--')
plt.axvline(quartiles['second_quartile'], color='red', linestyle='--')
plt.axvline(quartiles['third_quartile'], color='red', linestyle='--')

percentile_99 = workers['remuneracao'].quantile(0.99)
coordinators = workers[workers['cargo'] == 'Coordenador(a)']

num_coordinators = coordinators.shape[0]
num_coordinators_with_high_salary = coordinators[coordinators['remuneracao'] > percentile_99].shape[0]
print(num_coordinators_with_high_salary == num_coordinators) # Return True

# CLassying data by separative measurements #2
plt.figure(figsize=(15, 6))
sns.histplot(data=workers, x='idade', bins=10, cumulative=True, stat='proportion', kde=True)
plt.axhline(0.20, color='red', linestyle='dashed')

# Classifying workers and identifying public
ages_classification = workers.copy()
ages_classification = ages_classification.sort_values(by='idade')

ages_classification['cumulativo'] = (ages_classification.reset_index().index + 1) / ages_classification.shape[0]
ages_classification['qualificado'] = ages_classification['cumulativo'] <= 0.20

ages_qualified = ages_classification[ages_classification['qualificado'] == True]
ages_qualified.shape[0]

# # # Section of the course:
# 05. Analisando as variações dos dados
# # #