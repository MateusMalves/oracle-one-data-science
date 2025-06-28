# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import os
import sys
import re
import math
import numpy as np
import pandas as pd
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poisson
from scipy.stats import norm

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/02-estatistica-com-python_probabilidade-e-amostragem'
outputs_folder = data_folder + 'outputs/'

data = load_data(f'{data_folder}/dados.csv', is_pandas=True)

# # # Section of the course:
# 01. Distribuição binomial
# # #

# Combination 60 x 6 to 6, mega-sena
combinations = comb(60, 6)
probability = 1 / combinations
print('%0.15f' % probability)
print(probability * (probability ** 6) * ((1 - probability) ** 54))

# Show de premios Alura
# Suponha que acabamos de criar um jogo de loteria, chamado Show de prêmios da Alura. Neste nosso novo jogo, o apostador marca 20 números, dentre os 25 disponíveis no bilhete, e pode ganhar até 1 milhão de reais.

# Determine qual o número de combinações possíveis (espaço amostral) e a probabilidade de se ganhar o prêmio jogando apenas um bilhete (considere apenas quinze casas decimais).

print(comb(25, 20)) # Combinations
print('%0.15f' % (1 / comb(25, 20))) # Probability

# Em um concurso para preencher uma vaga de cientista de dados temos um total de **10 questões** de múltipla escolha com **3 alternativas possíveis** em cada questão. **Cada questão tem o mesmo valor.** Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova **vale 10 pontos e a nota de corte seja 5**, obtenha a probabilidade deste candidato **acertar 5 questões** e também a probabilidade deste candidato **passar para a próxima etapa do processo seletivo**.

# Number of trials
n = 10
# Sucess probability
alternatives = 3
p = 1 / alternatives
# Fail probability
q = 1 - p
# Number of successes needed
k = 5

# Probability of 5 sucesses
probability = (comb(n, k) * (p ** k) * (q ** (n - k)))
probability = binom.pmf(k, n, p)

# Probability of passing
probability = binom.pmf([k, k+1, k+2, k+3, k+4, k+5], n, p).sum()
probability = 1 - binom.cdf(4, n, p)
probability = binom.sf(4, n, p)

# Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. Na última gincana se sabe que a **proporção de participantes do sexo feminino foi de 60%**. **O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30**. Com as informações acima responda: Quantas equipes deverão ser formadas por **8 mulheres**?

# Probability for individual teams with 8 women
n_team = 12
p = 0.6
k = 8
probability = binom.pmf(k, n_team, p)

# Average of binomial distribution for 30 teams
n_teams = 30
expected_value = n_teams * probability

# Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?

# Probability per family
n_kids = 3
p = 0.22
k = 2

probability = binom.pmf(k, n_kids, p)

n_families = 50
expected_value = n_families * probability


# # # Section of the course:
# 02. Distribuição de Poisson
# # #

# Um restaurante recebe em média **20 pedidos por hora**. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba **15 pedidos**?
mi = 20
k = 15
e = np.e

probability = (e ** (-mi)) * (mi ** k) / (math.factorial(k))
print('%0.8f' % probability)

# Built-in way
probability = poisson.pmf(k, mi)
print('%0.8f' % probability)

# O número médio de clientes que entram em uma padaria por hora é igual a 20. Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes.
probability = poisson.pmf(25, 20)


# # # Section of the course:
# 03. Distribuição normal
# # #

# Z-score table
tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

# Problema:
# Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma **distribuição aproximadamente normal**, com **média 1,70** e **desvio padrão de 0,1**. Com estas informações obtenha o seguinte conjunto de probabilidades:

# > **A.** probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

# > **B.** probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

# > **C.** probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

def calculate_Z(x, mean, std):
    return (x - mean) / std

def get_probability(Z):
    split = str(Z).split('.') if str(Z)[0] != '-' else str(abs(Z)).split('.')
    integer = split[0]
    decimal = split[1]
    if len(decimal) < 2:
        decimal = decimal + '0'
    
    index = integer + '.' + decimal[0] + '0'
    column = '0.0' + decimal[1]

    probability = tabela_normal_padronizada.loc[index][column]
    if isinstance(probability, pd.Series):
        probability = probability.iloc[0]
    return float(probability) if Z >= 0 else 1 - float(probability)

mean = 1.7
std = 0.1

# A
z = calculate_Z(1.8, mean, std)
probability = get_probability(z)
norm.cdf(z) # Built-in way using scipy

# B
z1 = calculate_Z(1.6, mean, std)
z2 = calculate_Z(1.8, mean, std)
probability = get_probability(z2) - get_probability(z1)
probability = (get_probability(z2) - 0.5) * 2 # Another way, valid because the distance between the mean and both z1 and z2 are the same (0.1)

probability = norm.cdf(z2) - norm.cdf(z1) # Built-in way using scipy
probability = norm.cdf(z2) - (1 - norm.cdf(z2)) # Another way, valid because the distance between the mean and both z1 and z2 are the same (0.1)

# C
z = calculate_Z(1.9, mean, std)
probability = 1 - get_probability(z)
probability = 1 - norm.cdf(z) # Built-in way using scipy
probability = norm.cdf(-z) # Smarter way


# Problema:
# A aplicação de uma prova de estatística em um concurso apresentou um conjunto de notas normalmente distribuídas. Verificou-se que o conjunto de notas tinha média 70 e desvio padrão de 5 pontos.

# Qual a probabilidade de um aluno, selecionado ao acaso, ter nota menor que 85?
z = calculate_Z(85, 70, 5)
probability = norm.cdf(z)


# Problema
# O faturamento diário de um motorista de aplicativo segue uma distribuição aproximadamente normal, com média R$ 300,00 e desvio padrão igual a R$ 50,00. Obtenha as probabilidades de que, em um dia aleatório, o motorista ganhe:

# 1) Entre R$ 250,00 e R$ 350,00
# 2) Entre R$ 400,00 e R$ 500,00
mean = 300
std = 50

# 1
z1 = calculate_Z(250, mean, std)
z2 = calculate_Z(350, mean, std)
probability_1 = norm.cdf(z2) - norm.cdf(z1)
# 2
z1 = calculate_Z(400, mean, std)
z2 = calculate_Z(500, mean, std)
probability_2 = norm.cdf(z2) - norm.cdf(z1)


# Problema
# O Inmetro verificou que as lâmpadas incandescentes da fabricante XPTO apresentam uma vida útil normalmente distribuída, com média igual a 720 dias e desvio padrão igual a 30 dias. Calcule a probabilidade de uma lâmpada, escolhida ao acaso, durar:

# 1) Entre 650 e 750 dias
# 2) Mais que 800 dias
# 3) Menos que 700 dias
mean = 720
std = 30

# 1
z1 = calculate_Z(650, mean, std)
z2 = calculate_Z(750, mean, std)
probability_1 = norm.cdf(z2) - norm.cdf(z1)
# 2
z = calculate_Z(800, mean, std)
probability_2 = norm.cdf(-z)
# 3
z = calculate_Z(700, mean, std)
probability_3 = norm.cdf(z)

print(probability_1, probability_2, probability_3)


# Problema
# Utilizando a tabela padronizada, ou o ferramental disponibilizado pelo Python, encontre a área sob a curva normal para os valores de Z abaixo:

# 1) Z < 1,96
# 2) Z > 2,15
# 3) Z < -0,78
# 4) Z > 0,59

# 1
probability_1 = norm.cdf(1.96)
# 2
probability_2 = 1 - norm.cdf(2.15)
# 3
probability_3 = norm.cdf(-0.78)
# 4
probability_4 = norm.cdf(-0.59)

print(probability_1, probability_2, probability_3, probability_4)

# # # Section of the course:
# 04. Técnicas de amostragem
# # #

# # # Section of the course:
# 05. Nível de intervalo de confiança
# # #

# # # Section of the course:
# 06. Calculando o tamanho da amostra
# # #

# # # Section of the course:
# 07. Resumo e projeto final
# # #