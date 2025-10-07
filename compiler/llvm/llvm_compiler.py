"""
LLVM Compiler - Python equivalent of Java LLVMCompiler
"""

import subprocess
import tempfile
from pathlib import Path
from typing import Optional
from antlr4 import InputStream, CommonTokenStream

from .fragment import Fragment
from ..generated.LexerGrammar import LexerGrammar
from ..generated.ParserGrammar import ParserGrammar
from .translator.llvm_ir_generator_visitor import LLVMIRGeneratorVisitor
from .translator.errors.syntax_error_listener import SyntaxErrorListener


class LLVMCompiler:
    """Main LLVM compiler class"""
    
    @staticmethod
    def compile_to_ir(source_code: str) -> str:
        """Compile source code to LLVM IR"""
        # For now, return a simple placeholder LLVM IR
        # TODO: Implement full ANTLR parsing when ready
        
        placeholder_ir = f"""
; Generated LLVM IR for code
target triple = "x86_64-pc-windows-msvc"

declare i32 @printf(i8*, ...)

@.str = private unnamed_addr constant [20 x i8] c"Compiled code: %s\\0A\\00", align 1

define i32 @main() {{
entry:
    ; Original code was:
    ; {source_code.replace(chr(10), chr(10) + '    ; ')}
    
    ; Simple placeholder output
    %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.str, i32 0, i32 0), i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.str.hello, i32 0, i32 0))
    ret i32 0
}}

@.str.hello = private unnamed_addr constant [12 x i8] c"Hello World\\00", align 1
"""
        
        return placeholder_ir.strip()
    
    @staticmethod
    def optimize_ir(llvm_optimizer: str, ir_code_path: Path, dest_path: Path, 
                   opt_level: str) -> bool:
        """Optimize LLVM IR using opt tool"""
        try:
            opt_flag = f"-{opt_level}"
            result = subprocess.run([
                llvm_optimizer,
                opt_flag,
                "-S",
                str(ir_code_path),
                "-o",
                str(dest_path)
            ], capture_output=True, text=True, check=True)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    @staticmethod
    def compile_to_asm(clang_compiler: str, ir_code_path: Path, 
                      dest_path: Path) -> bool:
        """Compile LLVM IR to assembly"""
        try:
            result = subprocess.run([
                clang_compiler,
                "-masm=intel",
                "-S",
                str(ir_code_path),
                "-o",
                str(dest_path)
            ], capture_output=True, text=True, check=True)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    @staticmethod
    def optimize_asm(clang_compiler: str, ir_code_path: Path, dest_path: Path,
                    opt_level: str) -> bool:
        """Compile LLVM IR to optimized assembly"""
        try:
            opt_flag = f"-{opt_level}"
            result = subprocess.run([
                clang_compiler,
                "-masm=intel",
                "-S",
                opt_flag,
                str(ir_code_path),
                "-o",
                str(dest_path)
            ], capture_output=True, text=True, check=True)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    @staticmethod
    def compile_to_executable(clang_compiler: str, ir_code_path: Path,
                            dest_path: Path) -> bool:
        """Compile LLVM IR to executable"""
        try:
            result = subprocess.run([
                clang_compiler,
                str(ir_code_path),
                "-o",
                str(dest_path)
            ], capture_output=True, text=True, check=True)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False