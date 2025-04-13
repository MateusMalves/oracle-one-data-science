# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o que aprendemos até aqui solucionando os problemas propostos em código.

Aquecimento
1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

Aplicando a projetos
6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

Glicose igual ou inferior a 70: 'Hipoglicemia'
Glicose entre 70 a 99: 'Normal'
Glicose entre 100 e 125: 'Alterada'
Glicose superior a 125: 'Diabetes'
A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui o nome de apenas um Estado com valores repetidos.

10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de funcionários e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de funcionários referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de funcionários por Estado.
'''


# # # # #
# # # Desafios resolvidos
# # # # #


# Importando bibliotecas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from ui_desafios import controlador, saudar


# 
# Aquecimento
# 

saudar('Python para Data Science: trabalhando com funções > 03. Estruturas de dados > Desafio: hora da prática')

# 1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
# lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
mensagem_problema_1 = '# 1 => Vamos ler esta matrix e imprimir a soma de cada lista.'
controlador(mensagem_problema_1, primeiro_exercicio=True)

def problema_1():
    ...


problema_1()

# 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
# lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
mensagem_problema_2 = '# 2 => Vamos ler uma lista de tuplas e imprimir o terceiro elemento de cada tupla.'
controlador(mensagem_problema_2, mensagem_problema_anterior=mensagem_problema_1, problema_anterior=problema_1)

def problema_2():
    ...


problema_2()

# 3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.
mensagem_problema_3 = '# 3 => Vamos ler uma lista de nomes e imprimir uma tupla de índices.'
controlador(mensagem_problema_3, mensagem_problema_anterior=mensagem_problema_2, problema_anterior=problema_2)

def problema_3():
    ...


problema_3()

# 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
# aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
mensagem_problema_4 = '# 4 => Vamos ler uma lista de tuplas e imprimir o segundo elemento de cada\ntupla caso o primeiro elemento seja "Apartamento".'
controlador(mensagem_problema_4, mensagem_problema_anterior=mensagem_problema_3, problema_anterior=problema_3)

def problema_4():
    ...

    
problema_4()

# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
mensagem_problema_5 = '# 5 => Vamos ler duas listas e imprimir um dicionário com as chaves sendo\nos meses e os valores sendo as despesas.'
controlador(mensagem_problema_5, mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4)

def problema_5():
    ...
    

problema_5()


# 
# Aplicando a projetos
# 

# # # UI - Controle de fluxo
controlador(mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, abrir_nova_sessão=True, saudacao='Aplicando a projetos')


# 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:
# vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
# Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.
mensagem_problema_6 = '# 6 => Vamos filtrar as vendas do ano de 2022 que são maiores que 6000.'
controlador(mensagem_problema_6, mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, apos_saudacao=True, saudacao='Aplicando a projetos')

def problema_6():
    ...
    

problema_6()

# 7. Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

# Glicose igual ou inferior a 70: 'Hipoglicemia'
# Glicose entre 70 a 99: 'Normal'
# Glicose entre 100 e 125: 'Alterada'
# Glicose superior a 125: 'Diabetes'

# A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.
# glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
mensagem_problema_7 = '# 7 => Vamos rotular os dados de glicemia.'
controlador(mensagem_problema_7, mensagem_problema_anterior=mensagem_problema_6, problema_anterior=problema_6)

def problema_7():
    ...
    

problema_7()

# 8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

# id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
# preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.
# Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.
mensagem_problema_8 = '# 8 => Vamos estruturar os dados de vendas de um e-commerce em uma tabela.'
controlador(mensagem_problema_8, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7)

def problema_8():
    ...
    

problema_8()

# 9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].
# A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.
# A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.
# Dica: Você pode fazer um passo intermediário para gerar uma lista de listas em que cada uma das listas possui o nome de apenas um Estado com valores repetidos.
mensagem_problema_9 = '# 9 => Vamos contar o número de filiais de uma empresa por estado.'
controlador(mensagem_problema_9, mensagem_problema_anterior=mensagem_problema_8, problema_anterior=problema_8)

def problema_9():
    ...
    

problema_9()

# 10. Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de funcionários e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:
# funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
# A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de funcionários referentes ao Estado. Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de funcionários por Estado.
mensagem_problema_10 = '# 10 => Agora vamos contar o número de funcionarios por estado.'
controlador(mensagem_problema_10, mensagem_problema_anterior=mensagem_problema_9, problema_anterior=problema_9)

def problema_10():
    ...
    

problema_10()

controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_10, problema_anterior=problema_10, ultimo_exercicio=True)