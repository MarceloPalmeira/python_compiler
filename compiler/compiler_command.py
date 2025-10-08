"""
Compiler Command - Python equivalent of Java CompilerCommand
"""

import sys
from pathlib import Path
from typing import Optional


class CompilerCommand:
    """Handles compilation of code to LLVM IR"""
    
    def __init__(self):
        self.show_tree = False
    
    def run(self, input_file: Optional[str] = None, output_file: Optional[str] = None, 
            show_tree: bool = False):
        """Main compilation method"""
        self.show_tree = show_tree
        
        if input_file is None:
            self._run_interactive_compiler()
        else:
            self._compile_file(input_file, output_file)
    
    def _compile_file(self, input_file: str, output_file: Optional[str] = None):
        """Compile code from a file"""
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                code = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File '{input_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file '{input_file}': {e}")
            sys.exit(1)
        
        ir_program = self._compile_code(code)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(ir_program)
                print(f"Output written to {output_file}")
            except Exception as e:
                print(f"Error writing to file '{output_file}': {e}")
                sys.exit(1)
        else:
            print(ir_program)
    
    def _run_interactive_compiler(self):
        """Run interactive compiler mode"""
        print("Interactive Compiler Mode")
        print("Enter your code (type '--stop' to compile or '--exit' to exit):")
        
        while True:
            code_lines = []
            
            while True:
                try:
                    line = input()
                except EOFError:
                    sys.exit(0)
                
                if line.strip() == '--exit':
                    sys.exit(0)
                elif line.strip() == '--stop':
                    break
                else:
                    code_lines.append(line)
            
            code = '\n'.join(code_lines).strip()
            
            if not code:
                print("No input detected. Exiting...")
                sys.exit(0)
            
            try:
                ir_program = self._compile_code(code)
                print("\n" + "="*50)
                print("LLVM IR Output:")
                print("="*50)
                print(ir_program)
                print("="*50 + "\n")
            except Exception as e:
                print(f"Compilation error: {e}")
            
            print("Enter more code (--stop to compile, --exit to exit):")
    
    def _compile_code(self, code: str) -> str:
        """Compile MiniPar code string to LLVM IR"""
        try:
            # Use simple MiniPar compiler (no ANTLR dependencies)
            from .llvm.simple_minipar_compiler import SimpleMiniparCompiler
            compiler = SimpleMiniparCompiler()
            return compiler.compile_to_ir(code)
        except Exception as e:
            raise Exception(f"MiniPar compilation failed: {e}")
    
    def _show_parse_tree(self, parser, tree):
        """Display parse tree (placeholder for GUI implementation)"""
        print("\n" + "="*30)
        print("Parse Tree (text representation):")
        print("="*30)
        print(tree.toStringTree(recog=parser))
        print("="*30 + "\n")
        input("Press Enter to continue...")


if __name__ == "__main__":
    compiler = CompilerCommand()
    compiler.run()