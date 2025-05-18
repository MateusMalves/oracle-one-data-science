# Enunciado do desafio:
'''
Chegou a hora de testar os conhecimentos desenvolvidos durante a aula.

Vanessa é uma cientista de dados que está realizando algumas análises com dados ambientais. Ela está desenvolvendo um projeto para avaliar o impacto ambiental das atividades humanas em diferentes países do mundo, mas para isso precisa das estimativas populacionais desses países. Ao pesquisar na internet, encontrou uma tabela de estimativas populacionais em um artigo da página Wikipédia.

Assim como Vanessa, seu desafio é obter um DataFrame da tabela que contém as informações do número de habitantes de cada país.
'''

import pandas as pd

url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
data = pd.read_html(url, index_col=1)
data[0].drop(columns=['Unnamed: 0', 'Estimativa Oficial'], inplace=True)
data[0]

inhabitants_estimate_df = data[0]
inhabitants_estimate_df.head(10)