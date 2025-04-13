# Para rodar o código, basta executar o comando 'python3 projeto_final.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o que aprendemos até aqui solucionando os problemas propostos em código.

Aquecimento
1. Faça um programa que solicite ao usuário digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.

Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

2. Faça um programa que solicite ao usuário digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.

Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.

3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.

4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.' Dados para testar a função:

Valores sem erro:
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7,9]

Listas com tamanhos diferentes:
lista1 = [4,6,7,9,10,4]
lista2 = [-4,6,8,7,9]

Listas com valores incoerentes:
lista1 = [4,6,7,9,'A']
lista2 = [-4,'E',8,7,9]

Aplicando a projetos
5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

Gabarito da prova:
gabarito = ['D', 'A', 'B', 'C', 'A']

Abaixo temos 2 listas de listas que você pode usar como teste

Notas sem exceção:
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

Notas com exceção:
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.

6. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.

Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True

Os dados para o teste do código são:

Lista tratada:
lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

Lista não tratada:
lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

7. Você foi contratado(a) como um cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.

Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

Verificar se as listas têm o mesmo tamanho (ValueError)
Verificar se existe alguma divisão por zero (ZeroDivisionError)
Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:

Dados sem exceção:
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

Dados com exceção:
1) Exceção de ZeroDivisionError

pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

2) Exceção de ValueError

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.
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

saudar('Python para Data Science: trabalhando com funções > 01. Bibliotecas > Desafio: hora da prática')

# 1. Faça um programa que solicite ao usuário digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.
mensagem_problema_1 = '# 1 => Vamos dividir dois números float!'
controlador(mensagem_problema_1, primeiro_exercicio=True)

def problema_1():
    ...


problema_1()

# 2. Faça um programa que solicite ao usuário digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.
# Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.
mensagem_problema_2 = '# 2 => Vamos pesquisar por um nome num dicionário de idades!'
controlador(mensagem_problema_2, mensagem_problema_anterior=mensagem_problema_1, problema_anterior=problema_1)

def problema_2():
    ...


problema_2()

# 3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
mensagem_problema_3 = '# 3 => Vamos converter uma lista de valores para float!'
controlador(mensagem_problema_3, mensagem_problema_anterior=mensagem_problema_2, problema_anterior=problema_2)

def problema_3():
    ...


problema_3()

# 4. Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.' Dados para testar a função:

# Valores sem erro:
# lista1 = [4,6,7,9,10]
# lista2 = [-4,6,8,7,9]

# Listas com tamanhos diferentes:
# lista1 = [4,6,7,9,10,4]
# lista2 = [-4,6,8,7,9]

# Listas com valores incoerentes:
# lista1 = [4,6,7,9,'A']
# lista2 = [-4,'E',8,7,9]
mensagem_problema_4 = '# 4 => Vamos agrupar elementos de duas listas!'
controlador(mensagem_problema_4, mensagem_problema_anterior=mensagem_problema_3, problema_anterior=problema_3)

def problema_4():
    ...

    
problema_4()


# 
# Aplicando a projetos
# 

# # # UI - Controle de fluxo
controlador(mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4, abrir_nova_sessão=True, saudacao='Aplicando a projetos')


# 5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.
# Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.
# Os dados para o teste do código são:

# Gabarito da prova:
# gabarito = ['D', 'A', 'B', 'C', 'A']

# Abaixo temos 2 listas de listas que você pode usar como teste
# Notas sem exceção:
# testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Notas com exceção:
# testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.
mensagem_problema_5 = '# 5 => Vamos calcular a pontuação de estudantes!'
controlador(mensagem_problema_5, mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4, apos_saudacao=True, saudacao='Aplicando a projetos')

def problema_5():
    ...
    

problema_5()

# 6. Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.
# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

# Dica: Para verificar se uma ou mais das pontuações estão presentes em cada palavra, utilize a palavra chave or na condição if. Por exemplo, 'a' in 'alura' or 'b' in 'alura'… Saída: True

# Os dados para o teste do código são:
# Lista tratada:
# lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
#                   'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
#                   'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
mensagem_problema_6 = '# 6 => Vamos verificar se um texto apresenta pontuações!'
controlador(mensagem_problema_6, mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5)

def problema_6():
    ...
    

problema_6()

# 7. Você foi contratado(a) como um cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.
# Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

# Verificar se as listas têm o mesmo tamanho (ValueError)
# Verificar se existe alguma divisão por zero (ZeroDivisionError)

# Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

# Como teste, use os seguintes dados:

# Dados sem exceção:
# pressoes = [100, 120, 140, 160, 180]
# temperaturas = [20, 25, 30, 35, 40]

# Dados com exceção:
# 1) Exceção de ZeroDivisionError
# pressoes = [60, 120, 140, 160, 180]
# temperaturas = [0, 25, 30, 35, 40]
# 2) Exceção de ValueError
# pressoes = [100, 120, 140, 160]
# temperaturas = [20, 25, 30, 35, 40]

# Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.
mensagem_problema_7 = '# 7 => Vamos avaliar a razão entre dados de pressão e temperatura!'
controlador(mensagem_problema_7, mensagem_problema_anterior=mensagem_problema_6, problema_anterior=problema_6)

def problema_7():
    ...
    

problema_7()

controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7, ultimo_exercicio=True)