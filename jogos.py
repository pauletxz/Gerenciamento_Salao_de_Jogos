import numpy as np

class jogos:
    def adcionarJogo():
        nome = str(input('Informe o nome do jogo:'))
        tipo = str(input('Informe o tipo do jogo:'))
        precoJogatina = float(input('Informe o preco da hora jogada:'))
        generoJogo = str(input('Informe o genero do jogo:'))
        jogo = {
            'nome':nome,
            'tipo':tipo,
            'precoJogatina':precoJogatina,
            'gerenoJogo':generoJogo
        }
        jogos.append(jogo)
        print('Jogo adicionado com sucesso')
        return jogo

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
