lexer grammar LexerGrammarMinipar;

// Palavras-chave
VAR : 'var' ;
FUNC : 'func' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
FOR : 'for' ;
RETURN : 'return';
BREAK : 'break';
CONTINUE : 'continue';
IN : 'in';
PAR : 'par';
SEQ : 'seq';

// Tipos da linguagem MiniPar
TIPO_NUMBER : 'number' ;
TIPO_BOOL : 'bool' ;
TIPO_STRING : 'string' ;
TIPO_LIST : 'list' ;
TIPO_DICT : 'dict' ;
TIPO_VOID : 'void' ;
TIPO_ANY : 'any' ;

// Funções built-in
PRINT : 'print' ;
INPUT : 'input' ;
SLEEP : 'sleep' ;

// Operadores e símbolos
VIRGULA : ',' ;
PONTO_VIRGULA : ';' ;
DOIS_PONTOS : ':' ;
ARROW : '->' ;

PARENTESE_ABRE : '(';
PARENTESE_FECHA : ')';

COLCHETE_ABRE : '[';
COLCHETE_FECHA : ']';

CHAVE_ABRE : '{';
CHAVE_FECHA : '}';

PONTO : '.' ;

// Strings
STRING : '"' (~["\r\n])* '"' ;

// Operadores aritméticos
SINAL_MAIS : '+' ;
SINAL_MENOS : '-' ;
OP_MULTIPLICACAO : '*' ;
OP_DIVISAO : '/' ;
OP_RESTO_DIVISAO : '%' ;

// Operadores lógicos
OP_NEGACAO : '!' ;
OP_E : '&&' ;
OP_OU : '||' ;

// Operadores relacionais
OP_IGUAL : '==' ;
OP_DIFERENTE : '!=' ;
OP_MAIOR : '>';
OP_MAIOR_IGUAL : '>=';
OP_MENOR : '<' ;
OP_MENOR_IGUAL : '<=' ;

// Atribuição
OP_ATRIBUICAO : '=' ;

// Literais
TRUE: 'true';
FALSE: 'false';
NUM_INT : [0-9]+ ;
NUM_DEC : [0-9]+ '.' [0-9]+ | '.' [0-9]+ ;

// Identificadores
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

// Comentários
COMENTARIO_LINHA: '#' ~[\r\n]* -> skip ;
COMENTARIO_BLOCO: '/*' .*? '*/' -> skip ;

// Whitespace
WS: [ \t\n\r\f]+ -> skip ;