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
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
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
from plot_utils import label_plot, plot_central_tendency

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/03-data-science_testando-relacoes-com-regressao-linear/'
outputs_folder = data_folder + 'outputs/'

# # # Section of the course:
# 01. Ajustando uma reta
# # #

data = load_data(f'{data_folder}Preços_de_casas.csv', is_pandas=True)
data.drop(columns = "Id", inplace=True)

corr = data.corr()
corr['preco_de_venda']

# Mão na massa: Plotting a correlation heatmap
# 
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

plot_corr_heatmap(corr)

# Plotting a dispersion plot
plt.scatter(data['area_primeiro_andar'], data['preco_de_venda'])
plt.axline(xy1=(66,250000), xy2=(190,1700000), color='red')
label_plot(title='Relation Price vs Area', xlabel='Area 1st floor', ylabel='Price')

# Obtaining the best line
px.scatter(data, x='area_primeiro_andar', y='preco_de_venda', trendline_color_override='red', trendline='ols')

# # # Section of the course:
# 02. Explicando a reta
# # #

mean = data['preco_de_venda'].mean()
median = data['preco_de_venda'].median()
mode = data['preco_de_venda'].mode()

sns.boxplot(list(data['preco_de_venda']), showmeans=True)
plot_central_tendency(data['preco_de_venda'], axis=1)

sns.displot(list(data['preco_de_venda']), kde=True, color='green')
plot_central_tendency(data['preco_de_venda'])
label_plot(title='Price Distribution', xlabel='Price', ylabel='Frequency')

# Separating between train and test
# 
# Defining y and x
y = data['preco_de_venda']
x = data.drop(columns=['preco_de_venda'])
if data['preco_de_venda'].dtype == 'float64':
    print('opa')
# Applying the split of y and x
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=230)

# Training data to use the formula
df_train = pd.DataFrame(data=x_train)
df_train['preco_de_venda'] = y_train

# Adjusting the first model
model_0 = ols('preco_de_venda ~ area_primeiro_andar', data=df_train).fit()

# Visualizing params
model_0.params

# Visualizing summary
print(model_0.summary())

# Observing R²
model_0.rsquared

# Understanding residuals
# 
# Who are the residuals
model_0.resid

# How they are distributed
model_0.resid.describe()

# Plotting the residuals
model_0.resid.hist()
plot_central_tendency(model_0.resid)
label_plot(title='Residuals Distribution', xlabel='Residuals', ylabel='Frequency')

# Obtaining R² of the prediction
# 
# Defining the predicted Y
y_predict = model_0.predict(x_test)

# Printing r²
print("Test R²:", r2_score(y_test, y_predict))
sns.histplot(y_predict, kde=True, kde_kws={'bw_adjust':2}, color='green')
plot_central_tendency(y_predict)
label_plot(title='Residuals Distribution', xlabel='Residuals', ylabel='Frequency')


# # # Section of the course:
# 03. Adicionando outros fatores
# # #

# Other factors that may explain the prices
sns.pairplot(data)
# Filtering
sns.pairplot(data, y_vars='preco_de_venda', x_vars=['quantidade_banheiros', 'area_segundo_andar', 'capacidade_carros_garagem'])

# Adding a constant
x_train = sm.add_constant(x_train)
x_train = pd.DataFrame(x_train, columns=['const'] + list(x.columns))
x_train.head()

# Creating another model (no formula): saturated
model_1 = sm.OLS(y_train, x_train[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'area_segundo_andar', 'quantidade_banheiros', 'capacidade_carros_garagem', 'qualidade_da_cozinha_Excelente']]).fit()

# Model without second floor area
model_2 = sm.OLS(y_train, x_train[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'capacidade_carros_garagem', 'qualidade_da_cozinha_Excelente']]).fit()

# Model without information about garage
model_3 = sm.OLS(y_train, x_train[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']]).fit()

# Summaries of the models
print(model_0.summary())
print(model_1.summary())
print(model_2.summary())
print(model_3.summary())

# Comparing models
print("=> R²")
print("Model 0:", model_0.rsquared)
print("Model 1:", model_1.rsquared)
print("Model 2:", model_2.rsquared)
print("Model 3:", model_3.rsquared)

print("=> Lenght of the models")
print("Model 0:", len(model_0.params))
print("Model 1:", len(model_1.params))
print("Model 2:", len(model_2.params))
print("Model 3:", len(model_3.params))

# Analyzing the effect
model_3.params


# # # Section of the course:
# 04. Precificando as casas
# # #

# Obtaining R² of the prediction
x_test.columns
model_3.params

# Add constant
x_test = sm.add_constant(x_test)
x_test = pd.DataFrame(x_test, columns=['const'] + list(x.columns))
x_test.head()

# Predicting
predict_3 = model_3.predict(x_test[['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']])

# What's the R² of the prediction?
print(model_3.rsquared)
print("Test R²:", r2_score(y_test, predict_3))

# Precifying a house
# 
# House characteristics:
house = pd.DataFrame({
    'const': [1],
    'area_primeiro_andar': [120],
    'existe_segundo_andar': [1],
    'quantidade_banheiros': [2],
    'qualidade_da_cozinha_Excelente': [0]
})

# Predicting
print(f'{model_0.predict(house['area_primeiro_andar'])[0]:,.2f}')
print(f'{model_3.predict(house)[0]:,.2f}')

# Precifying various houses
new_houses = load_data(f'{data_folder}/Novas_casas.csv', delimiter=';', is_pandas=True)
new_houses.drop(columns=['Casa'], inplace=True)
new_houses = sm.add_constant(new_houses)
new_houses = pd.DataFrame(new_houses)
new_houses.head(10)

# Predicting
predict_new_houses = model_3.predict(new_houses)

# Saving model in a file using Pickle
file_name = 'linear_regression_model.pkl'
with open(f'{outputs_folder}{file_name}', 'wb') as file:
    pickle.dump(model_3, file)

# Loading model from file using Pickle
with open(f'{outputs_folder}{file_name}', 'rb') as file:
    model_3_loaded = pickle.load(file)


# # # Section of the course:
# 05. Investigando nosso modelo
# # #

explanatory_variables_1 = ['const', 'area_primeiro_andar', 'existe_segundo_andar', 'area_segundo_andar', 'quantidade_banheiros', 'capacidade_carros_garagem', 'qualidade_da_cozinha_Excelente']

explanatory_variables_2 = ['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'capacidade_carros_garagem', 'qualidade_da_cozinha_Excelente']

explanatory_variables_3 = ['const', 'area_primeiro_andar', 'existe_segundo_andar', 'quantidade_banheiros', 'qualidade_da_cozinha_Excelente']

# VIF 1
vif_1 = pd.DataFrame()
vif_1['variavel'] = explanatory_variables_1
vif_1['vif'] = [variance_inflation_factor(x_train[explanatory_variables_1], i) for i in range(len(explanatory_variables_1))]
vif_1.head(7)

# VIF 2
vif_2 = pd.DataFrame()
vif_2['variavel'] = explanatory_variables_2
vif_2['vif'] = [variance_inflation_factor(x_train[explanatory_variables_2], i) for i in range(len(explanatory_variables_2))]
vif_2.head(7)

# VIF 3
vif_3 = pd.DataFrame()
vif_3['variavel'] = explanatory_variables_3
vif_3['vif'] = [variance_inflation_factor(x_train[explanatory_variables_3], i) for i in range(len(explanatory_variables_3))]
vif_3.head(7)

# Comparing predicted vs real
# 
# Predicting values of train "x_train" [explanatory_3]
y_predict_train = model_3.predict(x_train[explanatory_variables_3])

# Plotting
fig = px.scatter(x=y_predict_train, y=y_train, title="Predicted vs Real", labels={'x': 'Predicted', 'y': 'Real'})
fig.show()

# Identifying homoscedasticity
# 
# Residuals
residuals = model_3.resid

# Plotting
fig, ax = plt.subplots(figsize=(20, 8))
sns.scatterplot(x=y_predict_train, y=residuals, s=150, ax=ax)
ax.set_title('Residuals vs Predicted', fontsize=18)
ax.set_xlabel('Predicted', fontsize=14)
ax.set_ylabel('Residuals', fontsize=14)
fig.show() # Heteroscedasticity detected