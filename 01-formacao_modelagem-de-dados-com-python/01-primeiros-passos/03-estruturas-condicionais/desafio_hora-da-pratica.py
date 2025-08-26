# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o uso de estruturas condicionais como o if, else e elif a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes: vamos trabalhar com projetos de código! Solucione os problemas de aquecimento para se preparar para os projetos:

Aquecendo na programação
1) Escreva um programa que peça ao usuário para fornecer dois números e exibir o número maior.

2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

3) Escreva um programa que determine se uma letra fornecida pelo usuário é uma vogal ou consoante.

4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

6) Escreva um programa que leia três números e os exiba em ordem decrescente.

7) Escreva um programa que pergunte em qual turno ao usuário estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

8) Escreva um programa que peça um número inteiro ao usuário e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

9) Escreva um programa que peça um número ao usuário e informe se ele é inteiro ou decimal.

Momento dos projetos
10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar ao usuário qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

11) Escreva um programa que peça ao usuário três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes.
12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

Para variação acima de 20%: bonificação para o time de vendas.
Para variação entre 2% e 20%: pequena bonificação para time de vendas.
Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
Para bonificações abaixo de -10%: corte de gastos.
'''

# # # # #
# # # Desafios resolvidos
# # # # #

# 
# Aquecendo na programação
# 

print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Bem vindo ao Hello World de condicionais em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com algumas condicionais...\n\n')

# 1. Escreva um programa que peça ao usuário para fornecer dois números e exibir o número maior.
print('# 1 => Digite dois números e descubra qual é o maior!\n')
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
if numero_1 > numero_2:
    print(f"\n=> O número {numero_1} é maior que o número {numero_2}.")
else:
    print(f"\n=> O número {numero_2} é maior que o número {numero_1}.")

# 2. Escreva um programa que peça ao usuário para fornecer seu nome e idade. Se ao usuário tiver menos de 18 anos, exiba a frase "Você é menor de idade." Caso contrário, exiba a frase "Você é maior de idade.".
print('\n\n# 2 => Digite seu nome e idade e descubra se é maior de idade ou não!\n')
nome = input("Digite seu nome: ").capitalize()
idade = int(input("Digite sua idade: "))
if idade < 18:
    print(f"\n=> Olá {nome}, você é menor de idade.")
else:
    print(f"\n=> Olá {nome}, você é maior de idade.")

# 3. Escreva um programa que determine se uma letra fornecida pelo usuário é uma vogal ou consoante.
print('\n\n# 3 => Digite uma letra e descubra se é uma vogal ou consoante!\n')
letra = input("Digite uma letra: ")
if letra in 'aeiou':
    print(f"\n=> A letra '{letra}' é uma vogal.")
else:
    print(f"\n=> A letra '{letra}' é uma consoante.")

# 4. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.
print('\n\n# 4 => Digite os preços médios do Fusca nos últimos 3 anos e descubra o mais alto e o mais baixo!\n')
preco_1 = int(input("Digite o preço médio do Fusca no primeiro ano: "))
preco_2 = float(input("Digite o preço médio do Fusca no segundo ano: "))
preco_3 = float(input("Digite o preço médio do Fusca no terceiro ano: "))
'''
# Forma mais eficaz de fazer essa comparação, built-in do Python
preco_maior = max(preco_1, preco_2, preco_3)
preco_menor = min(preco_1, preco_2, preco_3)
'''
if preco_1 > preco_2 and preco_1 > preco_3:
    preco_maior = preco_1
elif preco_1 < preco_2 and preco_1 < preco_3:
    preco_menor = preco_1
if preco_2 > preco_1 and preco_2 > preco_3:
    preco_maior = preco_2
elif preco_2 < preco_1 and preco_2 < preco_3:
    preco_menor = preco_2
if preco_3 > preco_1 and preco_3 > preco_2:
    preco_maior = preco_3
elif preco_3 < preco_1 and preco_3 < preco_2:
    preco_menor = preco_3
print(f"\n=> O preço mais alto é {preco_maior} e o preço mais baixo é {preco_menor}.")

# 5. Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.
print('\n\n# 5 => Digite os preços de 3 produtos e descubra qual é o mais barato!\n')
preco_1 = float(input("Digite o preço do primeiro produto: ").replace(',', '.'))
preco_2 = float(input("Digite o preço do segundo produto: ").replace(',', '.'))
preco_3 = float(input("Digite o preço do terceiro produto: ").replace(',', '.'))
'''
# Forma mais eficaz de fazer essa comparação, built-in do Python
preco_menor = min(preco_1, preco_2, preco_3)
'''
if preco_1 < preco_2 and preco_1 < preco_3:
    print(f"\n=> O produto mais barato é o primeiro, que custa R$ {preco_1:.2f}.")
elif preco_2 < preco_1 and preco_3:
    print(f"\n=> O produto mais barato é o segundo, que custa R$ {preco_2:.2f}.")
elif preco_3 < preco_1 and preco_3 < preco_2:
    print(f"\n=> O produto mais barato é o terceiro, que custa R$ {preco_3:.2f}.")

# 6. Escreva um programa que leia três números e os exiba em ordem decrescente.
print('\n\n# 6 => Digite três números aleatórios e os veja em ordem decrescente!\n')
numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))
print()
if numero_1 > numero_2 and numero_1 > numero_3:
    print(numero_1)
    if numero_2 > numero_3:
        print(numero_2)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_2)
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(numero_2)
    if numero_1 > numero_3:
        print(numero_1)
        print(numero_3)
    else:
        print(numero_3)
        print(numero_1)
else:
    print(numero_3)
    if numero_1 > numero_2:
        print(numero_1)
        print(numero_2)
    else:
        print(numero_2)
        print(numero_1)

# 7. Escreva um programa que pergunte em qual turno ao usuário estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.
print('\n\n# 7 => Digite o turno em que você estuda e receba um elogio!')
def saudar():
    turno = input("\nDigite o turno em que você estuda (manhã, tarde ou noite): ").lower().replace('ã', 'a')
    if turno == 'manha':
        print("\n=> Bom dia!")
        print('Parabéns pela sua dedicação aos estudos!')
    elif turno == 'tarde':
        print("\n=> Boa tarde!")
        print('Parabéns pela sua dedicação aos estudos!')
    elif turno == 'noite':
        print("\n=> Boa noite!")
        print('Parabéns pela sua dedicação aos estudos!')
    else:
        print("\n=> Valor inválido!")
        print('Tente novamente!')
        saudar()

saudar()

# 8. Escreva um programa que peça um número inteiro ao usuário e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.
print('\n\n# 8 => Digite um número inteiro e descubra se ele é par ou ímpar!\n')
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"\n=> O número {numero} é par.")
else:
    print(f"\n=> O número {numero} é ímpar.")

# 9. Escreva um programa que peça um número ao usuário e informe se ele é inteiro ou decimal.
print('\n\n# 9 => Digite um número e descubra se ele é inteiro ou decimal!\n')
numero = float(input("Digite um número: "))
if numero == int(numero):
    print(f"\n=> O número {numero} é inteiro.")
else:
    print(f"\n=> O número {numero} é decimal.")

# # # UI - Controle de fluxo
print('\nAgora vamos ver algumas coisas mais emocionantes?')

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
print('Bem vindo ao Hello World de projetinhos em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com algumas coisinhas daora...\n\n')

# 10. Um programa deve ser escrito para ler dois números e, em seguida, perguntar ao usuário qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

print('# 10 => Digite dois números e faça uma operação aritmética com eles\n')
def operacao_aritmetica(numero_1, numero_2):
    operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")
    if operacao == '+':
        resultado = numero_1 + numero_2
        print(f"\n=> {numero_1} + {numero_2} = {resultado}.")
    elif operacao == '-':
        resultado = numero_1 - numero_2
        print(f"\n=> {numero_1} - {numero_2} = {resultado}.")
    elif operacao == '*':
        resultado = numero_1 * numero_2
        print(f"\n=> {numero_1} * {numero_2} = {resultado}.")
    elif operacao == '/':
        resultado = numero_1 / numero_2
        print(f"\n=> {numero_1} / {numero_2} = {resultado}.")
    else:
        print("Operação inválida!\n")
        resultado = operacao_aritmetica(numero_1, numero_2)
    return resultado

def exibirDetalhesDoNumero(numero):
    detalhes = f'=> O número {numero} é'
    detalhes += f' {"par" if numero % 2 == 0 else "ímpar"},'
    detalhes += f' {"positivo" if numero > 0 else "negativo"} e'
    detalhes += f' {"inteiro" if numero % 1 == 0 else "decimal"}.\n'
    print(detalhes)

numero_1 = float(input("Digite o primeiro número: ").replace(',', '.'))
exibirDetalhesDoNumero(numero_1)
numero_2 = float(input("Digite o segundo número: ").replace(',', '.'))
exibirDetalhesDoNumero(numero_2)
resultado = operacao_aritmetica(numero_1, numero_2)
print(f"=> O resultado da operação é {resultado}.")
exibirDetalhesDoNumero(resultado)
    

# # 11. Escreva um programa que peça ao usuário três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# # Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# # Triângulo Equilátero: três lados iguais;
# # Triângulo Isósceles: quaisquer dois lados iguais;
# # Triângulo Escaleno: três lados diferentes.

print('\n# 11 => Digite três números e descubra se eles podem formar um triângulo e qual tipo de triângulo é!\n')
def tipo_triangulo(lado_1, lado_2, lado_3):
    if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3 > lado_1:
        if lado_1 == lado_2 == lado_3:
            print("\n=> O triângulo é equilátero.")
        elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            print("\n=> O triângulo é isósceles.")
        else:
            print("\n=> O triângulo é escaleno.")
    else:
        print("\n=> Os lados informados não formam um triângulo.")

lado_1 = float(input("Digite o primeiro lado do triângulo: "))
lado_2 = float(input("Digite o segundo lado do triângulo: "))
lado_3 = float(input("Digite o terceiro lado do triângulo: "))
tipo_triangulo(lado_1, lado_2, lado_3)

# 12. Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.

print('\n\n# 12 => Bem vindo ao posto baratão dos combustíveis!\n')
print('Descontos espetaculares! Confira:')
print('Etanol: 2% até 15 litros, 4% acima de 15 litros')
print('Diesel: 3% até 15 litros, 5% acima de 15 litros')
print('\nNossos preços:')
print('Etanol: R$ 1,70 por litro')
print('Diesel: R$ 2,00 por litro')
print('\n=> O que você gostaria de abastecer hoje?')
print('\nDigite o tipo de combustível e a quantidade de litros que deseja abastecer:')

def processar_compra(tipo_combustivel, quantidade_litros):
    # Cálculo do desconto e preço final
    preco_litro = 1.70 if tipo_combustivel == 'Etanol' else 2.0
    percentual_desconto = 0.02 if tipo_combustivel == 'Etanol' and quantidade_litros <= 15 else 0.04 if tipo_combustivel == 'Etanol' else 0.03 if tipo_combustivel == 'Diesel' and quantidade_litros <= 15 else 0.05

    preco_sem_desconto = preco_litro * quantidade_litros
    desconto = preco_sem_desconto * percentual_desconto
    preco_com_desconto = preco_sem_desconto - desconto

    # Exibição dos resultados
    print('\n=> Informações da compra:\n')
    print(f'Tipo de combustível adquirido: {tipo_combustivel}.')
    print(f'Preço por litro: R${preco_litro:.2f}.')
    print(f'Quantidade de litros: {quantidade_litros:.2f} litros.\n')
    print(f'Valor total da compra: R${preco_sem_desconto:.2f}.')
    print(f'Percentual de desconto: {percentual_desconto * 100:.2f}%.')
    print(f'Valor do desconto: R${desconto:.2f}.')
    print(f'Valor final: R${preco_com_desconto:.2f}.')
    print('\n=> Obrigado pela preferência!')

# Validação e formatação dos dados de entrada
def validarDados(tipo_combustivel, quantidade_litros):
    import re
    numberRegex = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    if tipo_combustivel:
        if tipo_combustivel not in ['E', 'D']:
            print('!! Tipo de combustível inválido.\n')
            tipo_combustivel = validarDados(input('Digite E para etanol ou D para diesel: ').upper(), False)
            return tipo_combustivel
        else:
            return tipo_combustivel
    if quantidade_litros:
        if re.match(numberRegex, quantidade_litros.strip()) is None:
            print('!! Quantidade de litros inválida. Por favor, digite um valor maior que zero.\n')
            quantidade_litros = validarDados(False, input('Digite a quantidade de litros: ').strip().replace(',', '.'))
            return quantidade_litros
        else:
            return quantidade_litros
    
tipo_combustivel = validarDados(input('Digite E para etanol ou D para diesel: ').upper(), False)
tipo_combustivel = 'Etanol' if tipo_combustivel == 'E' else 'Diesel'
print(f'Combustível: {tipo_combustivel}\n')
quantidade_litros = validarDados(False, input('Digite a quantidade de litros: ').strip().replace(',', '.'))
quantidade_litros = float(quantidade_litros)
print(f'Quantidade: {quantidade_litros:.2f} litros')

processar_compra(tipo_combustivel, quantidade_litros)

# 13. Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para bonificações abaixo de -10%: corte de gastos.

print('\n\n# 13 => Bem vindo ao sistema de análise de vendas!\n')

def calcular_variacao_percentual(vendas_2022, vendas_2023):
    # Converte as vendas para números inteiros
    vendas_2022 = int(vendas_2022)
    vendas_2023 = int(vendas_2023)

    # Calcula a variação percentual
    variacao_percentual = ((vendas_2023 - vendas_2022) / vendas_2022) * 100
    return variacao_percentual

def sugerir_acoes(variacao_percentual):
    # Define as ações com base na variação percentual
    if variacao_percentual > 20:
        return 'Ação sugerida: Bonificação para o time de vendas.'
    elif 2 <= variacao_percentual <= 20:
        return 'Ação sugerida: Pequena bonificação para time de vendas.'
    elif -10 <= variacao_percentual < 2:
        return 'Ação sugerida: Planejamento de políticas de incentivo às vendas.'
    else:
        return 'Ação sugerida: Corte de gastos.'

print('=> Digite os dados das vendas dos anos 2022 e 2023')
vendas_2022 = input('Digite a quantidade de vendas do ano de 2022: ')
vendas_2023 = input('Digite a quantidade de vendas do ano de 2023: ')
variacao_percentual = calcular_variacao_percentual(vendas_2022, vendas_2023)
print(f'\n=> Vendas 2022: R$ {vendas_2022} || Vendas 2023: R$ {vendas_2023} || Variação percentual: {variacao_percentual:.2f}%')
print(sugerir_acoes(variacao_percentual))