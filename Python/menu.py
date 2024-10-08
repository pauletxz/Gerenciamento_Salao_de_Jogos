import os 
from time import sleep
from re import search
from defs import Jogos, Sessao

class menu:
    
    def linha(tam=50):
        return '-' * tam

    def cabecalho(txt):
        print(menu.linha())
        print(txt.center(50))
        print(menu.linha())

    def verificaArquivo(nome):
        try:
            with open(nome, 'rt'):
                pass
        except FileNotFoundError:
            menu.criarArquivo(nome)

    def criarArquivo(nome):
        try:
            with open(nome, 'wt+'):
                pass
        except Exception as e:
            print(f"Erro ao criar arquivo: {e}")
        else:
            print("Arquivo criado com sucesso")

    def opcoes(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número inteiro válido.\033[m')
                continue
            except KeyboardInterrupt:
                print('\033[31mO usuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                return n

    def validarEntradasUsuario(msg):
        while True:
            entrada = input(msg).strip().lower()
            if not entrada:
                print('\033[31mERRO! Digite um valor válido.\033[m')
                continue
            if search(r'\s{2,}, , ', entrada):
                print('\033[31mERRO! Digite um valor válido.\033[m')
                continue
            if search(r'ㅤ', entrada):
                print('\033[31mERRO! Digite um valor válido.\033[m')
                continue
            return entrada
        
    def validarEntredaFloat(msg):
        while True:
            try:
                entrada = float(input(msg))
            except (ValueError, TypeError):
                print('\033[31mERRO! Digite um número válido.\033[m')
                continue
            except KeyboardInterrupt:
                print('\033[31mO usuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                return entrada

    def interface(listaOpc):
        menu.cabecalho("Menu Principal")
        for c, item in enumerate(listaOpc, start=1):
            print("\033[92m" + f"{c} - {item}" + "\033[0m") 
        print(menu.linha())
        opcao = menu.opcoes('Você escolheu: ')
        return opcao

    def limparTerminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def criar():
        menu.cabecalho('Gerenciamento CyberCafe')
        jogos = Jogos()
        sessao = Sessao()
        while True:
            resposta = menu.interface([
                'Adicionar Jogo', 'Remover Jogo', 'Editar Jogo',
                'Adicionar Nova Seção', 'Remover Seção Existente',
                'Todas as Seções', 'Buscar Jogos', 'Sair'
            ])  
            if resposta == 1:

                menu.cabecalho('Adicionar Jogo')
                nome = menu.validarEntradasUsuario('Informe o nome do jogo: ')
                tipo = menu.validarEntradasUsuario('Informe o tipo de jogo: ')
                preco_jogatina = menu.validarEntredaFloat('Informe o valor da hora: ')
                genero_jogo = menu.validarEntradasUsuario('Informe o gênero do jogo: ')
                jogos.adicionarJogo(nome, tipo, preco_jogatina, genero_jogo)
            
                sleep(1)
                menu.limparTerminal()

            elif resposta == 2:

                menu.cabecalho('Remover Jogo')
                nome = menu.validarEntradasUsuario('Informe o nome do jogo a remover: ')
                jogos.removerJogo(nome)

                sleep(1)
                menu.limparTerminal()

            elif resposta == 3:

                menu.cabecalho('Editar Jogo')
                jogosDisponivel = jogos.listarJogos()

                print('Jogos Disponiveis: ')
                print(jogosDisponivel)
                nome = menu.validarEntradasUsuario('Informe o nome do jogo que deseja editar: ')
                tipo = menu.validarEntradasUsuario('Informe o novo tipo do jogo: ')
                preco_jogatina = menu.validarEntredaFloat('Informe o novo valor da hora: ')
                genero_jogo = menu.validarEntradasUsuario('Informe o novo gênero do Jogo: ')
                jogos.editarJogo(nome, tipo, preco_jogatina, genero_jogo)

                sleep(1)
                menu.limparTerminal()

            elif resposta == 4:
                menu.cabecalho('Adicionar Nova Sessão')
                jogosDisponivel = jogos.listarJogos()

                if jogosDisponivel:
                    nome = menu.validarEntradasUsuario('Informe o nome da sessão: ')
                    descricao = menu.validarEntradasUsuario('Informe a descrição da sessão: ')
                    print("Jogos Disponiveis: ")
                    print(jogosDisponivel)
                    jogoSelecionado = menu.validarEntradasUsuario('Digite jogos listados acima: ')
                    sessao.adicionarSessao(nome, descricao, jogoSelecionado)
                else:
                    print("Nenhum jogo disponível.")

                sleep(1)
                menu.limparTerminal()


            elif resposta == 5:

                menu.cabecalho('Remover Sessão Existente')
                listaSessoes = sessao.listarSessoes()
                if listaSessoes:
                    print('Sessões Disponiveis: ')
                    print(listaSessoes)
                    nome = menu.validarEntradasUsuario('Informe o nome da sessão que deseja remover: ')
                    sessao.removerSessao(nome)
                
                sleep(1)
                menu.limparTerminal()

            elif resposta == 6:
                menu.cabecalho('Todas as Sessões')
                listaSessoes = sessao.listarSessoes()
                print("Sessões Disponiveis: ")
                print(listaSessoes)
                sair = input('Digite ENTER para voltar ao menu')

                sleep(1)
                menu.limparTerminal()

            elif resposta == 7:
                menu.cabecalho('Buscar Jogos')
                nome = menu.validarEntradasUsuario('Informe o nome do jogo que sera buscado: ')
                jogoBuscado = jogos.buscarJogo(nome)
                if jogoBuscado:
                    print(jogoBuscado)
                
                sair = input('Digite ENTER para voltar ao menu')
                sleep(1)
                menu.limparTerminal()

            elif resposta == 8:
                print('Salvando Alterações...')
                jogos.atualizarArquivoJogo()
                sessao.atualizarArquivoSessao()
                
                sleep(.5)
                print('Sistema Encerrado')
                menu.limparTerminal()
                sleep(.5)
                break
            else:
                print('Opção inválida')
            sleep(1)