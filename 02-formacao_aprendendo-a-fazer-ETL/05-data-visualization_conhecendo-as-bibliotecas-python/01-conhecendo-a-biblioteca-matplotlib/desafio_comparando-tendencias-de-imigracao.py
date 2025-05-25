# Enunciado do desafio:
'''
Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Nós criamos um gráfico com a função plt.plot() para analisar as intrigantes tendências de imigração do Brasil para o Canadá, no período de 1980 a 2013. Neste momento temos uma nova demanda: criar um gráfico de linhas comparando os números de imigrantes do Brasil e Argentina para o Canadá, que são os maiores países da América do Sul.

Prepare-se para um mergulho fascinante nas linhas que conectam esses países da América do Sul ao território canadense. Nessa missão, a elaboração desse gráfico pode ser útil para a compreensão das tendências migratórias desses países para o Canadá ao longo do tempo e como elas se comparam entre si. Ao analisar esses fatores, podemos obter uma visão mais abrangente do cenário migratório na América do Sul.

Fique tranquila(o)!

Essa nova tarefa é mais desafiadora, pois exige uma análise comparativa entre dois países. No entanto, ela também permitirá com que você obtenha uma aprendizagem enriquecedora. Por isso, explore as diversas possibilidades e lembre-se dos elementos essenciais de um gráfico: título, rótulos nos eixos x e y e os ticks do eixo x, que devem ser definidos de 5 em 5 anos.

Além disso, você precisará descobrir como adicionar uma legenda para que seja possível identificar a linha de cada país. Ao seguir essas orientações, você terá construído um gráfico robusto que te permitirá uma análise significativa e aprofundada.

Após criar o gráfico analise o resultado obtido e reflita nas seguintes questões:

Há alguma tendência ou padrão comum nos dados dos dois países?
Quais são os períodos com maior número de imigrantes nos dois países?
Vamos lá?
'''

# # Imports
#
import os
import sys
import re
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

df = load_data(f'{data_folder}/imigrantes_canada.csv', is_pandas=True)
df.info()

df.query('País == ["Brasil", "Argentina"]', inplace=True)
df.drop(['Continente', 'Região'], axis=1, inplace=True)
df.set_index('País', inplace=True)
df.drop('Total', axis=1, inplace=True)
years = list(map(str, range(1980, 2014)))

plt.figure(figsize=(8, 4))
plt.plot(years, df.iloc[0], label='Argentina')
plt.plot(years, df.iloc[1], label='Brasil')
plt.xticks(['1980', '1985', '1990', '1995', '2000', '2005', '2010'])
plt.yticks([500, 1000, 1500, 2000, 2500, 3000])
plt.title('Imigração de Brasileiros e Argentinos para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Número de imigrantes')
plt.legend()

# # 1. Há alguma tendência ou padrão comum nos dados dos dois países?
# Sim, há uma tendência de aumento nos números de imigrantes para o Canadá, que segue mais ou menos alinhado para os dois países. Seria interessante analisar a correlação com todos os países da América do Sul.

# # 2. Quais são os períodos com maior número de imigrantes nos dois países?
# Há um pico nos anos 90 e posteriormente outro pico entre os anos 2000 e 2010.