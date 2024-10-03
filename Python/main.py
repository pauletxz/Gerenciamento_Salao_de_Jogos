from menu import *

def main():
    arq1 = "jogo_log.txt"
    arq2 = "sessao_log.txt"
    menu.criarArquivo(arq1)
    menu.verificaArquivo(arq1)
    menu.criarArquivo(arq2)
    menu.verificaArquivo(arq2)
    menu.criar()

if __name__ == "__main__":
     main()