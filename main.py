from menu import *
from time import sleep
from jogos import *
from salao import *

arq = "log.txt"
menu.criarArquivo(arq)
menu.validarArquivo(arq)

def main():

    menu.cabecalho(f'Gerenciamento CyberCafe')
    while True:
        resposta = menu.interface(['Adicionar Jogo','Remover Jogo','Editar Jogo','Adcionar Nova Seccao', 'Remover Seccao Existente','Todas as Seccoes', 'Buscar Jogos', 'Sair'])
        if resposta == 1:
            menu.cabecalho('Adicionar Jogo')
            jogos.adcionarJogo()
            sleep(1)
        
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
            sleep(1)
            break
        
        else:
            print('Opção invalida')
        sleep(1)


if __name__ == "__main__":
     main()