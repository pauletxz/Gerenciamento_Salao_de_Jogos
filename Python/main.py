from menu import Menu
from defs import Jogos, Sessao
def main():
    
    jogos = Jogos()
    sessao = Sessao()

    jogos.carregarJogos()
    sessao.carregarSessoes()

    menu = Menu(jogos, sessao)
    menu.criar()
    
if __name__ == "__main__":
     main()