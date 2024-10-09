# Declarando a Class No
class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None
# Declarando a Class ListaEncadeada
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None 
    # Adciona um dicionario em uma lista encadeada
    def adicionar(self, dado):
        novoNo = No(dado)
        if self.cabeca is None:
            self.cabeca = novoNo
        else:
            atual = self.cabeca
            anterior = None
            # Percorre a lista Encadeada até o fim
            while atual is not None and atual.dado['nome'] < novoNo.dado['nome']:

                anterior = atual
                atual = atual.proximo
            
            # Cria um encadeamento na Lista 
            if anterior is None:
                novoNo.proximo = self.cabeca
                self.cabeca = novoNo
            else:
                novoNo.proximo = atual
                anterior.proximo = novoNo
            
        print(f"{dado['nome']} adicionado com sucesso.")
    
    # Verifica e remove o nome receido
    def remover(self, nome):
        atual = self.cabeca
        anterior = None

        # Percorre a lista verifica se o nome recebido está presente na Lista
        while atual is not None and atual.dado['nome'] != nome:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            print(f"{nome} não encontrado.")
            return

        if anterior is None:
            self.cabeca = atual.proximo
        else:
            anterior.proximo = atual.proximo

        print(f"{nome} removido com sucesso.")     

    # Busca o nome recebido na Lista
    def buscar(self, nome):
        atual = self.cabeca
        #Precorre toda a Lista
        while atual is not None:
            # Verifica se o nome esta presente na lista
            if atual.dado['nome'] == nome:
                return atual.dado
            atual = atual.proximo
        return None

class Jogos:
    def __init__(self):
        # Instaciando a class Lista em jogos
        self.Lista = ListaEncadeada()

    # Converte os dados recebido para um dicionario
    def adicionarJogo(self, nome, tipo, precoJogatina, generoJogo):
        jogo = {
            'nome': nome,
            'tipo': tipo,
            'preco_jogatina': precoJogatina,
            'genero_jogo': generoJogo
        }
        # Adciona o decionario na Lista
        self.Lista.adicionar(jogo)

    # Verifica se o nome recebido esta presente na lista e o remove
    def removerJogo(self, nome):
        jogoRemovido = self.Lista.buscar(nome)
        if jogoRemovido:
            self.Lista.remover(nome)
        else:
            print(f"Jogo {nome} não encontrado.")
  
    # Carrega os dados dos jogos usados anteriomente (com base nos dados salvos no jogos.txt)
    def carregarJogos(self):
        try:
            with open('jogos.txt', 'r') as arquivo:
                for linha in arquivo:
                    nome, tipo, precoJogatina, generoJogo = linha.strip().split(',')
                    self.adicionarJogo(nome, tipo , precoJogatina , generoJogo)

        except FileNotFoundError:
            pass
                    
    # Escreve os jogos salvos na lista no arquivo jogos.txt
    def salvarJogos(self):
        with open('jogos.txt', 'r+') as arquivo:
            atual = self.Lista.cabeca
            while atual:
                jogo = atual.dado
                arquivo.write(f"{jogo['nome']},{jogo['tipo']},{jogo['preco_jogatina']},{jogo['genero_jogo']}\n")
                atual = atual.proximo

    # Edita o jogo recebedio na variavel nome
    def editarJogo(self, nome, novoNome=None, novoTipo=None, novoPrecoJogatina=None, novoGeneroJogo=None):
        atual = self.Lista.cabeca

        while atual is not None:
            if atual.dado['nome'] == nome:
                if novoNome:
                    atual.dado['nome'] = novoNome
                if novoTipo:
                    atual.dado['tipo'] = novoTipo
                if novoPrecoJogatina:
                    atual.dado['preco_jogatina'] = novoPrecoJogatina
                if novoGeneroJogo:
                    atual.dado['genero_jogo'] = novoGeneroJogo
                print(f"Jogo {nome} atualizado com sucesso!")
                self.salvarJogos()
                return atual.dado
            atual = atual.proximo
        
        print(f"Jogo {nome} não encontrado.")
        return None
    
    # Busca o nome recebido
    def buscarJogo(self, nome):
        jogo = self.Lista.buscar(nome)
        if jogo:
            print(f"Jogo encontrado: {jogo}")
            return jogo
        else:
            print(f"Jogo {nome} não encontrado.")
            return None
        
    # Lista todos os jogos disponiveis
    def listarJogos(self):
        jogos = []
        atual = self.Lista.cabeca
        if atual is None:
            return None
        while atual is not None:
            jogos.append(atual.dado['nome'])
            atual = atual.proximo
        return jogos 
class Sessao:
    def __init__(self):
        # Instaciando a class Lista em jogos
        self.Lista = ListaEncadeada()

    # Converte as variaveis recebidas para dicionario
    def adicionarSessao(self, nome, descricao, jogoSessao):
        sessao = {
            'nome': nome,
            'descricao': descricao,
            'jogoSessao': jogoSessao
        }
        # Adciona o dicionario na Lista
        self.Lista.adicionar(sessao)
        print(f"Sessão {nome} adicionada com sucesso!")

    # Escreve o dados presente na Lista no arquivo sessoes.txt
    def salvarSessoes(self):
        with open('sessoes.txt', 'w') as arquivo:
            atual = self.Lista.cabeca
            while atual is not None:
                sessao = atual.dado
                # Foi utilizado o .get() para eveitar o keyError
                nome = sessao.get('nome')
                descricao = sessao.get('descricao')
                jogoSessao = sessao.get('jogoSessao')
                arquivo.write(f"{nome},{descricao},{jogoSessao}\n")
                atual = atual.proximo
     # Carrega os dados doas sessoes anteriores (com base nos dados salvos no sessoes.txt)
    def carregarSessoes(self):
        try:
            with open('sessoes.txt', 'r+') as arquivo:
                for linha in arquivo:
                    nome, descricao, jogoSessao = linha.strip().split(',')
                    self.adicionarSessao(nome, descricao ,jogoSessao)
        except FileNotFoundError:
            pass
    
    # Remove o nome recebido da Lista
    def removerSessao(self, nome):
        self.Lista.remover(nome)
        self.salvarSessoes()

    # Lista todas as sessões criadas
    def listarSessoes(self):
        sessoes = []
        atual = self.Lista.cabeca
        if atual is None:
            return None
        while atual is not None:
            sessoes.append(atual.dado['nome'])
            atual = atual.proximo
        return sessoes

