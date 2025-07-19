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
from typing import Literal, Optional, Any
from sklearn.dummy import DummyRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import make_column_transformer
from sklearn.model_selection import train_test_split, KFold, cross_validate
from sklearn.metrics import (
    root_mean_squared_error,
    mean_absolute_error,
    r2_score
)
from yellowbrick.regressor import prediction_error, residuals_plot


cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data
from plot_utils import label_plot, plot_central_tendency


data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/07-ia-aumentada_prevendo-atrasos-de-voos/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Explorando os dados
# # #

# Understanding the dataset
data = load_data(f'{data_folder}flights.csv', is_pandas=True)
data.shape
data.describe()
data.describe(include='O') # type: ignore
data.info()

# Graphic analysis
# 
def plot_barplot(x, y, data, title, order, palette):
    sns.barplot(x=x, y=y, data=data, order=order, palette=palette)

    label_plot(title=title, xlabel=x.capitalize(), ylabel=y.capitalize())
    plt.xticks(rotation=45)
    for i, v in enumerate(data[y]):
        plt.text(i, v, str(round(v, 2)), ha='center', va='bottom')

    plt.show()
    plt.close()

def plot_countplot(x, data, title, order, palette):
    sns.countplot(data=data, x=x, order=order, palette=palette)

    label_plot(title=title, xlabel=x.capitalize(), ylabel='Count')
    plt.xticks(rotation=45)
    for i, v in enumerate(data[x].value_counts().reindex(order)):
        plt.text(i, v, str(v), ha='center', va='bottom')
    
    plt.show()
    plt.close()

def plot_analysis(x, y, data):
    sns.set_style('darkgrid')

    data_sorted = data.sort_values(by=y, ascending=True)
    grouped = data_sorted.groupby(x)[y].mean().reset_index().sort_values(by=y, ascending=True)

    order = grouped[x].tolist()
    palette = sns.color_palette('Accent', n_colors=len(order))

    plot_barplot(x=x, y=y, data=grouped, title=f'Average {y.capitalize()} by {x.capitalize()}', order=order, palette=palette)
    plot_countplot(x=x, data=data_sorted, title=f'N occurrences of:\n{x.capitalize()}', order=order, palette=palette)

# Checking delay and flight counts per airline
plot_analysis(x='airline', y='delay', data=data)
# Checking delay per flight type: schengen or non-schengen
plot_analysis(x='schengen', y='delay', data=data)
# Checking delay relating to holidays
plot_analysis(x='is_holiday', y='delay', data=data)
# Checking dealy by aircraft type
plot_analysis(x='aircraft_type', y='delay', data=data)


# Analysing data distribution
# 
def calculate_bin_width(df, column):
    Q75, Q25 =  np.percentile(df[column], [75, 25])
    IQR = Q75 - Q25

    bin_width = 2 * IQR * np.power(len(df[column]), -1/3)
    return bin_width

def plot_histogram(data, x, bins=None):
    if bins is None:
        binwidth = calculate_bin_width(data, x)
        sns.histplot(data=data, x=x, kde=True, kde_kws={'bw_adjust': 1}, binwidth=binwidth)
    else:
        sns.histplot(data=data, x=x, kde=True, kde_kws={'bw_adjust': 1}, bins=bins)
    plot_central_tendency(column=data[x])
    label_plot(title=f'Histogram of {x.capitalize()}', xlabel=x.capitalize(), fontsizes='large')

plot_histogram(data=data, x='arrival_time')
plot_histogram(data=data, x='departure_time')

# Analysing target variable
mean_delay = data['delay'].mean()
median_delay = data['delay'].median()

fig, axes = plt.subplots(1, 2, figsize=(9, 4))

sns.boxplot(data=data, y='delay', ax=axes[0])
axes[0].set_title('Boxplot')
axes[0].axhline(y=mean_delay, color='r', linestyle='--', label='Mean')
axes[0].legend()

sns.histplot(data=data, x='delay', ax=axes[1], kde=True, binwidth=calculate_bin_width(data, 'delay'))
axes[1].set_title('Histogram')
plt.ylabel('Number of flights')
plt.grid(False)
axes[1].axvline(x=mean_delay, color='r', linestyle='--', label='Mean')
axes[1].axvline(x=median_delay, color='y', linestyle='--', label='Median')
axes[1].legend()

plt.tight_layout()
plt.show()
plt.close()


# # # Section of the course:
# 02. Feature engeneering
# # #

# Creating new columns
data['date'] = pd.to_datetime(data['year'].astype(str) + '-' + (data['day'] + 1).astype(str), format='%Y-%j')
data['is_weekend'] = data['date'].dt.weekday.isin([5, 6])
data['day_name'] = data['date'].dt.day_name()
data.head()

# Feature encoding
# 
data.nunique()

# Working with binary columns
binary_columns = ['schengen', 'is_holiday', 'is_weekend']
for col in binary_columns:
    print(data[col].unique())

# Transforming
data['schengen'] = data['schengen'].replace({'non-schengen': 0, 'schengen': 1})
for col in binary_columns[1:]:
    print('opa')
    data[col] = data[col].replace({False: 0, True: 1})

# Working with categorical columns > binary
categorical_variables = ['airline', 'aircraft_type', 'origin', 'day_name']

# Using get dummies
df_encoded = pd.get_dummies(data=data, columns=categorical_variables, dtype=int)
df_encoded.head()

# Cleaning data
#
# Checking correlation between arrival and departure time
data[['arrival_time', 'departure_time']].corr()

# What to remove?
# 'departure_time' due to the strong correlation with 'arrival_time'.
# flight_id, as it is unnecessary
# 'day', 'year' and 'data', for our model is not aimed at timestamp predictions
df_clean = df_encoded.drop(columns=['departure_time', 'flight_id', 'day', 'year', 'date'])
df_clean.head()
df_clean.columns

# Challenge: Mão na massa
# Using OneHotEncoder instead of get_dummies
one_hot = make_column_transformer((
    OneHotEncoder(drop='if_binary'),
    categorical_variables
), remainder='passthrough', sparse_threshold=0)

df_encoded = one_hot.fit_transform(data)
df_encoded = pd.DataFrame(df_encoded, columns=one_hot.get_feature_names_out()) # type: ignore


# # # Section of the course:
# 03. Seleção e validação do modelo
# # #

# Treinamento do DummyRegressor
X = df_clean.drop(['delay'], axis=1)
y = df_clean['delay']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model_dummy = DummyRegressor()
model_dummy.fit(X_train, y_train)

y_predict_dummy = model_dummy.predict(X_test)

def calculate_regression_metrics(y_test: pd.Series | list | np.ndarray,
                                 y_pred: pd.Series | list | np.ndarray
                                 ) -> dict:
    """
    Calculate metrics for regression models.

    Parameters
    ----------
    y_test : pd.Series, list or np.ndarray
        Target variable of test data.
    y_pred : pd.Series, list or np.ndarray
        Predicted values of test data.

    Returns
    -------
    dict
        A dictionary containing the metrics for the regression model, including
        Root Mean Squared Error (RMSE), Mean Absolute Error (MAE) and R2 Score.
    """
    rmse = root_mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    metrics = {
        'Root Mean Squared Error': round(rmse, 4),
        'Mean Absolute Error': round(mae, 4),
        'R2 Score': round(r2, 4)
    }

    return metrics

calculate_regression_metrics(y_test, y_predict_dummy) # type: ignore

# Challenge: Mão na massa
# Using diverse strategies for DummyRegressor
def test_strategy(X_train: pd.DataFrame,
                  X_test: pd.DataFrame,
                  y_train: pd.Series | list | np.ndarray,
                  strategy: Literal['mean', 'median', 'quantile', 'constant'] = 'mean',
                  constant_value: Optional[int | float | list] = None, quantile: Optional[float] = None
                  ) -> dict:
    """
    Test diverse strategies for DummyRegressor.

    Parameters
    ----------
    X_train : pd.DataFrame
        DataFrame with features of training data.
    X_test : pd.DataFrame
        DataFrame with features of testing data.
    y_train : pd.Series, list or np.ndarray
        Series with target variable of training data.
    strategy : {'mean', 'median', 'quantile', 'constant'}, optional
        Strategy to use for DummyRegressor. Default is 'mean'.
    constant_value : int, float, list, optional
        Value to use for 'constant' strategy. Default is None.
    quantile : float, optional
        Quantile value to use for 'quantile' strategy. Default is None.

    Returns
    -------
    dict
        Dictionary with regression metrics calculated for given strategy.
    """

    if strategy == 'quantile':
        model_dummy = DummyRegressor(strategy=strategy, quantile=quantile)
    elif strategy == 'constant':
        model_dummy = DummyRegressor(strategy=strategy, constant=constant_value)
    else:
        model_dummy = DummyRegressor(strategy=strategy)
        
    model_dummy.fit(X_train, y_train)
    y_predict_dummy = model_dummy.predict(X_test)

    return calculate_regression_metrics(y_test, y_predict_dummy) # type: ignore

test_strategy(X_train, X_test, y_train, strategy='mean')
test_strategy(X_train, X_test, y_train, strategy='quantile', quantile=0.25) # 1st quartile
test_strategy(X_train, X_test, y_train, strategy='median')
test_strategy(X_train, X_test, y_train, strategy='quantile', quantile=0.75) # 3rd quartile
test_strategy(X_train, X_test, y_train, strategy='constant', constant_value=0)

# Training and evaluation with RandomForestRegressor
def train_model(X_train: pd.DataFrame,
                y_train: pd.Series | list | np.ndarray,
                model: Any=RandomForestRegressor,
                max_depth: Optional[int] = 5,
                random_state: Optional[int] = 42
                ) -> Any:
    """
    Train a model.

    Parameters
    ----------
    model : Any
        Model to be trained. Default is RandomForestRegressor.
    X_train : pd.DataFrame
        DataFrame with features of training data.
    y_train : pd.Series, list or np.ndarray
        Series with target variable of training data.
    max_depth : int, optional
        Maximum depth of the tree. Default is None.

    Returns
    -------
    Any
        Trained model.
    """
    model_instance = model(max_depth=max_depth, random_state=random_state)
    model_instance.fit(X_train, y_train)
    return model_instance

model_rf = train_model(X_train, y_train)
y_pred_rf = model_rf.predict(X_test)
calculate_regression_metrics(y_test, y_pred_rf)

# Interpreting graphically
visualizer = prediction_error(model_rf, X_train, y_train, X_test, y_test)
viz = residuals_plot(model_rf, X_train, y_train, X_test, y_test)

# Cross validating
scoring = {
    'mae': 'neg_mean_absolute_error',
    'rmse': 'neg_root_mean_squared_error',
    'r2': 'r2'
}

cv = KFold(n_splits=5, shuffle=True, random_state=42)
cv_results = cross_validate(model_rf, X_train, y_train, cv=cv, scoring=scoring)
print(cv_results)

for metric in scoring.keys():
    scores = cv_results[f'test_{metric}']
    mean_score = np.mean(scores)
    std_score = np.std(scores)

    print(f'=> {metric.upper()}:')
    print(f'Scores: {scores}')
    print(f'Average: {mean_score:.4f} | Std: (+/- {std_score:.4f})')
    print('-' * 30)


# # # Section of the course:
# 04. Otimização de hiperparâmetros
# # #