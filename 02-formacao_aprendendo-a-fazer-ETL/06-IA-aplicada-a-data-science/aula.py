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
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/06-IA-aplicada-a-data-science/'
outputs_folder = data_folder + 'outputs/'

data_customers = load_data(data_folder + 'zoop_clientes.csv', is_pandas=True)
data_sales = load_data(data_folder + 'zoop_vendas.csv', is_pandas=True)

data_customers.rename(columns={'sexo_biologico': 'sexo'}, inplace=True)
data_customers['cidade'] = data_customers['cidade'].astype('category')
data_customers['uf'] = data_customers['uf'].astype('category')
data_customers['regiao'] = data_customers['regiao'].astype('category')
data_customers['sexo'] = data_customers['sexo'].astype('category')
data_customers['cashback'] = data_customers['cashback'].apply(lambda x: True if x == 'Sim' else False)

data_sales.rename(columns={'preco_unitario': 'preco'}, inplace=True)
data_sales['data'] = pd.to_datetime(data_sales['data'])
data_sales['categoria'] = data_sales['categoria'].astype('category')
data_sales['metodo_pagamento'] = data_sales['metodo_pagamento'].astype('category')


# Use GPT to generate a explore the data (portuguese outputs)
# 
# Expore data_customers DataFrame

# Exibir as primeiras linhas para ter uma visão geral dos dados
data_customers.head()

# Verificar o tamanho do DataFrame (número de linhas e colunas)
data_customers.shape

# Verificar os tipos de dados e valores nulos
data_customers.info()

# Obter estatísticas descritivas para colunas numéricas
data_customers.describe()

# Contagem de valores únicos por coluna categórica
data_customers['sexo'].value_counts()
data_customers['regiao'].value_counts()
data_customers['uf'].value_counts()
data_customers['cidade'].nunique()

# Verificar distribuição de idade
data_customers['idade'].describe()

# Verificar média de avaliação da compra
data_customers['avaliacao_compra'].mean()

# Verificar quantos participam do programa de cashback
data_customers['cashback'].value_counts()
data_customers['cashback'].value_counts(normalize=True)

# Verificar a quantidade de data_customers por faixa etária
bins = [0, 17, 25, 35, 45, 60, 100]
labels = ['0-17', '18-25', '26-35', '36-45', '46-60', '60+']
data_customers['faixa_etaria'] = pd.cut(data_customers['idade'], bins=bins, labels=labels)
data_customers['faixa_etaria'].value_counts().sort_index()

# Avaliação média por sexo
data_customers.groupby('sexo')['avaliacao_compra'].mean()

# Avaliação média por participação no cashback
data_customers.groupby('cashback')['avaliacao_compra'].mean()


# Expore data_sales DataFrame
# 
# Exibir as primeiras linhas do DataFrame
data_sales.head()

# Verificar o número de linhas e colunas
data_sales.shape

# Verificar os tipos de dados e se há valores nulos
data_sales.info()

# Ver estatísticas descritivas das colunas numéricas
data_sales.describe()

# Verificar quantidade de categorias de produtos
data_sales['categoria'].value_counts()

# Verificar o ticket médio (preço unitário * quantidade)
data_sales['valor_total'] = data_sales['preco'] * data_sales['quantidade']
data_sales['valor_total'].mean()

# Verificar os métodos de pagamento utilizados
data_sales['metodo_pagamento'].value_counts(normalize=True)

# Analisar valor médio do frete
data_sales['frete'].describe()

# Verificar vendas por dia da semana
data_sales['dia_semana'] = data_sales['data'].dt.day_name()
data_sales['dia_semana'].value_counts()

# Verificar horários com maior volume de compras
pd.to_datetime(data_sales['horario']).dt.time.value_counts()

# Verificar categorias com maior faturamento total
data_sales.groupby('categoria')['valor_total'].sum().sort_values(ascending=False)

# Verificar método de pagamento com maior faturamento
data_sales.groupby('metodo_pagamento')['valor_total'].sum().sort_values(ascending=False)

data_customers.head()

# #
# Tipos de gráficos
# 
# Mesclar os DataFrames pela chave 'ID_compra'
data_merged = pd.merge(data_sales, data_customers, on='ID_compra', how='inner')

# Reorganizar as colunas na ordem especificada
colunas_ordenadas = [
    'ID_compra',
    'data',
    'horario',
    'categoria',
    'preco',
    'quantidade',
    'frete',
    'metodo_pagamento',
    'ID_cliente',
    'idade',
    'sexo',
    'cidade',
    'uf',
    'regiao',
    'cashback',
    'avaliacao_compra'
]

# Aplicar a nova ordem de colunas
data_merged = data_merged[colunas_ordenadas]

# # #
# 02. Visualizando os dados

# Definindo os visuais

# Etapa 1: Criar a tabela resumo
metodos_de_pagamento = data_merged['metodo_pagamento'].value_counts().reset_index()
metodos_de_pagamento.columns = ['Metodo de Pagamento', 'Quantidade']

# Etapa 2: Visualização
plt.figure(figsize=(8, 6))
sns.barplot(data=metodos_de_pagamento, x='Metodo de Pagamento', y='Quantidade', hue='Metodo de Pagamento', palette='Set2', order=metodos_de_pagamento['Metodo de Pagamento'])

plt.title('Distribuição dos Métodos de Pagamento')
plt.xlabel('Método de Pagamento')
plt.ylabel('Quantidade de Compras')
plt.xticks(rotation=45)
plt.tight_layout()

# Comparando dados

# Etapa 1: Calcular faturamento total por linha
data_merged['faturamento'] = (data_merged['preco'] * data_merged['quantidade']) + data_merged['frete']

# Etapa 2: Agrupar por categoria e somar faturamentos
faturamento_categoria = data_merged.groupby('categoria')['faturamento'].sum().sort_values(ascending=True).reset_index()

# Etapa 3: Visualização - gráfico de barras horizontais
plt.figure(figsize=(10, 6))
sns.barplot(data=faturamento_categoria, x='faturamento', y='categoria', palette='viridis', order=faturamento_categoria['categoria'])

plt.title('Faturamento por Categoria de Produto')
plt.xlabel('Faturamento (R$)')
plt.ylabel('Categoria')
plt.tight_layout()

# Sales per month
# Dicionário de tradução dos meses
meses = {
    'January': 'Jan',
    'February': 'Fev',
    'March': 'Mar',
    'April': 'Abr',
    'May': 'Mai',
    'June': 'Jun',
    'July': 'Jul',
    'August': 'Ago',
    'September': 'Set',
    'October': 'Out',
    'November': 'Nov',
    'December': 'Dez'
}

# Garantir a coluna de faturamento (se ainda não existir)
if 'faturamento' not in data_merged.columns:
    data_merged['faturamento'] = (data_merged['preco'] * data_merged['quantidade']) + data_merged['frete']

# Extrair ano e mês (como datetime) para agrupar
data_merged['ano_mes'] = data_merged['data'].dt.to_period('M').dt.to_timestamp()

# Agrupar por mês e somar faturamento
vendas_mensais = data_merged.groupby('ano_mes')['faturamento'].sum().reset_index()

# Criar coluna com nome do mês traduzido
vendas_mensais['mes'] = vendas_mensais['ano_mes'].dt.strftime('%B').map(meses)

# Criar gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=vendas_mensais, x='mes', y='faturamento', marker='o', linewidth=2.5, color='royalblue')

plt.title('Faturamento Mensal da Zoop em 2023')
plt.xlabel('Mês')
plt.ylabel('Faturamento (R$)')
plt.grid(True)
plt.tight_layout()

# Compondo dados dinâmicos

# Garantir a coluna de faturamento (caso ainda não exista)
if 'faturamento' not in data_merged.columns:
    data_merged['faturamento'] = (data_merged['preco'] * data_merged['quantidade']) + data_merged['frete']

# Criar a coluna de trimestre (Ex: 2023Q1, 2023Q2 etc)
data_merged['trimestre'] = data_merged['data'].dt.to_period('Q').astype(str)

# Agrupar por trimestre e método de pagamento, somando o faturamento
vendas_trimestre = data_merged.groupby(['trimestre', 'metodo_pagamento'])['faturamento'].sum().unstack().fillna(0)

# Plotar o gráfico de barras empilhadas
vendas_trimestre.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

plt.title('Faturamento por Trimestre e Método de Pagamento - Zoop')
plt.xlabel('Trimestre')
plt.ylabel('Faturamento (R$)')
plt.legend(title='Método de Pagamento')
plt.tight_layout()

# # #
# 03. Gerando mais visuais

# Composing static data
# 
# Etapa 1: Contar os valores únicos da coluna 'cashback'
cashback_counts = data_merged['cashback'].value_counts()

# Etapa 2: Gráfico de pizza
plt.figure(figsize=(6, 6))
plt.pie(
    cashback_counts,
    labels=['Com cashback' if item == True else 'Sem cashback' for item in list(cashback_counts.index)],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66c2a5', '#fc8d62'],
    wedgeprops={'edgecolor': 'white'}
)

plt.title('Proporção de Usuários com Cashback na Zoop')
plt.axis('equal')  # Garante que a pizza fique redonda
plt.tight_layout()

# Invert colors and plot donut
# 
# Cores invertidas
cores = ['#fc8d62', '#66c2a5']

# Criar gráfico de rosca
plt.figure(figsize=(6, 6))
plt.pie(
    cashback_counts,
    labels=['Com cashback' if item == True else 'Sem cashback' for item in list(cashback_counts.index)],
    autopct='%1.1f%%',
    startangle=90,
    colors=cores,
    wedgeprops={'edgecolor': 'white', 'width': 0.6},
)

plt.title('Proporção de Usuários com Cashback na Zoop')
plt.axis('equal')  # Garante proporção circular
plt.tight_layout()

# Distributing data
# 
# Configura estilo do gráfico
sns.set_theme(style="whitegrid")

# Tamanho da figura
plt.figure(figsize=(10, 6))

# Gráfico de barras com contagem por avaliação
sns.countplot(data=data_merged, x='avaliacao_compra', palette='coolwarm', hue='avaliacao_compra', legend=False)

# Títulos e rótulos
plt.title('Distribuição das Avaliações dos Clientes')
plt.xlabel('Nota da Avaliação (0 a 10)')
plt.ylabel('Quantidade de Avaliações')
plt.xticks(range(0, 11))  # Garante que todas as notas de 0 a 10 apareçam

plt.tight_layout()

# Distributing data by characteristic
# 
# Tamanho da figura
plt.figure(figsize=(10, 6))

# Gráfico de densidade de idade segmentado por sexo
sns.histplot(
    data=data_merged,
    x='idade',
    hue='sexo',
    multiple='stack',        # Usa pilhas para melhor visualização
    palette='pastel',
    bins=20,                 # Número de faixas de idade
    kde=False                # Coloque True para densidade suavizada
)

# Títulos e eixos
plt.title('Distribuição da Idade por Sexo Biológico')
plt.xlabel('Idade')
plt.ylabel('Número de Compras')
plt.tight_layout()

# Change to boxplot
# Tamanho da figura
plt.figure(figsize=(8, 6))

# Boxplot de idade por sexo
sns.boxplot(
    data=data_merged,
    x='sexo',
    y='idade',
    palette='pastel'
)

# Títulos e rótulos
plt.title('Distribuição da Idade por Sexo Biológico')
plt.xlabel('Sexo')
plt.ylabel('Idade')
plt.tight_layout()

# # #
# 04. Técnicas de storytelling

# Adicionando as cores como variáveis do projeto
VERMELHO_1,	VERMELHO_2,	VERMELHO_3 = "#e23155",	"#cc2c4e", "#b32742"
AZUL_1,	AZUL_2,	AZUL_3 = "#203f75",	"#1c3867", "#19325b"
BRANCO,	CINZA_1, CINZA_2, CINZA_3, CINZA_4,	CINZA_5 = "#ffffff", "#ebebeb",	"#d9d9d9", "#cccccc", "#555655", "#231f20"
AQUA_1,	AQUA_2,	AQUA_3 = "#addcd4",	"#9fccc5", "#96bfb9"

# AI Context
plt.figure(figsize=(10, 6))
plt.bar(metodos_de_pagamento['Metodo de Pagamento'], metodos_de_pagamento['Quantidade'], color='skyblue')
plt.title('Quantidade de Métodos de Pagamento Utilizados')
plt.xlabel('Método de Pagamento')
plt.ylabel('Quantidade')
plt.xticks(rotation=45, ha='right')

# AI Answer
# Criação da tabela com a contagem de métodos de pagamento
sns.set_theme(style="white")
metodos_de_pagamento = data_merged['metodo_pagamento'].value_counts()

# Criar figura e eixos
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(CINZA_1)  # fundo da figura
ax.set_facecolor(CINZA_1)         # fundo do plot

# Gráfico de barras verticais
barras = ax.bar(
    list(metodos_de_pagamento.index),
    list(metodos_de_pagamento.values),
    color=VERMELHO_1
)

# Título
ax.set_title(
    'Métodos de pagamentos mais utilizados em 2023',
    fontsize=18,
    color=CINZA_5
)

# Eixo X
ax.set_xlabel('')
ax.set_xticklabels(metodos_de_pagamento.index, fontsize=12, color=AZUL_1)

# Eixo Y (suprimir)
ax.set_ylabel('')
ax.set_yticks([])

# Remover bordas
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# Adicionar valores acima das barras
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + max(metodos_de_pagamento.values) * 0.01,
        str(altura),
        ha='center',
        va='bottom',
        fontsize=12,
        color=AZUL_1
    )

plt.tight_layout()

# Adding text
# 
# Cálculo do percentual
top2 = metodos_de_pagamento.iloc[:2].sum()
total = metodos_de_pagamento.sum()
percentual = (top2 / total) * 100

# Criar figura
fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor(CINZA_1)
ax.set_facecolor(CINZA_1)

# Barras
barras = ax.bar(
    list(metodos_de_pagamento.index),
    list(metodos_de_pagamento.values),
    color=VERMELHO_1
)

# Título
ax.set_title(
    'Métodos de pagamentos mais utilizados em 2023',
    fontsize=18,
    color=CINZA_5
)

# Estilização do eixo X
ax.set_xlabel('')
ax.set_xticklabels(metodos_de_pagamento.index, fontsize=12, color=AZUL_1)

# Eixo Y removido
ax.set_ylabel('')
ax.set_yticks([])

# Bordas removidas
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)

# Valores acima das colunas
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2,
        altura + max(metodos_de_pagamento.values) * 0.01,
        str(altura),
        ha='center',
        va='bottom',
        fontsize=12,
        color=AZUL_1
    )

# Texto analítico dentro do plot
ax.text(
    x=2,
    y=2500,
    s=(
        f"$\\bf{percentual:.2f}$% dos clientes utilizam Cartão de Crédito ou PIX \n"
        "para pagamento. Seria interessante recorrer a parcerias\n"
        "com bancos para a construção de um Zoop Pay a fim\n"
        "de fidelizar a nossa clientela."
    ),
    fontsize=10,
    color=AZUL_3
)

plt.tight_layout()

# Adding visual elements
# 
# Dicionário de tradução de meses
meses = {
    'January': 'Jan',
    'February': 'Fev',
    'March': 'Mar',
    'April': 'Abr',
    'May': 'Mai',
    'June': 'Jun',
    'July': 'Jul',
    'August': 'Ago',
    'September': 'Set',
    'October': 'Out',
    'November': 'Nov',
    'December': 'Dez'
}

# Agrupar por mês e calcular as vendas totais
data_merged['mes'] = data_merged['data'].dt.strftime('%B')
vendas_mensais = data_merged.groupby('mes')['faturamento'].sum().reindex(list(meses.keys()))

# Configurações do gráfico
plt.figure(figsize=(12, 6))
plt.plot(vendas_mensais.index, vendas_mensais, marker='o', color='#1890FF', linewidth=2)

# Adicionar rótulos e título
plt.title('Vendas Totais Mensais da Zoop', fontsize=18, color='#555555')
plt.xlabel('Mês', fontsize=12, color='#1890FF')
plt.ylabel('Vendas', fontsize=12, color='#1890FF')

# Alterar rótulos do eixo x utilizando o dicionário de tradução
plt.xticks(vendas_mensais.index, [meses[mes] for mes in vendas_mensais.index], fontsize=10, color='#1890FF')

plt.show()

# Using AI to generate the plot
# Adiciona a coluna de mês
sns.set_theme(style="ticks")
data_merged['mes'] = data_merged['data'].dt.strftime('%B')

# Agrupamento por mês
vendas_mensais = data_merged.groupby('mes')['faturamento'].sum().reindex(list(meses.keys()))
vendas_mensais = vendas_mensais.rename(index=meses)  # traduz o índice

# Criação do gráfico
fig, ax = plt.subplots(figsize=(12, 6))
fig.patch.set_facecolor(CINZA_1)
ax.set_facecolor(CINZA_1)

# Linha de vendas
ax.plot(
    list(vendas_mensais.index),
    list(vendas_mensais.values),
    marker='o',
    color=AZUL_1,
    linewidth=2
)

# Título
ax.set_title('Vendas totais mensais em 2023', fontsize=18, color=CINZA_5)

# Eixos X e Y
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_xticks(range(len(vendas_mensais.index)))
ax.set_xticklabels(vendas_mensais.index, fontsize=12, color=AZUL_1)
ax.tick_params(axis='y', labelsize=12, colors=AZUL_1)

# Formato do eixo Y em milhões com R$
formatter = ticker.FuncFormatter(lambda x, _: f'R$ {x / 1e6:.2f} M')
ax.yaxis.set_major_formatter(formatter)

# Remover bordas
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# Emphasizing points
for i, point in enumerate([(4, vendas_mensais.iloc[4]), (7, vendas_mensais.iloc[7]), (10, vendas_mensais.iloc[10]), (11, vendas_mensais.iloc[11])], start=1):
    plt.scatter(point[0], point[1], s=200, color='none', edgecolors=VERMELHO_1, alpha=0.7)
    plt.text(point[0] - 0.3, point[1] + 0.1, str(i), fontsize=12, color=VERMELHO_1)


# # #
# 05. Concluindo o projeto