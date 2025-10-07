"""
Serviços de compilação - Gerencia cache de código e operações de compilação
"""
import hashlib
import json
import os
from datetime import datetime
from typing import Dict, Optional

class CompilerService:
    def __init__(self):
        self.cache_dir = "cache"
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
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
        Compila código para LLVM IR
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        # Por enquanto, retorna um LLVM IR simples como placeholder
        llvm_ir = f"""
; ModuleID = 'compiled_code_{code_id}'
source_filename = "input.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Código fonte original:
; {source_code}

; Função principal
define dso_local i32 @main() #0 {{
entry:
  %retval = alloca i32, align 4
  store i32 0, i32* %retval, align 4
  ret i32 0
}}

attributes #0 = {{ noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="all" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }}

!llvm.module.flags = !{{!0, !1, !2}}
!llvm.ident = !{{!3}}

!0 = !{{i32 1, !"wchar_size", i32 4}}
!1 = !{{i32 7, !"PIC Level", i32 2}}
!2 = !{{i32 7, !"PIE Level", i32 2}}
!3 = !{{!"clang version 11.0.0"}}
"""
        return llvm_ir.strip()
    
    def get_syntax_tree(self, code_id: str) -> Optional[Dict]:
        """
        Gera árvore sintática do código
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        # Placeholder para árvore sintática
        return {
            "type": "Program",
            "children": [
                {
                    "type": "FunctionDeclaration",
                    "name": "main",
                    "returnType": "int",
                    "parameters": [],
                    "body": {
                        "type": "Block",
                        "statements": [
                            {
                                "type": "ReturnStatement",
                                "value": {
                                    "type": "IntegerLiteral",
                                    "value": 0
                                }
                            }
                        ]
                    }
                }
            ]
        }
    
    def get_tokens(self, code_id: str) -> Optional[list]:
        """
        Gera lista de tokens do código
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        # Placeholder para tokenização simples
        tokens = []
        words = source_code.split()
        
        for i, word in enumerate(words):
            if word in ['int', 'float', 'char', 'void']:
                tokens.append({
                    "type": "TYPE",
                    "value": word,
                    "line": 1,
                    "column": i * 5
                })
            elif word in ['if', 'else', 'while', 'for', 'return']:
                tokens.append({
                    "type": "KEYWORD",
                    "value": word,
                    "line": 1,
                    "column": i * 5
                })
            elif word.isdigit():
                tokens.append({
                    "type": "NUMBER",
                    "value": word,
                    "line": 1,
                    "column": i * 5
                })
            else:
                tokens.append({
                    "type": "IDENTIFIER",
                    "value": word,
                    "line": 1,
                    "column": i * 5
                })
        
        return tokens
    
    def get_symbols_table(self, code_id: str) -> Optional[Dict]:
        """
        Gera tabela de símbolos
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        # Placeholder para tabela de símbolos
        return {
            "global_scope": {
                "functions": [
                    {
                        "name": "main",
                        "type": "function",
                        "return_type": "int",
                        "parameters": [],
                        "line": 1
                    }
                ],
                "variables": []
            },
            "function_scopes": {
                "main": {
                    "variables": [],
                    "parameters": []
                }
            }
        }
    
    def get_complexity_analysis(self, code_id: str) -> Optional[Dict]:
        """
        Gera análise de complexidade
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        # Placeholder para análise de complexidade
        return {
            "time_complexity": "O(1)",
            "space_complexity": "O(1)",
            "analysis": {
                "loops": 0,
                "recursive_calls": 0,
                "function_calls": 0,
                "conditional_statements": 0
            },
            "details": "Programa simples com função main que retorna constante."
        }

# Instância global do serviço
compiler_service = CompilerService()