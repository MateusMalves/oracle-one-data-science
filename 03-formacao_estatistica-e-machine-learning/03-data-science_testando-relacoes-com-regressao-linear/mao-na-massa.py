# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# Case 03: Precificação de quartos de hotéis
# Enunciado do desafio
'''
Como um Cientista de Dados, você está encarregado da análise do problema de precificação de quartos de hotéis, fazendo uso do conjunto de dados fornecidos.

Nesta atividade, sua tarefa envolve conduzir as seguintes etapas:

1. Análise inicial com o PairPlot da Seaborn;
2. Construir modelos de regressão linear; e
3. Realizar a comparação desses modelos.
'''

# #
# Imports
import os
import sys
import re
import math
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/03-data-science_testando-relacoes-com-regressao-linear/'
outputs_folder = data_folder + 'outputs/'

# Import data
data = load_data(f'{data_folder}/hoteis.csv', is_pandas=True)

# Analyze correlations
def plot_corr_heatmap(corr):
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Configure a matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Generate heatmap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                square=True, linewidths=.5, annot=True, cbar_kws={"shrink": .5})

corr = data.corr()
corr['Preco']

plot_corr_heatmap(corr)

# 1. Análise inicial com o PairPlot da Seaborn
sns.pairplot(data)

# 2. Construir modelos de regressão linear
y = data['Preco']
x = data.drop(columns=['Preco'])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=230)

df_train = pd.DataFrame(data=x_train)
df_train['Preco'] = y_train

model_0 = ols('Preco ~ Capacidade', data=df_train).fit()
model_1 = ols('Preco ~ Estrelas', data=df_train).fit()
model_2 = ols('Preco ~ ProximidadeTurismo', data=df_train).fit()

# Saturated models
# Full
x_train = sm.add_constant(x_train)
x_train = pd.DataFrame(x_train, columns=['const'] + list(x.columns))
model_3 = sm.OLS(y_train, x_train).fit()

# Removing Proximidade Turismo
model_4 = sm.OLS(y_train, x_train.drop(columns=['ProximidadeTurismo'])).fit()

# Removing Estrelas
model_5 = sm.OLS(y_train, x_train.drop(columns=['Estrelas'])).fit()

# 3. Realizar a comparação desses modelos
# 
# Summaries of the models
print("=> Summaries\n")
print("Simple models")
print(model_0.summary())
print(model_1.summary())
print(model_2.summary())
print("Saturated models")
print(model_3.summary())
print(model_4.summary())
print(model_5.summary())

print("=> R²")
print("Simple models")
print("Model 0:", model_0.rsquared)
print("Model 1:", model_1.rsquared)
print("Model 2:", model_2.rsquared)
print("Saturated models")
print("Model 3:", model_3.rsquared)
print("Model 4:", model_4.rsquared)
print("Model 5:", model_5.rsquared)

print("=> Lenght of the models")
print("Simple models")
print("Model 0:", len(model_0.params))
print("Model 1:", len(model_1.params))
print("Model 2:", len(model_2.params))
print("Saturated models")
print("Model 3:", len(model_3.params))
print("Model 4:", len(model_4.params))
print("Model 5:", len(model_5.params))

# Best model
print("=> Best model params")
print("Modelo 3:\n", model_3.params)


# Case 04: Precificação de uma casa
# Enunciado do desafio
'''
Você recebeu uma demanda para estimar o preço de uma casa com as seguintes características:

1 banheiro
Área 98m²
Não contém segundo andar
Qualidade da cozinha excelente

Sua tarefa é utilizar o modelo de regressão treinado durante o curso para obter o preço da casa com essas características. Por isso, crie um DataFrame com essas informações e faça a previsão do valor do imóvel.
'''

data_houses = load_data(f'{data_folder}Preços_de_casas.csv', is_pandas=True)

y = data_houses['preco_de_venda']
x = data_houses.drop(columns=['preco_de_venda'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=230)
x_train = sm.add_constant(x_train)
x_train = pd.DataFrame(x_train, columns=['const'] + list(x.columns))

model = sm.OLS(y_train, x_train[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']]).fit()

model.params
model.rsquared

x_test = sm.add_constant(x_test)
x_test = pd.DataFrame(x_test, columns=['const'] + list(x.columns))

y_predict = model.predict(x_test[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']])
print("Test R²:", r2_score(y_test, y_predict))

# Defining the house
house = pd.DataFrame({
    'const': [1],
    'area_primeiro_andar': [98],
    'existe_segundo_andar': [0],
    'quantidade_banheiros': [1],
    'qualidade_da_cozinha_Excelente': [1]
})

house_predict = model.predict(house)
print(f'House predict: {house_predict[0]:,.2f}')


# Case 05: Usina de energia
# Enunciado do desafio
'''
Nesta atividade, vamos aplicar os conceitos de multicolinearidade e homocedasticidade em um contexto diferente: o setor de energia. Utilizaremos esse dataset de uma usina de energia para explorar como esses conceitos podem afetar os nossos modelos de regressão. Vamos lá!

Sua tarefa envolve conduzir as seguintes etapas:

Primeira etapa: Verifique a multicolinearidade utilizando o conceito de VIF. Se houver indícios de multicolinearidade entre as variáveis, tente pensar em quais medidas podem ser tomadas. Para isso você deverá construir um modelo de regressão linear assumindo que a coluna PE é a variável y.

Segunda etapa: Realize uma análise de resíduos e identifique se há ou não heterocedasticidade nos dados.

Dedique-se às atividades e desenvolva as suas habilidades por meio da aplicação do seu conhecimento adquirido ao longo do curso.
'''

# 1st step
data_energy = load_data(f'{data_folder}usina.csv', is_pandas=True)
columns = data_energy.columns
data_energy = sm.add_constant(data_energy)
data_energy = pd.DataFrame(data_energy, columns=['const'] + list(columns))

y = data_energy['PE']
x = data_energy.drop(columns=['PE'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=230)

model_0 = sm.OLS(y_train, x_train).fit()
print(model_0.summary())

vif = pd.DataFrame()
vif['variable'] = x.columns
vif['VIF'] = [variance_inflation_factor(x_train, i) for i in range(x_train.shape[1])]
vif.head() # Variable AT has VIF > 5 (6.03)

# 2nd step
y_predict_train = model_0.predict(x_train)
residuals = model_0.resid

# Plotting
# 
# Comparing predicted vs real
fig = px.scatter(y_predict_train, y_train, title='Predicted Values vs Real Values', labels={'x': 'Predicted Values', 'y': 'Real Values'})
fig.show()

# Comparing predicted vs residuals
fig = px.scatter(y_predict_train, residuals, title='Predicted Values vs Residuals', labels={'x': 'Predicted Values', 'y': 'Residuals'})
fig.show()

# The model shows no heterocedasticity and the slight multicoliearity found in the variable AT (Air Temperature) does not impact the model significantly