def linha(tam = 50):
     return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

def opcoes(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')  # Corrigido o código de escape
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')  # Corrigido o código de escape
            return 0
        else:
            return n

def menu(listaOpc):
    cabecalho("Menu Principal")
    for c, item in enumerate(listaOpc, start=1):
        print(f"{c} - {item}")
    print(linha())
    opcao = opcoes('Voce escolheu: ')
    return opcao