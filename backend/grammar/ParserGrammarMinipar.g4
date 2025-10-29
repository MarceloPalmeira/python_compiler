parser grammar ParserGrammarMinipar;
options { tokenVocab=LexerGrammarMinipar; }

// Programa principal
programa
    : (declaracao | comando)* EOF
    ;

declaracao
    : declaracao_variavel
    | declaracao_funcao
    | comando
    ;

// Declaração de variável
declaracao_variavel
    : VAR ID (COLON ID)? (ASSIGN expressao)? SEMICOLON?
    ;

// Declaração de função
declaracao_funcao
    : FUNC ID LPAREN parametros? RPAREN (ARROW ID)? bloco
    ;

// Parâmetros de função
parametros
    : ID (COLON ID)? (COMMA ID (COLON ID)?)*
    ;

// Bloco de código
bloco
    : LBRACE (declaracao | comando)* RBRACE
    ;

// Comandos
comando
    : comando_linha SEMICOLON?
    | comando_bloco
    | bloco_paralelo
    ;

comando_linha
    : atribuicao           #ComandoAtribuicao
    | chamada_funcao       #ComandoChamadaFuncao
    | RETURN expressao?    #ComandoReturn
    | BREAK               #ComandoBreak
    | CONTINUE            #ComandoContinue
    | PRINT LPAREN argumentos? RPAREN  #ComandoPrint
    ;

comando_bloco
    : if_statement
    | while_statement
    | for_statement
    ;

// Bloco paralelo
bloco_paralelo
    : PAR bloco
    ;

// Atribuição
atribuicao
    : ID ASSIGN expressao
    ;

// Estrutura if/else
if_statement
    : IF LPAREN expressao RPAREN bloco (ELSE bloco)?
    ;

// Laço while
while_statement
    : WHILE LPAREN expressao RPAREN bloco
    ;

// Laço for
for_statement
    : FOR LPAREN VAR ID (COLON ID)? IN expressao RPAREN bloco
    ;

// Chamada de função
chamada_funcao
    : ID LPAREN argumentos? RPAREN
    ;

argumentos
    : expressao (COMMA expressao)*
    ;

// Expressões
expressao
    : expr_ou
    ;

expr_ou
    : expr_e (OR expr_e)*
    ;

expr_e
    : expr_relacional (AND expr_relacional)*
    ;

expr_relacional
    : expr_aditiva (op_relacional expr_aditiva)*
    ;

op_relacional
    : EQ | NEQ | GT | LT | GTE | LTE
    ;

expr_aditiva
    : expr_multiplicativa (op_aditivo expr_multiplicativa)*
    ;

op_aditivo
    : OP_PLUS | OP_MINUS
    ;

expr_multiplicativa
    : fator_unario (op_multiplicativo fator_unario)*
    ;

op_multiplicativo
    : OP_MULT | OP_DIV | OP_MOD
    ;

fator_unario
    : NOT fator_unario           #FatorNegacao
    | (OP_PLUS | OP_MINUS) fator_unario  #FatorSinal
    | fator_primario             #FatorPrimario
    ;

fator_primario
    : NUMBER                     #FatorNumero
    | STRING                     #FatorString  
    | TRUE                       #FatorTrue
    | FALSE                      #FatorFalse
    | ID                         #FatorIdentificador
    | chamada_funcao             #FatorChamada
    | PRINT LPAREN argumentos? RPAREN  #FatorPrint
    | LPAREN expressao RPAREN    #FatorExpressao
    ;