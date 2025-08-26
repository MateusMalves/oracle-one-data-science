# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Aquecimento
1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

2. Escreva um código para importar a biblioteca numpy com o alias np.

3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
Copiar código
4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.

Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.

5. Crie um programa que solicite ao usuário digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

Dica: use a função pow() da biblioteca math

Aplicando a projetos
6. Um programa deve ser escrito para sortear um seguidor de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça ao usuário para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.

7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita ao usuário o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

"Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas do cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
Copiar código
9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:

numeros = [2, 8, 15, 23, 91, 112, 256]
Copiar código
No final, informe quais números possuem raízes inteiras e seus respectivos valores.

Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:

num = 1.5
num_2 = 2
print(f'{num} é inteiro? :', num // 1 == num)
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)
Copiar código
Saída:

1.5 é inteiro? : False
2 é inteiro? : True
Copiar código
10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça ao usuário o raio da área circular e devolva o valor em reais do quanto precisará pagar.
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

# 1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.
'''
Feito via terminal
'''

# 2. Escreva um código para importar a biblioteca numpy com o alias np.
'''
Todas as importações
'''
import matplotlib.pyplot as plt
import numpy as np
import random

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
mensagem_problema_3 = '# 3 => Vamos escolher um número aleatório de uma lista.'
controlador(mensagem_problema_3, primeiro_exercicio=True)

def problema_3():
    print('A lista é:\n[8, 12, 54, 23, 43, 1, 90, 87, 105, 77]')
    lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
    numero_escolhido = random.choice(lista)
    print(f'\n=> Número escolhido aleatoriamente da lista:\n{numero_escolhido}')

problema_3()

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
# Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.
mensagem_problema_4 = '# 4 => Vamos escolher um número aleatório menor que 100.'
controlador(mensagem_problema_4, mensagem_problema_anterior=mensagem_problema_3, problema_anterior=problema_3)

def problema_4():
    numero_aleatorio = random.randrange(100)
    print(f'=> Número sorteado aleatoriamente menor que 100:\n{numero_aleatorio}')
    
problema_4()

# 5. Crie um programa que solicite ao usuário digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
# Dica: use a função pow() da biblioteca math
mensagem_problema_5 = '# 5 => Vamos calcular a potência de um número.'
controlador(mensagem_problema_5, mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4)

def problema_5():
    print('Digite dois números inteiros:')
    def validar_numero(numero, input_mensagem):
        try:
            numero = int(numero)
            return numero
        except ValueError:
            print('!! Digite um número inteiro.\n')
            return validar_numero(input(input_mensagem).strip(), input_mensagem)

    numero_1 = validar_numero(input('Número base: ').strip(), 'Número base: ')
    numero_2 = validar_numero(input('Número potência: ').strip(), 'Número potência: ')
    potencia = pow(numero_1, numero_2)
    print(f'\n=> A potência de {numero_1} elevado a {numero_2} é: {potencia}')

problema_5()

# # # UI - Controle de fluxo
controlador(mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, abrir_nova_sessão=True, saudacao='Aplicando a projetos')

# 
# Aplicando a projetos
# 

# 6. Um programa deve ser escrito para sortear um seguidor de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça ao usuário para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
mensagem_problema_6 = '# 6 => Vamos sortear um número de participante para o nosso sorteio.'
controlador(mensagem_problema_6, mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, apos_saudacao=True, saudacao='Aplicando a projetos')

def problema_6():
    def validar_numero_participantes(numero, input_mensagem):
        try:
            numero = int(numero)
            if numero <= 0:
                print('!! O número de participantes deve ser maior que zero.\n')
                return validar_numero_participantes(input(input_mensagem).strip(), input_mensagem)
            return numero
        except ValueError:
            print('!! Digite um número inteiro.\n')
            return validar_numero_participantes(input(input_mensagem).strip(), input_mensagem)
        
    def sortear_participante(quantidade_participantes):
        participante = random.randrange(1, quantidade_participantes + 1)
        return participante

    quantidade_participantes = validar_numero_participantes(input('Digite o número de participantes do sorteio: ').strip(), 'Digite o número de participantes do sorteio: ')
    participante_sorteado = sortear_participante(quantidade_participantes)
    print(f'\n=> O participante sorteado foi: {participante_sorteado}!')

problema_6()

# 7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita ao usuário o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
mensagem_problema_7 = '# 7 => Vamos gerar um token para você'
controlador(mensagem_problema_7, mensagem_problema_anterior=mensagem_problema_6, problema_anterior=problema_6)

def problema_7():
    def gerar_token_aleatorio(inicio, fim, passo):
        token = random.randrange(inicio, fim, passo)
        return token
    
    nome_usuario = input('Digite seu nome: ').strip().capitalize()
    token_gerado = gerar_token_aleatorio(1000, 9999, 2)
    print(f'\n=> Olá {nome_usuario}, o seu token de acesso é {token_gerado}!\nSeja bem-vindo(a)!')

problema_7()

# 8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas do cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

# frutas = ["maçã", "banana", "uva", "pêra",
#           "manga", "coco", "melancia", "mamão",
#           "laranja", "abacaxi", "kiwi", "ameixa"]
mensagem_problema_8 = '# 8 => Vamos fazer uma salada de frutas surpresa pra você.'
controlador(mensagem_problema_8, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7)

def problema_8():
    frutas = ["maçã", "banana", "uva", "pêra",
            "manga", "coco", "melancia", "mamão",
            "laranja", "abacaxi", "kiwi", "ameixa"]

    frutas_escolhidas = random.sample(frutas, 3)
    print(f'Sua salada de frutas surpresa:\n=> {frutas_escolhidas[0].capitalize()} com {frutas_escolhidas[1]} e {frutas_escolhidas[2]}!')
    print(f'\nBom apetite!')

problema_8()

# 9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte:

# numeros = [2, 8, 15, 23, 91, 112, 256]

# No final, informe quais números possuem raízes inteiras e seus respectivos valores.
# Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. Por exemplo:
# num = 1.5
# num_2 = 2
# print(f'{num} é inteiro? :', num // 1 == num)
# print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)

# Saída:
# 1.5 é inteiro? : False
# 2 é inteiro? : True
mensagem_problema_9 = '# 9 => Vamos calcular a raiz quadrada de uma lista de números e descobrir quais resultam em um número inteiro.'
controlador(mensagem_problema_9, mensagem_problema_anterior=mensagem_problema_8, problema_anterior=problema_8)

def problema_9():
    def calcular_raiz(numero):
        raiz = pow(numero, 0.5)
        return raiz

    def verificar_raiz_inteira(raiz):
        if raiz // 1 == raiz:
            return True
        else:
            return False

    numeros = [2, 8, 15, 23, 91, 112, 256]
    raizes = []
    # Armazena os índices dos números que possuem raiz inteira
    raizes_inteiras = []

    for numero in numeros:
        raiz = calcular_raiz(numero)
        raizes.append(raiz)
        if verificar_raiz_inteira(raiz):
            raizes_inteiras.append(numeros.index(numero))

    print(f'Lista de números:\n{numeros}\n')
    print('Raizes quadradas:\n')
    for numero, raiz in zip(numeros, raizes):
        if numeros.index(numero) in raizes_inteiras:
            print(f'=> {numero} possui raiz inteira!')
        else:
            print(f'{numero} NÃO possui raiz inteira!')
        print(f'A raiz quadrada de {numero} é:\n{int(raiz)}\n')

problema_9()

# 10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça ao usuário o raio da área circular e devolva o valor em reais do quanto precisará pagar.
# Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).
mensagem_problema_10 = '# 10 => Vamos calcular o preço da sua grama.'
controlador(mensagem_problema_10, mensagem_problema_anterior=mensagem_problema_9, problema_anterior=problema_9)

def problema_10():
    # Usa a variável pi da biblioteca math
    from math import pi
    # Usa regular expression para validar o formato do número
    import re
    numberRegex = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'

    def validar_numero_decimal(numero, input_mensagem):
        try:
            if re.match(numberRegex, numero):
                numero = float(numero)
                return numero
            else:
                print('!! Digite um número decimal válido.\n')
                return validar_numero_decimal(input(input_mensagem).strip(), input_mensagem)
        except ValueError:
            print('!! Digite um número decimal válido.\n')
            return validar_numero_decimal(input(input_mensagem).strip(), input_mensagem)
        
    # Calcula a área do círculo
    # A = π*r^2
    def calcular_area_circulo(raio):
        area = pi * pow(raio, 2)
        return area

    def calcular_preco(area, preco_por_metro):
        preco = area * preco_por_metro
        return preco

    preco_por_metro = 25.00
    raio = validar_numero_decimal(input('Digite o raio do jardim em metros: ').strip(), 'Digite o raio do jardim em metros: ')
    area = calcular_area_circulo(raio)
    preco = calcular_preco(area, preco_por_metro)

    print('\nO preço do metro quadrado da grama é de R$ 25,00.')
    print(f'A área do seu jardim circular de {raio} metros de raio é: {area:.2f} m²')
    print(f'O preço total da grama para o seu jardim circular de {area:.2f} m² é de R$ {preco:.2f}!')

problema_10()
controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_10, problema_anterior=problema_10, ultimo_exercicio=True)