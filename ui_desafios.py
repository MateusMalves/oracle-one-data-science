# UI - Controle de fluxo
def controlador(mensagem=False, mensagem_problema_anterior=False, problema_anterior=False, primeiro_exercicio=False, ultimo_exercicio=False, abrir_nova_sessão=False, apos_saudacao=False, loop=False):
    import re

    def coletar_resposta():
        if ultimo_exercicio:
            if not loop:
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n=> Este era o último exercício.')
                print('Deseja repetir o exercício?')
            print('\n=> Responda Y para sim e N para não:')
            resposta = input('Deseja continuar? ').upper()
            return resposta
        elif not abrir_nova_sessão and not loop:
            if not primeiro_exercicio:
                if not apos_saudacao:
                    print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
                print(f'\n\nVamos para o próximo exercício?')
            else:
                print(f'\n\nVamos resolver uns probleminhas legais?')
        elif abrir_nova_sessão and not loop:
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
            print(f'\n\nAgora vamos ver algumas coisas mais emocionantes?')
        
        print(f'\n=> Responda Y para sim e N para não {"(R para repetir o exercício anterior)" if not primeiro_exercicio else ""}:')
        resposta = input('Deseja continuar? ').upper()
        return resposta

    def continuar():
        if not abrir_nova_sessão:
            print('\n\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
            print(f'\n{mensagem.replace("?", ".")}\n')
        else:
            print('\n')

    def encerrar():
        print('\nOk, até a próxima!\n')
        quit()
    
    def repetir_exercicio():
        print('\n\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
        print(f'\n{mensagem_problema_anterior.replace("?", ".")}\n')
        problema_anterior()
        controlador(mensagem, mensagem_problema_anterior, problema_anterior, primeiro_exercicio=False, ultimo_exercicio=ultimo_exercicio, abrir_nova_sessão=abrir_nova_sessão, apos_saudacao=False, loop=False)
    
    def tratar_input_errado():
        print('!! Resposta inválida.')
        controlador(mensagem, mensagem_problema_anterior, problema_anterior, primeiro_exercicio=primeiro_exercicio, ultimo_exercicio=ultimo_exercicio, abrir_nova_sessão=abrir_nova_sessão, apos_saudacao=False, loop=True)

    resposta = coletar_resposta()
    if re.match(r'^[YNR]$', resposta):
        if ultimo_exercicio:
            if resposta == 'Y':
                repetir_exercicio()
            elif resposta == 'N':
                encerrar()
            elif resposta == 'R':
                tratar_input_errado()
        elif resposta == 'Y':
            continuar()
        elif resposta == 'N':
            encerrar()
        elif resposta == 'R' and not primeiro_exercicio:
            repetir_exercicio()
    else:
        tratar_input_errado()


def saudacao(mensagem):
    print('\n# # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # #\n')
    print(f'=> {mensagem}\n')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('# # # # # # # # # # # # # # # # # # # # # # # # # #')