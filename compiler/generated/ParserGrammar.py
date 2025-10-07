# Generated from ParserGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,375,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,5,0,86,8,0,10,0,12,0,89,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,3,1,97,8,1,1,1,1,1,1,1,1,2,1,2,3,2,104,8,2,1,3,1,3,5,
        3,108,8,3,10,3,12,3,111,9,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,3,6,120,
        8,6,1,6,1,6,1,6,1,6,3,6,126,8,6,1,6,1,6,1,6,5,6,131,8,6,10,6,12,
        6,134,9,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,5,8,143,8,8,10,8,12,8,146,
        9,8,1,8,5,8,149,8,8,10,8,12,8,152,9,8,1,8,1,8,1,9,1,9,1,9,1,9,5,
        9,160,8,9,10,9,12,9,163,9,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,171,
        8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,179,8,11,1,12,1,12,1,12,
        3,12,184,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,5,15,200,8,15,10,15,12,15,203,9,15,1,15,1,15,
        1,16,1,16,1,16,1,16,1,16,5,16,212,8,16,10,16,12,16,215,9,16,1,16,
        1,16,1,17,1,17,3,17,221,8,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        229,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,
        1,21,3,21,243,8,21,1,21,1,21,3,21,247,8,21,1,21,1,21,3,21,251,8,
        21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,5,23,263,8,
        23,10,23,12,23,266,9,23,1,24,1,24,1,25,1,25,1,25,1,25,3,25,274,8,
        25,1,25,1,25,1,26,1,26,1,26,5,26,281,8,26,10,26,12,26,284,9,26,1,
        27,1,27,3,27,288,8,27,1,28,1,28,1,29,1,29,1,29,5,29,295,8,29,10,
        29,12,29,298,9,29,1,30,1,30,1,30,5,30,303,8,30,10,30,12,30,306,9,
        30,1,31,1,31,1,31,1,31,5,31,312,8,31,10,31,12,31,315,9,31,1,32,1,
        32,1,33,1,33,1,33,1,33,5,33,323,8,33,10,33,12,33,326,9,33,1,34,1,
        34,1,35,1,35,1,35,1,35,5,35,334,8,35,10,35,12,35,337,9,35,1,36,1,
        36,1,37,3,37,342,8,37,1,37,1,37,1,37,1,37,1,37,3,37,349,8,37,1,37,
        1,37,1,37,1,37,3,37,355,8,37,1,38,1,38,1,38,3,38,360,8,38,1,39,1,
        39,1,40,1,40,1,41,1,41,1,41,4,41,369,8,41,11,41,12,41,370,3,41,373,
        8,41,1,41,0,0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,0,5,1,0,13,16,1,0,34,39,1,0,26,27,1,0,28,30,1,0,41,44,375,
        0,87,1,0,0,0,2,92,1,0,0,0,4,103,1,0,0,0,6,105,1,0,0,0,8,112,1,0,
        0,0,10,114,1,0,0,0,12,119,1,0,0,0,14,135,1,0,0,0,16,140,1,0,0,0,
        18,155,1,0,0,0,20,170,1,0,0,0,22,178,1,0,0,0,24,183,1,0,0,0,26,185,
        1,0,0,0,28,190,1,0,0,0,30,194,1,0,0,0,32,206,1,0,0,0,34,220,1,0,
        0,0,36,222,1,0,0,0,38,230,1,0,0,0,40,233,1,0,0,0,42,239,1,0,0,0,
        44,255,1,0,0,0,46,259,1,0,0,0,48,267,1,0,0,0,50,269,1,0,0,0,52,277,
        1,0,0,0,54,285,1,0,0,0,56,289,1,0,0,0,58,291,1,0,0,0,60,299,1,0,
        0,0,62,307,1,0,0,0,64,316,1,0,0,0,66,318,1,0,0,0,68,327,1,0,0,0,
        70,329,1,0,0,0,72,338,1,0,0,0,74,354,1,0,0,0,76,359,1,0,0,0,78,361,
        1,0,0,0,80,363,1,0,0,0,82,372,1,0,0,0,84,86,3,2,1,0,85,84,1,0,0,
        0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,90,1,0,0,0,89,87,
        1,0,0,0,90,91,3,14,7,0,91,1,1,0,0,0,92,93,3,4,2,0,93,94,5,45,0,0,
        94,96,5,19,0,0,95,97,3,12,6,0,96,95,1,0,0,0,96,97,1,0,0,0,97,98,
        1,0,0,0,98,99,5,20,0,0,99,100,3,16,8,0,100,3,1,0,0,0,101,104,3,6,
        3,0,102,104,5,12,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,5,1,0,0,
        0,105,109,3,8,4,0,106,108,3,10,5,0,107,106,1,0,0,0,108,111,1,0,0,
        0,109,107,1,0,0,0,109,110,1,0,0,0,110,7,1,0,0,0,111,109,1,0,0,0,
        112,113,7,0,0,0,113,9,1,0,0,0,114,115,5,21,0,0,115,116,5,41,0,0,
        116,117,5,22,0,0,117,11,1,0,0,0,118,120,5,11,0,0,119,118,1,0,0,0,
        119,120,1,0,0,0,120,121,1,0,0,0,121,122,3,6,3,0,122,132,5,45,0,0,
        123,125,5,17,0,0,124,126,5,11,0,0,125,124,1,0,0,0,125,126,1,0,0,
        0,126,127,1,0,0,0,127,128,3,6,3,0,128,129,5,45,0,0,129,131,1,0,0,
        0,130,123,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,
        0,133,13,1,0,0,0,134,132,1,0,0,0,135,136,5,1,0,0,136,137,5,19,0,
        0,137,138,5,20,0,0,138,139,3,16,8,0,139,15,1,0,0,0,140,144,5,23,
        0,0,141,143,3,18,9,0,142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,
        0,0,144,145,1,0,0,0,145,150,1,0,0,0,146,144,1,0,0,0,147,149,3,20,
        10,0,148,147,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,
        0,0,151,153,1,0,0,0,152,150,1,0,0,0,153,154,5,24,0,0,154,17,1,0,
        0,0,155,156,3,6,3,0,156,161,5,45,0,0,157,158,5,17,0,0,158,160,5,
        45,0,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,
        0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,165,5,18,0,0,165,19,1,
        0,0,0,166,167,3,22,11,0,167,168,5,18,0,0,168,171,1,0,0,0,169,171,
        3,24,12,0,170,166,1,0,0,0,170,169,1,0,0,0,171,21,1,0,0,0,172,179,
        3,26,13,0,173,179,3,32,16,0,174,179,3,30,15,0,175,179,3,44,22,0,
        176,179,3,50,25,0,177,179,3,54,27,0,178,172,1,0,0,0,178,173,1,0,
        0,0,178,174,1,0,0,0,178,175,1,0,0,0,178,176,1,0,0,0,178,177,1,0,
        0,0,179,23,1,0,0,0,180,184,3,36,18,0,181,184,3,40,20,0,182,184,3,
        42,21,0,183,180,1,0,0,0,183,181,1,0,0,0,183,182,1,0,0,0,184,25,1,
        0,0,0,185,186,5,2,0,0,186,187,5,19,0,0,187,188,3,82,41,0,188,189,
        5,20,0,0,189,27,1,0,0,0,190,191,5,21,0,0,191,192,3,66,33,0,192,193,
        5,22,0,0,193,29,1,0,0,0,194,195,5,4,0,0,195,196,5,19,0,0,196,201,
        5,25,0,0,197,198,5,17,0,0,198,200,3,34,17,0,199,197,1,0,0,0,200,
        203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,
        201,1,0,0,0,204,205,5,20,0,0,205,31,1,0,0,0,206,207,5,3,0,0,207,
        208,5,19,0,0,208,213,5,25,0,0,209,210,5,17,0,0,210,212,3,34,17,0,
        211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,
        214,216,1,0,0,0,215,213,1,0,0,0,216,217,5,20,0,0,217,33,1,0,0,0,
        218,221,5,25,0,0,219,221,3,56,28,0,220,218,1,0,0,0,220,219,1,0,0,
        0,221,35,1,0,0,0,222,223,5,5,0,0,223,224,5,19,0,0,224,225,3,56,28,
        0,225,226,5,20,0,0,226,228,3,16,8,0,227,229,3,38,19,0,228,227,1,
        0,0,0,228,229,1,0,0,0,229,37,1,0,0,0,230,231,5,6,0,0,231,232,3,16,
        8,0,232,39,1,0,0,0,233,234,5,7,0,0,234,235,5,19,0,0,235,236,3,56,
        28,0,236,237,5,20,0,0,237,238,3,16,8,0,238,41,1,0,0,0,239,240,5,
        8,0,0,240,242,5,19,0,0,241,243,3,46,23,0,242,241,1,0,0,0,242,243,
        1,0,0,0,243,244,1,0,0,0,244,246,5,18,0,0,245,247,3,56,28,0,246,245,
        1,0,0,0,246,247,1,0,0,0,247,248,1,0,0,0,248,250,5,18,0,0,249,251,
        3,46,23,0,250,249,1,0,0,0,250,251,1,0,0,0,251,252,1,0,0,0,252,253,
        5,20,0,0,253,254,3,16,8,0,254,43,1,0,0,0,255,256,3,82,41,0,256,257,
        5,40,0,0,257,258,3,48,24,0,258,45,1,0,0,0,259,264,3,44,22,0,260,
        261,5,17,0,0,261,263,3,44,22,0,262,260,1,0,0,0,263,266,1,0,0,0,264,
        262,1,0,0,0,264,265,1,0,0,0,265,47,1,0,0,0,266,264,1,0,0,0,267,268,
        3,56,28,0,268,49,1,0,0,0,269,270,5,9,0,0,270,271,5,45,0,0,271,273,
        5,19,0,0,272,274,3,52,26,0,273,272,1,0,0,0,273,274,1,0,0,0,274,275,
        1,0,0,0,275,276,5,20,0,0,276,51,1,0,0,0,277,282,3,56,28,0,278,279,
        5,17,0,0,279,281,3,56,28,0,280,278,1,0,0,0,281,284,1,0,0,0,282,280,
        1,0,0,0,282,283,1,0,0,0,283,53,1,0,0,0,284,282,1,0,0,0,285,287,5,
        10,0,0,286,288,3,56,28,0,287,286,1,0,0,0,287,288,1,0,0,0,288,55,
        1,0,0,0,289,290,3,58,29,0,290,57,1,0,0,0,291,296,3,60,30,0,292,293,
        5,33,0,0,293,295,3,60,30,0,294,292,1,0,0,0,295,298,1,0,0,0,296,294,
        1,0,0,0,296,297,1,0,0,0,297,59,1,0,0,0,298,296,1,0,0,0,299,304,3,
        62,31,0,300,301,5,32,0,0,301,303,3,62,31,0,302,300,1,0,0,0,303,306,
        1,0,0,0,304,302,1,0,0,0,304,305,1,0,0,0,305,61,1,0,0,0,306,304,1,
        0,0,0,307,313,3,66,33,0,308,309,3,64,32,0,309,310,3,66,33,0,310,
        312,1,0,0,0,311,308,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,
        314,1,0,0,0,314,63,1,0,0,0,315,313,1,0,0,0,316,317,7,1,0,0,317,65,
        1,0,0,0,318,324,3,70,35,0,319,320,3,68,34,0,320,321,3,70,35,0,321,
        323,1,0,0,0,322,319,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,
        325,1,0,0,0,325,67,1,0,0,0,326,324,1,0,0,0,327,328,7,2,0,0,328,69,
        1,0,0,0,329,335,3,74,37,0,330,331,3,72,36,0,331,332,3,74,37,0,332,
        334,1,0,0,0,333,330,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,
        336,1,0,0,0,336,71,1,0,0,0,337,335,1,0,0,0,338,339,7,3,0,0,339,73,
        1,0,0,0,340,342,3,78,39,0,341,340,1,0,0,0,341,342,1,0,0,0,342,343,
        1,0,0,0,343,355,3,76,38,0,344,355,5,25,0,0,345,346,5,31,0,0,346,
        355,3,74,37,0,347,349,3,78,39,0,348,347,1,0,0,0,348,349,1,0,0,0,
        349,350,1,0,0,0,350,351,5,19,0,0,351,352,3,56,28,0,352,353,5,20,
        0,0,353,355,1,0,0,0,354,341,1,0,0,0,354,344,1,0,0,0,354,345,1,0,
        0,0,354,348,1,0,0,0,355,75,1,0,0,0,356,360,3,82,41,0,357,360,3,80,
        40,0,358,360,3,50,25,0,359,356,1,0,0,0,359,357,1,0,0,0,359,358,1,
        0,0,0,360,77,1,0,0,0,361,362,7,2,0,0,362,79,1,0,0,0,363,364,7,4,
        0,0,364,81,1,0,0,0,365,373,5,45,0,0,366,368,5,45,0,0,367,369,3,28,
        14,0,368,367,1,0,0,0,369,370,1,0,0,0,370,368,1,0,0,0,370,371,1,0,
        0,0,371,373,1,0,0,0,372,365,1,0,0,0,372,366,1,0,0,0,373,83,1,0,0,
        0,35,87,96,103,109,119,125,132,144,150,161,170,178,183,201,213,220,
        228,242,246,250,264,273,282,287,296,304,313,324,335,341,348,354,
        359,370,372
    ]

class ParserGrammar ( Parser ):

    grammarFileName = "ParserGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'scanf'", "'println'", "'print'", 
                     "'if'", "'else'", "'while'", "'for'", "'func'", "'return'", 
                     "'input'", "'void'", "'char'", "'float'", "'int'", 
                     "'boolean'", "','", "';'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'>'", 
                     "'>='", "'<'", "'<='", "'='", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "SCANF", "PRINTLN", "PRINT", 
                      "IF", "ELSE", "WHILE", "FOR", "FUNC", "RETURN", "INPUT", 
                      "TIPO_VOID", "TIPO_CHAR", "TIPO_FLOAT", "TIPO_INT", 
                      "TIPO_BOOLEAN", "VIRGULA", "PONTO_VIRGULA", "PARENTESE_ABRE", 
                      "PARENTESE_FECHA", "COLCHETE_ABRE", "COLCHETE_FECHA", 
                      "CHAVE_ABRE", "CHAVE_FECHA", "TEXTO", "SINAL_MAIS", 
                      "SINAL_MENOS", "OP_MULTIPLICACAO", "OP_DIVISAO", "OP_RESTO_DIVISAO", 
                      "OP_NEGACAO", "OP_E", "OP_OU", "OP_IGUAL", "OP_DIFERENTE", 
                      "OP_MAIOR", "OP_MAIOR_IGUAL", "OP_MENOR", "OP_MENOR_IGUAL", 
                      "OP_ATRIBUICAO", "NUM_INT", "NUM_DEC", "TRUE", "FALSE", 
                      "ID", "WS", "COMENTARIO_LINHA", "COMENTARIO_BLOCO" ]

    RULE_programa = 0
    RULE_decfuncao = 1
    RULE_tiporetorno = 2
    RULE_tipo = 3
    RULE_tipobase = 4
    RULE_dimensao = 5
    RULE_parametros = 6
    RULE_principal = 7
    RULE_bloco = 8
    RULE_decvariavel = 9
    RULE_comando = 10
    RULE_comando_linha = 11
    RULE_comando_bloco = 12
    RULE_leitura = 13
    RULE_dimensao2 = 14
    RULE_escrita = 15
    RULE_escritaln = 16
    RULE_termoescrita = 17
    RULE_selecao = 18
    RULE_senao = 19
    RULE_enquanto = 20
    RULE_para = 21
    RULE_atribuicao = 22
    RULE_para_atribuicoes = 23
    RULE_complemento = 24
    RULE_funcao = 25
    RULE_argumentos = 26
    RULE_retorno = 27
    RULE_expressao = 28
    RULE_expr_ou = 29
    RULE_expr_e = 30
    RULE_expr_relacional = 31
    RULE_op_relacional = 32
    RULE_expr_aditiva = 33
    RULE_op_aditivo = 34
    RULE_expr_multiplicativa = 35
    RULE_op_multiplicativo = 36
    RULE_fator = 37
    RULE_termo = 38
    RULE_sinal = 39
    RULE_constante = 40
    RULE_acesso_id = 41

    ruleNames =  [ "programa", "decfuncao", "tiporetorno", "tipo", "tipobase", 
                   "dimensao", "parametros", "principal", "bloco", "decvariavel", 
                   "comando", "comando_linha", "comando_bloco", "leitura", 
                   "dimensao2", "escrita", "escritaln", "termoescrita", 
                   "selecao", "senao", "enquanto", "para", "atribuicao", 
                   "para_atribuicoes", "complemento", "funcao", "argumentos", 
                   "retorno", "expressao", "expr_ou", "expr_e", "expr_relacional", 
                   "op_relacional", "expr_aditiva", "op_aditivo", "expr_multiplicativa", 
                   "op_multiplicativo", "fator", "termo", "sinal", "constante", 
                   "acesso_id" ]

    EOF = Token.EOF
    MAIN=1
    SCANF=2
    PRINTLN=3
    PRINT=4
    IF=5
    ELSE=6
    WHILE=7
    FOR=8
    FUNC=9
    RETURN=10
    INPUT=11
    TIPO_VOID=12
    TIPO_CHAR=13
    TIPO_FLOAT=14
    TIPO_INT=15
    TIPO_BOOLEAN=16
    VIRGULA=17
    PONTO_VIRGULA=18
    PARENTESE_ABRE=19
    PARENTESE_FECHA=20
    COLCHETE_ABRE=21
    COLCHETE_FECHA=22
    CHAVE_ABRE=23
    CHAVE_FECHA=24
    TEXTO=25
    SINAL_MAIS=26
    SINAL_MENOS=27
    OP_MULTIPLICACAO=28
    OP_DIVISAO=29
    OP_RESTO_DIVISAO=30
    OP_NEGACAO=31
    OP_E=32
    OP_OU=33
    OP_IGUAL=34
    OP_DIFERENTE=35
    OP_MAIOR=36
    OP_MAIOR_IGUAL=37
    OP_MENOR=38
    OP_MENOR_IGUAL=39
    OP_ATRIBUICAO=40
    NUM_INT=41
    NUM_DEC=42
    TRUE=43
    FALSE=44
    ID=45
    WS=46
    COMENTARIO_LINHA=47
    COMENTARIO_BLOCO=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def principal(self):
            return self.getTypedRuleContext(ParserGrammar.PrincipalContext,0)


        def decfuncao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.DecfuncaoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.DecfuncaoContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ParserGrammar.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0):
                self.state = 84
                self.decfuncao()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.principal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecfuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tiporetorno(self):
            return self.getTypedRuleContext(ParserGrammar.TiporetornoContext,0)


        def ID(self):
            return self.getToken(ParserGrammar.ID, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def parametros(self):
            return self.getTypedRuleContext(ParserGrammar.ParametrosContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_decfuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecfuncao" ):
                listener.enterDecfuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecfuncao" ):
                listener.exitDecfuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecfuncao" ):
                return visitor.visitDecfuncao(self)
            else:
                return visitor.visitChildren(self)




    def decfuncao(self):

        localctx = ParserGrammar.DecfuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decfuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.tiporetorno()
            self.state = 93
            self.match(ParserGrammar.ID)
            self.state = 94
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 124928) != 0):
                self.state = 95
                self.parametros()


            self.state = 98
            self.match(ParserGrammar.PARENTESE_FECHA)
            self.state = 99
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TiporetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ParserGrammar.TipoContext,0)


        def TIPO_VOID(self):
            return self.getToken(ParserGrammar.TIPO_VOID, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_tiporetorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiporetorno" ):
                listener.enterTiporetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiporetorno" ):
                listener.exitTiporetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTiporetorno" ):
                return visitor.visitTiporetorno(self)
            else:
                return visitor.visitChildren(self)




    def tiporetorno(self):

        localctx = ParserGrammar.TiporetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tiporetorno)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.tipo()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(ParserGrammar.TIPO_VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipobase(self):
            return self.getTypedRuleContext(ParserGrammar.TipobaseContext,0)


        def dimensao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.DimensaoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.DimensaoContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = ParserGrammar.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.tipobase()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 106
                self.dimensao()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipobaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIPO_CHAR(self):
            return self.getToken(ParserGrammar.TIPO_CHAR, 0)

        def TIPO_FLOAT(self):
            return self.getToken(ParserGrammar.TIPO_FLOAT, 0)

        def TIPO_INT(self):
            return self.getToken(ParserGrammar.TIPO_INT, 0)

        def TIPO_BOOLEAN(self):
            return self.getToken(ParserGrammar.TIPO_BOOLEAN, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_tipobase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipobase" ):
                listener.enterTipobase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipobase" ):
                listener.exitTipobase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipobase" ):
                return visitor.visitTipobase(self)
            else:
                return visitor.visitChildren(self)




    def tipobase(self):

        localctx = ParserGrammar.TipobaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tipobase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLCHETE_ABRE(self):
            return self.getToken(ParserGrammar.COLCHETE_ABRE, 0)

        def NUM_INT(self):
            return self.getToken(ParserGrammar.NUM_INT, 0)

        def COLCHETE_FECHA(self):
            return self.getToken(ParserGrammar.COLCHETE_FECHA, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_dimensao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao" ):
                listener.enterDimensao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao" ):
                listener.exitDimensao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensao" ):
                return visitor.visitDimensao(self)
            else:
                return visitor.visitChildren(self)




    def dimensao(self):

        localctx = ParserGrammar.DimensaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dimensao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ParserGrammar.COLCHETE_ABRE)
            self.state = 115
            self.match(ParserGrammar.NUM_INT)
            self.state = 116
            self.match(ParserGrammar.COLCHETE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.TipoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.TipoContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.ID)
            else:
                return self.getToken(ParserGrammar.ID, i)

        def INPUT(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.INPUT)
            else:
                return self.getToken(ParserGrammar.INPUT, i)

        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = ParserGrammar.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 118
                self.match(ParserGrammar.INPUT)


            self.state = 121
            self.tipo()
            self.state = 122
            self.match(ParserGrammar.ID)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 123
                self.match(ParserGrammar.VIRGULA)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 124
                    self.match(ParserGrammar.INPUT)


                self.state = 127
                self.tipo()
                self.state = 128
                self.match(ParserGrammar.ID)
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrincipalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(ParserGrammar.MAIN, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_principal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrincipal" ):
                listener.enterPrincipal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrincipal" ):
                listener.exitPrincipal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrincipal" ):
                return visitor.visitPrincipal(self)
            else:
                return visitor.visitChildren(self)




    def principal(self):

        localctx = ParserGrammar.PrincipalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_principal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ParserGrammar.MAIN)
            self.state = 136
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 137
            self.match(ParserGrammar.PARENTESE_FECHA)
            self.state = 138
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAVE_ABRE(self):
            return self.getToken(ParserGrammar.CHAVE_ABRE, 0)

        def CHAVE_FECHA(self):
            return self.getToken(ParserGrammar.CHAVE_FECHA, 0)

        def decvariavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.DecvariavelContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.DecvariavelContext,i)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.ComandoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.ComandoContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = ParserGrammar.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ParserGrammar.CHAVE_ABRE)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0):
                self.state = 141
                self.decvariavel()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372090812) != 0):
                self.state = 147
                self.comando()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(ParserGrammar.CHAVE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecvariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(ParserGrammar.TipoContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.ID)
            else:
                return self.getToken(ParserGrammar.ID, i)

        def PONTO_VIRGULA(self):
            return self.getToken(ParserGrammar.PONTO_VIRGULA, 0)

        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_decvariavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecvariavel" ):
                listener.enterDecvariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecvariavel" ):
                listener.exitDecvariavel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecvariavel" ):
                return visitor.visitDecvariavel(self)
            else:
                return visitor.visitChildren(self)




    def decvariavel(self):

        localctx = ParserGrammar.DecvariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_decvariavel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.tipo()
            self.state = 156
            self.match(ParserGrammar.ID)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 157
                self.match(ParserGrammar.VIRGULA)
                self.state = 158
                self.match(ParserGrammar.ID)
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 164
            self.match(ParserGrammar.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando_linha(self):
            return self.getTypedRuleContext(ParserGrammar.Comando_linhaContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(ParserGrammar.PONTO_VIRGULA, 0)

        def comando_bloco(self):
            return self.getTypedRuleContext(ParserGrammar.Comando_blocoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = ParserGrammar.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comando)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 9, 10, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.comando_linha()
                self.state = 167
                self.match(ParserGrammar.PONTO_VIRGULA)
                pass
            elif token in [5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.comando_bloco()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_linhaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserGrammar.RULE_comando_linha

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ComandoLinhaAtribuicaoContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atribuicao(self):
            return self.getTypedRuleContext(ParserGrammar.AtribuicaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaAtribuicao" ):
                listener.enterComandoLinhaAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaAtribuicao" ):
                listener.exitComandoLinhaAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaAtribuicao" ):
                return visitor.visitComandoLinhaAtribuicao(self)
            else:
                return visitor.visitChildren(self)


    class ComandoLinhaFuncaoContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcao(self):
            return self.getTypedRuleContext(ParserGrammar.FuncaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaFuncao" ):
                listener.enterComandoLinhaFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaFuncao" ):
                listener.exitComandoLinhaFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaFuncao" ):
                return visitor.visitComandoLinhaFuncao(self)
            else:
                return visitor.visitChildren(self)


    class ComandoLinhaRetornoContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def retorno(self):
            return self.getTypedRuleContext(ParserGrammar.RetornoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaRetorno" ):
                listener.enterComandoLinhaRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaRetorno" ):
                listener.exitComandoLinhaRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaRetorno" ):
                return visitor.visitComandoLinhaRetorno(self)
            else:
                return visitor.visitChildren(self)


    class ComandoLinhaEscritaLnContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def escritaln(self):
            return self.getTypedRuleContext(ParserGrammar.EscritalnContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaEscritaLn" ):
                listener.enterComandoLinhaEscritaLn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaEscritaLn" ):
                listener.exitComandoLinhaEscritaLn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaEscritaLn" ):
                return visitor.visitComandoLinhaEscritaLn(self)
            else:
                return visitor.visitChildren(self)


    class ComandoLinhaLeituraContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def leitura(self):
            return self.getTypedRuleContext(ParserGrammar.LeituraContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaLeitura" ):
                listener.enterComandoLinhaLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaLeitura" ):
                listener.exitComandoLinhaLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaLeitura" ):
                return visitor.visitComandoLinhaLeitura(self)
            else:
                return visitor.visitChildren(self)


    class ComandoLinhaEscritaContext(Comando_linhaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Comando_linhaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def escrita(self):
            return self.getTypedRuleContext(ParserGrammar.EscritaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoLinhaEscrita" ):
                listener.enterComandoLinhaEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoLinhaEscrita" ):
                listener.exitComandoLinhaEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComandoLinhaEscrita" ):
                return visitor.visitComandoLinhaEscrita(self)
            else:
                return visitor.visitChildren(self)



    def comando_linha(self):

        localctx = ParserGrammar.Comando_linhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comando_linha)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = ParserGrammar.ComandoLinhaLeituraContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.leitura()
                pass
            elif token in [3]:
                localctx = ParserGrammar.ComandoLinhaEscritaLnContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.escritaln()
                pass
            elif token in [4]:
                localctx = ParserGrammar.ComandoLinhaEscritaContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.escrita()
                pass
            elif token in [45]:
                localctx = ParserGrammar.ComandoLinhaAtribuicaoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.atribuicao()
                pass
            elif token in [9]:
                localctx = ParserGrammar.ComandoLinhaFuncaoContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.funcao()
                pass
            elif token in [10]:
                localctx = ParserGrammar.ComandoLinhaRetornoContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.retorno()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comando_blocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selecao(self):
            return self.getTypedRuleContext(ParserGrammar.SelecaoContext,0)


        def enquanto(self):
            return self.getTypedRuleContext(ParserGrammar.EnquantoContext,0)


        def para(self):
            return self.getTypedRuleContext(ParserGrammar.ParaContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_comando_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando_bloco" ):
                listener.enterComando_bloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando_bloco" ):
                listener.exitComando_bloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando_bloco" ):
                return visitor.visitComando_bloco(self)
            else:
                return visitor.visitChildren(self)




    def comando_bloco(self):

        localctx = ParserGrammar.Comando_blocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comando_bloco)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.selecao()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.enquanto()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.para()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCANF(self):
            return self.getToken(ParserGrammar.SCANF, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def acesso_id(self):
            return self.getTypedRuleContext(ParserGrammar.Acesso_idContext,0)


        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeitura" ):
                return visitor.visitLeitura(self)
            else:
                return visitor.visitChildren(self)




    def leitura(self):

        localctx = ParserGrammar.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(ParserGrammar.SCANF)
            self.state = 186
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 187
            self.acesso_id()
            self.state = 188
            self.match(ParserGrammar.PARENTESE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimensao2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLCHETE_ABRE(self):
            return self.getToken(ParserGrammar.COLCHETE_ABRE, 0)

        def expr_aditiva(self):
            return self.getTypedRuleContext(ParserGrammar.Expr_aditivaContext,0)


        def COLCHETE_FECHA(self):
            return self.getToken(ParserGrammar.COLCHETE_FECHA, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_dimensao2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimensao2" ):
                listener.enterDimensao2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimensao2" ):
                listener.exitDimensao2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimensao2" ):
                return visitor.visitDimensao2(self)
            else:
                return visitor.visitChildren(self)




    def dimensao2(self):

        localctx = ParserGrammar.Dimensao2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dimensao2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ParserGrammar.COLCHETE_ABRE)
            self.state = 191
            self.expr_aditiva()
            self.state = 192
            self.match(ParserGrammar.COLCHETE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ParserGrammar.PRINT, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def TEXTO(self):
            return self.getToken(ParserGrammar.TEXTO, 0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def termoescrita(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.TermoescritaContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.TermoescritaContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscrita" ):
                return visitor.visitEscrita(self)
            else:
                return visitor.visitChildren(self)




    def escrita(self):

        localctx = ParserGrammar.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_escrita)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ParserGrammar.PRINT)
            self.state = 195
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 196
            self.match(ParserGrammar.TEXTO)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 197
                self.match(ParserGrammar.VIRGULA)
                self.state = 198
                self.termoescrita()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(ParserGrammar.PARENTESE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritalnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(ParserGrammar.PRINTLN, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def TEXTO(self):
            return self.getToken(ParserGrammar.TEXTO, 0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def termoescrita(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.TermoescritaContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.TermoescritaContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_escritaln

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritaln" ):
                listener.enterEscritaln(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritaln" ):
                listener.exitEscritaln(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritaln" ):
                return visitor.visitEscritaln(self)
            else:
                return visitor.visitChildren(self)




    def escritaln(self):

        localctx = ParserGrammar.EscritalnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_escritaln)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(ParserGrammar.PRINTLN)
            self.state = 207
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 208
            self.match(ParserGrammar.TEXTO)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 209
                self.match(ParserGrammar.VIRGULA)
                self.state = 210
                self.termoescrita()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 216
            self.match(ParserGrammar.PARENTESE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoescritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserGrammar.RULE_termoescrita

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermoEscritaTextoContext(TermoescritaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.TermoescritaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXTO(self):
            return self.getToken(ParserGrammar.TEXTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoEscritaTexto" ):
                listener.enterTermoEscritaTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoEscritaTexto" ):
                listener.exitTermoEscritaTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoEscritaTexto" ):
                return visitor.visitTermoEscritaTexto(self)
            else:
                return visitor.visitChildren(self)


    class TermoEscritaExpressaoContext(TermoescritaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.TermoescritaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoEscritaExpressao" ):
                listener.enterTermoEscritaExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoEscritaExpressao" ):
                listener.exitTermoEscritaExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoEscritaExpressao" ):
                return visitor.visitTermoEscritaExpressao(self)
            else:
                return visitor.visitChildren(self)



    def termoescrita(self):

        localctx = ParserGrammar.TermoescritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_termoescrita)
        try:
            self.state = 220
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = ParserGrammar.TermoEscritaTextoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(ParserGrammar.TEXTO)
                pass

            elif la_ == 2:
                localctx = ParserGrammar.TermoEscritaExpressaoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.expressao()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelecaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ParserGrammar.IF, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def senao(self):
            return self.getTypedRuleContext(ParserGrammar.SenaoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_selecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelecao" ):
                listener.enterSelecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelecao" ):
                listener.exitSelecao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelecao" ):
                return visitor.visitSelecao(self)
            else:
                return visitor.visitChildren(self)




    def selecao(self):

        localctx = ParserGrammar.SelecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_selecao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(ParserGrammar.IF)
            self.state = 223
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 224
            self.expressao()
            self.state = 225
            self.match(ParserGrammar.PARENTESE_FECHA)
            self.state = 226
            self.bloco()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 227
                self.senao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SenaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ParserGrammar.ELSE, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_senao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSenao" ):
                listener.enterSenao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSenao" ):
                listener.exitSenao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSenao" ):
                return visitor.visitSenao(self)
            else:
                return visitor.visitChildren(self)




    def senao(self):

        localctx = ParserGrammar.SenaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_senao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(ParserGrammar.ELSE)
            self.state = 231
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ParserGrammar.WHILE, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnquanto" ):
                listener.enterEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnquanto" ):
                listener.exitEnquanto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEnquanto" ):
                return visitor.visitEnquanto(self)
            else:
                return visitor.visitChildren(self)




    def enquanto(self):

        localctx = ParserGrammar.EnquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_enquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(ParserGrammar.WHILE)
            self.state = 234
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 235
            self.expressao()
            self.state = 236
            self.match(ParserGrammar.PARENTESE_FECHA)
            self.state = 237
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.atribuicaoInicio = None # Para_atribuicoesContext
            self.atribuicaoFinal = None # Para_atribuicoesContext

        def FOR(self):
            return self.getToken(ParserGrammar.FOR, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def PONTO_VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.PONTO_VIRGULA)
            else:
                return self.getToken(ParserGrammar.PONTO_VIRGULA, i)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def bloco(self):
            return self.getTypedRuleContext(ParserGrammar.BlocoContext,0)


        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def para_atribuicoes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Para_atribuicoesContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Para_atribuicoesContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = ParserGrammar.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(ParserGrammar.FOR)
            self.state = 240
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 241
                localctx.atribuicaoInicio = self.para_atribuicoes()


            self.state = 244
            self.match(ParserGrammar.PONTO_VIRGULA)
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68172103811584) != 0):
                self.state = 245
                self.expressao()


            self.state = 248
            self.match(ParserGrammar.PONTO_VIRGULA)
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 249
                localctx.atribuicaoFinal = self.para_atribuicoes()


            self.state = 252
            self.match(ParserGrammar.PARENTESE_FECHA)
            self.state = 253
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acesso_id(self):
            return self.getTypedRuleContext(ParserGrammar.Acesso_idContext,0)


        def OP_ATRIBUICAO(self):
            return self.getToken(ParserGrammar.OP_ATRIBUICAO, 0)

        def complemento(self):
            return self.getTypedRuleContext(ParserGrammar.ComplementoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = ParserGrammar.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.acesso_id()
            self.state = 256
            self.match(ParserGrammar.OP_ATRIBUICAO)
            self.state = 257
            self.complemento()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_atribuicoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.AtribuicaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_para_atribuicoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_atribuicoes" ):
                listener.enterPara_atribuicoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_atribuicoes" ):
                listener.exitPara_atribuicoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_atribuicoes" ):
                return visitor.visitPara_atribuicoes(self)
            else:
                return visitor.visitChildren(self)




    def para_atribuicoes(self):

        localctx = ParserGrammar.Para_atribuicoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_para_atribuicoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.atribuicao()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 260
                self.match(ParserGrammar.VIRGULA)
                self.state = 261
                self.atribuicao()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplementoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_complemento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplemento" ):
                listener.enterComplemento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplemento" ):
                listener.exitComplemento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplemento" ):
                return visitor.visitComplemento(self)
            else:
                return visitor.visitChildren(self)




    def complemento(self):

        localctx = ParserGrammar.ComplementoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_complemento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ParserGrammar.FUNC, 0)

        def ID(self):
            return self.getToken(ParserGrammar.ID, 0)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ParserGrammar.ArgumentosContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao" ):
                listener.enterFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao" ):
                listener.exitFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncao" ):
                return visitor.visitFuncao(self)
            else:
                return visitor.visitChildren(self)




    def funcao(self):

        localctx = ParserGrammar.FuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(ParserGrammar.FUNC)
            self.state = 270
            self.match(ParserGrammar.ID)
            self.state = 271
            self.match(ParserGrammar.PARENTESE_ABRE)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68172103811584) != 0):
                self.state = 272
                self.argumentos()


            self.state = 275
            self.match(ParserGrammar.PARENTESE_FECHA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.VIRGULA)
            else:
                return self.getToken(ParserGrammar.VIRGULA, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = ParserGrammar.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.expressao()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 278
                self.match(ParserGrammar.VIRGULA)
                self.state = 279
                self.expressao()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetornoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ParserGrammar.RETURN, 0)

        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_retorno

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorno" ):
                listener.enterRetorno(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorno" ):
                listener.exitRetorno(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetorno" ):
                return visitor.visitRetorno(self)
            else:
                return visitor.visitChildren(self)




    def retorno(self):

        localctx = ParserGrammar.RetornoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_retorno)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ParserGrammar.RETURN)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 68172103811584) != 0):
                self.state = 286
                self.expressao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_ou(self):
            return self.getTypedRuleContext(ParserGrammar.Expr_ouContext,0)


        def getRuleIndex(self):
            return ParserGrammar.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)




    def expressao(self):

        localctx = ParserGrammar.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expr_ou()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_ouContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_e(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Expr_eContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Expr_eContext,i)


        def OP_OU(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.OP_OU)
            else:
                return self.getToken(ParserGrammar.OP_OU, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_expr_ou

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_ou" ):
                listener.enterExpr_ou(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_ou" ):
                listener.exitExpr_ou(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_ou" ):
                return visitor.visitExpr_ou(self)
            else:
                return visitor.visitChildren(self)




    def expr_ou(self):

        localctx = ParserGrammar.Expr_ouContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr_ou)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.expr_e()
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 292
                self.match(ParserGrammar.OP_OU)
                self.state = 293
                self.expr_e()
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_eContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Expr_relacionalContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Expr_relacionalContext,i)


        def OP_E(self, i:int=None):
            if i is None:
                return self.getTokens(ParserGrammar.OP_E)
            else:
                return self.getToken(ParserGrammar.OP_E, i)

        def getRuleIndex(self):
            return ParserGrammar.RULE_expr_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_e" ):
                listener.enterExpr_e(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_e" ):
                listener.exitExpr_e(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_e" ):
                return visitor.visitExpr_e(self)
            else:
                return visitor.visitChildren(self)




    def expr_e(self):

        localctx = ParserGrammar.Expr_eContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expr_e)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.expr_relacional()
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32:
                self.state = 300
                self.match(ParserGrammar.OP_E)
                self.state = 301
                self.expr_relacional()
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_aditiva(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Expr_aditivaContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Expr_aditivaContext,i)


        def op_relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Op_relacionalContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Op_relacionalContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_expr_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_relacional" ):
                listener.enterExpr_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_relacional" ):
                listener.exitExpr_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_relacional" ):
                return visitor.visitExpr_relacional(self)
            else:
                return visitor.visitChildren(self)




    def expr_relacional(self):

        localctx = ParserGrammar.Expr_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expr_aditiva()
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0):
                self.state = 308
                self.op_relacional()
                self.state = 309
                self.expr_aditiva()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_IGUAL(self):
            return self.getToken(ParserGrammar.OP_IGUAL, 0)

        def OP_DIFERENTE(self):
            return self.getToken(ParserGrammar.OP_DIFERENTE, 0)

        def OP_MAIOR(self):
            return self.getToken(ParserGrammar.OP_MAIOR, 0)

        def OP_MENOR(self):
            return self.getToken(ParserGrammar.OP_MENOR, 0)

        def OP_MAIOR_IGUAL(self):
            return self.getToken(ParserGrammar.OP_MAIOR_IGUAL, 0)

        def OP_MENOR_IGUAL(self):
            return self.getToken(ParserGrammar.OP_MENOR_IGUAL, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_op_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_relacional" ):
                listener.enterOp_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_relacional" ):
                listener.exitOp_relacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_relacional" ):
                return visitor.visitOp_relacional(self)
            else:
                return visitor.visitChildren(self)




    def op_relacional(self):

        localctx = ParserGrammar.Op_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_op_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1082331758592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_aditivaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_multiplicativa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Expr_multiplicativaContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Expr_multiplicativaContext,i)


        def op_aditivo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Op_aditivoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Op_aditivoContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_expr_aditiva

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_aditiva" ):
                listener.enterExpr_aditiva(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_aditiva" ):
                listener.exitExpr_aditiva(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_aditiva" ):
                return visitor.visitExpr_aditiva(self)
            else:
                return visitor.visitChildren(self)




    def expr_aditiva(self):

        localctx = ParserGrammar.Expr_aditivaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr_aditiva)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr_multiplicativa()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 319
                self.op_aditivo()
                self.state = 320
                self.expr_multiplicativa()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_aditivoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINAL_MAIS(self):
            return self.getToken(ParserGrammar.SINAL_MAIS, 0)

        def SINAL_MENOS(self):
            return self.getToken(ParserGrammar.SINAL_MENOS, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_op_aditivo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_aditivo" ):
                listener.enterOp_aditivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_aditivo" ):
                listener.exitOp_aditivo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_aditivo" ):
                return visitor.visitOp_aditivo(self)
            else:
                return visitor.visitChildren(self)




    def op_aditivo(self):

        localctx = ParserGrammar.Op_aditivoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_op_aditivo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_multiplicativaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.FatorContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.FatorContext,i)


        def op_multiplicativo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Op_multiplicativoContext)
            else:
                return self.getTypedRuleContext(ParserGrammar.Op_multiplicativoContext,i)


        def getRuleIndex(self):
            return ParserGrammar.RULE_expr_multiplicativa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_multiplicativa" ):
                listener.enterExpr_multiplicativa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_multiplicativa" ):
                listener.exitExpr_multiplicativa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_multiplicativa" ):
                return visitor.visitExpr_multiplicativa(self)
            else:
                return visitor.visitChildren(self)




    def expr_multiplicativa(self):

        localctx = ParserGrammar.Expr_multiplicativaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr_multiplicativa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.fator()
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0):
                self.state = 330
                self.op_multiplicativo()
                self.state = 331
                self.fator()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_multiplicativoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULTIPLICACAO(self):
            return self.getToken(ParserGrammar.OP_MULTIPLICACAO, 0)

        def OP_DIVISAO(self):
            return self.getToken(ParserGrammar.OP_DIVISAO, 0)

        def OP_RESTO_DIVISAO(self):
            return self.getToken(ParserGrammar.OP_RESTO_DIVISAO, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_op_multiplicativo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_multiplicativo" ):
                listener.enterOp_multiplicativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_multiplicativo" ):
                listener.exitOp_multiplicativo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_multiplicativo" ):
                return visitor.visitOp_multiplicativo(self)
            else:
                return visitor.visitChildren(self)




    def op_multiplicativo(self):

        localctx = ParserGrammar.Op_multiplicativoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_op_multiplicativo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserGrammar.RULE_fator

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FatorTermoContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(ParserGrammar.TermoContext,0)

        def sinal(self):
            return self.getTypedRuleContext(ParserGrammar.SinalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFatorTermo" ):
                listener.enterFatorTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFatorTermo" ):
                listener.exitFatorTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFatorTermo" ):
                return visitor.visitFatorTermo(self)
            else:
                return visitor.visitChildren(self)


    class FatorNegacaoFatorContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OP_NEGACAO(self):
            return self.getToken(ParserGrammar.OP_NEGACAO, 0)
        def fator(self):
            return self.getTypedRuleContext(ParserGrammar.FatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFatorNegacaoFator" ):
                listener.enterFatorNegacaoFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFatorNegacaoFator" ):
                listener.exitFatorNegacaoFator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFatorNegacaoFator" ):
                return visitor.visitFatorNegacaoFator(self)
            else:
                return visitor.visitChildren(self)


    class FatorTextContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXTO(self):
            return self.getToken(ParserGrammar.TEXTO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFatorText" ):
                listener.enterFatorText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFatorText" ):
                listener.exitFatorText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFatorText" ):
                return visitor.visitFatorText(self)
            else:
                return visitor.visitChildren(self)


    class FatorExpressaoContext(FatorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.FatorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARENTESE_ABRE(self):
            return self.getToken(ParserGrammar.PARENTESE_ABRE, 0)
        def expressao(self):
            return self.getTypedRuleContext(ParserGrammar.ExpressaoContext,0)

        def PARENTESE_FECHA(self):
            return self.getToken(ParserGrammar.PARENTESE_FECHA, 0)
        def sinal(self):
            return self.getTypedRuleContext(ParserGrammar.SinalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFatorExpressao" ):
                listener.enterFatorExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFatorExpressao" ):
                listener.exitFatorExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFatorExpressao" ):
                return visitor.visitFatorExpressao(self)
            else:
                return visitor.visitChildren(self)



    def fator(self):

        localctx = ParserGrammar.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_fator)
        self._la = 0 # Token type
        try:
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                localctx = ParserGrammar.FatorTermoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26 or _la==27:
                    self.state = 340
                    self.sinal()


                self.state = 343
                self.termo()
                pass

            elif la_ == 2:
                localctx = ParserGrammar.FatorTextContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(ParserGrammar.TEXTO)
                pass

            elif la_ == 3:
                localctx = ParserGrammar.FatorNegacaoFatorContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(ParserGrammar.OP_NEGACAO)
                self.state = 346
                self.fator()
                pass

            elif la_ == 4:
                localctx = ParserGrammar.FatorExpressaoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==26 or _la==27:
                    self.state = 347
                    self.sinal()


                self.state = 350
                self.match(ParserGrammar.PARENTESE_ABRE)
                self.state = 351
                self.expressao()
                self.state = 352
                self.match(ParserGrammar.PARENTESE_FECHA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserGrammar.RULE_termo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermoConstanteContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constante(self):
            return self.getTypedRuleContext(ParserGrammar.ConstanteContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoConstante" ):
                listener.enterTermoConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoConstante" ):
                listener.exitTermoConstante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoConstante" ):
                return visitor.visitTermoConstante(self)
            else:
                return visitor.visitChildren(self)


    class TermoVariavelContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def acesso_id(self):
            return self.getTypedRuleContext(ParserGrammar.Acesso_idContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoVariavel" ):
                listener.enterTermoVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoVariavel" ):
                listener.exitTermoVariavel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoVariavel" ):
                return visitor.visitTermoVariavel(self)
            else:
                return visitor.visitChildren(self)


    class TermoFuncaoContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcao(self):
            return self.getTypedRuleContext(ParserGrammar.FuncaoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoFuncao" ):
                listener.enterTermoFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoFuncao" ):
                listener.exitTermoFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoFuncao" ):
                return visitor.visitTermoFuncao(self)
            else:
                return visitor.visitChildren(self)



    def termo(self):

        localctx = ParserGrammar.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_termo)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                localctx = ParserGrammar.TermoVariavelContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.acesso_id()
                pass
            elif token in [41, 42, 43, 44]:
                localctx = ParserGrammar.TermoConstanteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.constante()
                pass
            elif token in [9]:
                localctx = ParserGrammar.TermoFuncaoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 358
                self.funcao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINAL_MAIS(self):
            return self.getToken(ParserGrammar.SINAL_MAIS, 0)

        def SINAL_MENOS(self):
            return self.getToken(ParserGrammar.SINAL_MENOS, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_sinal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinal" ):
                listener.enterSinal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinal" ):
                listener.exitSinal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinal" ):
                return visitor.visitSinal(self)
            else:
                return visitor.visitChildren(self)




    def sinal(self):

        localctx = ParserGrammar.SinalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_sinal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(ParserGrammar.NUM_INT, 0)

        def NUM_DEC(self):
            return self.getToken(ParserGrammar.NUM_DEC, 0)

        def TRUE(self):
            return self.getToken(ParserGrammar.TRUE, 0)

        def FALSE(self):
            return self.getToken(ParserGrammar.FALSE, 0)

        def getRuleIndex(self):
            return ParserGrammar.RULE_constante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstante" ):
                listener.enterConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstante" ):
                listener.exitConstante(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstante" ):
                return visitor.visitConstante(self)
            else:
                return visitor.visitChildren(self)




    def constante(self):

        localctx = ParserGrammar.ConstanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_constante)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32985348833280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acesso_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ParserGrammar.RULE_acesso_id

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AcessoIdArrayContext(Acesso_idContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Acesso_idContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserGrammar.ID, 0)
        def dimensao2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParserGrammar.Dimensao2Context)
            else:
                return self.getTypedRuleContext(ParserGrammar.Dimensao2Context,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcessoIdArray" ):
                listener.enterAcessoIdArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcessoIdArray" ):
                listener.exitAcessoIdArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcessoIdArray" ):
                return visitor.visitAcessoIdArray(self)
            else:
                return visitor.visitChildren(self)


    class AcessoIdContext(Acesso_idContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ParserGrammar.Acesso_idContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ParserGrammar.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcessoId" ):
                listener.enterAcessoId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcessoId" ):
                listener.exitAcessoId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcessoId" ):
                return visitor.visitAcessoId(self)
            else:
                return visitor.visitChildren(self)



    def acesso_id(self):

        localctx = ParserGrammar.Acesso_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_acesso_id)
        self._la = 0 # Token type
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                localctx = ParserGrammar.AcessoIdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.match(ParserGrammar.ID)
                pass

            elif la_ == 2:
                localctx = ParserGrammar.AcessoIdArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(ParserGrammar.ID)
                self.state = 368 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 367
                    self.dimensao2()
                    self.state = 370 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==21):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





