# Encunciado do desafio
'''
Chegou a hora de pôr em prática tudo o que aprendemos durante as aulas. Preparei dois projetos extras para desenvolvermos durante o curso, para garantir que possamos praticar bastante! Para isso, vamos trabalhar com 2 novos conjuntos de dados, mas que dessa vez serão bem menores. As bases de dados estão disponíveis para download abaixo:

Projeto desafio 1: vendas online - dados_vendas_clientes.json;
Projeto desafio 2: administração de condomínios - dados_locacao_imoveis.json.
Em cada aula, desenvolveremos uma etapa dos projetos. Portanto, salve seu código de construção em cada desafio para que possa aplicá-lo nos desafios posteriores.

# # # # #

Etapa 1
Projeto desafio 1: vendas online
O objetivo desse projeto é realizar uma análise dos resultados de um evento com os clientes de uma empresa de vendas online. Foi coletado um conjunto de dados que contém os clientes que mais gastaram com produtos dentro de 5 dias de vendas, que é o período de duração do evento. Essa análise vai identificar o cliente com a maior compra na semana, que irá receber um prêmio da loja, e posteriormente, ela pode ajudar a empresa a criar novas estratégias para atrair mais clientes.

A base de dados utilizada nessa análise é a dados_vendas_clientes.json e contém informações importantes sobre os clientes como, o nome de cadastro do cliente, o valor total pago na compra e o dia da compra.

Sabendo essas informações, o desafio do projeto 1: vendas online será abrir a base de dados com Pandas e aplicar o json_normalize.

Projeto desafio 2: administração de condomínios
A administração de condomínios é uma tarefa que requer muita atenção e organização. Entre as diversas responsabilidades da gestão está o recebimento dos aluguéis dos locatários. Para garantir uma boa saúde financeira do empreendimento, é fundamental que esses pagamentos sejam feitos de forma regular e pontual. No entanto, sabemos que nem sempre isso acontece.

Pensando nisso, proponho um desafio de tratamento de dados com o objetivo de analisar o atraso no pagamento de aluguéis no condomínio de alguns moradores. Disponibilizo a base de dados dados_locacao_imoveis.json, que contém informações sobre o apartamento dos locatários, o dia acordado para o pagamento do aluguel, o dia da efetivação do pagamento de aluguel e o valor do aluguel.

Com essas informações, o desafio do projeto 2: administração de condomínios será similar ao desafio do projeto 1, abrir a base de dados com Pandas e aplicar o json_normalize no DataFrame.

# # # # #

Etapa 2
Projeto desafio 1: vendas online
Lemos a base de dados no desafio anterior, agora podemos avançar nas transformações desses dados. Então, o novo desafio do projeto 1 será dividido em algumas metas:

Remover os dados em listas dentro do DataFrame;
Verificar os tipos de dados;
Identificar colunas numéricas;
Transformar a coluna numérica para o tipo numérico.
Projeto desafio 2: administração de condomínios
Lemos a base de dados no desafio anterior, agora podemos avançar nas transformações desses dados. Então, da mesma forma que o projeto 1, o desafio do projeto 2 está listado em algumas metas:

Remover os dados em listas dentro do DataFrame;
Verificar os tipos de dados;
Identificar colunas numéricas;
Transformar a coluna numérica para o tipo numérico.

# # # # #

Etapa 3
Projeto desafio 1: vendas online
Na etapa 2, trabalhamos na transformação dos dados numéricos. Agora, podemos trabalhar com valores textuais.

Devido a uma instabilidade no site da empresa, tivemos problemas com os nomes dos clientes durante o salvamento. Isso resultou em uma coluna de nomes de clientes com uma mistura de letras, maiúsculas e minúsculas, números e outros caracteres.

Sabendo disso, manipule os textos presentes na coluna Cliente para que seja obtido como resultado os nomes dos clientes em letras minúsculas, com a ausência de caracteres especiais ou números.

Projeto desafio 2: administração de condomínios
Na etapa 2, trabalhamos na transformação dos dados numéricos. Agora, podemos trabalhar com valores textuais.

Buscando explicar a organização da identificação dos apartamentos, durante a criação do conjunto de dados, foi adicionado o texto (blocoAP). Esse texto informa que os nomes dos apartamentos estão organizados com a letra do bloco seguida do número do apartamento. No entanto, isso não traz nenhuma informação para nossos dados, sendo interessante realizar a remoção desse texto no conjunto de dados.

Com isso, manipule os textos na coluna apartamento para remover o texto (blocoAP) do DataFrame.

# # # # #

Etapa 4
Projeto desafio 1: vendas online
Nas etapas anteriores, já trabalhamos com vários tipos de dados, agora podemos trabalhar com os dados de tempo.

Na coluna Data de venda, temos datas em formato 'dia/mês/ano' (dd/mm/AAAA). Transforme esses dados para o tipo datetime e busque uma forma de visualização de subconjunto que possa contribuir no objetivo do contexto que os dados estão inseridos.

Se você não lembra o problema do projeto desafio 1, vou deixar abaixo o texto da situação para facilitar o encontro da informação:

O objetivo desse projeto é realizar uma análise dos resultados de um evento com os clientes de uma empresa de vendas online. Foi coletado um conjunto de dados que contém os clientes que mais gastaram com produtos dentro de 5 dias de vendas, que é o período de duração do evento. Essa análise vai identificar o cliente com a maior compra na semana, que irá receber um prêmio da loja, e posteriormente, ela pode ajudar a empresa a criar novas estratégias para atrair mais clientes.

Projeto desafio 2: administração de condomínios
Assim como no projeto desafio 1, trabalhamos com todas as colunas exceto as que envolvem datas.

Nas colunas datas_de_pagamento e datas_combinadas_pagamento, temos datas em formato 'dia/mês/ano' (dd/mm/AAAA). Transforme esses dados para o tipo datetime e busque uma forma de visualização de subconjunto que possa contribuir no objetivo do contexto que os dados estão inseridos.

Se você não lembra o problema do projeto desafio 2, vou deixar abaixo o texto da situação para facilitar o encontro da informação:

A administração de condomínios é uma tarefa que requer muita atenção e organização. Entre as diversas responsabilidades da gestão está o recebimento dos aluguéis dos locatários. Para garantir uma boa saúde financeira do empreendimento, é fundamental que esses pagamentos sejam feitos de forma regular e pontual. No entanto, sabemos que nem sempre isso acontece. Pensando nisso, proponho um desafio de tratamento de dados com o objetivo de analisar o atraso no pagamento de aluguéis no condomínio fictício de alguns moradores.
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

data_folder = cwd + '/data/04-pandas_transformacao-e-manipulacao-de-dados/'
outputs_folder = data_folder + 'outputs/'

# # # 
# Etapa 1
# # # 

# # #
# Projeto desafio 1: vendas online

data_sales_customers = pd.read_json(data_folder + 'dados_vendas_clientes.json')
data_sales_customers = pd.json_normalize(data_sales_customers['dados_vendas'].tolist())
data_sales_customers.head()

# # #
# Projeto desafio 2: administração de condomínios

data_condominium_lease = pd.read_json(data_folder + 'dados_locacao_imoveis.json')
data_condominium_lease = pd.json_normalize(data_condominium_lease['dados_locacao'].tolist())
data_condominium_lease.head()

# # # 
# Etapa 2
# # # 

# # # 
# Etapa 3
# # # 

# # # 
# Etapa 4
# # # 