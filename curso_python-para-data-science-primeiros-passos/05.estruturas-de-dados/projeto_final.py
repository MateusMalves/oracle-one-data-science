# Para rodar o código, basta executar o comando 'python3 projeto_final.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o uso de estruturas de dados, como as listas e os dicionários, a partir de algumas atividades. Agora que estamos avançando nos conteúdos, podemos tornar os desafios mais interessantes. Para isso, vamos trabalhar com projetos de código!

Primeiro, vamos solucionar alguns problemas para aquecer e nos prepararmos para os projetos.

Aquecendo na programação
1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].

4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

Momento dos projetos
7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

Escreva um código que calcule o total de vendas e o produto mais vendido.

12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos


Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

13) Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) funcionários(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().

15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de funcionários(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Sabendo que cada setor tem 10 funcionários(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
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
print('Bem vindo ao desafio Hello World final em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com tudo que vimos até agora...\n\n')

# 1. Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().
print('# 1 => Vamos calcular a média de gastos da empresa de papel\n')
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media_gastos = sum(gastos) / len(gastos)
print(f'Gastos:\n{gastos}')
print(f'\nA soma dos gastos é: {sum(gastos)}')
print(f'A média de gastos da empresa de papel é: R$ {media_gastos:.2f} reais.')

# 2. Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
print('\n\n# 2 => Vamos calcular quantas compras foram realizadas acima de 3000 reais\n')
gastos_acima_3000 = [gasto for gasto in gastos if gasto > 3000]
quantidade_acima_3000 = len(gastos_acima_3000)
porcentagem_acima_3000 = (quantidade_acima_3000 / len(gastos)) * 100
print(f'Foram realizadas {quantidade_acima_3000} compras acima de 3000 reais, o que representa {porcentagem_acima_3000:.2f}% do total de compras.')

# 3. Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
print('\n\n# 3 => Vamos coletar 5 números inteiros e imprimi-los')
def validar_numero_inteiro(numero):
    if re.match(numberRegex, numero):
        print(f'!! Número válido: {numero}')
        return int(numero)
    else:
        print('!! Número inválido. Tente novamente.')
        numero = input('\nDigite um número inteiro: ')
        return validar_numero_inteiro(numero)

numeros_inteiros = []
for _ in range(5):
    numero = input('\nDigite um número inteiro: ')
    numero = validar_numero_inteiro(numero)
    numeros_inteiros.append(numero)

print(f'\n=> A lista de números inteiros é: {numeros_inteiros}')

# 4. Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
print('\n\n# 4 => Vamos coletar mais 5 números inteiros e imprimi-los na ordem inversa')
numeros_inteiros_2 = []
for _ in range(5):
    numero = input('\nDigite um número inteiro: ')
    numero = validar_numero_inteiro(numero)
    numeros_inteiros_2.append(numero)

print(f'\nA lista de números inteiros coletados (ordem inversa) é: {numeros_inteiros_2[::-1]}')

# 5. Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
print('\n\n# 5 => Vamos criar uma lista com todos os números primos entre 1 e o número digitado')
def verificar_numero_primo(numero):
    numero = int(numero)
    if numero < 2:
        # print(f'!! O número {numero} não é primo.')
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            # print(f'!! O número {numero} não é primo.')
            return False
    print(f'!! O número {numero} é primo.')
    return True

numeros_primos = []
numero = validar_numero_inteiro(input('\nDigite um número inteiro: '))
for i in range(1, int(numero) + 1):
    if verificar_numero_primo(i):
        numeros_primos.append(i)

print(f'\nA lista de números primos entre 1 e {numero} é:\n{numeros_primos}')


# 6. Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
print('\n\n# 6 => Vamos validar uma data informando o dia, mês e ano')
def parsear_data(data):
    if re.match(r'^\d{2}-\d{2}-\d{4}$', data):
        dia, mes, ano = map(int, data.split('-'))
        return dia, mes, ano
    else:
        print('!! Formato de data inválido. Use o formato DD-MM-AAAA.')
        data = input('\nDigite a data (DD-MM-AAAA): ')
        return parsear_data(data)

def validar_data(data):
    dia, mes, ano = parsear_data(data)
    if mes < 1 or mes > 12:
        print('\n=> Mês inválido.')
        return False
    if dia < 1 or dia > 31:
        print('\n=> Dia inválido.')
        return False
    if mes == 2 and dia > 29:
        print('\n=> Dia inválido para fevereiro.')
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        print('\n=> Dia inválido para o mês informado.')
        return False
    print('\n=> Data válida.')
    return True

data = input('\nDigite a data (DD-MM-AAAA): ')
validar_data(data)



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
print('Bem vindo ao Hello World final de projetinhos em Python!')
print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')
print('Vamos brincar com algumas coisinhas daora...\n\n')

# 7. Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).
print('# 7 => Vamos calcular o percentual de crescimento de bactérias por dia')
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentuais_crescimento = []

for bacteria in bacterias:
    bacteria = int(bacteria * 1000)

for i in range(1, len(bacterias)):
    percentual = (bacterias[i] - bacterias[i - 1]) / bacterias[i - 1] * 100
    percentuais_crescimento.append(percentual)

for i in range(1, len(bacterias)):
    print('\n=> Bactérias:')
    print(f'Dia {i - 1}: {bacterias[i - 1]} || Dia {i}: {bacterias[i] * 1000}')
    print(f'Percentual de crescimento: {percentuais_crescimento[i - 1]:.2f}%')

# 8. Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
print('\n\n# 8 => Vamos separar os produtos alimentícios em doces e amargos')
def validar_id_produto(id_produto):
    if re.match(r'^\d+$', id_produto):
        print(f'!! ID de produto válido: {id_produto}')
        return int(id_produto)
    else:
        print('!! ID de produto inválido. Tente novamente.')
        id_produto = input('\nDigite o ID do produto: ').strip()
        return validar_id_produto(id_produto)

ids_produtos = []
for _ in range(10):
    id_produto = validar_id_produto(input('\nDigite o ID do produto: ').strip())
    ids_produtos.append(id_produto)

doces = [id_produto for id_produto in ids_produtos if id_produto % 2 == 0]
amargos = [id_produto for id_produto in ids_produtos if id_produto % 2 != 0]

print('\n=> Resultados:')
print(f'A lista de IDs dos produtos é: {ids_produtos}')
print(f'A quantidade de produtos doces (ID par) é: {len(doces)}')
print(f'A quantidade de produtos amargos (ID ímpar) é: {len(amargos)}')

# 9. Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

# Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

print('\n\n# 9 => Vamos corrigir a prova do(a) aluno(a)')
def validar_resposta(resposta):
    if resposta not in ['A', 'B', 'C', 'D']:
        print('!! Resposta inválida. Tente novamente.')
        resposta = input(f'\nQual a resposta da questão {i}? ').upper()
        return validar_resposta(resposta)
    return resposta

gabarito = {
    1: 'D',
    2: 'A',
    3: 'C',
    4: 'B',
    5: 'A',
    6: 'D',
    7: 'C',
    8: 'C',
    9: 'A',
    10: 'B'
}

respostas_aluno = {}
acertos = 0
erros = 0
for i in range(1, 11):
    resposta = validar_resposta(input(f'\nQual a resposta da questão {i}? ').upper())
    respostas_aluno[i] = resposta

for i, (gabarito_questao, resposta_aluno) in enumerate(zip(gabarito.values(), respostas_aluno.values()), start=1):
    print(f'\n=> Questão {i}:')
    print(f'Gabarito: {gabarito_questao} || Resposta do aluno: {resposta_aluno}')
    if gabarito_questao == resposta_aluno:
        acertos += 1
        print('Resposta correta!')
    else:
        erros += 1
        print('Resposta incorreta!')


print('\n=> Resultado final:')
print(f'Total de acertos: {acertos}')
print(f'Total de erros: {erros}')

# 10. Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
print('\n\n# 10 => Vamos calcular a média anual das temperaturas e mostrar as temperaturas acima da média anual')
def validar_temperatura(temperatura, mes):
    if re.match(numberRegex, temperatura):
        print(f'!! Temperatura válida: {temperatura}')
        return float(temperatura)
    else:
        print('!! Temperatura inválida. Tente novamente.')
        temperatura = input(f'\nDigite a temperatura média de {mes}: ')
        return validar_temperatura(temperatura, mes)

meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]
temperaturas = []
for mes in meses:
    temperatura = validar_temperatura(input(f'\nDigite a temperatura média de {mes}: '), mes)
    temperaturas.append(temperatura)

media_anual = sum(temperaturas) / len(temperaturas)
print(f'\n=> A média anual das temperaturas é: {media_anual:.2f} graus Celsius')

print('\n=> Temperaturas acima da média anual:')
for mes, temperatura in zip(meses, temperaturas):
    if temperatura > media_anual:
        print(f'{mes}: {temperatura:.2f} graus Celsius')

# 11. Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

# {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
#  'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

# Escreva um código que calcule o total de vendas e o produto mais vendido.
print('\n\n# 11 => Vamos calcular o total de vendas e o produto mais vendido')
vendas = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30
}
total_vendas = sum(vendas.values())
produto_mais_vendido = max(vendas, key=vendas.get)

print(f'\n=> Total de vendas: {total_vendas}')
print(f'Produto mais vendido: {produto_mais_vendido} com {vendas[produto_mais_vendido]} vendas')

# 12. Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos

# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
print('\n\n# 12 => Vamos calcular o design vencedor e a porcentagem de votos recebidos')
votos = {
    'Design 1': 1334,
    'Design 2': 982,
    'Design 3': 1751,
    'Design 4': 210,
    'Design 5': 1811
}

total_votos = sum(votos.values())
design_vencedor = max(votos, key=votos.get)
porcentagem_votos = (votos[design_vencedor] / total_votos) * 100
print(f'\n=> Design vencedor: {design_vencedor} com {votos[design_vencedor]} votos')
print(f'Porcentagem de votos recebidos: {porcentagem_votos:.2f}%')

# 13. Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) funcionários(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
print('\n\n# 13 => Vamos calcular o total de gastos com o abono e quantos(as) funcionários(as) receberam o abono mínimo')
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}
abono_minimo = 200
total_gastos = 0
quantidade_abono_minimo = 0
maior_abono = 0

for salario in salarios:
    abono = max(round(salario * 0.10, 2), abono_minimo)
    abonos[salario] = abono
    total_gastos += abono
    if abono == abono_minimo:
        quantidade_abono_minimo += 1
    if abono > maior_abono:
        maior_abono = abono

print(f'\n=> Abonos:\n{abonos}')
print(f'\n=> Relatório de abonos:')
print(f'Total de gastos com o abono: R$ {total_gastos:.2f}')
print(f'Quantidade de funcionários(as) que receberam o abono mínimo: {quantidade_abono_minimo}')
print(f'Maior valor de abono fornecido: R$ {maior_abono:.2f}')

# 14. Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

# {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}

# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
print('\n\n# 14 => Vamos calcular a média de espécies por área e identificar a área com a maior diversidade biológica')
areas = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

total_especies_areas = {area: sum(especies) for area, especies in areas.items()}
media_especies = sum(total_especies_areas.values()) / len(total_especies_areas)
area_maior_diversidade = max(total_especies_areas, key=total_especies_areas.get)

print(f'\n=> Areas:\n{areas}')
print(f'\n=> Total de espécies por área:\n{total_especies_areas}')
print(f'\n=> Média de espécies por área: {media_especies:.2f}')
print(f'\n=> Área com a maior diversidade biológica: {area_maior_diversidade}')
  
# 15. O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de funcionários(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Sabendo que cada setor tem 10 funcionários(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
print('\n\n# 15 => Vamos calcular a média de idade de cada setor e a idade média geral entre todos os setores')
setores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

media_idade_setores = {setor: sum(idades) / len(idades) for setor, idades in setores.items()}
media_idade_geral = sum(media_idade_setores.values()) / len(media_idade_setores)
quantidade_acima_media = sum(1 for idades in setores.values() for idade in idades if idade > media_idade_geral)

print(f'\n=> Média de idade de cada setor:')
for setor, media_idade in media_idade_setores.items():
    print(f'{setor}: {media_idade:.2f}')
print(f'\n=> Idade média geral entre todos os setores: {media_idade_geral:.2f}')
print(f'Quantidade de pessoas acima da idade média geral: {quantidade_acima_media}')

print('\n\n=> Esse foi nosso projeto final Hello World em Python!\n')
print('Espero que tenha gostado!')
print('Até a próxima!')