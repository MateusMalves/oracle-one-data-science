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
from scipy.special import comb
from scipy.stats import binom

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
probability

# Probability of passing
probability = binom.pmf([k, k+1, k+2, k+3, k+4, k+5], n, p).sum()
probability = 1 - binom.cdf(4, n, p)
probability = binom.sf(4, n, p)


# # # Section of the course:
# 02.
# # #

# # # Section of the course:
# 03.
# # #

# # # Section of the course:
# 04.
# # #

# # # Section of the course:
# 05.
# # #

# # # Section of the course:
# 06.
# # #

# # # Section of the course:
# 07.
# # #