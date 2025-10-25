"""
Simple LLVM IR Generator - Basic implementation for testing
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from ..fragment import FragmentBlock, SimpleFragment
from ..generated.ParserGrammarVisitor import ParserGrammarVisitor


class LLVMIRGeneratorVisitor(ParserGrammarVisitor):
    """
    Simple LLVM IR Generator Visitor
    Basic implementation for demonstration purposes
    """
    
    def __init__(self):
        super().__init__()
        self.temp_var_counter = 0
        self.string_counter = 0
        self.strings = {}
    
    def get_temp_var(self):
        """Generate a temporary variable name"""
        self.temp_var_counter += 1
        return f"%temp{self.temp_var_counter}"
    
    def visitPrograma(self, ctx):
        """Visit program node"""
        program = FragmentBlock()
        
        # Add basic LLVM IR header
        program.add_text("; Generated LLVM IR")
        program.add_text("target triple = \"x86_64-pc-windows-msvc\"")
        program.add_text("")
        
        # Add printf declaration for println
        program.add_text("declare i32 @printf(i8*, ...)")
        program.add_text("")
        
        # Visit main function if exists
        if ctx.principal():
            main_func = self.visitPrincipal(ctx.principal())
            program.add(main_func)
        
        # Visit other functions
        for func_ctx in ctx.decfuncao():
            func = self.visitDecfuncao(func_ctx)
            program.add(func)
        
        return program
    
    def visitPrincipal(self, ctx):
        """Visit main function"""
        main_func = FragmentBlock()
        
        # Main function signature
        main_func.add_text("define i32 @main() {")
        main_func.add_text("entry:")
        
        # Visit function body
        if ctx.bloco():
            body = self.visitBloco(ctx.bloco())
            # Add indentation to body
            for fragment in body.fragments:
                main_func.add_text(f"    {fragment.get_text()}")
        
        # Default return
        main_func.add_text("    ret i32 0")
        main_func.add_text("}")
        main_func.add_text("")
        
        return main_func
    
    def visitDecfuncao(self, ctx):
        """Visit function declaration"""
        func = FragmentBlock()
        
        func_name = ctx.ID().getText()
        
        # Simple function signature (placeholder)
        func.add_text(f"; Function {func_name} - placeholder")
        func.add_text(f"define i32 @{func_name}() {{")
        func.add_text("entry:")
        
        # Visit function body
        if ctx.bloco():
            body = self.visitBloco(ctx.bloco())
            for fragment in body.fragments:
                func.add_text(f"    {fragment.get_text()}")
        
        func.add_text("    ret i32 0")
        func.add_text("}")
        func.add_text("")
        
        return func
    
    def visitBloco(self, ctx):
        """Visit block"""
        block = FragmentBlock()
        
        # Variable declarations
        for decl_ctx in ctx.decvariavel():
            decl = self.visitDecvariavel(decl_ctx)
            block.add(decl)
        
        # Commands
        for cmd_ctx in ctx.comando():
            cmd = self.visitComando(cmd_ctx)
            if cmd:
                block.add(cmd)
        
        return block
    
    def visitDecvariavel(self, ctx):
        """Visit variable declaration"""
        decl = FragmentBlock()
        
        # Get type
        var_type = self.get_llvm_type_from_ctx(ctx.tipo())
        
        # Declare each variable
        for id_node in ctx.ID():
            var_name = id_node.getText()
            decl.add_text(f"%{var_name} = alloca {var_type}")
        
        return decl
    
    def visitComando(self, ctx):
        """Visit command"""
        if ctx.comando_linha():
            return self.visitComando_linha(ctx.comando_linha())
        elif ctx.comando_bloco():
            return self.visitComando_bloco(ctx.comando_bloco())
        return None
    
    def visitComando_linha(self, ctx):
        """Visit line command"""
        # Simple placeholder implementation
        cmd = FragmentBlock()
        cmd.add_text(f"; Command: {ctx.getText()}")
        return cmd
    
    def visitComando_bloco(self, ctx):
        """Visit block command"""
        # Simple placeholder implementation
        cmd = FragmentBlock()
        cmd.add_text(f"; Block command: {ctx.getText()}")
        return cmd
    
    def get_llvm_type_from_ctx(self, tipo_ctx):
        """Convert grammar type to LLVM type"""
        if tipo_ctx.tipobase():
            tipo_text = tipo_ctx.tipobase().getText()
            type_map = {
                'number': 'double',
                'bool': 'i1',
                'string': 'i8*',
                'void': 'void'
            }
            return type_map.get(tipo_text, 'i32')
        return 'i32'
    
    def visit_programa(self, ctx):
        """Alternative method name for compatibility"""
        return self.visitPrograma(ctx)