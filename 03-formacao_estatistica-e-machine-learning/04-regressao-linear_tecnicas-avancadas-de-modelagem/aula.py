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
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data
from plot_utils import label_plot, plot_central_tendency

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/04-regressao-linear_tecnicas-avancadas-de-modelagem/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Análises Preliminares
# # #
data = load_data(f'{data_folder}dataset.csv', is_pandas=True, delimiter=';')
data.head()

# Descriptive analysis
# 
# Descriptive statistics
data.describe().round(2)

# Correlation analysis
corr = data.corr().round(4)
mask = np.zeros_like(corr, dtype=bool)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)


# # # Section of the course:
# 02. Análises gráficas
# # #

# Behaviour of the Dependent Variable (Y)
sns.set_palette('Accent')
sns.set_style('darkgrid')

plt.figure(figsize=(20, 5))
sns.boxplot(data=data, x='Valor', orient='h', width=0.3)
label_plot(title='Valor', xlabel='Reais', fontsizes='large')
plot_central_tendency(column=data['Valor'])

# Frequency distribution
plt.figure(figsize=(20, 6))
sns.histplot(list(data['Valor']), kde=True, color='green')
label_plot(title='Distribuição de Frequências', xlabel='Preço dos Imóveis (R$)', fontsizes='large')
plot_central_tendency(column=data['Valor'])

# Dispersion between variables
plt.suptitle('Dispersão entre variáveis', fontsize=20, y=1.05)
sns.pairplot(data=data, y_vars='Valor', x_vars=['Area', 'Dist_Praia', 'Dist_Farmacia'], height=5, kind='reg')


# # # Section of the course:
# 03. Transformação de variáveis
# # #

np.log(1) # Returns 0
np.log(0) # Returns -inf

def add_log(data: pd.DataFrame, columns_with_zeros: list[str])-> None:
    columns = list(data.columns)
    for column in columns:
        if not column in columns_with_zeros:
            data[f'log_{column}'] = np.log(data[column])
        else:
            data[f'log_{column}'] = np.log(data[column] + 1)

add_log(data, columns_with_zeros=['Dist_Praia', 'Dist_Farmacia'])
data.head()

plt.figure(figsize=(20, 6))
sns.histplot(list(data['log_Valor']), kde=True, color='green')
label_plot(title='Distribuição de Frequências', xlabel='log do Preço dos Imóveis', fontsizes='large')
plot_central_tendency(column=data['log_Valor'])


# Verifying linear relation
sns.pairplot(data=data, y_vars='log_Valor', x_vars=['log_Area', 'log_Dist_Praia', 'log_Dist_Farmacia'], height=5, kind='reg')


# # # Section of the course:
# 04. Regressão linear com Statsmodels
# # #
y = data['log_Valor']
X = data[['log_Area', 'log_Dist_Praia', 'log_Dist_Farmacia']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2811)

X_train_with_constant = sm.add_constant(X_train)
model_statsmodels = sm.OLS(y_train, X_train_with_constant, hasconst=True).fit()

print(model_statsmodels.summary())

# Modifying model and reevaluating
X = data[['log_Area', 'log_Dist_Praia']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2811)

X_train_with_constant = sm.add_constant(X_train)
new_model_statsmodels = sm.OLS(y_train, X_train_with_constant, hasconst=True).fit()

print(new_model_statsmodels.summary())


# # # Section of the course:
# 05. Regressão linear com Scikit-learn
# # #

# Estimating the model with training data
model = LinearRegression()
model.fit(X_train, y_train)

print('R² = {}'.format(model.score(X_train, y_train)))

# Testing the model
y_predict = model.predict(X_test)

print('R² = %s' % metrics.r2_score(y_test, y_predict))

# Obtaining punctual predictions
entry = X_test[0:1]

model.predict(entry)[0] # Returns log(y)
# Inverting transformation to obtain R$ values
np.exp(model.predict(entry)[0])

# Creating a simple simulator
def predict_property_price(model, property: dict, is_log: bool = False, add_const: bool = False) -> float:
    log_area = property['Area'] if is_log else np.log(property['Area'])
    log_dist_praia = property['Dist_Praia'] if is_log else np.log(property['Dist_Praia'] + 1)

    if add_const:
        X = pd.DataFrame({
            'const': [1.0],
            'log_Area': log_area,
            'log_Dist_Praia': log_dist_praia,
        }, index=[0])

        return np.exp(model.predict(X)[0])
    
    X = pd.DataFrame({
        'log_Area': log_area,
        'log_Dist_Praia': log_dist_praia,
    }, index=[0])

    return np.exp(model.predict(X)[0])

property = {
    'Area': 250,
    'Dist_Praia': 1,
}

predicted = predict_property_price(model, property)
print('R$ {0:,.2f}'.format(predicted))

# Playing
def build_property_obj(area: float, dist_praia: float) -> dict:
    return {
        'Area': area,
        'Dist_Praia': dist_praia,
    }

predict_property_price(model, build_property_obj(250, 100))
predict_property_price(model, build_property_obj(100, 100))
predict_property_price(model, build_property_obj(50, 10))
predict_property_price(model, build_property_obj(50, 100))
predict_property_price(model, build_property_obj(50, 10000)) # Starts to fail and predict absurd values for high distances

# Interpreting the estimated coefficients
# 
# Obtaining the intercept
model.intercept_ # Returns log(y)
np.exp(model.intercept_) # Transforming back

# Obtaining the coefficients B2* ... Bn
# (Some literatures may use B1, B2, ... Bn, and B0 for the intercept)
model.coef_
# 
# Storing the coefficients in a DataFrame
X.columns # Confirming the order of the variables
index = ['Intercept', 'log_Area (m²)', 'log_Distance to the Beach (km)']
coefs = pd.DataFrame(data=np.append(model.intercept_, model.coef_), index=index, columns=['Parameters'])

# Graphical analysis of the model's results
# 
# Generating previsions of the model for training data
y_predict_train = model.predict(X_train)

# Plotting
plt.figure(figsize=(12, 6))
sns.scatterplot(x=y_predict_train, y=y_train)
label_plot(title='Previsões do Modelo', xlabel='Previsões', ylabel='Valores Reais', footer='Valores em log', fontsizes='large')

# Analyzing residuals
residuals = y_train - y_predict_train

# Plotting
plt.figure(figsize=(12, 6))
sns.histplot(residuals, kde=True, color='green')
label_plot(title='Residuals Frequency Distribution', xlabel='log of the Price', fontsizes='large')