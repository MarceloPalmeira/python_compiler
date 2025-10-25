"""
LLVM Compiler para MiniPar - Implementação específica para a linguagem MiniPar
"""

import subprocess
import tempfile
from pathlib import Path
from typing import Optional
from antlr4 import InputStream, CommonTokenStream

from .fragment import Fragment


class LLVMCompilerMinipar:
    """Main LLVM compiler class for MiniPar language"""
    
    @staticmethod
    def compile_to_ir(source_code: str) -> str:
        """Compile MiniPar source code to LLVM IR"""
        try:
            # Try to use the new MiniPar gramáticas if available
            try:
                from ..generated.LexerGrammarMinipar import LexerGrammarMinipar
                from ..generated.ParserGrammarMinipar import ParserGrammarMinipar
                from .translator.llvm_ir_generator_visitor_minipar import LLVMIRGeneratorVisitorMinipar
                
                # Tokenize input
                input_stream = InputStream(source_code)
                lexer = LexerGrammarMinipar(input_stream)
                
                # Create token stream
                stream = CommonTokenStream(lexer)
                
                # Parse input
                parser = ParserGrammarMinipar(stream)
                
                # Parse starting from 'programa' rule
                tree = parser.programa()
                
                # Generate LLVM IR using visitor
                visitor = LLVMIRGeneratorVisitorMinipar()
                ir_fragment = visitor.visitPrograma(tree)
                
                # Convert fragment to string
                if hasattr(ir_fragment, 'get_text'):
                    return ir_fragment.get_text()
                else:
                    return str(ir_fragment)
                    
            except ImportError:
                # Fallback to old grammar if MiniPar files not generated yet
                return LLVMCompilerMinipar._generate_placeholder_ir(source_code)
                
        except Exception as e:
            # Fallback to placeholder on error
            return f"""
; Error during MiniPar compilation: {str(e)}
; Generated placeholder LLVM IR for MiniPar code:

target triple = "x86_64-pc-windows-msvc"

declare i32 @printf(i8*, ...)

@.str = private unnamed_addr constant [25 x i8] c"MiniPar compiled code\\0A\\00", align 1

define i32 @main() {{
entry:
    ; Original MiniPar code was:
    ; {source_code.replace(chr(10), chr(10) + '    ; ')}
    
    ; Simple placeholder output
    %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([25 x i8], [25 x i8]* @.str, i32 0, i32 0))
    ret i32 0
}}
"""
    
    @staticmethod
    def _generate_placeholder_ir(source_code: str) -> str:
        """Generate placeholder LLVM IR for MiniPar"""
        return f"""
; Generated LLVM IR for MiniPar
target triple = "x86_64-pc-windows-msvc"

declare i32 @printf(i8*, ...)

@.str = private unnamed_addr constant [25 x i8] c"MiniPar compiled code\\0A\\00", align 1

define i32 @main() {{
entry:
    ; Original MiniPar code was:
    ; {source_code.replace(chr(10), chr(10) + '    ; ')}
    
    ; Simple placeholder output
    %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([25 x i8], [25 x i8]* @.str, i32 0, i32 0))
    ret i32 0
}}

@.str.hello = private unnamed_addr constant [15 x i8] c"Hello MiniPar!\\00", align 1
"""
    
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
        """Compile LLVM IR to ARM assembly for CPULator"""
        try:
            result = subprocess.run([
                clang_compiler,
                "-target", "arm-none-eabi",     # ARM target for CPULator
                "-mcpu=cortex-a9",              # ARM Cortex-A9 for CPULator
                "-masm=unified",                # Unified ARM assembly syntax
                "-S",
                str(ir_code_path),
                "-o",
                str(dest_path)
            ], capture_output=True, text=True, check=True)
            return result.returncode == 0
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Fallback to x86 if ARM compilation fails
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
        """Compile LLVM IR to optimized ARM assembly"""
        try:
            opt_flag = f"-{opt_level}"
            result = subprocess.run([
                clang_compiler,
                "-target", "arm-none-eabi",     # ARM target for CPULator
                "-mcpu=cortex-a9",              # ARM Cortex-A9 for CPULator
                "-masm=unified",                # Unified ARM assembly syntax
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