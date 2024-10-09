# Gerenciamento Salao de Jogos

## Descrição

Este projeto tem como objetivo criar um sistema para gerenciamento de jogos e sessões em um CyberCafe. O sistema permite o cadastro, remoção e busca de jogos e sessões de jogatina. Além disso, conta com a funcionalidade de listar jogos e sessões, salvando essas informações em um arquivo.

## Funcionalidades

1. **Jogos:**
   - Adicionar novo jogo com nome, tipo, preço da jogatina e gênero.
   - Editar jogo existente.
   - Remover jogo existente.
   - Listar todos os jogos cadastrados.
   - Buscar um jogo específico pelo nome.
   - Salvar as informações dos jogos em um arquivo.

2. **Sessões:**
   - Adicionar nova sessão com nome, descrição e jogos associados.
   - Editar sessão existente.
   - Remover sessão existente.
   - Listar todas as sessões cadastradas.
   - Salvar as informações das sessões em um arquivo.

## Estrutura do Projeto

- **`defs.py`:** Contém as classes de manipulação de listas encadeadas e gerenciamento de dados, como as classes `No`, `ListaEncadeada`, `Jogos`, e `Sessoes`. Essas classes implementam a lógica de adicionar, remover, listar e buscar elementos.
- **`main.py`:** É o ponto de entrada do sistema. Implementa o menu de interação do usuário e as operações para gerenciar jogos e sessões.
- **`menu.py`:** Contém funções auxiliares como a exibição de menus, validação de entradas do usuário e controle de fluxo.

## Instruções de Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/usuario/repo-gerenciamento-cybercafe.git
2. Execute o seguinte comando:
   ```bash
   python main.py

## Exemplo de Uso
Ao iniciar o sistema, o menu principal exibirá as opções disponíveis:

- Adicionar jogo
- Remover jogo
- Listar jogos
- Adicionar sessão
- Remover sessão
- Listar sessões
- Buscar jogo
- Salvar alterações e sair
- Siga as instruções do menu para realizar as operações desejadas.

## Estrutura do Código

### ListaEncadeada (Em defs.py)

- Adicionar: Insere novos jogos ou sessões de maneira ordenada.
- Remover: Remove um elemento com base no nome.
- Listar: Lista todos os elementos da lista encadeada.
- Buscar: Busca um jogo ou sessão específica.

### Jogos e Sessoes (Em defs.py)

- Adicionar jogo/sessão: Adiciona novos itens com atributos como nome, tipo e preço.
- Remover jogo/sessão: Exclui itens com base no nome.
- Listar jogos/sessões: Exibe todos os jogos ou sessões cadastrados.

## Desenvolvedores:

- [Igor Cavalcante Rocha](https://github.com/Igor-C-Rocha)

- [Paulo Henrique Souza Lima](https://github.com/pauletxz)