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
import matplotlib.pyplot as plt
import seaborn as sns

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


# # # Section of the course:
# 03. Seleção e validação do modelo
# # #


# # # Section of the course:
# 04. Otimização de hiperparâmetros
# # #