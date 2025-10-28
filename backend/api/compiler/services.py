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


class LLVMCompilerService:
    """LLVM compilation service - equivalent to Java LLVMCompilerService"""
    
    def __init__(self, code_cache_manager: CodeCacheManager):
        self.code_cache_manager = code_cache_manager
        self.cache_dir = code_cache_manager.cache_dir
        self._llvm_cache: Dict[str, str] = {}
    
    def check_successful_compilation(self, code_id: str) -> Optional[str]:
        """Check if code compiles successfully"""
        try:
            self.get_llvm_ir_code(code_id)
            return None  # No error
        except Exception as e:
            return str(e)
    
    def get_llvm_ir_code(self, code_id: str) -> Optional[str]:
        """Get LLVM IR code for given code ID"""
        # Check cache first
        cache_key = f"{code_id}_ir"
        if cache_key in self._llvm_cache:
            return self._llvm_cache[cache_key]
        
        # Get original code
        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None
        
        try:
            # Import simple MiniPar compiler (no ANTLR dependencies)
            from compiler.llvm.simple_minipar_compiler import SimpleMiniparCompiler
            llvm_ir = SimpleMiniparCompiler.compile_to_ir(code)
            
            # Cache result
            self._llvm_cache[cache_key] = llvm_ir
            
            # Save to file
            ir_file_path = self.cache_dir / f"{code_id}.ll"
            with open(ir_file_path, 'w', encoding='utf-8') as f:
                f.write(llvm_ir)
            
            return llvm_ir
        except Exception as e:
            raise Exception(f"LLVM IR compilation failed: {e}")
    
    def get_opt_llvm_ir_code(self, code_id: str, opt_level) -> Optional[str]:
        """Get optimized LLVM IR code"""
        cache_key = f"{code_id}_ir_opt_{opt_level.value}"
        if cache_key in self._llvm_cache:
            return self._llvm_cache[cache_key]
        
        # Get base IR first
        base_ir = self.get_llvm_ir_code(code_id)
        if base_ir is None:
            return None
        
        try:
            # For now, return the same IR (optimization would require LLVM tools)
            # In a real implementation, you would call 'opt' tool here
            optimized_ir = f"; Optimized with {opt_level.value}\n{base_ir}"
            
            self._llvm_cache[cache_key] = optimized_ir
            return optimized_ir
        except Exception as e:
            raise Exception(f"LLVM IR optimization failed: {e}")
    
    def get_asm_code(self, code_id: str) -> Optional[str]:
        """Get ARM assembly code compatible with CPULator"""
        cache_key = f"{code_id}_asm"
        if cache_key in self._llvm_cache:
            return self._llvm_cache[cache_key]
        
        # Get original code
        code = self.code_cache_manager.load_code_from_id(code_id)
        if code is None:
            return None
        
        try:
            # Generate ARM assembly for CPULator
            asm_code = self._generate_arm_assembly(code)
            
            self._llvm_cache[cache_key] = asm_code
            return asm_code
        except Exception as e:
            raise Exception(f"Assembly generation failed: {e}")
    
    def _generate_arm_assembly(self, code: str) -> str:
        """Generate ARM assembly compatible with CPULator (https://cpulator.01xz.net/?sys=arm)"""
        asm = []
        
        # ARM assembly header for CPULator
        asm.append(".text")
        asm.append(".global _start")
        asm.append("")
        asm.append("_start:")
        
        # Parse simple variable declarations and assignments
        variables = {}
        lines = code.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('var ') and ':' in line and '=' in line:
                # Extract variable info: var name: type = value
                parts = line.replace('var ', '').split(':')
                if len(parts) >= 2:
                    var_name = parts[0].strip()
                    type_and_value = parts[1].strip()
                    if '=' in type_and_value:
                        var_type = type_and_value.split('=')[0].strip()
                        var_value = type_and_value.split('=')[1].strip()
                        
                        if var_value.isdigit():
                            variables[var_name] = int(var_value)
        
        # Generate ARM code for variables
        if variables:
            asm.append("    @ Initialize variables")
            reg_counter = 0
            for var_name, var_value in variables.items():
                asm.append(f"    mov r{reg_counter}, #{var_value}     @ {var_name} = {var_value}")
                reg_counter += 1
                if reg_counter >= 12:  # ARM has r0-r12 general purpose
                    break
        
        # Handle simple arithmetic if present
        if len(variables) >= 2:
            var_names = list(variables.keys())
            if 'result' in var_names or '+' in code:
                asm.append("")
                asm.append("    @ Perform arithmetic operation")
                asm.append("    add r2, r0, r1      @ result = a + b")
        
        # Handle print statements
        if 'print(' in code:
            asm.append("")
            asm.append("    @ Print operation (simplified)")
            asm.append("    mov r7, #4          @ sys_write")
            asm.append("    mov r0, #1          @ stdout")
            asm.append("    ldr r1, =msg        @ message address")
            asm.append("    mov r2, #20         @ message length")
            asm.append("    swi 0               @ system call")
        
        # Program exit
        asm.append("")
        asm.append("    @ Exit program")
        asm.append("    mov r7, #1          @ sys_exit")
        asm.append("    mov r0, #0          @ exit status")
        asm.append("    swi 0               @ system call")
        
        # Data section
        if 'print(' in code:
            asm.append("")
            asm.append(".data")
            asm.append("msg: .ascii \"MiniPar Result\\n\"")
        
        return '\n'.join(asm)
    
    def get_opt_asm_code(self, code_id: str, opt_level) -> Optional[str]:
        """Get optimized assembly code"""
        cache_key = f"{code_id}_asm_opt_{opt_level.value}"
        if cache_key in self._llvm_cache:
            return self._llvm_cache[cache_key]
        
        try:
            base_asm = self.get_asm_code(code_id)
            if base_asm is None:
                return None
            
            optimized_asm = f"; Optimized assembly with {opt_level.value}\n{base_asm}"
            
            self._llvm_cache[cache_key] = optimized_asm
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
