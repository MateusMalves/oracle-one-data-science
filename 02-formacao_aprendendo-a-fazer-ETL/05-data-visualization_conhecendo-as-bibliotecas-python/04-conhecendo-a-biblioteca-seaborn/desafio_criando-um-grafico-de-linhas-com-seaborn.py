# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #

# Enunciado do desafio:
'''
Parabéns por chegar até aqui, em mais um desafio! Voltando aos dados utilizados no projeto que nós estamos desenvolvendo neste curso, agora chegou o momento de utilizar todos os conhecimentos adquiridos sobre as bibliotecas Matplotlib e Seaborn.

Nesta etapa, seu desafio é criar uma figura contendo as tendências de imigração dos 4 maiores países da América latina: Brasil, Argentina, Peru e Colômbia. Através dessa criação você pode explorar diversas possibilidades e reconhecer de forma atrativa o seu processo de desenvolvimento.E não nos esqueçamos das orientações! Essa figura precisa ter uma linha para cada país, título, rótulos nos eixos, cores apropriadas, um tema da biblioteca Seaborn e legenda. Por isso, pense nas questões de acessibilidade, como tamanho das fontes e espessura das linhas. É importante escolher cores adequadas que não causem cansaço visual ou dificultem a leitura das informações. Além disso, o tamanho das fontes deve ser legível o suficiente para que as pessoas possam interpretar os dados com facilidade.

Dica: para escolher a paleta de cores, você também pode consultar a documentação da biblioteca Matploltib. A Seaborn utiliza as colormaps do Matplotlib por padrão, além de oferecer suas próprias paletas de cores. Para aplicar uma paleta de cores a todas as linhas da figura você pode usar a função sns.set_palette() e passar a ela o nome da paleta escolhida.

Estamos empolgados para ver o resultado do seu trabalho e as histórias que você irá contar através deste gráfico. Mãos à obra e divirta-se!
'''

# # Imports
#
import os
import sys
import re
from typing import Literal
import matplotlib.pyplot as plt
import seaborn as sns

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/05-data-visualization_conhecendo-as-bibliotecas-python/'
outputs_folder = data_folder + 'outputs/'

df = load_data(f'{data_folder}/imigrantes_canada.csv', is_pandas=True)

countries = ['Brasil', 'Argentina', 'Peru', 'Colômbia']
df = df[df['País'].isin(countries)]
df.drop(columns=['Continente', 'Região'], inplace=True)
df.set_index('País', inplace=True)
df.sort_values(by='Total', ascending=False, inplace=True)

def plot(palette, theme: Literal['darkgrid', 'whitegrid', 'dark', 'white', 'ticks'] = 'darkgrid'):
    sns.set_theme(style=theme)
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=df, y=countries, x='Total', orient='h', palette=palette)
    ax.set_title('Imigração para o Canadá\n1980 - 2013', fontsize=16, loc='left')
    ax.set_xlabel('Número de imigrantes', fontsize=14)
    ax.set_ylabel('')
    ax.tick_params(labelsize=12)
    sns.despine()

plot(palette='viridis', theme='ticks')
plot(palette='magma', theme='dark')
plot(palette='plasma', theme='whitegrid')
plot(palette='inferno', theme='white')

# The best option for the challenge
plot(palette='cividis', theme='darkgrid')