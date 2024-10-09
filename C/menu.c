#include <stdio.h>
#include <stdlib.h>
#include <windows.h>
#include <stdarg.h>
#include <unistd.h>
#include "jogo.h"

#define TITULO_OPCAO1 "Adicionar Jogo"
#define TITULO_OPCAO2 "Remover Jogo"
#define TITULO_OPCAO3 "Editar Jogo"
#define TITULO_OPCAO4 "Adicionar Sessao"
#define TITULO_OPCAO5 "Remover Sessao"
#define TITULO_OPCAO6 "Listar Sessoes"
#define TITULO_OPCAO7 "Buscar Jogo"
#define TITULO_OPCAO8 "Saida do programa"

#define N_OPCOES 8
#define OPCAO1 '1'
#define OPCAO2 '2'
#define OPCAO3 '3'
#define OPCAO4 '4'
#define OPCAO5 '5'
#define OPCAO6 '6'
#define OPCAO7 '7'
#define OPCAO8 '8'

void LimpaBuffer(void){
    int valorLido;
    do{
        valorLido = getchar();
    } while ((valorLido != '\n') && (valorLido != EOF));
}

int LeOpcao(int menorValor, int maiorValor){
    int op;
    while (1){
        printf("\nDigite sua opcao: ");
        op = getchar();
        if (op >= menorValor && op <= maiorValor){
            LimpaBuffer();
            break;
        } 
    }
    return op;
}

float LeFloat(void){
    float umFloat;
    printf("Digite o valor:\n ");
    while (scanf("%f", &umFloat) != 1){
        LimpaBuffer();
        printf("Entrada incorreta. Digite um valor real: ");
    }
    LimpaBuffer();
    return umFloat; 
}

void ApresentaMenu(int nItens, int menorOpcao, ...){
    int i;
    va_list argumentos;
    va_start(argumentos, menorOpcao);
    for (i = 0; i < nItens; ++i){
        printf("%c - %s\n", menorOpcao++, va_arg(argumentos, char *));
    }
    va_end(argumentos);
}

void limparTerminal(){
    #ifdef _WIN32 
    system ("cls");
    #elif __linux__
    system ("clear");
    #elif __APPLE__
    system ("clear");
    #else 
    printf("\033[H\033[J");

    #endif
}

void delay(){
    sleep(1.75);
}