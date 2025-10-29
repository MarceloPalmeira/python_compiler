# Pseudo-Código do Compilador MiniPar

Este documento apresenta o pseudo-código dos principais componentes do compilador MiniPar, incluindo análise léxica, sintática, semântica, tabela de símbolos e geração de código intermediário.

---

## 1. Analisador Léxico (Lexer)

### Interface Lexer
```
interface Lexer:
    método tokenize(source: string) -> lista[Token]
```

### Classe LexerImpl implementa Lexer
```
classe LexerImpl implementa Lexer:
    token_spec: lista[tupla(nome, regex)]
    keywords: conjunto[string]
    
    método inicialização:
        # Define especificação de tokens
        token_spec = [
            ("NUMBER", r"\b\d+(?:\.\d+)?\b"),
            ("STRING", r'"[^"\\]*(?:\\.[^"\\]*)*"'),
            ("COMMENT", r"#.*"),
            ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
            ("GTE", r">="),
            ("LTE", r"<="),
            ("EQ", r"=="),
            ("NEQ", r"!="),
            ("GT", r">"),
            ("LT", r"<"),
            ("AND", r"&&"),
            ("OR", r"\|\|"),
            ("NOT", r"!"),
            ("ASSIGN", r"="),
            ("ARROW", r"->"),
            ("OP", r"[+\-*/%]"),
            ("COLON", r":"),
            ("LBRACKET", r"\["),
            ("RBRACKET", r"\]"),
            ("LPAREN", r"\("),
            ("RPAREN", r"\)"),
            ("LBRACE", r"\{"),
            ("RBRACE", r"\}"),
            ("COMMA", r","),
            ("SEMICOLON", r";"),
            ("NEWLINE", r"\n"),
            ("SKIP", r"[ \t]+"),
            ("MISMATCH", r".")
        ]
        
        # Define palavras-chave
        keywords = {
            "var", "func", "return", "print", "if", "else", 
            "while", "for", "break", "continue", "true", 
            "false", "in", "par", "seq"
        }
        
        # Compila regex mestre combinando todos os padrões
        master_regex = compila_regex_combinada(token_spec)
    
    método tokenize(source: string) -> lista[Token]:
        tokens = []
        line_num = 1
        line_start = 0
        
        # Itera sobre todos os matches no código fonte
        para cada match em master_regex.finditer(source):
            kind = match.lastgroup
            value = match.group()
            col = match.start() - line_start + 1
            
            # Trata cada tipo de token
            se kind == "NUMBER":
                val = value
                
            senão se kind == "ID":
                # Verifica se é palavra-chave
                se value em keywords:
                    kind = value.uppercase()
                val = value
                
            senão se kind == "STRING":
                val = value
                
            senão se kind == "NEWLINE":
                line_num += 1
                line_start = match.end()
                continue  # Não adiciona token de nova linha
                
            senão se kind == "SKIP":
                continue  # Ignora espaços em branco
                
            senão se kind == "COMMENT":
                continue  # Ignora comentários
                
            senão se kind == "MISMATCH":
                lança SyntaxError(f"Caractere inesperado {value} na linha {line_num} coluna {col}")
                
            senão:
                val = value
            
            # Adiciona token à lista
            tokens.append({
                "type": kind,
                "value": val,
                "line": line_num,
                "col": col
            })
        
        retorna tokens
```

---

## 2. Analisador Sintático (Parser)

### Interface Parser
```
interface Parser:
    método parse(source: string) -> AST
```

### Classe TokStream (Stream de Tokens)
```
classe TokStream:
    tokens: lista[Token]
    i: integer
    
    método inicialização(tokens: lista[Token]):
        self.tokens = tokens
        self.i = 0
    
    método peek() -> Token:
        # Retorna token atual sem consumir
        se self.i < tamanho(self.tokens):
            retorna self.tokens[self.i]
        retorna Token(type="EOF", value="", line=-1, col=-1)
    
    método next() -> Token:
        # Consome e retorna token atual
        t = self.peek()
        self.i += 1
        retorna t
    
    método accept(*types) -> Token ou None:
        # Consome token se corresponder aos tipos esperados
        se self.peek().type em types:
            retorna self.next()
        retorna None
    
    método expect(*types) -> Token:
        # Consome token ou lança erro se não corresponder
        t = self.accept(*types)
        se t é None:
            lança SyntaxError(f"Esperado {types}, encontrado {self.peek()}")
        retorna t
```

### Classe ParserImpl implementa Parser
```
classe ParserImpl implementa Parser:
    ts: TokStream
    
    método parse(source: string) -> AST:
        tokens = Lexer.tokenize(source)
        self.ts = TokStream(tokens)
        retorna self.parse_program()
    
    método parse_program() -> NodoPrograma:
        body = []
        enquanto ts.peek().type != "EOF":
            node = self.parse_statement()
            se node não é None:
                body.append(node)
        retorna {"type": "Program", "body": body}
    
    método parse_statement() -> NodoStatement:
        p = ts.peek()
        
        # Declaração de variável: var x = expr;
        se p.type == "VAR":
            ts.next()
            name = ts.expect("ID").value
            
            # Anotação de tipo opcional: : type
            se ts.accept("COLON"):
                se ts.peek().type == "ID":
                    ts.next()
            
            # Inicializador
            se ts.accept("ASSIGN"):
                expr = self.parse_expression()
            senão:
                expr = {"type": "Literal", "value": "0"}
            
            ts.accept("SEMICOLON")
            retorna {
                "type": "VariableDeclaration",
                "name": name,
                "init": expr
            }
        
        # Declaração de função: func nome(params) { body }
        se p.type == "FUNC":
            ts.next()
            name = ts.expect("ID").value
            ts.expect("LPAREN")
            
            params = []
            se ts.peek().type != "RPAREN":
                loop:
                    param = ts.expect("ID").value
                    # Tipo opcional do parâmetro
                    se ts.accept("COLON"):
                        se ts.peek().type == "ID":
                            ts.next()
                    params.append(param)
                    se não ts.accept("COMMA"):
                        break
            
            ts.expect("RPAREN")
            
            # Tipo de retorno opcional: -> type
            se ts.accept("ARROW"):
                se ts.peek().type == "ID":
                    ts.next()
            
            ts.expect("LBRACE")
            body = []
            enquanto ts.peek().type != "RBRACE":
                body.append(self.parse_statement())
            ts.expect("RBRACE")
            
            retorna {
                "type": "FunctionDeclaration",
                "name": name,
                "params": params,
                "body": body
            }
        
        # Comando print: print(expr);
        se p.type == "PRINT":
            ts.next()
            ts.expect("LPAREN")
            args = []
            se ts.peek().type != "RPAREN":
                loop:
                    args.append(self.parse_expression())
                    se não ts.accept("COMMA"):
                        break
            ts.expect("RPAREN")
            ts.accept("SEMICOLON")
            retorna {
                "type": "CallStatement",
                "callee": "print",
                "args": args
            }
        
        # Atribuição: x = expr;
        se p.type == "ID":
            idtok = ts.next()
            se ts.accept("ASSIGN"):
                expr = self.parse_expression()
                ts.accept("SEMICOLON")
                retorna {
                    "type": "Assignment",
                    "name": idtok.value,
                    "value": expr
                }
            # Chamada de função como statement
            senão se ts.peek().type == "LPAREN":
                ts.next()
                args = []
                se ts.peek().type != "RPAREN":
                    loop:
                        args.append(self.parse_expression())
                        se não ts.accept("COMMA"):
                            break
                ts.expect("RPAREN")
                ts.accept("SEMICOLON")
                retorna {
                    "type": "CallStatement",
                    "callee": idtok.value,
                    "args": args
                }
        
        # Comando return: return expr;
        se p.type == "RETURN":
            ts.next()
            expr = self.parse_expression()
            ts.accept("SEMICOLON")
            retorna {
                "type": "ReturnStatement",
                "argument": expr
            }
        
        # Comando if: if (cond) { ... } else { ... }
        se p.type == "IF":
            ts.next()
            ts.expect("LPAREN")
            condition = self.parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            
            then_body = []
            enquanto ts.peek().type != "RBRACE":
                then_body.append(self.parse_statement())
            ts.expect("RBRACE")
            
            # Bloco else opcional
            else_body = None
            se ts.accept("ELSE"):
                ts.expect("LBRACE")
                else_body = []
                enquanto ts.peek().type != "RBRACE":
                    else_body.append(self.parse_statement())
                ts.expect("RBRACE")
            
            retorna {
                "type": "IfStatement",
                "test": condition,
                "consequent": then_body,
                "alternate": else_body
            }
        
        # Comando while: while (cond) { ... }
        se p.type == "WHILE":
            ts.next()
            ts.expect("LPAREN")
            condition = self.parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            
            body = []
            enquanto ts.peek().type != "RBRACE":
                body.append(self.parse_statement())
            ts.expect("RBRACE")
            
            retorna {
                "type": "WhileStatement",
                "test": condition,
                "body": body
            }
        
        # Comando for: for (var x in iterable) { ... }
        se p.type == "FOR":
            ts.next()
            ts.expect("LPAREN")
            ts.expect("VAR")
            var_name = ts.expect("ID").value
            ts.accept("COLON")  # tipo opcional
            se ts.peek().type == "ID":
                ts.next()
            ts.expect("IN")
            iterable = self.parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            
            body = []
            enquanto ts.peek().type != "RBRACE":
                body.append(self.parse_statement())
            ts.expect("RBRACE")
            
            retorna {
                "type": "ForStatement",
                "variable": var_name,
                "iterable": iterable,
                "body": body
            }
        
        # Bloco paralelo: par { ... }
        se p.type == "PAR":
            ts.next()
            ts.expect("LBRACE")
            body = []
            enquanto ts.peek().type != "RBRACE":
                body.append(self.parse_statement())
            ts.expect("RBRACE")
            retorna {
                "type": "ParallelBlock",
                "body": body
            }
        
        # Statement vazio
        se p.type == "SEMICOLON":
            ts.next()
            retorna None
        
        # Expressão como statement
        expr = self.parse_expression()
        ts.accept("SEMICOLON")
        retorna {
            "type": "ExpressionStatement",
            "expression": expr
        }
    
    método parse_expression() -> NodoExpression:
        retorna self.parse_logical_or()
    
    método parse_logical_or() -> NodoExpression:
        # Operador lógico OR (||) - menor precedência
        node = self.parse_logical_and()
        enquanto ts.peek().type == "OR":
            op = ts.next().value
            right = self.parse_logical_and()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_logical_and() -> NodoExpression:
        # Operador lógico AND (&&)
        node = self.parse_equality()
        enquanto ts.peek().type == "AND":
            op = ts.next().value
            right = self.parse_equality()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_equality() -> NodoExpression:
        # Operadores de igualdade (==, !=)
        node = self.parse_relational()
        enquanto ts.peek().type em ("EQ", "NEQ"):
            op = ts.next().value
            right = self.parse_relational()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_relational() -> NodoExpression:
        # Operadores relacionais (<, <=, >, >=)
        node = self.parse_additive()
        enquanto ts.peek().type em ("LT", "LTE", "GT", "GTE"):
            op = ts.next().value
            right = self.parse_additive()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_additive() -> NodoExpression:
        # Operadores aditivos (+, -)
        node = self.parse_multiplicative()
        enquanto ts.peek().type == "OP" e ts.peek().value em ("+", "-"):
            op = ts.next().value
            right = self.parse_multiplicative()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_multiplicative() -> NodoExpression:
        # Operadores multiplicativos (*, /, %)
        node = self.parse_unary()
        enquanto ts.peek().type == "OP" e ts.peek().value em ("*", "/", "%"):
            op = ts.next().value
            right = self.parse_unary()
            node = {
                "type": "BinaryExpression",
                "operator": op,
                "left": node,
                "right": right
            }
        retorna node
    
    método parse_unary() -> NodoExpression:
        # Operadores unários (!, +, -)
        se ts.peek().type == "NOT":
            op = ts.next().value
            expr = self.parse_unary()
            retorna {
                "type": "UnaryExpression",
                "operator": op,
                "argument": expr
            }
        se ts.peek().type == "OP" e ts.peek().value em ("+", "-"):
            op = ts.next().value
            expr = self.parse_unary()
            retorna {
                "type": "UnaryExpression",
                "operator": op,
                "argument": expr
            }
        retorna self.parse_primary()
    
    método parse_primary() -> NodoExpression:
        # Fatores primários (literais, identificadores, chamadas, parênteses)
        p = ts.peek()
        
        se p.type == "NUMBER":
            retorna {
                "type": "Literal",
                "value": ts.next().value
            }
        
        se p.type == "STRING":
            retorna {
                "type": "Literal",
                "value": ts.next().value
            }
        
        se p.type == "TRUE":
            ts.next()
            retorna {"type": "Literal", "value": "true"}
        
        se p.type == "FALSE":
            ts.next()
            retorna {"type": "Literal", "value": "false"}
        
        se p.type == "ID":
            idt = ts.next().value
            # Chamada de função
            se ts.peek().type == "LPAREN":
                ts.next()
                args = []
                se ts.peek().type != "RPAREN":
                    loop:
                        args.append(self.parse_expression())
                        se não ts.accept("COMMA"):
                            break
                ts.expect("RPAREN")
                retorna {
                    "type": "CallExpression",
                    "callee": idt,
                    "arguments": args
                }
            # Identificador simples
            retorna {"type": "Identifier", "name": idt}
        
        # Expressão entre parênteses
        se p.type == "LPAREN":
            ts.next()
            node = self.parse_expression()
            ts.expect("RPAREN")
            retorna node
        
        lança SyntaxError(f"Token inesperado em expressão primária: {p}")
```

---

## 3. Analisador Semântico

### Interface SemanticAnalyzer
```
interface SemanticAnalyzer:
    método semantic_check(ast: AST) -> ResultadoSemantico
```

### Classe SemanticAnalyzerImpl implementa SemanticAnalyzer
```
classe SemanticAnalyzerImpl implementa SemanticAnalyzer:
    errors: lista[string]
    globals_sym: TabelaSimbolos
    
    método semantic_check(ast: AST) -> ResultadoSemantico:
        self.errors = []
        self.globals_sym = {
            "functions": {},
            "variables": conjunto[]
        }
        
        # Pré-carrega funções built-in
        self.globals_sym.functions["print"] = True
        
        # Primeira passagem: coleta funções e variáveis globais
        para cada node em ast.body:
            t = node.type
            
            se t == "FunctionDeclaration":
                self.globals_sym.functions[node.name] = node
            
            senão se t == "VariableDeclaration":
                self.globals_sym.variables.add(node.name)
        
        # Segunda passagem: verificações semânticas
        para cada top em ast.body:
            self.check_node(top, local_vars=conjunto[])
        
        retorna {
            "symbols": self.globals_sym,
            "errors": self.errors
        }
    
    método check_node(node: NodoAST, local_vars: conjunto[string]):
        t = node.type
        
        se t == "VariableDeclaration":
            # Verifica inicializador
            se node.init:
                self.check_node(node.init, local_vars)
            # Adiciona variável ao escopo local
            local_vars.add(node.name)
        
        senão se t == "Assignment":
            # Verifica expressão do lado direito
            self.check_node(node.value, local_vars)
            # Verifica se variável foi declarada
            name = node.name
            se name não em local_vars e name não em self.globals_sym.variables:
                self.errors.append(f"Atribuição a variável não declarada '{name}'")
        
        senão se t == "ExpressionStatement":
            self.check_node(node.expression, local_vars)
        
        senão se t == "Identifier":
            # Verifica se identificador foi declarado
            name = node.name
            se name não em local_vars e 
               name não em self.globals_sym.variables e
               name não em self.globals_sym.functions:
                self.errors.append(f"Uso de identificador não declarado '{name}'")
        
        senão se t em ("CallStatement", "CallExpression"):
            # Verifica se função foi declarada
            callee = node.callee
            se callee não em self.globals_sym.functions:
                self.errors.append(f"Chamada a função não declarada '{callee}'")
            # Verifica argumentos
            args = node.args se node.args senão node.arguments
            para cada a em args:
                self.check_node(a, local_vars)
        
        senão se t == "FunctionDeclaration":
            # Verifica corpo da função com parâmetros no escopo
            params = conjunto(node.params)
            para cada st em node.body:
                self.check_node(st, local_vars=params.copy())
        
        senão se t == "BinaryExpression":
            # Verifica operandos esquerdo e direito
            self.check_node(node.left, local_vars)
            self.check_node(node.right, local_vars)
        
        senão se t == "UnaryExpression":
            # Verifica operando
            self.check_node(node.argument, local_vars)
        
        senão se t == "ReturnStatement":
            # Verifica expressão de retorno
            self.check_node(node.argument, local_vars)
        
        senão se t == "IfStatement":
            # Verifica condição
            self.check_node(node.test, local_vars)
            # Verifica bloco then
            para cada st em node.consequent:
                self.check_node(st, local_vars)
            # Verifica bloco else (se existir)
            se node.alternate:
                para cada st em node.alternate:
                    self.check_node(st, local_vars)
        
        senão se t == "WhileStatement":
            # Verifica condição
            self.check_node(node.test, local_vars)
            # Verifica corpo
            para cada st em node.body:
                self.check_node(st, local_vars)
        
        senão se t == "ForStatement":
            # Verifica iterável
            self.check_node(node.iterable, local_vars)
            # Adiciona variável de loop ao escopo
            loop_vars = local_vars.copy()
            loop_vars.add(node.variable)
            # Verifica corpo
            para cada st em node.body:
                self.check_node(st, loop_vars)
        
        senão se t == "ParallelBlock":
            # Verifica corpo do bloco paralelo
            para cada st em node.body:
                self.check_node(st, local_vars)
        
        senão se t == "Literal":
            # Literais não precisam de verificação
            pass
        
        senão:
            # Outros nodos: processa recursivamente
            para cada key, value em node.items():
                se value é dict e "type" em value:
                    self.check_node(value, local_vars)
                senão se value é lista:
                    para cada item em value:
                        se item é dict e "type" em item:
                            self.check_node(item, local_vars)
```

---

## 4. Tabela de Símbolos

### Estrutura TabelaSimbolos
```
estrutura TabelaSimbolos:
    functions: dicionário[string, InformaçãoFunção]
    variables: conjunto[string]

estrutura InformaçãoFunção:
    name: string
    params: lista[string]
    body: lista[NodoStatement]
    return_type: string (opcional)

estrutura InformaçãoVariável:
    name: string
    type: string (opcional)
    scope: string  # "global" ou "local"
    line: integer  # linha de declaração
```

### Classe SymbolTableManager
```
classe SymbolTableManager:
    global_table: TabelaSimbolos
    local_scopes: pilha[dicionário[string, InformaçãoVariável]]
    
    método inicialização:
        self.global_table = {
            "functions": {},
            "variables": conjunto[]
        }
        self.local_scopes = []
        # Adiciona funções built-in
        self.add_builtin_function("print")
    
    método add_builtin_function(name: string):
        self.global_table.functions[name] = {
            "name": name,
            "builtin": True
        }
    
    método enter_scope():
        # Entra em um novo escopo local (função, bloco)
        self.local_scopes.push({})
    
    método exit_scope():
        # Sai do escopo local atual
        se self.local_scopes não está vazio:
            self.local_scopes.pop()
    
    método declare_function(name: string, params: lista[string], body: lista):
        se name em self.global_table.functions:
            lança SemanticError(f"Função '{name}' já declarada")
        self.global_table.functions[name] = {
            "name": name,
            "params": params,
            "body": body,
            "builtin": False
        }
    
    método declare_variable(name: string, scope: string):
        se scope == "global":
            se name em self.global_table.variables:
                lança SemanticError(f"Variável global '{name}' já declarada")
            self.global_table.variables.add(name)
        senão:
            # Adiciona ao escopo local atual
            se self.local_scopes não está vazio:
                current_scope = self.local_scopes.top()
                se name em current_scope:
                    lança SemanticError(f"Variável local '{name}' já declarada neste escopo")
                current_scope[name] = {
                    "name": name,
                    "scope": "local"
                }
    
    método lookup_variable(name: string) -> booleano:
        # Procura variável começando pelo escopo mais interno
        para cada scope em reversed(self.local_scopes):
            se name em scope:
                retorna True
        # Procura no escopo global
        se name em self.global_table.variables:
            retorna True
        retorna False
    
    método lookup_function(name: string) -> InformaçãoFunção ou None:
        se name em self.global_table.functions:
            retorna self.global_table.functions[name]
        retorna None
    
    método get_all_symbols() -> TabelaSimbolos:
        retorna self.global_table
```

---

## 5. Gerador de Código Intermediário (TAC)

### Interface CodeGenerator
```
interface CodeGenerator:
    método generate_tac(ast: AST) -> lista[string]
```

### Classe TACGenerator implementa CodeGenerator
```
classe TACGenerator implementa CodeGenerator:
    output: lista[string]
    temp_counter: integer
    label_counter: integer
    
    método inicialização:
        self.output = []
        self.temp_counter = 0
        self.label_counter = 0
    
    método new_temp() -> string:
        # Gera novo temporário único
        self.temp_counter += 1
        retorna f"t{self.temp_counter}"
    
    método new_label() -> string:
        # Gera novo rótulo único
        self.label_counter += 1
        retorna f"L{self.label_counter}"
    
    método emit(instruction: string):
        # Emite instrução TAC
        self.output.append(instruction)
    
    método generate_tac(ast: AST) -> lista[string]:
        # Gera código TAC para programa completo
        para cada node em ast.body:
            self.gen_statement(node)
        retorna self.output
    
    método expr_to_tac(expr: NodoExpression) -> string:
        # Gera TAC para expressão e retorna nome do temporário/variável
        t = expr.type
        
        se t == "Literal":
            tmp = self.new_temp()
            self.emit(f"{tmp} = {expr.value}")
            retorna tmp
        
        se t == "Identifier":
            retorna expr.name
        
        se t == "BinaryExpression":
            left = self.expr_to_tac(expr.left)
            right = self.expr_to_tac(expr.right)
            tmp = self.new_temp()
            self.emit(f"{tmp} = {left} {expr.operator} {right}")
            retorna tmp
        
        se t == "UnaryExpression":
            operand = self.expr_to_tac(expr.argument)
            tmp = self.new_temp()
            self.emit(f"{tmp} = {expr.operator}{operand}")
            retorna tmp
        
        se t == "CallExpression":
            # Prepara argumentos
            args = []
            para cada a em expr.arguments:
                args.append(self.expr_to_tac(a))
            # Emite instruções param
            para cada a em args:
                self.emit(f"param {a}")
            # Emite chamada e captura retorno
            ret_tmp = self.new_temp()
            self.emit(f"{ret_tmp} = call {expr.callee} , {tamanho(args)}")
            retorna ret_tmp
        
        # Fallback
        tmp = self.new_temp()
        self.emit(f"{tmp} = 0")
        retorna tmp
    
    método gen_statement(node: NodoStatement):
        t = node.type
        
        se t == "VariableDeclaration":
            name = node.name
            se node.init:
                val = self.expr_to_tac(node.init)
                self.emit(f"{name} = {val}")
            senão:
                self.emit(f"{name} = 0")
        
        senão se t == "Assignment":
            val = self.expr_to_tac(node.value)
            self.emit(f"{node.name} = {val}")
        
        senão se t == "ExpressionStatement":
            self.expr_to_tac(node.expression)
        
        senão se t == "CallStatement":
            # Prepara argumentos
            args_loc = []
            para cada a em node.args:
                args_loc.append(self.expr_to_tac(a))
            # Emite params e call
            para cada a em args_loc:
                self.emit(f"param {a}")
            self.emit(f"call {node.callee} , {tamanho(args_loc)}")
        
        senão se t == "FunctionDeclaration":
            self.emit(f"func {node.name}")
            # Emite declarações de parâmetros
            params = node.params
            para i, param em enumerate(params):
                se i < 4:
                    # Primeiros 4 parâmetros vêm de registradores r0-r3
                    self.emit(f"{param} = r{i}    ; param {i}")
                senão:
                    # Parâmetros adicionais vêm da pilha
                    offset = (i - 4) * 4
                    self.emit(f"{param} = stack[{offset}]    ; param {i}")
            # Gera código do corpo
            para cada st em node.body:
                self.gen_statement(st)
            self.emit(f"endfunc {node.name}")
        
        senão se t == "ReturnStatement":
            val = self.expr_to_tac(node.argument)
            self.emit(f"ret {val}")
        
        senão se t == "IfStatement":
            else_label = self.new_label()
            end_label = self.new_label()
            
            # Avalia condição
            cond = self.expr_to_tac(node.test)
            self.emit(f"if_false {cond} goto {else_label}")
            
            # Bloco then
            para cada st em node.consequent:
                self.gen_statement(st)
            self.emit(f"goto {end_label}")
            
            # Bloco else
            self.emit(f"{else_label}:")
            se node.alternate:
                para cada st em node.alternate:
                    self.gen_statement(st)
            
            self.emit(f"{end_label}:")
        
        senão se t == "WhileStatement":
            loop_start = self.new_label()
            loop_end = self.new_label()
            
            self.emit(f"{loop_start}:")
            cond = self.expr_to_tac(node.test)
            self.emit(f"if_false {cond} goto {loop_end}")
            
            # Corpo do loop
            para cada st em node.body:
                self.gen_statement(st)
            
            self.emit(f"goto {loop_start}")
            self.emit(f"{loop_end}:")
        
        senão se t == "ForStatement":
            loop_start = self.new_label()
            loop_end = self.new_label()
            
            # Inicialização do loop
            iterable = self.expr_to_tac(node.iterable)
            var_name = node.variable
            self.emit(f"for_init {var_name} {iterable}")
            
            # Loop
            self.emit(f"{loop_start}:")
            self.emit(f"for_check {var_name} goto {loop_end}")
            
            # Corpo
            para cada st em node.body:
                self.gen_statement(st)
            
            # Incremento
            self.emit(f"for_next {var_name}")
            self.emit(f"goto {loop_start}")
            self.emit(f"{loop_end}:")
        
        senão se t == "BreakStatement":
            self.emit("break")
        
        senão se t == "ContinueStatement":
            self.emit("continue")
        
        senão se t == "ParallelBlock":
            self.emit("par_start")
            para cada st em node.body:
                self.gen_statement(st)
            self.emit("par_end")
        
        senão:
            # Processa nodos aninhados recursivamente
            para cada key, value em node.items():
                se value é dict e "type" em value:
                    self.gen_statement(value)
                senão se value é lista:
                    para cada item em value:
                        se item é dict e "type" em item:
                            self.gen_statement(item)
```

---

## 6. Pipeline Completo de Compilação

### Classe Compiler
```
classe Compiler:
    lexer: Lexer
    parser: Parser
    semantic_analyzer: SemanticAnalyzer
    code_generator: CodeGenerator
    
    método inicialização:
        self.lexer = LexerImpl()
        self.parser = ParserImpl()
        self.semantic_analyzer = SemanticAnalyzerImpl()
        self.code_generator = TACGenerator()
    
    método compile(source: string) -> ResultadoCompilação:
        resultado = {
            "tokens": None,
            "ast": None,
            "symbols": None,
            "errors": [],
            "tac": None
        }
        
        # Fase 1: Análise Léxica
        tenta:
            resultado.tokens = self.lexer.tokenize(source)
        captura SyntaxError como e:
            resultado.errors.append(f"Erro léxico: {e}")
            retorna resultado
        
        # Fase 2: Análise Sintática
        tenta:
            resultado.ast = self.parser.parse(source)
        captura SyntaxError como e:
            resultado.errors.append(f"Erro sintático: {e}")
            retorna resultado
        
        # Fase 3: Análise Semântica
        tenta:
            sem_result = self.semantic_analyzer.semantic_check(resultado.ast)
            resultado.symbols = sem_result.symbols
            resultado.errors.extend(sem_result.errors)
            
            # Se há erros semânticos, não gera código
            se tamanho(sem_result.errors) > 0:
                retorna resultado
        captura Exception como e:
            resultado.errors.append(f"Erro semântico: {e}")
            retorna resultado
        
        # Fase 4: Geração de Código Intermediário
        tenta:
            resultado.tac = self.code_generator.generate_tac(resultado.ast)
        captura Exception como e:
            resultado.errors.append(f"Erro na geração de código: {e}")
            retorna resultado
        
        retorna resultado
```

---

## Notas Finais

Este pseudo-código apresenta a arquitetura do compilador MiniPar de forma simplificada e didática. O compilador segue o pipeline clássico:

1. **Análise Léxica**: Converte código fonte em tokens
2. **Análise Sintática**: Converte tokens em árvore sintática abstrata (AST)
3. **Análise Semântica**: Verifica consistência semântica e constrói tabela de símbolos
4. **Geração de Código**: Converte AST em código intermediário TAC (Three-Address Code)

Cada fase pode detectar erros específicos:
- **Erros Léxicos**: Caracteres inválidos
- **Erros Sintáticos**: Estrutura incorreta do programa
- **Erros Semânticos**: Variáveis não declaradas, tipos incompatíveis, etc.

O código TAC gerado pode ser posteriormente traduzido para assembly ARM ou executado por um interpretador.

