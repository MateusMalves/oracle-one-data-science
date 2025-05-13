# Enunciado do desafio:
'''
Chegou a hora de você testar os conhecimentos desenvolvidos durante a aula. Nós temos um link do Google Planilhas que contém dados importantes sobre as emissões de gás carbônico pelo mundo. O conjunto de dados foi obtido no Kaggle e consiste em emissões de CO2 per capita de todos os países do mundo de 1990 a 2019.

Neste desafio, a sua função é efetuar a leitura desse link do Google Planilhas e depois salvar o DataFrame obtido no formato CSV. Pronto(a) para começar?
'''

# # Imports
#
import os
import sys
import re
import pandas as pd

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/'
outputs_folder = data_folder + 'outputs/'

sheet_id = '1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw'
sheet_name = 'CO2_emission'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
data_co2_sheets = pd.read_csv(url)
data_co2_sheets.head()