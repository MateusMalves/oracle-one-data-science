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
import matplotlib.pyplot as plt
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

# Amostragem aleatória simples
income_mean = data['Renda'].mean()

sample = data.sample(n=1000, random_state=101)
sample['Renda'].mean()

data['Sexo'].value_counts(normalize=True)
sample['Sexo'].value_counts(normalize=True)


# # # Section of the course:
# 05. Nível de intervalo de confiança
# # #

n = 2000
total_samples = 1500

columns = []
for i in range(total_samples):
    _ = data.Idade.sample(n)
    _.index = range(0, len(_)) # type: ignore
    _.name = f'Sample_{i}'
    columns.append(_)

samples = pd.concat(columns, axis=1)

# > O **Teorema do Limite Central** afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal com média igual à média da população e desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. Este fato é assegurado para $n$ maior ou igual a 30.

# Checking through histogram
samples.mean().hist()

# Checking the mean
samples.mean().mean()
data.Idade.mean()

# Checking the standard deviation
samples.mean().std()
print(data.Idade.std() / np.sqrt(n))

# Checking samples : Personal experiment
samples_std_by_sqrt_n = []
for i in range(total_samples):
    samples_std_by_sqrt_n.append(samples['Sample_' + str(i)].std()  / np.sqrt(n))

error = []
higher_limit = samples.mean().std() + (samples.mean().std() * 0.05)
lower_limit = samples.mean().std() - (samples.mean().std() * 0.05)
for i in range(total_samples):
    if samples_std_by_sqrt_n[i] > higher_limit or samples_std_by_sqrt_n[i] < lower_limit:
        error.append(samples_std_by_sqrt_n[i])
len(error)

print(samples['Sample_0'].std() / np.sqrt(n))

# Further testing:
def generate_sample_df(data, variable, n):
    n = n
    total_samples = 1500

    columns = []
    for i in range(total_samples):
        _ = data[variable].sample(n)
        _.index = range(0, len(_)) # type: ignore
        _.name = f'Sample_{i}'
        columns.append(_)

    samples = pd.concat(columns, axis=1)
    return samples


def check_central_limit_theorem(data, variable, n):
    """
    Demonstrates the Central Limit Theorem for a given variable from a dataset.

    Parameters:
    - data (pd.DataFrame): The original dataset.
    - variable (str): Name of the numeric column to analyze.
    - n (int): Sample size to draw repeatedly.
    """

    # Generate samples DataFrame: each column is a sample of size `n`
    samples = generate_sample_df(data, variable, n)

    # === Pre-computations ===
    sample_means = samples.mean()
    population_mean = data[variable].mean()
    population_std = data[variable].std()
    se = population_std / np.sqrt(n)
    z = norm.ppf(0.975)  # 95% confidence (two-tailed)
    margin_of_error = z * se
    ci_lower = population_mean - margin_of_error
    ci_upper = population_mean + margin_of_error
    sample_means_std = sample_means.std()

    # === Display Histogram of Sample Means ===
    print("\n📊 Histogram of sample means:")
    plt.title(f"Distribution of Sample Means ({variable})")
    plt.xlabel("Sample Mean")
    plt.ylabel("Frequency")
    sample_means.hist(grid=True)
    plt.axvline(population_mean, color='red', linestyle='dashed', label='Population Mean')
    plt.legend()
    plt.show()

    # === Display Summary Statistics ===
    print("\n🔍 Descriptive Statistics:\n")
    print(f"→ Population mean:        {population_mean:.4f}")
    print(f"→ Mean of sample means:   {sample_means.mean():.4f}")
    print(f"→ Population std dev:     {population_std:.4f}")
    print(f"→ Standard error (σ/√n):  {se:.4f}")
    print(f"→ Std dev of sample means:{sample_means_std:.4f}")

    # === Confidence Interval ===
    print("\n📏 95% Confidence Interval for the Mean:")
    print(f"→ z-score (95%):          {z:.4f}")
    print(f"→ Margin of error:        ±{margin_of_error:.4f}")
    print(f"→ Confidence Interval:    ({ci_lower:.4f}, {ci_upper:.4f})")

    # === Summary Line ===
    within_ci = (sample_means >= ci_lower) & (sample_means <= ci_upper)
    percent_within = within_ci.mean() * 100
    print(f"\n✅ {percent_within:.2f}% of the sample means fall within the 95% confidence interval.")

quantitative_columns = ['Idade', 'Renda', 'Altura']
for column in quantitative_columns:
    print(f'\n\n# # # # # # # # # #\nChecking statistics for {column}:')
    print('\n\n')
    check_central_limit_theorem(data, column, 2000)


# Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de **desvio padrão populacional igual a 150 g**. Selecionada uma **amostra aleatório de 20 sacos** de um lote específico, obteve-se um **peso médio de 5.050 g**. Construa um **intervalo de confiança para a média populacional** assumindo um **nível de significância de 5%**.
mean_sample = 5050
std = 150
n = 20
significance_level = 0.05
trust_level = 1 - significance_level

# Calculating z
z = norm.ppf(trust_level + (significance_level / 2)) # 0.975

# Calculating $\sigma_{\bar{x}}$ 
sigma = std / np.sqrt(n)

# O **erro inferencial** é definido pelo **desvio padrão das médias amostrais** $\sigma_{\bar{x}}$ e pelo **nível de confiança** determinado para o processo.
e = z * sigma
# Calculating the confidence interval
confidence_interval = (
    mean_sample - e,
    mean_sample + e,
)

interval = norm.interval(confidence = 0.95, loc = mean_sample, scale = sigma) # Built-in way


# # # Section of the course:
# 06. Calculando o tamanho da amostra
# # #

# Infinite population

# Problema
# Estamos estudando o rendimento mensal dos chefes de domicílios com renda até R$\$$ 5.000,00 no Brasil. Nosso supervisor determinou que o **erro máximo em relação a média seja de R$ 100,00**. Sabemos que o **desvio padrão populacional** deste grupo de trabalhadores é de **R$\$$ 3323.39**. Para um **nível de confiança de 95%**, qual deve ser o tamanho da amostra de nosso estudo?
z = norm.ppf(0.975)
sigma = 3323.39
e = 100
n = (z * (sigma / e)) ** 2
print(int(np.round(n)))

# Problema
# O valor do gasto médio dos clientes de uma loja de conveniência é de R$ 45,50. Assumindo que o desvio padrão dos gastos é igual a R$ 15,00, qual deve ser o tamanho da amostra para estimarmos a média populacional com um nível de significância de 10%?

# Considere que o erro máximo aceitável seja de 10%.
z = norm.ppf(0.95)
sigma = 15
e = 45.5 * 0.1
n = (z * (sigma / e)) ** 2
print(int(np.round(n)))

# Finite population

# Problema
# Em um lote de **10.000 latas** de refrigerante foi realizada uma amostra aleatória simples de **100 latas** e foi obtido o **desvio padrão amostral do conteúdo das latas igual a 12 ml**. O fabricante estipula um **erro máximo sobre a média populacional de apenas 5 ml**. Para garantir um **nível de confiança de 95%** qual o tamanho de amostra deve ser selecionado para este estudo?
z = norm.ppf(0.975)
N = 10000
s = 12
e = 5
n = ((z**2) * (s**2) * N) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
print(int(np.round(n)))

# Problema
# Um fabricante de farinha verificou que, em uma amostra aleatória formada por 200 sacos de 25 kg de um lote formado por 2.000 sacos, apresentou um desvio padrão amostral do peso igual a 480 g.

# Considerando um erro máximo associado à média populacional igual a 0,3 kg e um nível de confiança igual a 95%, qual tamanho de amostra deveria ser selecionado para obtermos uma estimativa confiável do parâmetro populacional?
z = norm.ppf(0.975)
N = 2000
s = 0.480
e = 0.3
n = ((z**2) * (s**2) * N) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
print(int(np.round(n)))


# # # Section of the course:
# 07. Resumo e projeto final
# # #