# Enunciado do desafio:
'''
Na atividade anterior foi possível compreender como criar uma animação com a biblioteca Plotly. Agora vem mais um desafio!

Lembra que nós criamos uma figura estática contendo os dados de imigração do Brasil e Argentina? Sua tarefa é criar um gráfico animado com o Plotly que mostre esses dados. O gráfico deve ter as seguintes características:

Duas linhas: uma para o Brasil e outra para a Argentina.
Um botão "Play" para iniciar a animação, mostrando o aumento ou diminuição do número de imigrantes ao longo dos anos.
As configurações de animação devem fazer com que as duas linhas sejam exibidas e animadas ao mesmo tempo.
Dicas:

Crie um DataFrame com os dados da Argentina e não se esqueça de deixar a coluna de anos no tipo int(inteiro).
Use o código fornecido para o Brasil como base e adapte-o para incluir os dados da Argentina.
Para configurar as animações você pode fazer um Loop for para percorrer o DataFrame dados_brasil e para cada iteração, criar uma nova lista contendo dois objetos do tipo go.Scatter, um para cada país. Em seguida, cada lista pode ser usada para criar um objeto go.Frame, que é adicionado à lista de frames. Por fim, a lista de frames pode ser atribuída ao objeto fig, que é a figura do gráfico a ser animado. Com isso, quando a animação for iniciada, o gráfico exibirá as duas linhas em movimento, uma para o Brasil e outra para a Argentina.
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