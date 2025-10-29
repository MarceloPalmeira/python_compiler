"""
Serviços de compilação - Gerencia cache de código e operações de compilação
"""
import hashlib
import json
import os
from datetime import datetime
from typing import Dict, Optional, List
import sys
import tempfile
import re
import importlib.util
import pathlib

class CompilerService:
    def __init__(self):
        self.cache_dir = "cache"
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        # Initialize the MiniPar compiler implementation.
        # We require a functional compiler at backend/compiler/simple_minipar_compiler.py
        # that exposes at least `parse` and `tokenize`. Fail fast if not present so
        # the project uses the single canonical compiler implementation.
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'compiler'))
        sm_path = os.path.join(base_dir, 'simple_minipar_compiler.py')
        if not os.path.exists(sm_path):
            raise RuntimeError(f"Required compiler module not found: {sm_path}")

        spec = importlib.util.spec_from_file_location('simple_minipar_compiler', sm_path)
        sm_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sm_mod)
        if not (hasattr(sm_mod, 'parse') and hasattr(sm_mod, 'tokenize') and hasattr(sm_mod, 'generate_tac')):
            raise RuntimeError("simple_minipar_compiler.py must expose parse(), tokenize() and generate_tac()")

        # Use the module object directly (functional API)
        self.minipar_compiler = sm_mod
    
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
        except Exception:
            # On error, return None so callers can handle failure uniformly.
            return None

    def compile_to_tac(self, code_id: str) -> Optional[List[str]]:
        """
        Gera código intermediário TAC a partir da AST do código MiniPar
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None

        try:
            ast = self.minipar_compiler.parse(source_code)
            # Prefer the functional compiler's TAC generator directly
            tac = self.minipar_compiler.generate_tac(ast)
            return tac
        except Exception as e:
            return [f"; Erro gerando TAC: {str(e)}"]

    def compile_tac_to_arm(self, code_id: str) -> Optional[str]:
        """
        Gera assembly ARM (compatível com CPULator) a partir do TAC gerado para o código.
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None

        try:
            # Gera AST -> TAC
            ast = self.minipar_compiler.parse(source_code)
            # Use the functional compiler's TAC generator directly
            tac = self.minipar_compiler.generate_tac(ast)

            # Load tac_to_arm (dynamic import) from the canonical file.
            # We removed the development-only fallback so the service always
            # loads `tac_to_arm.py` present in the compiler directory.
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'compiler'))
            # use the canonical functional TAC->ARM translator module
            tac2arm_path = os.path.join(base_dir, 'tac_to_arm.py')
            spec2 = importlib.util.spec_from_file_location('tac_to_arm', tac2arm_path)
            tac2arm_mod = importlib.util.module_from_spec(spec2)
            spec2.loader.exec_module(tac2arm_mod)

            # Our tac_to_arm module exposes tac_to_arm(tac: List[str]) -> str
            asm = tac2arm_mod.tac_to_arm(tac)
            return asm
        except Exception as e:
            return f"; Erro gerando ARM a partir do TAC: {str(e)}"
    
    def get_symbols_table(self, code_id: str) -> Optional[Dict]:
        """
        Gera tabela de símbolos do código MiniPar
        """
        source_code = self.get_code(code_id)
        if not source_code:
            return None
        
        try:
            # Our functional compiler provides semantic_check(ast) which
            # returns symbols and errors. Use that to produce the symbol table.
            ast = self.minipar_compiler.parse(source_code)
            sem = self.minipar_compiler.semantic_check(ast)
            return sem.get("symbols")
        except Exception:
            return None
    
# Instância global do serviço
compiler_service = CompilerService()