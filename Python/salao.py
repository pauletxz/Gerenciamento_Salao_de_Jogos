class sessao:
    def __init__(self, nome, descricao, jogos):
        self.nome = nome
        self.descricao = descricao
        self.jogos = jogos
    
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

class listaEncadeada:
    def __init__(self):
        self.primeiro = None
    
    def inserirInicio(self,valor):
        novo = No(valor)
        novo.prox = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        aux = self.primeiro
        while aux != None:
            print(aux.valor, end=' ')
            aux = aux.prox

    def excluirPrimeiro(self):
        temp = self.primeiro
        if self.primeiro.prox == None:
            return None
        self.primeiro = self.primeiro.prox
        return temp

