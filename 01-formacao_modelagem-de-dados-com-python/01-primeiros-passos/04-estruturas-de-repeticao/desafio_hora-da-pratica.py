# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o uso de estruturas de repetição como o while e o for a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes. Para isso, vamos trabalhar com projetos de código!

Primeiro, vamos solucionar alguns problemas para aquecer e nos prepararmos para os projetos.

Aquecendo na programação
1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

3) Para tratar uma quantidade de 15 dados de avaliações de usuários de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que o usuário insira um valor válido.

4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

Momento dos projetos
6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha do usuário. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20
Copiar código
7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

9) Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

Cada funcionário(a) votou em um dos quatro candidatos (que representamos pelos números 1, 2, 3 e 4).
Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
'''

# # # # #
# # # Desafios resolvidos
# # # # #

import re
numberRegex = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'

# 
# Aquecendo na programação
# 

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo ao Hello World de loops em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com alguns loops...\n\n')

# 1. Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
print('# 1 => Insira dois números inteiros e veja todos os números inteiros entre eles.\n')
def printar_numeros(num1, num2):
    numeros = []
    if num1 == num2:
        print('!! Os números são iguais. Não há números entre eles.')
        num1 = int(input('\nInsira o primeiro número inteiro: '))
        num2 = int(input('Insira o segundo número inteiro: '))
        printar_numeros(num1, num2)
        return
    elif num1 > num2:
        num1, num2 = num2, num1
    for i in range(num1 + 1, num2):
        numeros.append(i)
    print(f'\n=> Os números inteiros entre {num1} e {num2} são:\n{numeros}')

num1 = int(input('Insira o primeiro número inteiro: '))
num2 = int(input('Insira o segundo número inteiro: '))
printar_numeros(num1, num2)

# 2. Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
print('\n\n# 2 => Vamos calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B.')
def calcular_dias_para_ultrapassar(colonia_a, colonia_b):
    dias = 0
    while colonia_a < colonia_b:
        colonia_a *= 1.03
        colonia_b *= 1.015
        dias += 1
    return dias, colonia_a, colonia_b

colonia_a_inicio = 4
colonia_b_inicio = 10
dias, colonia_a_fim, colonia_b_fim = calcular_dias_para_ultrapassar(colonia_a_inicio, colonia_b_inicio)
print('Início da observação:')
print(f'\nColônia A: {colonia_a_inicio:.2f} | Colônia B: {colonia_b_inicio:.2f}')
print(f'Levará {dias} dias para a colônia A ultrapassar ou igualar a colônia B.\n')
print(f'Final da observação (após {dias} dias):')
print(f'Colônia A: {colonia_a_fim:.2f} | Colônia B: {colonia_b_fim:.2f}')

# 3. Para tratar uma quantidade de 15 dados de avaliações de usuários de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que o usuário insira um valor válido.
print('\n\n# 3 => Vamos verificar se as notas são válidas.\n')
def verificar_notas_validas(nota):
    if re.match(numberRegex, nota):
        nota = float(nota)
        if nota >= 0 and nota <= 5:
            print('=> Nota válida.')
            return nota
        else:
            print('!! Nota inválida. Tente novamente.\n')
            nota = verificar_notas_validas(input(f'Insira uma nota de 0 a 5 (digite "quit" para sair): ').replace(',', '.'))
            return nota
    else:
        print('!! Nota inválida. Tente novamente.\n')
        nota = verificar_notas_validas(input(f'Insira uma nota de 0 a 5 (digite "quit" para sair): ').replace(',', '.'))
        return nota

notas = []
for i in range(15):
    nota = input(f'Insira uma nota de 0 a 5 (digite "quit" para sair): ').replace(',', '.')
    if nota.upper() == 'QUIT':
        break
    nota = verificar_notas_validas(nota)
    nota = round(nota, 2)
    print(f'Nota {i + 1}: {nota}\n')
    notas.append(nota)

if notas:
    print(f'\n=> Notas válidas: {notas}')
    print(f'=> Média das notas: {sum(notas) / len(notas)}')
else:
    print('!! Nenhuma nota válida foi inserida.')

# 4. Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
print('\n\n# 4 => Vamos ler um conjunto indeterminado de temperaturas em Celsius e informar a média delas.\n')
def verificar_temperaturas_validas(temperatura):
    if temperatura is not None and re.match(numberRegex, temperatura):
        temperatura = float(temperatura)
        print('=> Tempeartura válida.\n')
        return temperatura
    else:
        print('!! Temperatura inválida. Tente novamente.\n')
        temperatura = verificar_temperaturas_validas(input(f'Insira uma temperatura em Celsius (-273 para encerrar): ').replace(',', '.'))
        return temperatura

def calcular_media_temperaturas(temperaturas):
    if len(temperaturas) == 0:
        print('!! Nenhuma temperatura válida foi inserida.')
        return None
    else:
        media = sum(temperaturas) / len(temperaturas)
        return media
    
temperaturas = []
temperaturas_formatadas = []
while True:
    temperatura = input('Insira uma temperatura em Celsius (-273 para encerrar): ').replace(',', '.')
    temperatura = verificar_temperaturas_validas(temperatura)
    temperaturas.append(round(temperatura, 4))
    temperaturas_formatadas.append(f'{round(temperatura, 2)}°C')
    if temperatura == -273:
        break

media = calcular_media_temperaturas(temperaturas)
print(f'\n=> Temperaturas válidas: {temperaturas_formatadas}')
print(f'=> Média das temperaturas: {media}°C')

# 5. Escreva um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
print('\n\n# 5 => Vamos calcular o fatorial de um número inteiro positivo.\nLimite: Até 12\n')
def calcular_fatorial(numero):
    if re.match(numberRegex, numero):
        numero = int(numero)
        print(numero)
        if numero > 12:
            print('!! O número é muito grande. Tente um número menor que 13.\n')
            numero = calcular_fatorial(input('Insira um número inteiro positivo: '))
            return numero
        if numero < 0:
            print('!! Fatorial não definido para números negativos.\n')
            numero = calcular_fatorial(input('Insira um número inteiro positivo: '))
            return numero
        elif numero == 0 or numero == 1:
            return numero, 1
        else:
            fatorial = 1
            for i in range(2, numero + 1):
                fatorial *= i
            return numero, fatorial
    else:
        print('!! Número inválido. Tente novamente.\n')
        numero = calcular_fatorial(input('Insira um número inteiro positivo: '))
        return numero

numero = input('Insira um número inteiro positivo: ').replace(',', '.')
numero, fatorial = calcular_fatorial(numero)
print(f'\n=> O fatorial de {numero} é: {fatorial}')

# # # UI - Controle de fluxo
print('\n\nAgora vamos ver algumas coisas mais emocionantes?')

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
# Momento dos projetos
# 

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo ao Hello World de projetinhos com loops em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com algumas coisinhas daora...\n\n')

# 6. Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha do usuário. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20
print('# 6 => Vamos gerar a tabuada de um número inteiro de 1 a 10.\n')
def gerar_tabuada(numero):
    if numero is not None and re.match(numberRegex, numero):
        numero = int(numero)
        print(f'=> Tabuada do {numero}:')
        for i in range(1, 11):
            resultado = numero * i
            print(f'{numero} x {i} = {resultado}')
    else:
        print('!! Número inválido. Tente novamente.\n')
        numero = gerar_tabuada(input('Insira um número inteiro: ').replace(',', '.'))
        return numero

numero = input('Insira um número inteiro: ').replace(',', '.')
numero = gerar_tabuada(numero)

# 7. Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
print('\n\n# 7 => Vamos verificar se um número é primo.\n')
def verificar_numero_primo(numero):
    if numero is not None and re.match(numberRegex, numero):
        numero = int(numero)
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True
    else:
        print('!! Número inválido. Tente novamente.\n')
        numero = verificar_numero_primo(input('Insira um número inteiro: ').replace(',', '.'))
        return numero

numero = input('Insira um número inteiro: ').replace(',', '.')
isPrimo = verificar_numero_primo(numero)
if isPrimo:
    print(f'=> O número {numero} é primo.')
else:
    print(f'=> O número {numero} não é primo.')

# 8. Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
print('\n\n# 8 => Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência.\n')
def verificar_idade_valida(idade):
    if idade is not None and re.match(numberRegex, idade):
        idade = int(idade)
        return idade
    else:
        print('!! Idade inválida. Tente novamente.\n')
        idade = verificar_idade_valida(input('Insira uma idade (número negativo para encerrar): ').replace(',', '.'))
        return idade

def calcular_distribuicao_idades(idades):
    if len(idades) == 0:
        return None
    else:
        distribuicao = {
            '[0-25]': 0,
            '[26-50]': 0,
            '[51-75]': 0,
            '[76-100]': 0
        }
        for idade in idades:
            if idade < 26:
                distribuicao['[0-25]'] += 1
            elif idade < 51:
                distribuicao['[26-50]'] += 1
            elif idade < 76:
                distribuicao['[51-75]'] += 1
            elif idade < 101:
                distribuicao['[76-100]'] += 1
        return distribuicao

idades = []
while True:
    idade = input('Insira uma idade (número negativo para encerrar): ').replace(',', '.')
    idade = verificar_idade_valida(idade)
    if idade < 0:
        break
    if idade > 100:
        print('!! Idade inválida. Insira uma idade até 100 anos\n')
        idade = verificar_idade_valida(input('Insira uma idade (número negativo para encerrar): ').replace(',', '.'))
        continue
    print('=> Idade válida.')
    print(f'Idade: {idade}\n')
    idades.append(int(idade))

distribuicao = calcular_distribuicao_idades(idades)
if distribuicao is None:
    print('!! Nenhuma idade válida foi inserida.')
else:
    print(f'\n=> Distribuição de idades:')
    print(f'[0-25]: {distribuicao["[0-25]"]}')
    print(f'[26-50]: {distribuicao["[26-50]"]}')
    print(f'[51-75]: {distribuicao["[51-75]"]}')
    print(f'[76-100]: {distribuicao["[76-100]"]}')

# 9. Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada funcionário(a) votou em um dos quatro candidatos (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).

# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
print('\n\n# 9 => Vamos calcular o(a) vencedor(a) da eleição.\n')
def validar_voto(voto):
    if voto is not None and re.match(numberRegex, voto):
        voto = int(voto)
        if voto < 1 or voto > 6:
            print('!! Voto inválido. Tente novamente.\n')
            voto = validar_voto(input('Insira seu voto de 1 a 6 (5 para nulo e 6 para branco): ').replace(',', '.'))
            return voto
        else:
            print('=> Voto válido.')
            if voto == 5:
                print('Voto nulo.\n')
            elif voto == 6:
                print('Voto em branco.\n')
            else:
                print(f'Voto para o candidato {voto}.\n')
            return voto
    else:
        print('!! Voto inválido. Tente novamente.\n')
        voto = validar_voto(input('Insira seu voto de 1 a 6 (5 para nulo e 6 para branco): ').replace(',', '.'))
        return voto

def processar_resultados(votos):
    if len(votos) == 0:
        print('!! Nenhum voto válido foi inserido.')
        return None
    else:
        total_votos = len(votos)
        votos_validos = [voto for voto in votos if voto != 5 and voto != 6]
        votos_nulos = votos.count(5)
        votos_brancos = votos.count(6)
        candidatos = [1, 2, 3, 4]
        resultados = {candidato: votos_validos.count(candidato) for candidato in candidatos}
        vencedor = max(resultados, key=resultados.get)
        porcentagem_candidatos = {candidato: (resultados[candidato] / total_votos) * 100 for candidato in candidatos}
        porcentagem_nulos = (votos_nulos / total_votos) * 100
        porcentagem_brancos = (votos_brancos / total_votos) * 100
        dados_eleicao = {
            'total_votos': total_votos,
            'votos_validos': votos_validos,
            'resultados': resultados,
            'vencedor': vencedor,
            'votos_nulos': votos_nulos,
            'votos_brancos': votos_brancos,
            'porcentagem_candidatos': porcentagem_candidatos,
            'porcentagem_nulos': porcentagem_nulos,
            'porcentagem_brancos': porcentagem_brancos
        }
        return dados_eleicao

def apresentar_resultados(dados_eleicao):
    print('\n=> Resultados da eleição:\n')
    print(f'O(a) vencedor(a) é o(a) candidato(a): {dados_eleicao["vencedor"]}')
    print(f'Número total de votos: {dados_eleicao["total_votos"]}')
    print(f'Número total de votos válidos: {len(dados_eleicao["votos_validos"])}\n')
    for candidato, votos in dados_eleicao['resultados'].items():
        print(f'Votos para o candidato {candidato}: {votos} ({dados_eleicao["porcentagem_candidatos"][candidato]:.2f}%)')
    print(f'Votos nulos: {dados_eleicao["votos_nulos"]} ({dados_eleicao["porcentagem_nulos"]:.2f}%)')
    print(f'Votos em branco: {dados_eleicao["votos_brancos"]} ({dados_eleicao["porcentagem_brancos"]:.2f}%)')

    print('\n=> Percentuais relativos à quantidade total de votos *')

votos = []
for i in range(20):
    voto = input(f'Insira seu voto de 1 a 6 (5 para nulo e 6 para branco): ').replace(',', '.')
    voto = validar_voto(voto)
    if voto == 'quit':
        break
    votos.append(int(voto))

dados_eleicao = processar_resultados(votos)
apresentar_resultados(dados_eleicao)

print('\n\n=> Esse foi nosso Hello World de loops em Python!\n')
print('Espero que tenha gostado!')
print('Até a próxima!')