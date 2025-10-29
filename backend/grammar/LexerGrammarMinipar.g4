lexer grammar LexerGrammarMinipar;

// Palavras-chave implementadas
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
TRUE : 'true';
FALSE : 'false';

// Funções built-in implementadas
PRINT : 'print' ;

// Operadores relacionais
GTE : '>=' ;
LTE : '<=' ;
EQ : '==' ;
NEQ : '!=' ;
GT : '>' ;
LT : '<' ;

// Operadores lógicos
AND : '&&' ;
OR : '||' ;
NOT : '!' ;

// Operadores aritméticos
OP_PLUS : '+' ;
OP_MINUS : '-' ;
OP_MULT : '*' ;
OP_DIV : '/' ;
OP_MOD : '%' ;

// Atribuição e setas
ASSIGN : '=' ;
ARROW : '->' ;

// Símbolos e pontuação
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACKET : '[' ;
RBRACKET : ']' ;
COMMA : ',' ;
SEMICOLON : ';' ;
COLON : ':' ;

// Literais
STRING : '"' (~["\r\n])* '"' ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

// Identificadores
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

// Comentários
COMMENT: '#' ~[\r\n]* -> skip ;

// Whitespace
WS: [ \t\n\r\f]+ -> skip ;