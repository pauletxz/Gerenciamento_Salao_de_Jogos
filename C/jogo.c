#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "jogo.h"

struct jogo{
    char nome[50];
    char tipo[50];
    float preco;
    char genero[50];
};

struct no{
    Jogo * Jogo;
    No * prox;
};

struct sessao{
    char descricao[250];
    char nome[50];
    int num_jogos;
    struct sessao * prox;
};

void criarArquivoTexto(const char * jogos){
    FILE *arquivo = fopen(jogos, "w");
    if (arquivo == NULL) {
        perror("Erro ao criar o arquivo\n");
        return;
    }
}

No * adicionar(No * lista , char nome[], char tipo[], float preco, char genero[]){
    Jogo * novo_jogo = (Jogo*)malloc(sizeof(Jogo));
        if (novo_jogo == NULL){
            printf("Erro ao alocar memoria\n");
                exit(1);
        }
    strcpy(novo_jogo->nome, nome);
    strcpy(novo_jogo->tipo, tipo);
    strcpy(novo_jogo->genero, genero);
    novo_jogo->preco = preco;

    No * novo = (No*)malloc(sizeof(No));
        novo->Jogo = novo_jogo;
        novo->prox = lista;
    printf("jogo salvos \n");
    return novo;
}

No* tira(No * lista, char * nome){
    No* aux = lista;
    No* ant = NULL;
    int inf;
        while(aux != NULL){
    inf = strcmp(aux->Jogo->nome, nome);
        if (inf == 0){
            if(ant == NULL){
                lista = aux->prox;
            }else{
                ant->prox = aux->prox;
            }
    free(aux->Jogo);
    free(aux);
    printf("\nJogo removido");
    return lista;
        }
        ant = aux;
        aux = aux->prox;
    }
    printf("\nJogo nao encontrado");
    return lista; 
}

No * busca(No * lista, char * nome){
    No* aux = lista;
    int inf;
        for(aux; aux != NULL; aux = aux->prox){
            printf("qual jogo quer encontrar: \n");
                scanf("%c", nome);
    inf = strcmp(aux->Jogo->nome, nome);    
            if(inf == 0){
                printf("\n");
                printf("jogo encontrado: %s\n", aux->Jogo->nome);
                return aux;
            }
        }
    printf("jogo nao existente\n");
    return NULL;
}

void salvar(No * lista){
    No* aux = lista;
    FILE* arquivo = fopen("jogos.txt", "w+");
        if(arquivo == NULL){
    printf("arquivo vazio \n");
    }
        while(aux != NULL){
    fprintf(arquivo, "---------------------\n");
    fprintf(arquivo, "Nome: %s\n", aux->Jogo->nome);
    fprintf(arquivo, "Tipo: %s\n", aux->Jogo->tipo);
    fprintf(arquivo, "Genero: %s\n", aux->Jogo->genero);
    fprintf(arquivo, "Valor: %.2f\n", aux->Jogo->preco);
    fprintf(arquivo, "---------------------\n");
    printf("\n");
    aux = aux->prox;
    }
    fclose(arquivo);
    printf("dados salvos \n");
}

void editar(No * lista){
    int op;
    char nome[50];
            printf("Digite o nome do jogo que deseja editar: \n");
        scanf("%s", nome);
    No *jogo = busca(lista, nome);
        if(jogo){
    char novo_nome[50], novo_tipo[50], novo_genero[50];
    float novo_preco;

    printf("se nao quiser alterar aperte 1 \n");
    scanf("%d", &op);
        if(op == 1){return;}
    printf("Novo nome do jogo: \n");
    scanf("%c", &novo_nome);
    fgets(novo_nome, sizeof(novo_nome), stdin);
    strtok(novo_nome, "\n");

    printf("Novo tipo do jogo: \n");
    scanf("%c", &novo_tipo);
    fgets(novo_tipo, sizeof(novo_tipo), stdin);
    strtok(novo_tipo, "\n");

    printf("Novo genero do jogo: \n");
    scanf("%c", &novo_genero);
    fgets(novo_genero, sizeof(novo_genero), stdin);
    strtok(novo_genero, "\n");

    printf("Novo preco do jogo: \n");
    scanf("%f", &novo_preco);
    getchar(); 

        if(strlen(novo_nome) > 0) strcpy(jogo->Jogo->nome, novo_nome);
        if(strlen(novo_tipo) > 0) strcpy(jogo->Jogo->tipo, novo_tipo);
        if(novo_preco >= 0) jogo->Jogo->preco = novo_preco;
        if(strlen(novo_genero) > 0) strcpy(jogo->Jogo->genero, novo_genero);

    printf("Jogo editado com sucesso!\n");
    }else{
        printf("Jogo nao encontrado.\n");
    }
}

void liberar_jogos(No * lista){
    No *aux;
        while(lista != NULL){
            aux = lista;
            lista = lista->prox;
            free(aux);
    }
}

struct sessao * criar_sessao(const char * descricao, const char * nome){
    struct sessao * nova_sessao = (struct sessao*)malloc(sizeof(struct sessao));
        if(nova_sessao == NULL){
            printf("\n");
            printf("Erro ao alocar memoria para a sessao\n");
            exit(1);
    }
    strcpy(nova_sessao->descricao, descricao);
    strcpy(nova_sessao->nome, nome);
    nova_sessao->num_jogos = 0;
    nova_sessao->prox = NULL; 
    return nova_sessao;
}

struct sessao * adicionar_sessao(struct sessao * lista, const char * descricao, const char * nome){
    struct sessao * nova_sessao = criar_sessao(descricao, nome);
    nova_sessao->prox = lista;
    return nova_sessao;
}

struct sessao * excluir_sessao(struct sessao * lista, const char * nome){
    struct sessao* aux = lista;
    struct sessao* ant = NULL;
        while(aux != NULL){
            if(strcmp(aux->nome, nome) == 0){
                if(ant == NULL){
                lista = aux->prox;
                }else{
                ant->prox = aux->prox;
            }
            free(aux);
            printf("\n");
            printf("Sessao '%s' excluida.\n", nome);
            return lista;
        }
        ant = aux;
        aux = aux->prox;
    }
    printf("\n");
    printf("Sessao '%s' nao encontrada.\n", nome);
    return lista;
}

void listar_sessoes(struct sessao * lista){
        if(lista == NULL){
            printf("\n");
            printf("Nenhuma sessao registrada.\n");
        return;
    }
    printf("Sessoes registradas:\n");
    struct sessao * aux = lista;
        while(aux != NULL){
            printf("\n");
            printf("Nome: %s, Descricao: %s, Numero de Jogos: %d\n", aux->nome, aux->descricao, aux->num_jogos);
            aux = aux->prox;
    }
}

void liberar_sessoes(struct sessao * lista){
    struct sessao *aux;
        while(lista != NULL){
            aux = lista;
            lista = lista->prox;
            free(aux);
    }
}