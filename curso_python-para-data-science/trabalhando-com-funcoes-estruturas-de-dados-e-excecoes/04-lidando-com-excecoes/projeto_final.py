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

saudar('Python para Data Science: trabalhando com funções > 04. Lidando com exceções > Projeto Final')

# 1. Faça um programa que solicite ao usuário digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.
# Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.
mensagem_problema_1 = '# 1 => Vamos dividir dois números float!'
controlador(mensagem_problema_1, primeiro_exercicio=True)

def problema_1():
    try:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        resultado = num1 / num2
    except ZeroDivisionError:
        print('\n=> Não é possível dividir por zero!')
    except ValueError:
        print('\n=> Digite apenas números!')
    except Exception as e:
        print(f'\n=> Ocorreu um erro: {e}')
    else:
        print(f'\n=> O resultado da divisão é: {resultado}')
    finally:
        print('\nFim do problema 1!')

problema_1()

# 2. Faça um programa que solicite ao usuário digitar um texto que será uma chave a ser pesquisada no seguinte dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, armazenando o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.
# Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.
mensagem_problema_2 = '# 2 => Vamos pesquisar por um nome num dicionário de idades!'
controlador(mensagem_problema_2, mensagem_problema_anterior=mensagem_problema_1, problema_anterior=problema_1)

def problema_2():
    idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
    print(f'=> Dicionário de idades:\n{idades}\n')

    try:
        nome = input('Digite o nome que deseja pesquisar: ').capitalize()
        idade = idades[nome]
    except KeyError:
        print('\n=> Nome não encontrado')
    else:
        print(f'\n=> A idade de {nome} é: {idade}')
    finally:
        print('\nFim do problema 2!')

problema_2()

# 3. Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.
mensagem_problema_3 = '# 3 => Vamos criar uma função para converter uma lista de valores para float!'
controlador(mensagem_problema_3, mensagem_problema_anterior=mensagem_problema_2, problema_anterior=problema_2)

def problema_3():
    def converter_lista_para_float(lista):
        print('# Dentro da função\nConvertendo lista para float...')
        try:
            lista_float = [float(x) for x in lista]
        except Exception as e:
            print(f'\n=> Ocorreu um erro: {e}')
        else:
            print('\n=> Lista convertida com sucesso!')
            return lista_float
        finally:
            print('\nFim da execução da função!\n')
    
    lista_que_passa = ['10', '20', '30', '40', '50']
    lista_ValueError = ['10', '20', '30', '40', '50', 'a']
    print(f'=> Lista de entrada:\n{lista_que_passa}\n')
    lista = converter_lista_para_float(lista_que_passa)
    print(f'=> Lista de entrada:\n{lista_ValueError}\n')
    lista_errada = converter_lista_para_float(lista_ValueError)
    print('# Fora da função:\n')
    print(f'=> Lista convertida para float:\n{lista}\n')
    print(f'=> Lista com erro:\n{lista_errada}')

    print('\n\nFim do problema 3!')

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
    def agrupar_elementos_listas(lista1, lista2):
        print('# Dentro da função\nAgrupando elementos das listas...')
        try:
            if len(lista1) != len(lista2):
                raise IndexError('A quantidade de elementos em cada lista é diferente.')
            else:
                lista_tuplas = []
                for i in range(len(lista1)):
                    lista_tuplas.append((lista1[i], lista2[i], lista1[i] + lista2[i]))
        except IndexError as e:
            print(f'\n=> Ocorreu um erro: {e}')
        except Exception as e:
            print(f'\n=> Ocorreu um erro: {e}')
        else:
            print('\n=> Agrupamento realizado com sucesso!')
            print(f'\n=> Lista de tuplas:\n{lista_tuplas}')
            return lista_tuplas
        finally:
            print('\nFim da execução da função!\n\n')

    # Valores sem erro:
    lista1 = [4,6,7,9,10]
    lista2 = [-4,6,8,7,9]
    print(f'=> Lista 1:\n{lista1}')
    print(f'=> Lista 2:\n{lista2}')
    lista_tuplas = agrupar_elementos_listas(lista1, lista2)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_tuplas}\n\n')

    # Listas com tamanhos diferentes:
    lista1 = [4,6,7,9,10,4]
    lista2 = [-4,6,8,7,9]
    print(f'=> Lista 1:\n{lista1}')
    print(f'=> Lista 2:\n{lista2}')
    lista_tuplas = agrupar_elementos_listas(lista1, lista2)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_tuplas}\n\n')

    # Listas com valores incoerentes:
    lista1 = [4,6,7,9,'A']
    lista2 = [-4,'E',8,7,9]
    print(f'=> Lista 1:\n{lista1}')
    print(f'=> Lista 2:\n{lista2}')
    lista_tuplas = agrupar_elementos_listas(lista1, lista2)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_tuplas}')

    print('\n\nFim do problema 4!')
    
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
    def contabilizar_pontuacoes(gabarito, testes):
        print('\n\n# Dentro da função\nCalculando pontuação...')
        try:
            lista_pontuacoes = []
            for i in range(len(testes)):
                if len(gabarito) != len(testes[i]):
                    raise IndexError('A quantidade de questões do gabarito é diferente da quantidade de questões dos testes.')
                else:
                    pontuacao = 0
                    for j in range(len(testes[i])):
                        if testes[i][j].capitalize() not in ['A', 'B', 'C', 'D']:
                            raise ValueError(f'A alternativa {testes[i][j]} não é uma opção de alternativa válida.\nEm teste número {i+1}: {testes[i]}\nEm questão número {j+1}: {testes[i][j]}')
                        elif testes[i][j] == gabarito[j]:
                            pontuacao += 1
                    lista_pontuacoes.append((f'Aluno {i + 1}', pontuacao))
                    pontuacao = 0
        except IndexError as e:
            print(f'\n=> Ocorreu um erro: {e}')
        except ValueError as e:
            print(f'\n=> Ocorreu um erro: {e}')
        except Exception as e:
                print(f'\n=> Ocorreu um erro: {e}')
        else:
            print('\n=> Pontuação calculada com sucesso!')
            print(f'\n=> Lista de pontuações:\n{lista_pontuacoes}')
            return lista_pontuacoes
        finally:
            print('\nFim da execução da função!\n\n')

    # Gabarito da prova:
    gabarito = ['D', 'A', 'B', 'C', 'A']
    # Notas sem exceção:
    testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
    # Notas com exceção:
    testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
    print(f'=> Gabarito:\n{gabarito}')
    print(f'=> Testes sem exceção:\n{testes_sem_ex}')
    lista_pontuacoes = contabilizar_pontuacoes(gabarito, testes_sem_ex)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_pontuacoes}\n\n')
    print(f'=> Gabarito:\n{gabarito}')
    print(f'=> Testes com exceção:\n{testes_com_ex}')
    lista_pontuacoes = contabilizar_pontuacoes(gabarito, testes_com_ex)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_pontuacoes}')

    print('\n\nFim do problema 5!')    

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
    def verificar_pontuacoes(lista):
        print('\n\n# Dentro da função\nVerificando pontuações...')
        try:
            for i in range(len(lista)):
                if ',' in lista[i] or '.' in lista[i] or '!' in lista[i] or '?' in lista[i]:
                    raise ValueError(f'O texto apresenta pontuações na palavra "{lista[i]}"')
        except ValueError as e:
            print(f'\n=> Ocorreu um erro: {e}')
        except Exception as e:
                print(f'\n=> Ocorreu um erro: {e}')
        else:
            print('\n=> Pontuações verificadas com sucesso!')
            print(f'\n=> Lista verificada:\n{lista}')
            return lista
        finally:
            print('\nFim da execução da função!\n\n')

    lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                      'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                      'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
    lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,',
                         'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,','desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
    print(f'=> Lista tratada:\n{lista_tratada}')
    lista_retornada = verificar_pontuacoes(lista_tratada)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_retornada}\n\n')
    print(f'=> Lista não tratada:\n{lista_nao_tratada}')
    lista_retornada = verificar_pontuacoes(lista_nao_tratada)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_retornada}')

    print('\n\nFim do problema 6!')    

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
    def divide_colunas(lista_1, lista_2):
        print('\n\n# Dentro da função\nDividindo colunas...')
        try:
            razoes = []
            if len(lista_1) != len(lista_2):
                raise ValueError('As listas não possuem o mesmo tamanho!')
            for i in range(len(lista_1)):
                if lista_2[i] == 0:
                    raise ZeroDivisionError('Divisão por zero não é permitida!')
                resultado = round(lista_1[i] / lista_2[i], 2)
                razoes.append(resultado)
                print(f'{lista_1[i]} / {lista_2[i]} = {resultado}')
        # # # Código desnecessário, apenas para testar o funcionamento das exceções
        # except ValueError as e:
        #     print(f'\n=> Ocorreu um erro: {e}')
        # except ZeroDivisionError as e:
        #     print(f'\n=> Ocorreu um erro: {e}')
        except Exception as e:
                print(f'\n=> Ocorreu um erro: {e}')
        else:
            print('\n=> Divisão realizada com sucesso!')
            print(f'\n=> Lista de razões pressão / temperatura:\n{razoes}')
            return razoes
        finally:
            print('\nFim da execução da função!\n\n')

    # Dados sem exceção:
    pressoes = [100, 120, 140, 160, 180]
    temperaturas = [20, 25, 30, 35, 40]
    print('=> Dados sem exceção:\n')
    print(f'=> Lista de pressões:\n{pressoes}')
    print(f'=> Lista de temperaturas:\n{temperaturas}')
    lista_retornada = divide_colunas(pressoes, temperaturas)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_retornada}\n\n')

    # Dados com exceção:
    # 1) Exceção de ZeroDivisionError
    print('=> Dados com exceção:\n')
    pressoes = [60, 120, 140, 160, 180]
    temperaturas = [0, 25, 30, 35, 40]
    print(f'=> Lista de pressões:\n{pressoes}')
    print(f'=> Lista de temperaturas:\n{temperaturas}')
    lista_retornada = divide_colunas(pressoes, temperaturas)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_retornada}\n\n')
    # 2) Exceção de ValueError
    pressoes = [100, 120, 140, 160]
    temperaturas = [20, 25, 30, 35, 40]
    print(f'=> Lista de pressões:\n{pressoes}')
    print(f'=> Lista de temperaturas:\n{temperaturas}')
    lista_retornada = divide_colunas(pressoes, temperaturas)
    print('# Fora da função:\n')
    print(f'=> Retorno da função:\n{lista_retornada}')

    print('\n\n# Fim do problema 7!')    

problema_7()

controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7, ultimo_exercicio=True)