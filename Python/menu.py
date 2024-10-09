import os 
from time import sleep
from re import search
from defs import Jogos, Sessao

class Menu:
    def __init__(self, jogo, sessao):
        # Instanciando as class Jogos e sessao no Menu
        self.jogos = jogo
        self.sessao = sessao
        pass
    
    # Função para criar as linhas no menu
    def linha(tam=50):
        return '-' * tam

    # Função que cria e centraliza o cabecalho
    def cabecalho(txt):
        print(Menu.linha())
        print(txt.center(50))
        print(Menu.linha())

    # Função para receber e verificar as opções digitadas pelo usuario
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
    # verifica a entrada (Verificando se o usuario 2 espaços em branco, ou digitou algum caracter invisivel)
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
    # verifica a entrada (Verificando se a entrada do usaurio foi um numero inteiro ou real)
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

    # Cria a interface
    def interface(listaOpc):
        Menu.cabecalho("Menu Principal")
        for c, item in enumerate(listaOpc, start=1):
            print("\033[92m" + f"{c} - {item}" + "\033[0m") 
        print(Menu.linha())
        opcao = Menu.opcoes('Você escolheu: ')
        return opcao

    # Virifica qual o OS do usario e limpa o terminal
    def limparTerminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    #Cria o menu
    def criar(self):
        Menu.cabecalho('Gerenciamento CyberCafe')
        jogos = self.jogos
        sessao = self.sessao
        while True:
            resposta = Menu.interface([
                'Adicionar Jogo', 'Remover Jogo', 'Editar Jogo',
                'Adicionar Nova Seção', 'Remover Seção Existente',
                'Todas as Seções', 'Buscar Jogos', 'Sair'
            ])  
            if resposta == 1:

                Menu.cabecalho('Adicionar Jogo')

                nome = Menu.validarEntradasUsuario('Informe o nome do jogo: ')
                tipo = Menu.validarEntradasUsuario('Informe o tipo de jogo: ')
                preco_jogatina = Menu.validarEntredaFloat('Informe o valor da hora: ')
                genero_jogo = Menu.validarEntradasUsuario('Informe o gênero do jogo: ')

                jogos.adicionarJogo(nome, tipo, preco_jogatina, genero_jogo)
            
                sleep(1)
                Menu.limparTerminal()

            elif resposta == 2:

                Menu.cabecalho('Remover Jogo')
                nome = Menu.validarEntradasUsuario('Informe o nome do jogo a remover: ')
                jogos.removerJogo(nome)

                sleep(1)
                Menu.limparTerminal()

            elif resposta == 3:

                Menu.cabecalho('Editar Jogo')
                jogosDisponivel = jogos.listarJogos()

                print('Jogos Disponiveis: ')
                print(jogosDisponivel)
                nome = Menu.validarEntradasUsuario('Informe o nome do jogo que deseja editar: ')
                novoNome = Menu.validarEntradasUsuario('Informe o novo nome para o jogo: ')
                tipo = Menu.validarEntradasUsuario('Informe o novo tipo do jogo: ')
                preco_jogatina = Menu.validarEntredaFloat('Informe o novo valor da hora: ')
                genero_jogo = Menu.validarEntradasUsuario('Informe o novo gênero do Jogo: ')
                jogos.editarJogo(nome, novoNome, tipo, preco_jogatina, genero_jogo)
                

                sleep(1)
                Menu.limparTerminal()

            elif resposta == 4:
                Menu.cabecalho('Adicionar Nova Sessão')
                jogosDisponivel = jogos.listarJogos()

                if jogosDisponivel:
                    nome = Menu.validarEntradasUsuario('Informe o nome da sessão: ')
                    descricao = Menu.validarEntradasUsuario('Informe a descrição da sessão: ')
                    print("Jogos Disponiveis: ")
                    print(jogosDisponivel)
                    jogoSelecionado = Menu.validarEntradasUsuario('Digite jogos listados acima: ')
                    sessao.adicionarSessao(nome, descricao, jogoSelecionado)
                else:
                    print("Nenhum jogo disponível.")

                sleep(1)
                Menu.limparTerminal()


            elif resposta == 5:

                Menu.cabecalho('Remover Sessão Existente')
                listaSessoes = sessao.listarSessoes()
                if listaSessoes:
                    print('Sessões Disponiveis: ')
                    print(listaSessoes)
                    nome = Menu.validarEntradasUsuario('Informe o nome da sessão que deseja remover: ')
                    sessao.removerSessao(nome)
                
                sleep(1)
                Menu.limparTerminal()

            elif resposta == 6:
                Menu.cabecalho('Todas as Sessões')
                listaSessoes = sessao.listarSessoes()
                print("Sessões Disponiveis: ")
                print(listaSessoes)
                sair = input('Digite ENTER para voltar ao menu')

                sleep(1)
                Menu.limparTerminal()

            elif resposta == 7:
                Menu.cabecalho('Buscar Jogos')
                nome = Menu.validarEntradasUsuario('Informe o nome do jogo que sera buscado: ')
                jogoBuscado = jogos.buscarJogo(nome)
                
                sair = input('Digite ENTER para voltar ao menu')
                sleep(1)
                Menu.limparTerminal()

            elif resposta == 8:
                print('Salvando Alterações...')
                jogos.salvarJogos()
                sessao.salvarSessoes()

                sleep(.5)
                print('Sistema Encerrado')
                Menu.limparTerminal()
                sleep(.5)
                break
            else:
                print('Opção inválida')
            sleep(1)