import os
from time import sleep
from jogos import *
from salao import *

class menu:
    def linha(tam = 50):
        return '-' * tam

    def cabecalho(txt):
        print(menu.linha())
        print(txt.center(50))

    def verificaArquivo(nome):
        try:
            arquivo = open(nome, 'rt')
            arquivo.close()
        except:
            menu.criarArquivo(nome)

    def criarArquivo(nome): 
        try:
            arquivo = open(nome, 'wt+')
            arquivo.close()
        except Exception as e:
            print(f"Erro ao criar arquivo: {e}")
        else:
            print("Arquivo criado com sucesso")

    def opcoes(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            except KeyboardInterrupt:
                print('\033[31mO usuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                return n

    def interface(listaOpc):
        menu.cabecalho("Menu Principal")
        for c, item in enumerate(listaOpc, start=1):
            print("\033[92m" + f"{c} - {item}" + "\033[0m")
        print(menu.linha())
        opcao = menu.opcoes('Voce escolheu: ')
        return opcao
    
    def limparTerminal():
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Linux e Unix
            os.system('clear')
    
    def criar():
        menu.cabecalho(f'Gerenciamento CyberCafe')
        while True:
            resposta = menu.interface(['Adicionar Jogo','Remover Jogo','Editar Jogo','Adcionar Nova Seccao', 'Remover Seccao Existente','Todas as Seccoes', 'Buscar Jogos', 'Sair'])
            if resposta == 1:
                menu.cabecalho('Adicionar Jogo')
                jogos.adcionarJogo()
                sleep(1)
                menu.limparTerminal()
            
            elif resposta == 2:
                menu.cabecalho('Remover Jogo')
                jogos.removerJogo()
                sleep(1)


            elif resposta == 3:
                menu.cabecalho('Editar Jogo')

            elif resposta == 4:
                menu.cabecalho('Adicionar Nova Seccao')

            elif resposta == 5:
                menu.cabecalho('Remover Seccao Existente')

            elif resposta == 6:
                menu.cabecalho('Todas as Seccoes')

            elif resposta == 7:
                menu.cabecalho('Buscar Jogos')
            
            elif resposta == 8:
                print('Salvando Alterecoes...')
                sleep(1)
                print('Sistema Encerrado')
                #menu.limparTerminal()
                sleep(1)
                break
            
            else:
                print('Opção invalida')
            sleep(1)
            #menu.limparTerminal()