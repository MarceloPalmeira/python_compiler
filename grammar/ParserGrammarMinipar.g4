parser grammar ParserGrammarMinipar;
options { tokenVocab=LexerGrammarMinipar; }

// Programa principal - sequência de declarações e comandos
programa
    : (declaracao | comando)* EOF
    ;

declaracao
    : declaracao_variavel
    | declaracao_funcao
    | comando
    ;

// Declaração de variável: var nome: tipo = valor
declaracao_variavel
    : VAR ID DOIS_PONTOS tipo (OP_ATRIBUICAO expressao)? PONTO_VIRGULA?
    ;

// Declaração de função: func nome(param: tipo) -> tipo { ... }
declaracao_funcao
    : FUNC ID PARENTESE_ABRE parametros? PARENTESE_FECHA (ARROW tipo)? bloco
    ;

// Tipos da linguagem MiniPar
tipo
    : TIPO_NUMBER
    | TIPO_BOOL
    | TIPO_STRING
    | TIPO_LIST
    | TIPO_DICT
    | TIPO_VOID
    | TIPO_ANY
    ;

// Parâmetros de função
parametros
    : parametro (VIRGULA parametro)*
    ;

parametro
    : ID DOIS_PONTOS tipo (OP_ATRIBUICAO expressao)?  // Parâmetro com valor padrão
    ;

// Bloco de código
bloco
    : CHAVE_ABRE (declaracao | comando)* CHAVE_FECHA
    ;

// Comandos
comando
    : comando_linha PONTO_VIRGULA?
    | comando_bloco
    | bloco_paralelo
    ;

comando_linha
    : atribuicao           #ComandoAtribuicao
    | chamada_funcao       #ComandoChamadaFuncao
    | RETURN expressao?    #ComandoReturn
    | BREAK               #ComandoBreak
    | CONTINUE            #ComandoContinue
    ;

comando_bloco
    : if_statement
    | while_statement
    | for_statement
    ;

// Bloco paralelo: par { ... }
bloco_paralelo
    : PAR bloco
    ;

// Atribuição: variavel = expressao
atribuicao
    : acesso_variavel OP_ATRIBUICAO expressao
    ;

// Estrutura if/else
if_statement
    : IF PARENTESE_ABRE expressao PARENTESE_FECHA bloco (ELSE bloco)?
    ;

// Laço while
while_statement
    : WHILE PARENTESE_ABRE expressao PARENTESE_FECHA bloco
    ;

// Laço for
for_statement
    : FOR PARENTESE_ABRE VAR ID DOIS_PONTOS tipo IN expressao PARENTESE_FECHA bloco
    ;

// Chamada de função
chamada_funcao
    : ID PARENTESE_ABRE argumentos? PARENTESE_FECHA
    ;

argumentos
    : expressao (VIRGULA expressao)*
    ;

// Expressões
expressao
    : expr_ou
    ;

expr_ou
    : expr_e (OP_OU expr_e)*
    ;

expr_e
    : expr_relacional (OP_E expr_relacional)*
    ;

expr_relacional
    : expr_aditiva (op_relacional expr_aditiva)*
    ;

op_relacional
    : OP_IGUAL
    | OP_DIFERENTE
    | OP_MAIOR
    | OP_MENOR
    | OP_MAIOR_IGUAL
    | OP_MENOR_IGUAL
    ;

expr_aditiva
    : expr_multiplicativa (op_aditivo expr_multiplicativa)*
    ;

op_aditivo
    : SINAL_MAIS
    | SINAL_MENOS
    ;

expr_multiplicativa
    : fator (op_multiplicativo fator)*
    ;

op_multiplicativo
    : OP_MULTIPLICACAO
    | OP_DIVISAO
    | OP_RESTO_DIVISAO
    ;

fator
    : (sinal)? termo                                    #FatorTermo
    | STRING                                            #FatorString
    | OP_NEGACAO fator                                  #FatorNegacao
    | (sinal)? PARENTESE_ABRE expressao PARENTESE_FECHA #FatorExpressao
    ;

termo
    : acesso_variavel      #TermoVariavel
    | constante           #TermoConstante
    | chamada_funcao      #TermoFuncao
    | lista               #TermoLista
    ;

sinal
    : SINAL_MAIS
    | SINAL_MENOS
    ;

constante
    : NUM_INT
    | NUM_DEC
    | TRUE
    | FALSE
    | STRING
    ;

// Acesso a variáveis e arrays
acesso_variavel
    : ID                                           #AcessoSimples
    | ID COLCHETE_ABRE expressao COLCHETE_FECHA    #AcessoArray
    | ID PONTO ID                                  #AcessoPropriedade
    ;

// Lista literal
lista
    : COLCHETE_ABRE (expressao (VIRGULA expressao)*)? COLCHETE_FECHA
    ;