# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o uso de vários tipos de variáveis e da função input a partir de algumas atividades. Solucione os problemas propostos em código.


Coleta e amostragem de dados
1. Crie um programa que solicite ao usuário digitar seu nome, e imprima “Olá, [nome]!”.
2. Crie um programa que solicite ao usuário digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
3. Crie um programa que solicite ao usuário digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

Calculadora com operadores
1. Crie um programa que solicite dois valores numéricos ao usuário e imprima a soma dos dois valores.
2. Crie um programa que solicite três valores numéricos ao usuário e imprima a soma dos três valores.
3. Crie um programa que solicite dois valores numéricos ao usuário e imprima a subtração do primeiro pelo o segundo valor.
4. Crie um programa que solicite dois valores numéricos ao usuário e imprima a multiplicação dos dois valores.
5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.

Editando textos
1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
2. Crie um código que solicite uma frase e depois imprima a frase na tela.
3. Crie um código que solicite uma frase ao usuário e imprima a mesma frase digitada mas com todas as letras maiúsculas.
4. Crie um código que solicite uma frase ao usuário e imprima a mesma frase digitada mas com todas as letras minúsculas.
5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
6. Crie um código que solicite uma frase ao usuário e imprima a mesma frase sem espaços em branco no início e no fim.
7. Crie um código que solicite uma frase ao usuário e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
8. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
9. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
10. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
'''


# # # # #
# # # Desafios resolvidos
# # # # #


# 
# Coleta e amostragem de dados
# 

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo ao Hello World de coleta de dados em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Queremos te conhecer melhor...\n\n')

# 1. Crie um programa que solicite ao usuário digitar seu nome, e imprima “Olá, [nome]!”.
nome = input("Digite seu nome: ").capitalize()
print(f'Olá, {nome}!\n')

# 2. Crie um programa que solicite ao usuário digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
'''
nome = input("Digite seu nome: ").capitalize() # já foi definido acima
'''
idade = int(input("Digite sua idade: "))
print(f'Olá {nome}, você tem {idade} anos.\n')

# 3. Crie um programa que solicite ao usuário digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
'''
nome = input("Digite seu nome: ").capitalize() # já foi definido acima
idade = int(input("Digite sua idade: ")) # já foi definido acima
'''
altura = float(input("Digite sua altura em metros: ").replace(',', '.'))
print(f'Olá {nome}, você tem {idade} anos e mede {altura} metros!\n')


# # # UI - Controle de fluxo
print('\nAgora vamos fazer algumas contas?')

def controladorConfirmacao() :
    print('\n=> Responda Y para sim e N para não.')
    confirmacao = input('Deseja continuar? ').upper()
    if confirmacao == 'N':
        print('\nOk, até a próxima!')
        quit()
    elif confirmacao != 'Y':
        print('!! Resposta inválida.')
        controladorConfirmacao()
    elif confirmacao == 'Y':
        print('\n')

controladorConfirmacao()


# 
# Calculadora com operadores
# 

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo à calculadora Hello World em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos fazer algumas contas...\n\n')

# 1. Crie um programa que solicite dois valores numéricos ao usuário e imprima a soma dos dois valores.
print('=> Vamos somar dois números!')
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
soma = int(num1) + int(num2)
print(f'A soma dos dois números é {soma}\n')

# 2. Crie um programa que solicite três valores numéricos ao usuário e imprima a soma dos três valores.
print('=> Vamos somar três números!')
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
num3 = input("Digite o terceiro número: ")
soma = int(num1) + int(num2) + int(num3)
print(f'A soma dos três números é {soma}\n')

# 3. Crie um programa que solicite dois valores numéricos ao usuário e imprima a subtração do primeiro pelo o segundo valor.
print('=> Vamos subtrair dois números!')
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
subtracao = int(num1) - int(num2)
print(f'A subtração do primeiro pelo segundo número é {subtracao}\n')

# 4. Crie um programa que solicite dois valores numéricos ao usuário e imprima a multiplicação dos dois valores.
print('=> Vamos multiplicar dois números!')
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
multiplicacao = int(num1) * int(num2)
print(f'A multiplicação dos dois números é {multiplicacao}\n')

# 5. Crie um programa que solicite dois valores numéricos ao usuário e imprima a divisão do primeiro pelo o segundo valor. Deixe claro que o valor do denominador não pode ser 0.
print('=> Vamos dividir dois números!')
numerador = input("Digite o numerador: ")
denominador = input("Digite o denominador: ")
if int(denominador) == 0:
    print("O denominador não pode ser zero.")
else:
    divisao = float(int(numerador) / int(denominador))
    print(f'A divisão do primeiro pelo segundo número é {divisao}\n')

# 6. Crie um programa que solicite dois valores numéricos ao usuário e imprima o resto da divisão do primeiro pelo o segundo valor.
print('=> Vamos dividir dois números inteiros e descobrir o resto!')

def calculadorDeResto() :
    numerador = int(input("Digite o numerador: "))
    denominador = int(input("Digite o denominador: "))
    if denominador == 0:
        print("O denominador não pode ser zero.\n")
        calculadorDeResto()
    else:
        resto = numerador % denominador
        print(f'O resto da divisão do primeiro pelo segundo número é {resto}\n')

calculadorDeResto()

# 7. Crie um programa que solicite dois valores numéricos ao usuário e imprima o resultado da exponenciação do primeiro pelo o segundo valor.
print('=> Vamos elevar um número a outro!')
base = input("Digite a base: ")
expoente = input("Digite o expoente: ")
exponenciacao = int(base) ** int(expoente)
print(f'O resultado da exponenciação é {exponenciacao}\n')

# 8. Crie um programa que solicite dois valores numéricos ao usuário e imprima o resultado da raiz quadrada do primeiro pelo o segundo valor.
print('=> Vamos calcular a raiz quadrada de um número!')
radicando = input("Digite o radicando: ")
raiz = int(radicando) ** (1 / 2)
print(f'A raiz quadrada do número é {raiz}\n')

# 9. Crie um programa que solicite dois valores numéricos ao usuário e imprima o resultado da raiz cúbica do primeiro pelo o segundo valor.
print('=> Vamos calcular a raiz cúbica de um número!')
radicando = input("Digite o radicando: ")
raiz = int(radicando) ** (1 / 3)
print(f'A raiz cúbica do número é {raiz}\n')

# 10. Crie um programa que solicite dois valores numéricos ao usuário e imprima o resultado da raiz enésima do primeiro pelo o segundo valor.
print('=> Vamos calcular a raiz enésima de um número!')
radicando = input("Digite o radicando: ")
indice  = input("Digite o índice: ")
raiz = int(radicando) ** (1 / int(indice))
print(f'A raiz enésima do número é {raiz}')

# 11. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
print('\n\n=> Vamos calcular a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4!\n')
notas = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]
media_ponderada = sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)
print(f'A média ponderada é: {media_ponderada}\n')

# # # UI - Controle de fluxo
print('\nAgora vamos estudar manipulação de strings em Python?')

controladorConfirmacao()


# 
# Editando textos
#

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo ao Hello World de manipulação de strings em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com algumas strings...\n\n')

# 1. Crie uma variável chamada frase e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = 'Hello World!'
print(f'=> Atividade 1: A frase digitada foi: {frase}\n')

# 2. Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input("Digite uma frase: ")
print(f'A frase digitada foi: {frase}\n')

# 3. Crie um código que solicite uma frase ao usuário e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input("Digite uma frase: ").upper()
print(f'A frase digitada transformada em uppercase é:\n{frase}\n')

# 4. Crie um código que solicite uma frase ao usuário e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input("Digite uma frase: ").lower()
print(f'A frase digitada transformada em lowercase é:\n{frase}\n')

# 5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = ' Hello World! '
print(f'=> Atividade 5: A frase digitada original é:\n{frase}\n')
frase = frase.strip()
print(f'A frase digitada trimmada é:\n{frase}\n')

# 6. Crie um código que solicite uma frase ao usuário e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input("Digite uma frase: ").strip()
print(f'A frase digitada trimmada é:\n{frase}\n')

# 7. Crie um código que solicite uma frase ao usuário e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input("Digite uma frase: ").strip().lower()
print(f'A frase digitada trimmada e transformada em lowercase é:\n{frase}\n')

# 8. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input("Digite uma frase: ").replace('e', 'f')
print(f'A frase digitada com as vogais "e" trocadas pela letra "f" é:\n{frase}\n')

# 9. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input("Digite uma frase: ").replace('a', '@')
print(f'A frase digitada com as vogais "a" trocadas pelo caractere "@" é:\n{frase}\n')

# 10. Crie um código que solicite uma frase ao usuário e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input("Digite uma frase: ").replace('s', '$')
print(f'A frase digitada com as consoantes "s" trocadas pelo caractere "$" é:\n{frase}\n')

# # # UI - Despedida
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Esse foi o nosso Hello World de manipulação de dados em Python!')
print('\nAté mais! \\o/')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')