from menu import *
from time import sleep

arq = "log.txt"
criarArquivo(arq)
validarArquivo(arq)

def main():

    cabecalho(f'Gerenciamento CyberCafe')
    while True:
        resposta = menu(['Adicionar Jogo','Remover Jogo','Editar Jogo','Adcionar Nova Seccao', 'Remover Seccao Existente','Todas as Seccoes', 'Buscar Jogos', 'Sair'])
        if resposta == 1:
            cabecalho('Adicionar Jogo')

        elif resposta == 2:
            cabecalho('Remover Jogo')

        elif resposta == 3:
            cabecalho('Editar Jogo')

        elif resposta == 4:
            cabecalho('Adicionar Nova Seccao')

        elif resposta == 5:
            cabecalho('Remover Seccao Existente')

        elif resposta == 6:
            cabecalho('Todas as Seccoes')

        elif resposta == 7:
            cabecalho('Buscar Jogos')
        
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