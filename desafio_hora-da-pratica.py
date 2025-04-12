# Para rodar o código, basta executar o comando 'python3 desafio_hora-da-pratica.py'

# 
# Enunciado do desafio
# 

'''
Vamos praticar o que aprendemos até aqui solucionando os problemas propostos em código.

Aquecimento
1. Escreva um código que lê a lista abaixo e faça:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

A leitura do tamanho da lista
A leitura do maior e menor valor
A soma dos valores da lista
Ao final exiba uma mensagem dizendo:

"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"

Dica: use as funções embutidas presentes na documentação do Python.

2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70

3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3.

4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

Aplicando a projetos
5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

"Nota da manobra: [media]"

6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

maior nota
menor nota
média
situação (Aprovado(a) ou Reprovado(a))
Para testar o comportamento da função, os dados podem ser exibidos em um texto:

"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"

7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

O texto exibido ao fim deve ser parecido com:

"Nome completo: Ana Silva"

Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.

8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

Para teste, utilize as seguintes listas de gols marcados e sofridos:

gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

Provável texto exibido:

"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"

9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.
'''


# # # # #
# # # Desafios resolvidos
# # # # #


# Importando bibliotecas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from ui_desafios import controlador, saudar


# 
# Aquecimento
# 

saudar('Python para Data Science: trabalhando com funções > 02. Funcoes > Desafio: hora da prática')

# 1. Escreva um código que lê a lista abaixo e faça:

# lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# A leitura do tamanho da lista
# A leitura do maior e menor valor
# A soma dos valores da lista
# Ao final exiba uma mensagem dizendo:

# "A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"

# Dica: use as funções embutidas presentes na documentação do Python.
mensagem_problema_1 = '# 1 => Vamos ler uma lista de números e calcular o tamanho, maior, menor e soma dos valores.'
controlador(mensagem_problema_1, primeiro_exercicio=True)

def problema_1():
    lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
    tam = len(lista)
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    print(f'=> A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}.\nA soma dos valores presentes nela é igual a {soma}')

problema_1()

# 2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# Tabuada do 7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70
mensagem_problema_2 = '# 2 => Vamos gerar a tabuada de um número inteiro de 1 a 10.'
controlador(mensagem_problema_2, mensagem_problema_anterior=mensagem_problema_1, problema_anterior=problema_1)

def problema_2():
    def coletar_numero():
        numero = input('Digite um número inteiro de 1 a 10: ')
        if numero.isdigit():
            return int(numero)
        else:
            print('Número inválido. Tente novamente.\n')
            return coletar_numero()
    
    numero = coletar_numero()
    print(f'\n=> Tabuada do {numero}:\n')
    list(map(lambda x: print(f'{numero} x {x} = {numero * x}'), range(11)))

problema_2()

# 3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Utilize o return na função e salve a nova lista na variável mult_3.
mensagem_problema_3 = '# 3 => Vamos criar uma nova lista com os múltiplos de 3.'
controlador(mensagem_problema_3, mensagem_problema_anterior=mensagem_problema_2, problema_anterior=problema_2)

def problema_3():
    lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
    mult_3 = list(filter(lambda x: x % 3 == 0, lista))
    print(f'=> A lista original é:\n{lista}\n')
    print(f'=> A nova lista com os múltiplos de 3 é:\n{mult_3}')
    return mult_3

problema_3()

# 4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
mensagem_problema_4 = '# 4 => Vamos criar uma lista com os quadrados dos números de 1 a 10.'
controlador(mensagem_problema_4, mensagem_problema_anterior=mensagem_problema_3, problema_anterior=problema_3)

def problema_4():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quadrados = list(map(lambda x: x**2, lista))
    print(f'=> A lista original é:\n{lista}\n')
    print(f'=> A lista dos quadrados é:\n{quadrados}')
    
problema_4()


# 
# Aplicando a projetos
# 

# # # UI - Controle de fluxo
controlador(mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4, abrir_nova_sessão=True, saudacao='Aplicando a projetos')


# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"
mensagem_problema_5 = '# 5 => Vamos calcular a pontuação dos(as) skatistas eliminando a maior e menor nota.'
controlador(mensagem_problema_5, mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4, apos_saudacao=True, saudacao='Aplicando a projetos')

def problema_5():
    notas = []
    while len(notas) < 5:
        i = len(notas)
        nota = input(f'Digite a {i+1}ª nota: ')
        if nota.isdigit():
            notas.append(float(nota))
        else:
            print('Nota inválida. Tente novamente.\n')
            continue
    
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(map(lambda x: x if x != maior_nota and x != menor_nota else 0, notas)) / 3
    
    print(f'\n=> Nota da manobra: {media}')

problema_5()

# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))
# Para testar o comportamento da função, os dados podem ser exibidos em um texto:

# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
mensagem_problema_6 = '# 6 => Vamos criar uma função que receba uma lista de 4 notas de um aluno e retorne a maior nota, menor nota, média e situação.'
controlador(mensagem_problema_6, mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5)

def problema_6():
    import re
    notas = []
    while len(notas) < 4:
        nota = input(f'Digite a {len(notas)+1}ª nota: ').replace(',', '.')
        if re.match(r'^\d+(\.\d+)?$', nota):
            notas.append(float(nota))
        else:
            print('Nota inválida. Tente novamente.\n')

    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    situacao = 'Aprovado(a)' if media >= 7 else 'Reprovado(a)'
    print(f'\n=> O(a) estudante obteve uma média de {media:.2f}, com a sua maior nota de {maior_nota:.2f} pontos\ne a menor nota de {menor_nota:.2f} pontos e foi {situacao}')

problema_6()

# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]
# O texto exibido ao fim deve ser parecido com:
# "Nome completo: Ana Silva"
# Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
mensagem_problema_7 = '# 7 => Vamos tratar 2 listas com os nomes e sobrenomes de cada estudante\nconcatenando-as para apresentar seus nomes completos.'
controlador(mensagem_problema_7, mensagem_problema_anterior=mensagem_problema_6, problema_anterior=problema_6)

def problema_7():
    nomes = ["joão", "MaRia", "JOSÉ"]
    sobrenomes = ["SILVA", "souza", "Tavares"]
    nomes_completos = list(map(lambda x, y: f'{x.title()} {y.title()}', nomes, sobrenomes))
    print(f'=> Os nomes completos são:\n')
    for nome in nomes_completos:
        print(f'Nome completo: {nome}')

problema_7()

# 8. Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols marcados e sofridos em cada jogo.

# Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 pontos, o empate vale 1 ponto e a derrota 0 pontos.

# Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.

# Para teste, utilize as seguintes listas de gols marcados e sofridos:
# gols_marcados = [3, 2, 1, 4, 0]
# gols_sofridos = [1, 2, 3, 0, 1]
# Provável texto exibido:
# "A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
mensagem_problema_8 = '# 8 => Vamos calcular a pontuação do time no campeonato nacional\na partir dos dados de gols marcados e sofridos em cada jogo.'
controlador(mensagem_problema_8, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7)

def problema_8():
    def calcula_pontos(lista_gols_marcados, lista_gols_sofridos):
        pontos = 0
        for gols_marcados, gols_sofridos in zip(lista_gols_marcados, lista_gols_sofridos):
            if gols_marcados > gols_sofridos:
                pontos += 3
            elif gols_marcados == gols_sofridos:
                pontos += 1
        max_pontos = len(lista_gols_marcados) * 3
        aproveitamento = (pontos / max_pontos) * 100 if max_pontos > 0 else 0
        return pontos, aproveitamento

    gols_marcados = [3, 2, 1, 4, 0]
    gols_sofridos = [1, 2, 3, 0, 1]
    pontos, aproveitamento = calcula_pontos(gols_marcados, gols_sofridos)
    print(f'=> Gols marcados:\n{gols_marcados}\n')
    print(f'=> Gols sofridos:\n{gols_sofridos}\n')
    print(f'=> A pontuação do time foi de {pontos} e seu aproveitamento foi de {aproveitamento:.2f}%')

problema_8()

# 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
# "Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"
mensagem_problema_9 = '# 9 => Vamos calcular os gastos de uma viagem para Salvador, Fortaleza, Natal ou Aracaju, partindo de Recife.'
controlador(mensagem_problema_9, mensagem_problema_anterior=mensagem_problema_8, problema_anterior=problema_8)

def problema_9():
    def gasto_hotel(dias):
        return dias * 150

    def gasto_gasolina(distancia):
        consumo_gasolina = 14
        preco_gasolina = 5
        ida_e_volta = 2
        distancia = distancia * ida_e_volta
        return (distancia / consumo_gasolina) * preco_gasolina

    def gasto_passeio(dias, gasto_passeios_diario):
        return dias * gasto_passeios_diario

    def simular_viagem(cidade, dias):
        cidades = ["Salvador", "Fortaleza", "Natal", "Aracaju"]
        gastos_passeios = [200, 400, 250, 300]
        distancias = [850, 800, 300, 550]

        indice_cidade = cidades.index(cidade)
        gastos, distancia = gastos_passeios[indice_cidade], distancias[indice_cidade]
        total_gastos = gasto_hotel(dias) + gasto_gasolina(distancia) + gasto_passeio(dias, gastos)
        return total_gastos
    
    dias = 3
    cidade = "Salvador"
    total_gastos = simular_viagem(cidade, dias)

    print(f'=> Com base nos gastos definidos, uma viagem de {dias} dias para {cidade}\nsaindo de Recife custaria {total_gastos:.2f} reais.')

problema_9()

# 10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

# Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

# Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.
mensagem_problema_10 = '# 10 => Vamos filtrar palavras com tamanho maior ou igual a 5.'
controlador(mensagem_problema_10, mensagem_problema_anterior=mensagem_problema_9, problema_anterior=problema_9)

def problema_10():
    def validar_frase(frase):
        if isinstance(frase, str):
            return frase
        else:
            print('Frase inválida. Tente novamente.')
            problema_10()
    
    def tratar_frase(frase):
        validar_frase(frase)
        frase = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ')
        return frase
    

    frase = "Aprender Python aqui na Alura é muito bom"
    frase_tratada = tratar_frase(frase)
    palavras = frase_tratada.split()
    palavras_filtradas = list(filter(lambda palavra: len(palavra) >= 5, palavras))
    print(f'=> A quantidade de palavras com tamanho maior ou igual a 5 é: {len(palavras_filtradas)}\n')
    print(f'=> As palavras filtradas são:\n{palavras_filtradas}')


problema_10()

controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_10, problema_anterior=problema_10, ultimo_exercicio=True)