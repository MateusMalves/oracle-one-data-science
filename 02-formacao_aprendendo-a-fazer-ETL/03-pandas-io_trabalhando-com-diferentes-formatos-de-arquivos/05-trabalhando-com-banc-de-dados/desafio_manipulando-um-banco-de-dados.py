# Enunciado do desafio
'''
Chegou a hora de testar os conhecimentos desenvolvidos durante a aula.

Você é responsável por criar um banco de dados local de clientes para uma instituição financeira. Temos o arquivo CSV com os dados de clientes.

Sua missão é:

Criar o banco de dados local com a biblioteca SQLAlchemy.
Escrever os dados do arquivo CSV neste banco de dados local.
Realizar três atualizações no banco de dados:
Atualizar o registro do cliente de ID 6840104 que teve o rendimento anual alterado para 300000.
Excluir o registro do cliente de ID 5008809, pois essa pessoa não possui mais conta na instituição financeira.
Criar um novo registro de cliente seguindo as especificações abaixo:
ID_Cliente: 6850985
Idade: 33
Grau_escolaridade: Doutorado
Estado_civil: Solteiro
Tamanho_familia: 1
Categoria_de_renda: Empregado
Ocupacao: TI
Anos_empregado: 2
Rendimento_anual: 290000
Tem_carro: 0
Moradia: Casa/apartamento próprio
Dica importante: Para adicionar um(a) novo(a) cliente à tabela, utilize a cláusula INSERT INTO seguida do nome da tabela e depois especifique entre parênteses os nomes das colunas da tabela. Utilize a cláusula VALUES e, em seguida, passe entre parênteses os novos valores para esse novo registro. Certifique-se de que os valores estejam na ordem correta e no formato adequado para cada coluna.
'''

# # Imports
#
import os
import sys
import re
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/'
outputs_folder = data_folder + 'outputs/'

# 1. Criar o banco de dados local com a biblioteca SQLAlchemy.
engine = create_engine('sqlite:///:memory:')

# 2. Escrever os dados do arquivo CSV neste banco de dados local.
data = pd.read_csv(data_folder + 'clientes_banco.csv')
data

data.to_sql('customers', engine, index=False)
inspector = inspect(engine)
print(inspector.get_table_names())

# 3. Realizar três atualizações no banco de dados:
# Atualizar o registro do cliente de ID 6840104 que teve o rendimento anual alterado para 300000.
# Excluir o registro do cliente de ID 5008809, pois essa pessoa não possui mais conta na instituição financeira.
# Criar um novo registro de cliente seguindo as especificações abaixo:
# ID_Cliente: 6850985
# Idade: 33
# Grau_escolaridade: Doutorado
# Estado_civil: Solteiro
# Tamanho_familia: 1
# Categoria_de_renda: Empregado
# Ocupacao: TI
# Anos_empregado: 2
# Rendimento_anual: 290000
# Tem_carro: 0
# Moradia: Casa/apartamento próprio

def update_db(query):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        conn.commit()

pd.read_sql('SELECT * FROM customers WHERE ID_Cliente IN (6840104, 6850985)', engine)
query1 = 'UPDATE customers SET Rendimento_anual = 300000 WHERE ID_Cliente = 6840104'
query2 = 'DELETE FROM customers WHERE ID_Cliente = 5008809'
query3 = 'INSERT INTO customers (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, Rendimento_anual, Tem_carro, Moradia) VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", 2, 290000, 0, "Casa/apartamento próprio")'
update_db(query1)
update_db(query2)
update_db(query3)