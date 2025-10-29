"""
Services for the compiler API - Python equivalent of Java services
"""

import hashlib
import tempfile
import os
import json
from pathlib import Path
from typing import Optional, Dict
import subprocess
import sys
import importlib.util

# Add project root to path for compiler imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))


class CodeCacheManager:
    """Manages cached code files - equivalent to Java CodeCacheManager"""
    
    def __init__(self, cache_dir: Optional[str] = None):
        self.cache_dir = Path(cache_dir) if cache_dir else Path(tempfile.gettempdir()) / "compiler_cache"
        # Ensure the cache directory exists with proper permissions
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._code_cache: Dict[str, str] = {}
        print(f"Cache directory initialized at: {self.cache_dir}")
    
    def save_code_file(self, code: str) -> str:
        """Save code and return unique ID"""
        # Generate unique ID based on code content
        code_id = hashlib.sha256(code.encode('utf-8')).hexdigest()[:16]
        
        # Ensure cache directory exists
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Cache in memory
        self._code_cache[code_id] = code
        
        # Also save to file
        file_path = self.cache_dir / f"{code_id}.txt"
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f"Code saved to: {file_path}")
        except Exception as e:
            print(f"Error saving code to file: {e}")
            # Continue with just memory cache if file save fails
        
        return code_id
    
    def load_code_from_id(self, code_id: str) -> Optional[str]:
        """Load code by ID"""
        # Try memory cache first
        if code_id in self._code_cache:
            print(f"Code loaded from memory cache: {code_id}")
            return self._code_cache[code_id]
        
        # Try file cache
        file_path = self.cache_dir / f"{code_id}.txt"
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    self._code_cache[code_id] = code
                    print(f"Code loaded from file cache: {file_path}")
                    return code
            except Exception as e:
                print(f"Error reading code file {file_path}: {e}")
        
        print(f"Code not found for ID: {code_id}")
        return None
    
    def get_file_path(self, code_id: str) -> Optional[Path]:
        """Get file path for code ID"""
        file_path = self.cache_dir / f"{code_id}.txt"
        return file_path if file_path.exists() else None


class TACCompilerService:
    """TAC/Assembly service. Produces TAC (three-address code) and ARM
    assembly via dynamic imports of the lightweight translators.
    """

    def __init__(self, code_cache_manager: CodeCacheManager):
        self.code_cache_manager = code_cache_manager
        self.cache_dir = code_cache_manager.cache_dir
        # Cache stores TAC and ASM results keyed by suffixes
        self._tac_cache: Dict[str, str] = {}

    def check_successful_compilation(self, code_id: str) -> Optional[str]:
        try:
            self.get_tac_code(code_id)
            return None
        except Exception as e:
            return str(e)

    def get_tac_code(self, code_id: str) -> Optional[str]:
        """Produce TAC for a stored code id. Returns TAC as plain text."""
        cache_key = f"{code_id}_tac"
        if cache_key in self._tac_cache:
            return self._tac_cache[cache_key]

        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None

        try:
            # Load tac_generator dynamically from backend/compiler/tac_generator.py
            tac_path = os.path.abspath(os.path.join(Path(__file__).parent.parent, 'compiler', 'tac_generator.py'))
            spec = importlib.util.spec_from_file_location('tac_generator', tac_path)
            tac_mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(tac_mod)

            # Try to interpret stored code as JSON AST; otherwise fallback to
            # an empty AST body so the generator can still run.
            try:
                possible_ast = json.loads(code)
            except Exception:
                possible_ast = {'body': []}

            tac_lines = tac_mod.generate_tac(possible_ast)
            tac_text = '\n'.join(tac_lines) if isinstance(tac_lines, list) else str(tac_lines)

            # Cache and persist
            self._tac_cache[cache_key] = tac_text
            tac_file = self.cache_dir / f"{code_id}.tac"
            with open(tac_file, 'w', encoding='utf-8') as f:
                f.write(tac_text)

            return tac_text
        except Exception as e:
            raise Exception(f"TAC generation failed: {e}")

    def get_opt_tac_code(self, code_id: str, opt_level) -> Optional[str]:
        cache_key = f"{code_id}_tac_opt_{opt_level.value}"
        if cache_key in self._tac_cache:
            return self._tac_cache[cache_key]

        base = self.get_tac_code(code_id)
        if base is None:
            return None

        try:
            optimized = f"; Optimization level {opt_level.value}\n{base}"
            self._tac_cache[cache_key] = optimized
            return optimized
        except Exception as e:
            raise Exception(f"TAC optimization failed: {e}")

    def get_asm_code(self, code_id: str) -> Optional[str]:
        """Generate ARM assembly (CPULator) from TAC via tac_to_arm translator."""
        cache_key = f"{code_id}_asm"
        if cache_key in self._tac_cache:
            return self._tac_cache[cache_key]

        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None

        try:
            # First generate TAC
            tac_text = self.get_tac_code(code_id)
            if tac_text is None:
                return None
            tac_lines = tac_text.split('\n')

            # Load tac_to_arm translator
            tac2arm_path = os.path.abspath(os.path.join(Path(__file__).parent.parent, 'compiler', 'tac_to_arm.py'))
            spec2 = importlib.util.spec_from_file_location('tac_to_arm', tac2arm_path)
            tac2arm_mod = importlib.util.module_from_spec(spec2)
            spec2.loader.exec_module(tac2arm_mod)

            asm = tac2arm_mod.tac_to_arm(tac_lines)

            self._tac_cache[cache_key] = asm
            return asm
        except Exception as e:
            raise Exception(f"Assembly generation failed: {e}")

    def get_opt_asm_code(self, code_id: str, opt_level) -> Optional[str]:
        cache_key = f"{code_id}_asm_opt_{opt_level.value}"
        if cache_key in self._tac_cache:
            return self._tac_cache[cache_key]

        try:
            base_asm = self.get_asm_code(code_id)
            if base_asm is None:
                return None

            optimized_asm = f"; Optimized assembly with {opt_level.value}\n{base_asm}"
            self._tac_cache[cache_key] = optimized_asm
            return optimized_asm
        except Exception as e:
            raise Exception(f"Optimized assembly generation failed: {e}")


class SyntaxTreeService:
    """Syntax tree service"""
    
    def __init__(self, code_cache_manager: CodeCacheManager):
        self.code_cache_manager = code_cache_manager
        self._cache: Dict[str, str] = {}
    
    def get_syntax_tree(self, code_id: str) -> Optional[str]:
        """Get syntax tree representation"""
        if code_id in self._cache:
            return self._cache[code_id]
        
        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None
        
        try:
            # Placeholder implementation
            syntax_tree = f"Syntax tree for code ID: {code_id}\n(Implementation pending - requires ANTLR parser)"
            
            self._cache[code_id] = syntax_tree
            return syntax_tree
        except Exception as e:
            raise Exception(f"Syntax tree generation failed: {e}")


class TokenListService:
    """Token list service"""
    
    def __init__(self, code_cache_manager: CodeCacheManager):
        self.code_cache_manager = code_cache_manager
        self._cache: Dict[str, str] = {}
    
    def get_token_list(self, code_id: str) -> Optional[str]:
        """Get token list representation"""
        if code_id in self._cache:
            return self._cache[code_id]
        
        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None
        
        try:
            # Placeholder implementation
            token_list = f"Token list for code ID: {code_id}\n(Implementation pending - requires ANTLR lexer)"
            
            self._cache[code_id] = token_list
            return token_list
        except Exception as e:
            raise Exception(f"Token list generation failed: {e}")


class SymbolsTableService:
    """Symbols table service"""
    
    def __init__(self, code_cache_manager: CodeCacheManager):
        self.code_cache_manager = code_cache_manager
        self._cache: Dict[str, str] = {}
    
    def get_symbols_table(self, code_id: str) -> Optional[str]:
        """Get symbols table"""
        if code_id in self._cache:
            return self._cache[code_id]
        
        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None
        
        try:
            # Placeholder implementation
            symbols_table = f"Symbols table for code ID: {code_id}\n(Implementation pending - requires semantic analysis)"
            
            self._cache[code_id] = symbols_table
            return symbols_table
        except Exception as e:
            raise Exception(f"Symbols table generation failed: {e}")
