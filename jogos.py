class Jogos:
    def __init__(self):
        self.jogos = []

    def adicionarJogo(self, nome, tipo, preco_jogatina, genero_jogo):
        jogo = {
            'nome': nome,
            'tipo': tipo,
            'preco_jogatina': preco_jogatina,
            'genero_jogo': genero_jogo
        }
        self.jogos.append(jogo)

        print('Jogo adicionado com sucesso')
        return jogo

    def removerJogo(self, nome):
        for jogo in self.jogos:
            if jogo['nome'] == nome:
                self.jogos.remove(jogo)
                print(f'Jogo {nome} removido com sucesso!')
                return
        print(f'Jogo {nome} não encontrado.')

class Seccao:
    def __init__(self):
        self.seccao = []

    def adicionarSecao(self, nome, descricao, jogoSessao):
        secao = {
            'nome': nome,
            'descricao': descricao,
            'jogos': jogoSessao  # Lista de jogos relacionados à seção
        }
        self.secoes.append(secao)
        print('Seção adicionada com sucesso')
        return secao

    
