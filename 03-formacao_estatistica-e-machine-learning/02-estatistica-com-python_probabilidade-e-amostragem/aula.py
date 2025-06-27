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
from scipy.special import comb
from scipy.stats import binom
from scipy.stats import poisson

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