import numpy as np

class jogos:
    def __init__(self, nome, tipo, precoJogatina, generoJogo):
        self.nome = nome
        self.tipo = tipo
        self.precoJogatina = precoJogatina
        self.gerenoJogo = generoJogo

class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

