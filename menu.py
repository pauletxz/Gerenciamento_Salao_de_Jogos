class menu:
    def linha(tam = 50):
        return '-' * tam

    def cabecalho(txt):
        print(menu.linha())
        print(txt.center(50))

    def verificaArquivo(nome):
        try:
            arquivo = open(nome, 'rt')
            arquivo.close()
        except FileExistsError:
            return False
        else:
            return True
        
    def validarArquivo(nome): # tentar unir validarArquivo e verificarArquivo em uma funcao só
        if menu.verificaArquivo(nome): # ta uma gambiarra massa essas 3 funcoes pra so saber a existencia desse arquivo kkk
            print("Arquivo encontrado")
        else:
            menu.criarArquivo(nome)

    def criarArquivo(nome): 
        try:
            arquivo = open(nome, 'wt+')
            arquivo.close()
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

    def interface(listaOpc):
        menu.cabecalho("Menu Principal")
        for c, item in enumerate(listaOpc, start=1):
            print("\033[92m" + f"{c} - {item}" + "\033[0m")
        print(menu.linha())
        opcao = menu.opcoes('Voce escolheu: ')
        return opcao