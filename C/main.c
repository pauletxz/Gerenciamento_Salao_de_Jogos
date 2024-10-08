#include "jogo.c"
#include "menu.c"

int main(){
    
    criarArquivoTexto("jogos.txt");
    No *lista_jogos = NULL;
    Sessao *lista_sessoes = NULL;
    unsigned char op;
    unsigned int saida = 0;

    do{
        ApresentaMenu(N_OPCOES, OPCAO1,
                      TITULO_OPCAO1, TITULO_OPCAO2,
                      TITULO_OPCAO3, TITULO_OPCAO4,
                      TITULO_OPCAO5, TITULO_OPCAO6,
                      TITULO_OPCAO7, TITULO_OPCAO8);
        op = LeOpcao(OPCAO1, OPCAO1 + N_OPCOES - 1);

        switch (op){
            case OPCAO1:{
                Beep(1000, 500);
                char nome[50], tipo[50], genero[50];
                float preco;
                printf("---------------------\n");
                printf("Nome do jogo: \n");
                scanf("%s", nome);
                printf("Tipo do jogo: \n");
                scanf("%s", tipo);
                preco = LeFloat();
                printf("Genero do jogo: \n");
                scanf("%s", genero);
                printf("---------------------\n");
                lista_jogos = adicionar(lista_jogos, nome, tipo, preco, genero);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO2:{
                Beep(1000, 500);
                char nome[50];
                printf("---------------------\n");
                printf("Digite o nome do jogo a ser removido: \n");
                scanf("%s", nome);
                printf("---------------------\n");
                lista_jogos = tira(lista_jogos, nome);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO3:{
                Beep(1000, 500);
                editar(lista_jogos);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO4:{
                Beep(1000, 500);
                char nome[50], descricao[250];
                printf("---------------------\n");
                printf("Nome da sessao: \n");
                scanf("%s", nome);
                printf("Descricao da sessao: \n");
                scanf(" %[^\n]", descricao);
                printf("---------------------\n");
                lista_sessoes = adicionar_sessao(lista_sessoes, descricao, nome);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO5:{
                Beep(1000, 500);
                char nome[50];
                printf("---------------------\n");
                printf("Digite o nome da sessao a ser removida: \n");
                scanf("%s", nome);
                printf("---------------------\n");
                lista_sessoes = excluir_sessao(lista_sessoes, nome);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO6:{
                Beep(1000, 500);
                listar_sessoes(lista_sessoes);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO7:{
                Beep(1000, 500);
                char nome[50];
                lista_jogos = busca(lista_jogos, nome);
                delay();
                limparTerminal();
                break;
            }

            case OPCAO8:{
                Beep(1000, 500);
                printf("---------------------\n");
                printf("Saindo...\n");
                saida = 1;
                break;
            }

            default:{
                printf("Opcao invalida! Tente novamente.\n");
                delay();
                limparTerminal();
                break;
            }
        }
    } while (!saida);

    liberar_sessoes(lista_sessoes);
    liberar_jogos(lista_jogos);

    return 0;
}