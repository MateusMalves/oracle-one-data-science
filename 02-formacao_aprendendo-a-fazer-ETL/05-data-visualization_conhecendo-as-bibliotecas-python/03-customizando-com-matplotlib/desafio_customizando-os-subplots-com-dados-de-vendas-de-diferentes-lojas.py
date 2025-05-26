# Enunciado do desafio:
'''
Mais uma etapa de desafio se inicia! Aproveite a oportunidade proposta e mergulhe nas possibilidades. Na aula anterior, você teve o desafio de criar uma figura com subplots que apresentam a variação no número de vendas em quatro diferentes lojas ao longo de um ano. Agora é o momento de elevar essa figura a um novo patamar! É a hora de personalizá-la! Nesta segunda parte do desafio, você deve explorar as opções de customização dos subplots para deixar a figura mais clara e atraente para a gerência da empresa.

Algumas ideias de customização que você pode explorar são:

Alterar a posição dos títulos dos subplots para esquerda.
Aumentar o tamanho da fonte do título geral da figura para destacá-lo.
Aumentar o tamanho dos títulos e rótulos dos eixos dos subplots.
Deixar as linhas com a espessura maior.
Alterar a cor das linhas de cada loja para diferenciá-las ainda mais.
Fique à vontade para testar mais customizações!

E mais uma dica: você pode reduzir o tamanho do código utilizando o comando for i, ax in enumerate(axs.flat): que permite um loop iterando sobre todos os subplots da figura. Dentro desse loop você pode passar as funções plot, set_title, set_xlabel, set_ylabel e etc…

Lembrando que os dados são os seguintes:

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

# Criando DataFrame
df = pd.DataFrame(vendas_2022, index=lojas)
Copiar código
Agora é hora de colocar a mão na massa! Experimente diferentes customizações e deixe a figura ainda mais impressionante. Bora?!
'''

# # Imports
#
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

data_folder = cwd + '/data/05-data-visualization_conhecendo-as-bibliotecas-python/'
outputs_folder = data_folder + 'outputs/'

# Load data
lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}

# Criando DataFrame
df = pd.DataFrame(vendas_2022, index=lojas)
df = df.T

fig, axs = plt.subplots(2, 2, figsize=(14, 8))
fig.subplots_adjust(hspace=0.4)
fig.suptitle('Vendas de 2022', fontsize=16)
colors = ['#008fd5', '#fc4f30', '#e5ae38', '#6d904f']

for i, ax in enumerate(axs.flat):
    ax.plot(df.index, df[df.columns[i]], label=df.columns[i], lw=3, color=colors[i])
    ax.set_title(f'Loja {df.columns[i]}', loc='left', fontsize=14)
    ax.set_xlabel('Mês', fontsize=12)
    ax.set_ylabel('Vendas', fontsize=12)
    ax.legend()

together_fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df.index, df, label=df.columns)
ax.set_title('Imigração de Brasileiros para o Canadá', fontsize=14)
ax.set_xlabel('Ano', fontsize=12)
ax.set_ylabel('Número de imigrantes', fontsize=12)
ax.tick_params(axis='x', labelsize=10)
ax.legend()
ax.grid()