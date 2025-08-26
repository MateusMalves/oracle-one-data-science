"""
==============================================
Oracle ONE - Data Science Course
==============================================

File: template_desafio_hora-da-pratica.py
Author: Mateus Alves de Mendonça
Description: Template for course challenges and exercises
Created: Oracle ONE Data Science Program
License: MIT

Este template serve como base para resolver os desafios
do programa Oracle Next Education em Data Science.

Para executar: python3 desafio_hora-da-pratica.py
"""

# 
# Enunciado do desafio
# 

'''

'''

# ==============================================
# Desafios resolvidos
# ==============================================

# Standard library imports
import sys
import os

# Adding project root to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

# Project imports
from ui_desafios import controlador, saudar

# 
# Aquecimento
# 

saudar('Python para Data Science: trabalhando com funções > 01. Bibliotecas > Desafio: hora da prática')

# 1. 
mensagem_problema_1 = '# 1 =>'
controlador(mensagem_problema_1, primeiro_exercicio=True)

def problema_1():
    ...

problema_1()

# 2. 
mensagem_problema_2 = '# 2 =>'
controlador(mensagem_problema_2, mensagem_problema_anterior=mensagem_problema_1, problema_anterior=problema_1)

def problema_2():
    ...

problema_2()

# 3. 
mensagem_problema_3 = '# 3 =>'
controlador(mensagem_problema_3, mensagem_problema_anterior=mensagem_problema_2, problema_anterior=problema_2)

def problema_3():
    ...

problema_3()

# 4. 
mensagem_problema_4 = '# 4 =>'
controlador(mensagem_problema_4, mensagem_problema_anterior=mensagem_problema_3, problema_anterior=problema_3)

def problema_4():
    ...

    
problema_4()

# 5. 
mensagem_problema_5 = '# 5 =>'
controlador(mensagem_problema_5, mensagem_problema_anterior=mensagem_problema_4, problema_anterior=problema_4)

def problema_5():
    ...
    

problema_5()

# 
# Aplicando a projetos
# 

# # # UI - Controle de fluxo
controlador(mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, abrir_nova_sessão=True, saudacao='Aplicando a projetos')

# 6. 
mensagem_problema_6 = '# 6 =>'
controlador(mensagem_problema_6, mensagem_problema_anterior=mensagem_problema_5, problema_anterior=problema_5, apos_saudacao=True, saudacao='Aplicando a projetos')

def problema_6():
    ...
    

problema_6()

# 7. 
mensagem_problema_7 = '# 7 =>'
controlador(mensagem_problema_7, mensagem_problema_anterior=mensagem_problema_6, problema_anterior=problema_6)

def problema_7():
    ...
    

problema_7()

# 8. 
mensagem_problema_8 = '# 8 =>'
controlador(mensagem_problema_8, mensagem_problema_anterior=mensagem_problema_7, problema_anterior=problema_7)

def problema_8():
    ...
    

problema_8()

# 9. 
mensagem_problema_9 = '# 9 =>'
controlador(mensagem_problema_9, mensagem_problema_anterior=mensagem_problema_8, problema_anterior=problema_8)

def problema_9():
    ...
    

problema_9()

# 10. 
mensagem_problema_10 = '# 10 =>'
controlador(mensagem_problema_10, mensagem_problema_anterior=mensagem_problema_9, problema_anterior=problema_9)

def problema_10():
    ...
    

problema_10()

controlador(mensagem=False, mensagem_problema_anterior=mensagem_problema_10, problema_anterior=problema_10, ultimo_exercicio=True)