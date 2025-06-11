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
import re
import pandas as pd
import matplotlib.pyplot as plt

cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
data_folder = cwd + '/data/03-pandas-io_trabalhando-com-diferentes-formatos-de-arquivos/'

data = pd.read_csv(data_folder + 'dados_sus.csv', encoding='ISO-8859-1', skiprows=3, skipfooter=9, engine='python', sep=';', thousands='.', decimal=',')
data

df_months = data.drop(columns=['Unidade da Federação', 'Total']).iloc[-1]
df_months = df_months.apply(pd.to_numeric, errors="coerce")
df_months

df_ufs = data.iloc[:-1].set_index('Unidade da Federação')['Total']
df_ufs = df_ufs.apply(pd.to_numeric, errors="coerce").sort_values()
df_ufs = df_ufs / 1e+09
df_ufs

other = df_ufs[:13].sum()
df_ufs_simplified = df_ufs.drop(df_ufs[:14].index)
df_ufs_simplified["Outros"] = other
df_ufs_simplified

# First plot (Bar chart for months)
fig, ax = plt.subplots(figsize=(12, 28))
ax.barh(df_months.index, df_months.values, height=0.65)
ax.set_xlim(right=2e+09)
ax.set_title('Total de internações registradas no SUS por mês: 2008/2021', fontsize=14)
ax.set_xlabel('Total de internações', fontsize=12)
ax.set_ylabel('Ano/Mês', fontsize=12)
ax.text(0.98, 0.02, 'Escala: 1: 1 bilhão', transform=ax.transAxes,
        ha='right', va='bottom', fontsize=10, color='black')
for index, value in enumerate(df_months.values):
    ax.text(value + 0.1e+09, index, f'{value / 1e+09:.2f}', va='center', fontsize=8, color='black')
ax.tick_params(axis='y', labelsize=8)
for x in [0.5e+09, 1e+09, 1.5e+09]:
    ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.7)
plt.tight_layout()
plt.savefig('internacoes_sus_mes.pdf', format='pdf')
plt.show()

# Create a figure with 2 subplots arranged vertically
fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(15, 36))

# Second plot (Bar chart for UFs)
axs[0].barh(df_ufs.index, df_ufs.values, height=0.8)
axs[0].set_xlim(right=df_ufs.max() * 1.1)
axs[0].set_title('Internações registradas no SUS: 2008/2021', fontsize=16)
axs[0].set_xlabel('Total de internações', fontsize=14)
axs[0].set_ylabel('Unidade da Federação', fontsize=14)
axs[0].text(0.98, 0.02, 'Escala: 1: 1 bilhão', transform=axs[0].transAxes,
            ha='right', va='bottom', fontsize=14, color='black')
for index, value in enumerate(df_ufs.values):
    axs[0].text(value, index, f'{value:.2f}b', va='center', fontsize=10, color='black')
axs[0].tick_params(axis='y', labelsize=10)
for x in [10, 20, 30, 40]:
    axs[0].axvline(x=x, color='gray', linestyle='--', linewidth=0.7)

# Third plot (Pie chart for UFs)
wedges, texts, autotexts = axs[1].pie(df_ufs_simplified.values, labels=df_ufs_simplified.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors, textprops={'fontsize': 10})
axs[1].set_title('Proporção de internações registradas no SUS por Unidade da Federação: 2008/2021', fontsize=16)
axs[1].text(0.98, 0.02, 'Escala: 1: 1 bilhão', transform=axs[1].transAxes,
            ha='right', va='bottom', fontsize=14, color='black')

fig.tight_layout()

plt.savefig('internacoes_sus_estados.pdf', format='pdf')
plt.show()