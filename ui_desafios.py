"""
==============================================
Oracle ONE - Data Science Course
==============================================

File: ui_desafios.py
Author: Mateus Alves de Mendonça
Description: CLI interface for course challenges navigation
Created: Oracle ONE Data Science Program
License: MIT

Este módulo fornece uma interface de linha de comando para
navegação entre os desafios do curso, melhorando a experiência
do usuário durante a resolução dos exercícios.
"""

# UI - Controle de fluxo
def controlador(
    mensagem: str = None,
    mensagem_problema_anterior: str = None,
    problema_anterior: callable = None,
    primeiro_exercicio: bool = False,
    ultimo_exercicio: bool = False,
    abrir_nova_sessão: bool = False,
    apos_saudacao: bool = False,
    saudacao: str = None,
    isRecursion: bool = False
) -> None:
    """
    ### 🎯 Função principal para controle de fluxo dos desafios do curso ONE - Oracle Next Education

    Controla a navegação entre os desafios no terminal, melhorando a experiência do usuário.

    Você pode copiar um template de código para os desafios neste link: [Template de código](./template_desafio_hora-da-pratica.py)

    ---
    ## 🧾 Parâmetros:

    - **mensagem** (`str`, opcional):  
      Mensagem de contextualização do problema.  
      *Default: None*

    - **mensagem_problema_anterior** (`str`, opcional):  
      Mensagem do problema anterior para referência.  
      *Default: None*

    - **problema_anterior** (`function`, opcional):  
      Função executada para repetir o exercício anterior.  
      *Default: None*

    - **primeiro_exercicio** (`bool`):  
      Define se é o primeiro exercício.  
      *Default: False*

    - **ultimo_exercicio** (`bool`):  
      Define se é o último exercício.  
      *Default: False*

    - **abrir_nova_sessao** (`bool`):  
      Inicia uma nova sessão dos desafios.  
      *Default: False*

    - **apos_saudacao** (`bool`):  
      Indica se o exercício atual vem após a saudação de uma nova sessão.  
      *Default: False*

    - **saudacao** (`str`, opcional):  
      Saudação exibida ao iniciar nova sessão.  
      *Default: None*

    - **isRecursion** (`bool`):  
      ⚠️ Não alterar: Variável interna para controle de recursões.
      *Default: False*

    ---
    ⚠️ *Parâmetros marcados como “Não alterar” são utilizados internamente para controle da aplicação.*
    """

    def coletar_resposta():
        if ultimo_exercicio:
            if not isRecursion:
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n\n=> Este era o último exercício.')
                print('\nDeseja repetir o exercício?')
            print('\n=> Responda Y para sim e N para não:')
            resposta = input('Deseja repetir? ').upper()
            return resposta
        elif not abrir_nova_sessão and not isRecursion:
            if not primeiro_exercicio:
                if not apos_saudacao:
                    print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
                    print('\n\nVamos para o próximo exercício?')
                else:
                    print('Vamos resolver uns probleminhas legais?')
            else:
                print('Vamos resolver uns probleminhas legais?')
        elif abrir_nova_sessão and not isRecursion:
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
            print(f'\n\nAgora vamos ver algumas coisas mais emocionantes?')
        
        print(f'\n=> Responda Y para sim e N para não {"(R para repetir o exercício anterior)" if not primeiro_exercicio else ""}:')
        resposta = input('Deseja continuar? ').upper()
        return resposta

    def tratar_input_errado():
        print('!! Resposta inválida.')
        controlador(mensagem, mensagem_problema_anterior, problema_anterior, primeiro_exercicio=primeiro_exercicio, ultimo_exercicio=ultimo_exercicio, abrir_nova_sessão=abrir_nova_sessão, apos_saudacao=False, isRecursion=True)

    def validar_resposta(resposta):
        import re
        validation_regex = r'^[YNR]$' if not primeiro_exercicio and not ultimo_exercicio else r'^[YN]$'
        if re.match(validation_regex, resposta):
            return resposta
        else:
            tratar_input_errado()

    def formatar_mensagens(mensagem):
        if len(mensagem) > 360:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 8 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:divisor * 3]) + '\n' + ' '.join(mensagem[divisor * 3:divisor * 4]) + '\n' + ' '.join(mensagem[divisor * 4:divisor * 5]) + '\n' + ' '.join(mensagem[divisor * 5:divisor * 6]) + '\n' + ' '.join(mensagem[divisor * 6:divisor * 7]) + '\n' + ' '.join(mensagem[divisor * 7:])
        elif len(mensagem) > 315:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 7 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:divisor * 3]) + '\n' + ' '.join(mensagem[divisor * 3:divisor * 4]) + '\n' + ' '.join(mensagem[divisor * 4:divisor * 5]) + '\n' + ' '.join(mensagem[divisor * 5:divisor * 6]) + '\n' + ' '.join(mensagem[divisor * 6:])
        elif len(mensagem) > 270:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 6 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:divisor * 3]) + '\n' + ' '.join(mensagem[divisor * 3:divisor * 4]) + '\n' + ' '.join(mensagem[divisor * 4:divisor * 5]) + '\n' + ' '.join(mensagem[divisor * 5:])
        elif len(mensagem) > 225:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 5 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:divisor * 3]) + '\n' + ' '.join(mensagem[divisor * 3:divisor * 4]) + '\n' + ' '.join(mensagem[divisor * 4:])
        elif len(mensagem) > 180:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 4 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:divisor * 3]) + '\n' + ' '.join(mensagem[divisor * 3:])
        elif len(mensagem) > 135:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 3 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:divisor * 2]) + '\n' + ' '.join(mensagem[divisor * 2:])
        elif len(mensagem) > 90:
            mensagem = mensagem.split(' ')
            divisor = len(mensagem) // 2 + 3
            mensagem = ' '.join(mensagem[:divisor]) + '\n' + ' '.join(mensagem[divisor:])
        
        return mensagem

    def continuar():
        if abrir_nova_sessão:
            saudar(saudacao, espacos_inicio=3, espacos_final=3) if saudacao else None
        else:
            print('\n\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
            if mensagem is not None:
                print(f'\n{formatar_mensagens(mensagem.replace("?", "."))}\n')

    def encerrar():
        print('\n\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
        print('\n\nObrigado por participar!')
        print('Até a próxima! \\o/\n\n')
        quit()
    
    def repetir_exercicio():
        print('\n\n=> Repetindo o exercício anterior...')
        print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
        if mensagem_problema_anterior is not None:
            print(f'\n{formatar_mensagens(mensagem_problema_anterior.replace("?", "."))}\n')
        if problema_anterior is not None and callable(problema_anterior):
            problema_anterior()
        else:
            print('!!! Problema anterior não encontrado.\n')
        print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #\n') if apos_saudacao else None
        controlador(mensagem, mensagem_problema_anterior, problema_anterior, primeiro_exercicio=False, ultimo_exercicio=ultimo_exercicio, abrir_nova_sessão=abrir_nova_sessão, apos_saudacao=apos_saudacao, saudacao=saudacao, isRecursion=False)

    import time
    time.sleep(0.2)
    resposta = validar_resposta(coletar_resposta())
    if resposta == 'Y':
        if not ultimo_exercicio:
            continuar()
        else:
            repetir_exercicio()
    elif resposta == 'N':
        encerrar()
    elif resposta == 'R':
        repetir_exercicio()

def saudar(mensagem: str=None, espacos_inicio: int=2, espacos_final: int=2) -> None:
    '''
    Exibe uma saudação formatada com cabeçalho e rodapé decorativos.

    A função imprime uma mensagem com linhas decorativas antes e depois, 
    além de espaços em branco configuráveis acima e abaixo do conteúdo.

    Parâmetros:
    ----------
    - **mensagem** (str, obrigatório):
        A mensagem que será exibida no centro do bloco.
        *Default: 2*
    
    - **espacos_inicio** (int, opcional):
        Quantidade de linhas em branco antes do cabeçalho.
        *Default: 2*
    
    - **espacos_final** (int, opcional):
        Quantidade de linhas em branco após o rodapé.
        *Default: 2*
        
    Exemplo de saída:
    -----------------

    ```

    {espacos_iniciais}
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # #

    => Sua mensagem aqui

    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    {espacos_finais}

    ```
    
    -----------------
    Caso falte o argumento **mensagem**, a função retorna um espaçamento de 2 linhas.

    Exemplo de saída:
    -----------------

    ```

    {espacos_iniciais}
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # #
    {espacos_finais}

    ```
    '''
    espacos_iniciais = '\n' * espacos_inicio
    espacos_finais = '\n' * espacos_final
    if mensagem and isinstance(mensagem, str):
        print(f'{espacos_iniciais}# # # # # # # # # # # # # # # # # # # # # # # # # #')
        print('# # # # # # # # # # # # # # # # # # # # # # # # # #\n')
        print(f'=> {mensagem}\n')
        print('# # # # # # # # # # # # # # # # # # # # # # # # # #')
        print(f'# # # # # # # # # # # # # # # # # # # # # # # # # #{espacos_finais}')
    else:
        print(f'{espacos_iniciais}# # # # # # # # # # # # # # # # # # # # # # # # # #')
        print(f'# # # # # # # # # # # # # # # # # # # # # # # # # #{espacos_finais}')