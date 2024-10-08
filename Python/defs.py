class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None 
    
    def adicionar(self, dado):
        novo_no = No(dado)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            anterior = None
            
            while atual is not None and atual.dado['nome'] < novo_no.dado['nome']:
                anterior = atual
                atual = atual.proximo
            
          
            if anterior is None:
                novo_no.proximo = self.cabeca
                self.cabeca = novo_no
            else:
                novo_no.proximo = atual
                anterior.proximo = novo_no
            
        print(f"{dado['nome']} adicionado com sucesso.")
    
    def remover(self, nome):
        atual = self.cabeca
        anterior = None

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
    
    def listar(self):
        atual = self.cabeca
        if atual is None:
            print("Nenhuma dado encontrada.")
        while atual is not None:
            print(atual.dado)
            atual = atual.proximo
            
        

    def buscar(self, nome):
        atual = self.cabeca
        while atual is not None:
            if atual.dado['nome'] == nome:
                return atual.dado
            atual = atual.proximo
        return None

class Jogos:
    def __init__(self):
        self.jogos = ListaEncadeada()

    def adicionarJogo(self, nome, tipo, preco_jogatina, genero_jogo):
        jogo = {
            'nome': nome,
            'tipo': tipo,
            'preco_jogatina': preco_jogatina,
            'genero_jogo': genero_jogo
        }
        self.jogos.adicionar(jogo)
        self.atualizarArquivoJogo()
        return jogo

    def adicionarJogoArquivo(self, nome, tipo, preco_jogatina, genero_jogo):
        with open('jogo_log.txt', 'a') as arquivo:
            arquivo.write(f"Nome: {nome}, Tipo: {tipo}, Preço: {preco_jogatina}, Gênero: {genero_jogo}\n")
        print(f"Jogo {nome} salvo no arquivo com sucesso!")

    def removerJogo(self, nome):
        jogo_removido = self.jogos.buscar(nome)
        if jogo_removido:
            self.jogos.remover(nome)
            self.atualizarArquivoJogo()
        else:
            print(f"Jogo {nome} não encontrado.")

    def atualizarArquivoJogo(self):
        with open('jogo_log.txt', 'w') as arquivo:
            atual = self.jogos.cabeca
            while atual is not None:
                arquivo.write(f"Nome: {atual.dado['nome']}, Tipo: {atual.dado['tipo']}, Preço: {atual.dado['preco_jogatina']}, Gênero: {atual.dado['genero_jogo']}\n")
                atual = atual.proximo
        print("Arquivo atualizado com os jogos restantes.")

    def editarJogo(self, nome, novo_nome=None, novo_tipo=None, novo_preco_jogatina=None, novo_genero_jogo=None):
        atual = self.jogos.cabeca
        
        while atual is not None:
            if atual.dado['nome'] == nome:
                if novo_nome:
                    atual.dado['nome'] = novo_nome
                if novo_tipo:
                    atual.dado['tipo'] = novo_tipo
                if novo_preco_jogatina:
                    atual.dado['preco_jogatina'] = novo_preco_jogatina
                if novo_genero_jogo:
                    atual.dado['genero_jogo'] = novo_genero_jogo
                print(f"Jogo {nome} atualizado com sucesso!")
                self.atualizarArquivoJogo()
                return atual.dado
            atual = atual.proximo
        
        print(f"Jogo {nome} não encontrado.")
        return None

    def buscarJogo(self, nome):
        jogo = self.jogos.buscar(nome)
        if jogo:
            print(f"Jogo encontrado: {jogo}")
            return jogo
        else:
            print(f"Jogo {nome} não encontrado.")
            return None
        

    def listarJogos(self):
        jogos = []
        atual = self.jogos.cabeca
        if atual is None:
            return None
        while atual is not None:
            jogos.append(atual.dado['nome'])
            atual = atual.proximo
        return jogos 
class Sessao:
    def __init__(self):
        self.sessoes = ListaEncadeada()

    def adicionarSessao(self, nome, descricao, jogoSessao):
        sessao = {
            'nome': nome,
            'descricao': descricao,
            'jogos': jogoSessao
        }
        self.sessoes.adicionar(sessao)
        self.atualizarArquivoSessao()

    def atualizarArquivoSessao(self):
        with open('sessao_log.txt', 'w') as arquivo:
            atual = self.sessoes.cabeca
            while atual is not None:
                arquivo.write(f"Nome: {atual.dado['nome']}, Descrição: {atual.dado['descricao']}, Jogos: {atual.dado['jogos']}\n")
                atual = atual.proximo
        print("Arquivo de seções atualizado.")

    def removerSessao(self, nome):
        self.sessoes.remover(nome)
        self.atualizarArquivoSessao()
        
    def listarSessoes(self):
        sessoes = []
        atual = self.sessoes.cabeca
        if atual is None:
            return None
        while atual is not None:
            sessoes.append(atual.dado['nome'])
            atual = atual.proximo
        return sessoes

