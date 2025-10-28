"""
Serviços de compilação - Gerencia cache de código e operações de compilação
"""
import hashlib
import json
import os
from datetime import datetime
from typing import Dict, Optional
import sys
import tempfile

# Adiciona o diretório do compilador ao path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'compiler', 'llvm'))
from simple_minipar_compiler import SimpleMiniparCompiler

class CompilerService:
    def __init__(self):
        self.cache_dir = "cache"
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        # Inicializa o compilador MiniPar
        self.minipar_compiler = SimpleMiniparCompiler()
    
    def upload_code(self, source_code: str) -> str:
        """
        Armazena código fonte e retorna um ID único
        """
        # Gera ID único baseado no hash do código + timestamp
        timestamp = str(int(datetime.now().timestamp()))
        content = f"{source_code}_{timestamp}"
        code_id = hashlib.md5(content.encode()).hexdigest()[:16]
        
        # Salva o código no cache
        cache_data = {
            "source_code": source_code,
            "timestamp": timestamp,
            "code_id": code_id
        }
        
        cache_file = os.path.join(self.cache_dir, f"{code_id}.json")
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
        
        return code_id
    
    def get_code(self, code_id: str) -> Optional[str]:
        """
        Recupera código fonte pelo ID
        """
        cache_file = os.path.join(self.cache_dir, f"{code_id}.json")
        if not os.path.exists(cache_file):
            return None
        
        with open(cache_file, 'r', encoding='utf-8') as f:
            cache_data = json.load(f)
        
        return cache_data.get("source_code")
    
    def compile_to_llvm_ir(self, code_id: str) -> Optional[str]:
        """
        Compila código MiniPar para LLVM IR usando SimpleMiniparCompiler
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        try:
            # Usa o compilador MiniPar para gerar LLVM IR
            llvm_ir = self.minipar_compiler.compile_to_ir(source_code)
            return llvm_ir
        except Exception as e:
            # Em caso de erro, retorna um IR básico com comentário do erro
            return f"""; Erro na compilação: {str(e)}
; Código fonte:
; {source_code}

define i32 @main() {{
entry:
    ret i32 1
}}
"""
    
    def get_syntax_tree(self, code_id: str) -> Optional[Dict]:
        """
        Gera árvore sintática do código MiniPar
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        try:
            # Usa o compilador MiniPar para gerar AST
            ast = self.minipar_compiler.parse(source_code)
            return ast
        except Exception as e:
            # Retorna informações de erro
            return {
                "error": f"Erro na análise sintática: {str(e)}",
                "source_code": source_code
            }
    
    def get_tokens(self, code_id: str) -> Optional[list]:
        """
        Gera lista de tokens do código MiniPar
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        try:
            # Usa o compilador MiniPar para tokenizar
            tokens = self.minipar_compiler.tokenize(source_code)
            return tokens
        except Exception as e:
            # Retorna tokenização básica em caso de erro
            lines = source_code.split('\n')
            tokens = []
            
            for line_num, line in enumerate(lines, 1):
                words = line.strip().split()
                col = 0
                
                for word in words:
                    if word in ['var', 'func', 'print', 'if', 'else', 'while', 'for', 'return']:
                        tokens.append({
                            "type": "KEYWORD",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    elif word in ['number', 'string', 'bool']:
                        tokens.append({
                            "type": "TYPE",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    elif word.replace('.', '').isdigit():
                        tokens.append({
                            "type": "NUMBER",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    elif word.startswith('"') and word.endswith('"'):
                        tokens.append({
                            "type": "STRING",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    elif word in ['=', '+', '-', '*', '/', '(', ')', '{', '}', ':', ',']:
                        tokens.append({
                            "type": "OPERATOR",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    else:
                        tokens.append({
                            "type": "IDENTIFIER",
                            "value": word,
                            "line": line_num,
                            "column": col
                        })
                    col += len(word) + 1
            
            return tokens
    
    def get_symbols_table(self, code_id: str) -> Optional[Dict]:
        """
        Gera tabela de símbolos do código MiniPar
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        try:
            # Usa o compilador MiniPar para gerar tabela de símbolos
            symbols = self.minipar_compiler.get_symbols_table(source_code)
            return symbols
        except Exception as e:
            # Análise básica em caso de erro
            symbols = {
                "variables": [],
                "functions": [],
                "error": str(e)
            }
            
            # Busca por declarações de variáveis
            lines = source_code.split('\n')
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if line.startswith('var '):
                    parts = line.split()
                    if len(parts) >= 4:
                        var_name = parts[1].rstrip(':')
                        var_type = parts[2]
                        symbols["variables"].append({
                            "name": var_name,
                            "type": var_type,
                            "line": line_num,
                            "scope": "global"
                        })
                elif line.startswith('func '):
                    func_name = line.split('(')[0].replace('func ', '').strip()
                    symbols["functions"].append({
                        "name": func_name,
                        "line": line_num,
                        "scope": "global"
                    })
            
            return symbols
    
# Instância global do serviço
compiler_service = CompilerService()