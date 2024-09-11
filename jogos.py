class jogos:
    def adcionarJogo():
        jogo = {
            'nome':nome,
            'tipo':tipo,
            'precoJogatina':precoJogatina,
            'gerenoJogo':generoJogo
        }
        nome = str(input('Informe o nome do jogo:'))
        tipo = str(input('Informe o tipo do jogo:'))
        precoJogatina = float(input('Informe o preco da hora jogada:'))
        generoJogo = str(input('Informe o genero do jogo:'))

        jogos.append(jogo)
        print('Jogo adicionado com sucesso')
        return jogo