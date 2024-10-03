typedef struct jogo Jogo;

typedef struct no No;

typedef struct sessao Sessao;

void criarArquivoTexto(const char * jogos);

No * adicionar(No * lista , char nome[], char tipo[], float preco, char genero[]);

No * tira(No * lista, char * nome);

No * busca(No * lista, char * nome);

void editar(No * lista);

void salvar(No * lista);

void liberar_jogos(No * lista);

struct sessao * criar_sessao(const char * descricao, const char * nome);

struct sessao * adicionar_sessao(struct sessao * lista, const char * descricao, const char * nome);

struct sessao * excluir_sessao(struct sessao * lista, const char * nome);

void listar_sessoes(struct sessao * lista);

void liberar_sessoes(struct sessao * lista);