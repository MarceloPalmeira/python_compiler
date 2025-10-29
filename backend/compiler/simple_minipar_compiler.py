"""Simple functional MiniPar compiler.

Exports:
 - tokenize(src: str) -> List[dict]
 - parse(src: str) -> dict  # AST-like structure
 - semantic_check(ast: dict) -> dict  # returns symbol tables and issues
 - generate_tac(ast: dict) -> List[str]

This is intentionally small and pragmatic: enough structure to feed
`tac_generator` / `tac_to_arm` in the repo and run an end-to-end
pipeline: source -> tokens -> AST -> TAC -> ARM.

The implementation uses plain dicts/lists as AST nodes (no classes)
to keep the code lightweight and easy to inspect.
"""

import re
from typing import List, Dict, Any, Tuple

# ---------------------
# Lexer
# ---------------------

TOKEN_SPEC = [
    ("NUMBER", r"\b\d+(?:\.\d+)?\b"),
    ("STRING", r'"[^"\\]*(?:\\.[^"\\]*)*"'),
    ("COMMENT", r"#.*"),
    ("ID", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    # Operadores relacionais (ordem importante - >= antes de >)
    ("GTE", r">="),
    ("LTE", r"<="),
    ("EQ", r"=="),
    ("NEQ", r"!="),
    ("GT", r">"),
    ("LT", r"<"),
    # Operadores lógicos
    ("AND", r"&&"),
    ("OR", r"\|\|"),
    ("NOT", r"!"),
    # Atribuição e setas
    ("ASSIGN", r"="),
    ("ARROW", r"->"),
    # Operadores aritméticos
    ("OP", r"[+\-*/%]"),
    # Símbolos
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

MASTER_RE = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))

KEYWORDS = {
    "var", "func", "return", "print", "if", "else", "while", "for", 
    "break", "continue", "true", "false", "in", "par", "seq"
}


def tokenize(src: str) -> List[Dict[str, Any]]:
    """Return a list of token dicts: {type, value, line, col}.

    This lexer is intentionally simple but robust enough for small
    example programs used in the project.
    """
    tokens = []
    line_num = 1
    line_start = 0
    for mo in MASTER_RE.finditer(src):
        kind = mo.lastgroup
        value = mo.group()
        col = mo.start() - line_start + 1
        if kind == "NUMBER":
            val = value
        elif kind == "ID":
            if value in KEYWORDS:
                kind = value.upper()
            val = value
        elif kind == "STRING":
            val = value
        elif kind == "NEWLINE":
            line_num += 1
            line_start = mo.end()
            continue
        elif kind == "SKIP":
            continue
        elif kind == "COMMENT":
            # skip comments (from # to end of line)
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value!r} at line {line_num} col {col}")
        else:
            val = value

        tokens.append({"type": kind, "value": val, "line": line_num, "col": col})

    return tokens


# ---------------------
# Parser (very small recursive-descent)
# ---------------------

class _TokStream:
    def __init__(self, tokens: List[Dict[str, Any]]):
        self.tokens = tokens
        self.i = 0

    def peek(self) -> Dict[str, Any]:
        if self.i < len(self.tokens):
            return self.tokens[self.i]
        return {"type": "EOF", "value": "", "line": -1, "col": -1}

    def next(self) -> Dict[str, Any]:
        t = self.peek()
        self.i += 1
        return t

    def accept(self, *types):
        if self.peek()["type"] in types:
            return self.next()
        return None

    def expect(self, *types):
        t = self.accept(*types)
        if t is None:
            raise SyntaxError(f"Expected one of {types} but got {self.peek()}")
        return t


def parse(src: str) -> Dict[str, Any]:
    """Parse source into a simple AST (dict-based).

    Supported constructs (minimal):
    - var <id> = <expr> ;
    - <id> = <expr> ;
    - func <id>([params]) { ... }
    - return <expr> ;
    - print(<expr>) ;
    - expression statements
    """
    tokens = tokenize(src)
    ts = _TokStream(tokens)

    def parse_program():
        body = []
        while ts.peek()["type"] != "EOF":
            node = parse_statement()
            if node is not None:
                body.append(node)
        return {"type": "Program", "body": body}

    def parse_statement():
        p = ts.peek()
        # Handle built-in print as a call statement
        if p["type"] == "PRINT":
            ts.next()
            ts.expect("LPAREN")
            args = []
            if ts.peek()["type"] != "RPAREN":
                while True:
                    args.append(parse_expression())
                    if ts.accept("COMMA"):
                        continue
                    break
            ts.expect("RPAREN")
            ts.accept("SEMICOLON")
            return {"type": "CallStatement", "callee": "print", "args": args}

        if p["type"] == "VAR":
            ts.next()
            name_tok = ts.expect("ID")
            # optional type annotation: : TYPE
            if ts.accept("COLON"):
                # consume type identifier (if present)
                if ts.peek()["type"] == "ID":
                    ts.next()
            # initializer
            if ts.accept("ASSIGN"):
                expr = parse_expression()
            else:
                expr = {"type": "Literal", "value": "0"}
            # optional semicolon
            ts.accept("SEMICOLON")
            return {"type": "VariableDeclaration", "name": name_tok["value"], "init": expr}

        if p["type"] == "FUNC":
            ts.next()
            name_tok = ts.expect("ID")
            ts.expect("LPAREN")
            params = []
            if ts.peek()["type"] != "RPAREN":
                while True:
                    param = ts.expect("ID")
                    # optional type annotation for param: : TYPE
                    if ts.accept("COLON"):
                        if ts.peek()["type"] == "ID":
                            ts.next()
                    params.append(param["value"])
                    if ts.accept("COMMA"):
                        continue
                    break
            ts.expect("RPAREN")
            # optional return type: -> TYPE
            if ts.accept("ARROW"):
                if ts.peek()["type"] == "ID":
                    ts.next()
            ts.expect("LBRACE")
            body = []
            while ts.peek()["type"] != "RBRACE":
                body.append(parse_statement())
            ts.expect("RBRACE")
            return {"type": "FunctionDeclaration", "name": name_tok["value"], "params": params, "body": body}

        if p["type"] == "ID":
            # could be assignment or call
            idtok = ts.next()
            if ts.accept("ASSIGN"):
                expr = parse_expression()
                ts.accept("SEMICOLON")
                return {"type": "Assignment", "name": idtok["value"], "value": expr}
            elif ts.peek()["type"] == "LPAREN":
                # function call as statement
                ts.next()
                args = []
                if ts.peek()["type"] != "RPAREN":
                    while True:
                        args.append(parse_expression())
                        if ts.accept("COMMA"):
                            continue
                        break
                ts.expect("RPAREN")
                ts.accept("SEMICOLON")
                return {"type": "CallStatement", "callee": idtok["value"], "args": args}
            else:
                # bare identifier as expression statement
                ts.accept("SEMICOLON")
                return {"type": "ExpressionStatement", "expression": {"type": "Identifier", "name": idtok["value"]}}

        if p["type"] == "RETURN":
            ts.next()
            expr = parse_expression()
            ts.accept("SEMICOLON")
            return {"type": "ReturnStatement", "argument": expr}

        if p["type"] == "IF":
            ts.next()
            ts.expect("LPAREN")
            condition = parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            then_body = []
            while ts.peek()["type"] != "RBRACE":
                then_body.append(parse_statement())
            ts.expect("RBRACE")
            
            # Optional else
            else_body = None
            if ts.accept("ELSE"):
                ts.expect("LBRACE")
                else_body = []
                while ts.peek()["type"] != "RBRACE":
                    else_body.append(parse_statement())
                ts.expect("RBRACE")
            
            return {"type": "IfStatement", "test": condition, "consequent": then_body, "alternate": else_body}

        if p["type"] == "WHILE":
            ts.next()
            ts.expect("LPAREN")
            condition = parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            body = []
            while ts.peek()["type"] != "RBRACE":
                body.append(parse_statement())
            ts.expect("RBRACE")
            return {"type": "WhileStatement", "test": condition, "body": body}

        if p["type"] == "FOR":
            ts.next()
            ts.expect("LPAREN")
            ts.expect("VAR")
            var_name = ts.expect("ID")["value"]
            ts.accept("COLON")  # optional type annotation
            if ts.peek()["type"] == "ID":
                ts.next()  # consume type
            ts.expect("IN")
            iterable = parse_expression()
            ts.expect("RPAREN")
            ts.expect("LBRACE")
            body = []
            while ts.peek()["type"] != "RBRACE":
                body.append(parse_statement())
            ts.expect("RBRACE")
            return {"type": "ForStatement", "variable": var_name, "iterable": iterable, "body": body}

        if p["type"] == "BREAK":
            ts.next()
            ts.accept("SEMICOLON")
            return {"type": "BreakStatement"}

        if p["type"] == "CONTINUE":
            ts.next()
            ts.accept("SEMICOLON")
            return {"type": "ContinueStatement"}

        if p["type"] == "PAR":
            ts.next()
            ts.expect("LBRACE")
            body = []
            while ts.peek()["type"] != "RBRACE":
                body.append(parse_statement())
            ts.expect("RBRACE")
            return {"type": "ParallelBlock", "body": body}

        if p["type"] == "ID" and p["value"] == "print":
            # should be handled above as ID LPAREN, but keeping for safety
            pass

        if p["type"] == "SEMICOLON":
            ts.next()
            return None

        # expression statement fallback
        expr = parse_expression()
        ts.accept("SEMICOLON")
        return {"type": "ExpressionStatement", "expression": expr}

    def parse_expression():
        return parse_logical_or()

    def parse_logical_or():
        node = parse_logical_and()
        while ts.peek()["type"] == "OR":
            op = ts.next()["value"]
            right = parse_logical_and()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_logical_and():
        node = parse_equality()
        while ts.peek()["type"] == "AND":
            op = ts.next()["value"]
            right = parse_equality()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_equality():
        node = parse_relational()
        while ts.peek()["type"] in ("EQ", "NEQ"):
            op = ts.next()["value"]
            right = parse_relational()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_relational():
        node = parse_additive()
        while ts.peek()["type"] in ("LT", "LTE", "GT", "GTE"):
            op = ts.next()["value"]
            right = parse_additive()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_additive():
        node = parse_multiplicative()
        while ts.peek()["type"] == "OP" and ts.peek()["value"] in ("+", "-"):
            op = ts.next()["value"]
            right = parse_multiplicative()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_multiplicative():
        node = parse_unary()
        while ts.peek()["type"] == "OP" and ts.peek()["value"] in ("*", "/", "%"):
            op = ts.next()["value"]
            right = parse_unary()
            node = {"type": "BinaryExpression", "operator": op, "left": node, "right": right}
        return node

    def parse_unary():
        if ts.peek()["type"] == "NOT":
            op = ts.next()["value"]
            expr = parse_unary()
            return {"type": "UnaryExpression", "operator": op, "argument": expr}
        if ts.peek()["type"] == "OP" and ts.peek()["value"] in ("+", "-"):
            op = ts.next()["value"]
            expr = parse_unary()
            return {"type": "UnaryExpression", "operator": op, "argument": expr}
        return parse_primary()

    def parse_primary():
        p = ts.peek()
        if p["type"] == "NUMBER":
            return {"type": "Literal", "value": ts.next()["value"]}
        if p["type"] == "STRING":
            return {"type": "Literal", "value": ts.next()["value"]}
        if p["type"] == "TRUE":
            ts.next()
            return {"type": "Literal", "value": "true"}
        if p["type"] == "FALSE":
            ts.next()
            return {"type": "Literal", "value": "false"}
        if p["type"] == "ID":
            idt = ts.next()["value"]
            if ts.peek()["type"] == "LPAREN":
                ts.next()
                args = []
                if ts.peek()["type"] != "RPAREN":
                    while True:
                        args.append(parse_expression())
                        if ts.accept("COMMA"):
                            continue
                        break
                ts.expect("RPAREN")
                return {"type": "CallExpression", "callee": idt, "arguments": args}
            return {"type": "Identifier", "name": idt}
        if p["type"] == "PRINT":
            # parse print(...) as a call expression returning a temp
            ts.next()
            ts.expect("LPAREN")
            args = []
            if ts.peek()["type"] != "RPAREN":
                while True:
                    args.append(parse_expression())
                    if ts.accept("COMMA"):
                        continue
                    break
            ts.expect("RPAREN")
            return {"type": "CallExpression", "callee": "print", "arguments": args}
        if p["type"] == "LPAREN":
            ts.next()
            node = parse_expression()
            ts.expect("RPAREN")
            return node

        raise SyntaxError(f"Unexpected token in primary: {p}")

    return parse_program()


# ---------------------
# Semantic analysis (lightweight)
# ---------------------

def semantic_check(ast: Dict[str, Any]) -> Dict[str, Any]:
    """Perform light semantic checks: undefined vars/functions and simple scoping.

    Returns a dict with 'symbols' and a list of 'errors'. For the purposes of
    the project we keep it small but useful to detect major issues before
    generating TAC.
    """
    errors = []
    globals_sym = {"functions": {}, "variables": set()}

    # Preload builtins to avoid false 'undefined' errors
    globals_sym["functions"]["print"] = True

    # First pass: collect function names and top-level vars
    for node in ast.get("body", []):
        t = node.get("type")
        if t == "FunctionDeclaration":
            globals_sym["functions"][node["name"]] = node
        elif t == "VariableDeclaration":
            globals_sym["variables"].add(node["name"])

    # second pass: simple checks
    def check_node(node, local_vars=None):
        if local_vars is None:
            local_vars = set()

        t = node.get("type")
        if t == "VariableDeclaration":
            init = node.get("init")
            check_node(init, local_vars)
            local_vars.add(node["name"])
        elif t == "Assignment":
            check_node(node.get("value"), local_vars)
            name = node.get("name")
            if name not in local_vars and name not in globals_sym["variables"]:
                errors.append(f"Assignment to undefined variable '{name}'")
        elif t in ("ExpressionStatement",):
            check_node(node.get("expression"), local_vars)
        elif t == "Identifier":
            name = node.get("name")
            if name not in local_vars and name not in globals_sym["variables"] and name not in globals_sym["functions"]:
                errors.append(f"Use of undefined identifier '{name}'")
        elif t == "CallStatement" or t == "CallExpression":
            callee = node.get("callee")
            if callee not in globals_sym["functions"]:
                errors.append(f"Call to undefined function '{callee}'")
            for a in node.get("args", node.get("arguments", [])):
                check_node(a, local_vars)
        elif t == "FunctionDeclaration":
            # check body with params as local vars
            params = set(node.get("params", []))
            for st in node.get("body", []):
                check_node(st, local_vars=params.copy())
        elif t == "BinaryExpression":
            check_node(node.get("left"), local_vars)
            check_node(node.get("right"), local_vars)
        elif t == "ReturnStatement":
            check_node(node.get("argument"), local_vars)
        elif t == "Literal":
            pass
        else:
            # other nodes may contain nested expressions
            for k, v in node.items():
                if isinstance(v, dict) and "type" in v:
                    check_node(v, local_vars)
                elif isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict) and "type" in it:
                            check_node(it, local_vars)

    for top in ast.get("body", []):
        check_node(top)

    return {"symbols": globals_sym, "errors": errors}


# ---------------------
# TAC generation
# ---------------------

def generate_tac(ast: Dict[str, Any]) -> List[str]:
    """Generate simple TAC (list of strings) from AST.

    TAC conventions used here (simple and textual):
    - assignments:    x = y
    - temporaries:    t1 = a + b
    - calls:          call func, N  ; pushes args before call are explicit
    - return:         ret x
    - print:          print x

    The TAC is intentionally minimal but deterministic so the back-end
    translator to ARM can consume it.
    """
    out: List[str] = []
    temp_counter = 0
    label_counter = 0

    def new_temp() -> str:
        nonlocal temp_counter
        temp_counter += 1
        return f"t{temp_counter}"

    def emit(s: str):
        out.append(s)

    def expr_to_tac(expr) -> str:
        """Ensure expression value is in a variable/temporary and return its name."""
        t = expr.get("type")
        if t == "Literal":
            tmp = new_temp()
            emit(f"{tmp} = {expr['value']}")
            return tmp
        if t == "Identifier":
            return expr["name"]
        if t == "BinaryExpression":
            left = expr_to_tac(expr["left"])
            right = expr_to_tac(expr["right"])
            tmp = new_temp()
            emit(f"{tmp} = {left} {expr['operator']} {right}")
            return tmp
        if t == "CallExpression":
            args = []
            for a in expr.get("arguments", []):
                args.append(expr_to_tac(a))
            # push args in order (simple textual TAC instruction)
            for a in args:
                emit(f"param {a}")
            ret_tmp = new_temp()
            emit(f"{ret_tmp} = call {expr['callee']} , {len(args)}")
            return ret_tmp
        if t == "UnaryExpression":
            operand = expr_to_tac(expr["argument"])
            tmp = new_temp()
            emit(f"{tmp} = {expr['operator']}{operand}")
            return tmp

        # fallback
        tmp = new_temp()
        emit(f"{tmp} = 0")
        return tmp

    def gen_statement(node):
        nonlocal label_counter
        t = node.get("type")
        if t == "VariableDeclaration":
            name = node["name"]
            if node.get("init"):
                val = expr_to_tac(node["init"])
                emit(f"{name} = {val}")
            else:
                emit(f"{name} = 0")
        elif t == "Assignment":
            val = expr_to_tac(node["value"])
            emit(f"{node['name']} = {val}")
        elif t == "ExpressionStatement":
            expr_to_tac(node.get("expression"))
        elif t == "CallStatement":
            args_loc = []
            for a in node.get("args", []):
                args_loc.append(expr_to_tac(a))
            for a in args_loc:
                emit(f"param {a}")
            emit(f"call {node['callee']} , {len(args_loc)}")
            # For call statements, we don't need to store the return value
        elif t == "FunctionDeclaration":
            emit(f"func {node['name']}")
            # Emit parameter declarations for ARM register mapping
            params = node.get('params', [])
            for i, param in enumerate(params):
                if i < 4:  # First 4 params go to r0-r3
                    emit(f"{param} = r{i}    ; param {i}")
                else:
                    # Additional params come from stack
                    offset = (i - 4) * 4
                    emit(f"{param} = stack[{offset}]    ; param {i}")
            for st in node.get("body", []):
                gen_statement(st)
            emit(f"endfunc {node['name']}")
        elif t == "ReturnStatement":
            val = expr_to_tac(node.get("argument"))
            emit(f"ret {val}")
        elif t == "IfStatement":
            else_label = f"L{label_counter}"
            label_counter += 1
            end_label = f"L{label_counter}"
            label_counter += 1
            
            # Evaluate condition
            cond = expr_to_tac(node["test"])
            emit(f"if_false {cond} goto {else_label}")
            
            # Then branch
            for stmt in node.get("consequent", []):
                gen_statement(stmt)
            emit(f"goto {end_label}")
            
            # Else branch
            emit(f"{else_label}:")
            if node.get("alternate"):
                for stmt in node["alternate"]:
                    gen_statement(stmt)
            
            emit(f"{end_label}:")
            
        elif t == "WhileStatement":
            loop_start = f"L{label_counter}"
            label_counter += 1
            loop_end = f"L{label_counter}"
            label_counter += 1
            
            emit(f"{loop_start}:")
            cond = expr_to_tac(node["test"])
            emit(f"if_false {cond} goto {loop_end}")
            
            for stmt in node.get("body", []):
                gen_statement(stmt)
            
            emit(f"goto {loop_start}")
            emit(f"{loop_end}:")
            
        elif t == "ForStatement":
            loop_start = f"L{label_counter}"
            label_counter += 1
            loop_end = f"L{label_counter}"
            label_counter += 1
            
            # For now, treat as simple iteration over a range
            # This is a simplified implementation
            iterable = expr_to_tac(node["iterable"])
            var_name = node["variable"]
            emit(f"for_init {var_name} {iterable}")
            emit(f"{loop_start}:")
            emit(f"for_check {var_name} goto {loop_end}")
            
            for stmt in node.get("body", []):
                gen_statement(stmt)
            
            emit(f"for_next {var_name}")
            emit(f"goto {loop_start}")
            emit(f"{loop_end}:")
            
        elif t == "BreakStatement":
            emit("break")
            
        elif t == "ContinueStatement":
            emit("continue")
            
        elif t == "ParallelBlock":
            emit("par_start")
            for stmt in node.get("body", []):
                gen_statement(stmt)
            emit("par_end")
        else:
            # recursively handle nested shapes
            for k, v in node.items():
                if isinstance(v, dict) and "type" in v:
                    gen_statement(v)
                elif isinstance(v, list):
                    for it in v:
                        if isinstance(it, dict) and "type" in it:
                            gen_statement(it)

    for top in ast.get("body", []):
        gen_statement(top)

    return out


if __name__ == "__main__":
    src = """
    var x = 10;
    func add(a, b) { return a + b; }
    var y = add(x, 20);
    print(y);
    """
    tree = parse(src)
    print("AST:\n", tree)
    sem = semantic_check(tree)
    print("SEMANTICS:\n", sem)
    tac = generate_tac(tree)
    print("TAC:\n", "\n".join(tac))
