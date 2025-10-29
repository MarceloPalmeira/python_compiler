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

// Funções built-in (apenas print implementado)
PRINT : 'print' ;

// Operadores e símbolos
COMMA : ',' ;
SEMICOLON : ';' ;
COLON : ':' ;
ARROW : '->' ;

LPAREN : '(';
RPAREN : ')';

LBRACKET : '[';
RBRACKET : ']';

LBRACE : '{';
RBRACE : '}';

// Strings
STRING : '"' (~["\r\n])* '"' ;

// Operadores aritméticos (implementados como OP regex)
OP_PLUS : '+' ;
OP_MINUS : '-' ;
OP_MULT : '*' ;
OP_DIV : '/' ;
OP_MOD : '%' ;

// Operadores lógicos
NOT : '!' ;
AND : '&&' ;
OR : '||' ;

// Operadores relacionais
EQ : '==' ;
NEQ : '!=' ;
GTE : '>=' ;
LTE : '<=' ;
GT : '>';
LT : '<' ;

// Atribuição
ASSIGN : '=' ;

// Literais
NUMBER : [0-9]+ ('.' [0-9]+)? ;  // Implementado como NUMBER regex

// Identificadores
ID: [a-zA-Z_][a-zA-Z_0-9]* ;

// Comentários (implementado como COMMENT regex)
COMMENT: '#' ~[\r\n]* -> skip ;

// Whitespace
WS: [ \t\n\r\f]+ -> skip ;