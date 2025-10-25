"""
LLVM IR Generator Visitor para MiniPar
Baseado na estrutura real da linguagem MiniPar
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from ..fragment import FragmentBlock, SimpleFragment


class LLVMIRGeneratorVisitorMinipar:
    """
    LLVM IR Generator Visitor para linguagem MiniPar
    Baseado na gramática e exemplos reais do MiniPar
    """
    
    def __init__(self):
        self.temp_var_counter = 0
        self.string_counter = 0
        self.strings = {}
        self.variables = {}  # Mapa de variáveis declaradas
        self.functions = {}  # Mapa de funções declaradas
    
    def get_temp_var(self):
        """Generate a temporary variable name"""
        self.temp_var_counter += 1
        return f"%temp{self.temp_var_counter}"
    
    def get_string_label(self, text):
        """Generate string constant label"""
        self.string_counter += 1
        label = f"str{self.string_counter}"
        self.strings[label] = text
        return label
    
    def visitPrograma(self, ctx):
        """Visit program node - programa principal do MiniPar"""
        program = FragmentBlock()
        
        # Add basic LLVM IR header
        program.add_text("; Generated LLVM IR for MiniPar")
        program.add_text("target triple = \"x86_64-pc-windows-msvc\"")
        program.add_text("")
        
        # Add printf declaration for print function
        program.add_text("declare i32 @printf(i8*, ...)")
        program.add_text("declare i8* @gets(i8*)")
        program.add_text("declare void @llvm.memset.p0i8.i64(i8*, i8, i64, i1)")
        program.add_text("")
        
        # Process global string constants first
        if self.strings:
            for label, text in self.strings.items():
                escaped_text = text.replace('\\', '\\\\').replace('"', '\\"')
                str_len = len(escaped_text) + 1
                program.add_text(f'@.{label} = private unnamed_addr constant [{str_len} x i8] c"{escaped_text}\\00", align 1')
            program.add_text("")
        
        # Create main function to wrap the program
        program.add_text("define i32 @main() {")
        program.add_text("entry:")
        
        # Visit all declarations and commands
        if hasattr(ctx, 'children') and ctx.children:
            for child in ctx.children:
                if hasattr(child, 'declaracao') and child.declaracao():
                    decl = self.visitDeclaracao(child.declaracao())
                    if decl:
                        for fragment in decl.fragments:
                            program.add_text(f"    {fragment.get_text()}")
                elif hasattr(child, 'comando') and child.comando():
                    cmd = self.visitComando(child.comando())
                    if cmd:
                        for fragment in cmd.fragments:
                            program.add_text(f"    {fragment.get_text()}")
        
        # Default return
        program.add_text("    ret i32 0")
        program.add_text("}")
        program.add_text("")
        
        return program
    
    def visitDeclaracao(self, ctx):
        """Visit declaracao node"""
        if hasattr(ctx, 'declaracao_variavel') and ctx.declaracao_variavel():
            return self.visitDeclaracao_variavel(ctx.declaracao_variavel())
        elif hasattr(ctx, 'declaracao_funcao') and ctx.declaracao_funcao():
            return self.visitDeclaracao_funcao(ctx.declaracao_funcao())
        return None
    
    def visitDeclaracao_variavel(self, ctx):
        """Visit variable declaration: var nome: tipo = valor"""
        decl = FragmentBlock()
        
        if not hasattr(ctx, 'ID') or not ctx.ID():
            return decl
            
        var_name = ctx.ID().getText()
        
        # Get type
        var_type = self.get_llvm_type_from_minipar_type(ctx.tipo())
        
        # Declare variable (alloca)
        decl.add_text(f"%{var_name} = alloca {var_type}")
        
        # Store variable in our map
        self.variables[var_name] = var_type
        
        # Initialize if there's an expression
        if hasattr(ctx, 'expressao') and ctx.expressao():
            # For now, simple initialization
            if hasattr(ctx.expressao(), 'getText'):
                expr_text = ctx.expressao().getText()
                if expr_text.isdigit():
                    decl.add_text(f"store {var_type} {expr_text}, {var_type}* %{var_name}")
                elif expr_text in ['true', 'false']:
                    bool_val = "1" if expr_text == 'true' else "0"
                    decl.add_text(f"store {var_type} {bool_val}, {var_type}* %{var_name}")
                else:
                    # More complex expression - placeholder
                    decl.add_text(f"; Initialize {var_name} = {expr_text}")
                    decl.add_text(f"store {var_type} 0, {var_type}* %{var_name}")
        
        return decl
    
    def visitDeclaracao_funcao(self, ctx):
        """Visit function declaration: func nome(...) -> tipo { ... }"""
        func = FragmentBlock()
        
        if not hasattr(ctx, 'ID') or not ctx.ID():
            return func
            
        func_name = ctx.ID().getText()
        
        # For now, simple function placeholder
        func.add_text(f"; Function {func_name} - placeholder")
        func.add_text(f"define i32 @{func_name}() {{")
        func.add_text("entry:")
        
        # Visit function body
        if hasattr(ctx, 'bloco') and ctx.bloco():
            body = self.visitBloco(ctx.bloco())
            if body:
                for fragment in body.fragments:
                    func.add_text(f"    {fragment.get_text()}")
        
        func.add_text("    ret i32 0")
        func.add_text("}")
        func.add_text("")
        
        return func
    
    def visitComando(self, ctx):
        """Visit comando node"""
        if hasattr(ctx, 'comando_linha') and ctx.comando_linha():
            return self.visitComando_linha(ctx.comando_linha())
        elif hasattr(ctx, 'comando_bloco') and ctx.comando_bloco():
            return self.visitComando_bloco(ctx.comando_bloco())
        elif hasattr(ctx, 'bloco_paralelo') and ctx.bloco_paralelo():
            return self.visitBloco_paralelo(ctx.bloco_paralelo())
        return None
    
    def visitComando_linha(self, ctx):
        """Visit line command"""
        cmd = FragmentBlock()
        
        # Check the type of line command
        if hasattr(ctx, 'atribuicao') and ctx.atribuicao():
            return self.visitAtribuicao(ctx.atribuicao())
        elif hasattr(ctx, 'chamada_funcao') and ctx.chamada_funcao():
            return self.visitChamada_funcao(ctx.chamada_funcao())
        else:
            cmd.add_text(f"; Line command: {ctx.getText()}")
        
        return cmd
    
    def visitChamada_funcao(self, ctx):
        """Visit function call - especialmente print()"""
        cmd = FragmentBlock()
        
        if not hasattr(ctx, 'ID') or not ctx.ID():
            return cmd
            
        func_name = ctx.ID().getText()
        
        # Handle print function specially
        if func_name == 'print':
            if hasattr(ctx, 'argumentos') and ctx.argumentos():
                # Create format string for printf
                string_label = self.get_string_label("MiniPar Output\\n")
                temp_var = self.get_temp_var()
                cmd.add_text(f"{temp_var} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([{len('MiniPar Output') + 2} x i8], [{len('MiniPar Output') + 2} x i8]* @.{string_label}, i32 0, i32 0))")
        else:
            # Other function calls
            cmd.add_text(f"; Function call: {func_name}")
        
        return cmd
    
    def visitAtribuicao(self, ctx):
        """Visit assignment: var = expr"""
        cmd = FragmentBlock()
        
        if hasattr(ctx, 'acesso_variavel') and ctx.acesso_variavel():
            var_name = ctx.acesso_variavel().getText()
            
            if hasattr(ctx, 'expressao') and ctx.expressao():
                expr_text = ctx.expressao().getText()
                
                # Get variable type
                var_type = self.variables.get(var_name, 'i32')
                
                # Simple assignment
                if expr_text.isdigit():
                    cmd.add_text(f"store {var_type} {expr_text}, {var_type}* %{var_name}")
                else:
                    cmd.add_text(f"; Assignment: {var_name} = {expr_text}")
                    cmd.add_text(f"store {var_type} 0, {var_type}* %{var_name}")
        
        return cmd
    
    def visitBloco(self, ctx):
        """Visit bloco"""
        bloco = FragmentBlock()
        
        if hasattr(ctx, 'children') and ctx.children:
            for child in ctx.children:
                if hasattr(child, 'declaracao') and child.declaracao():
                    decl = self.visitDeclaracao(child.declaracao())
                    if decl:
                        bloco.add(decl)
                elif hasattr(child, 'comando') and child.comando():
                    cmd = self.visitComando(child.comando())
                    if cmd:
                        bloco.add(cmd)
        
        return bloco
    
    def visitBloco_paralelo(self, ctx):
        """Visit par block"""
        cmd = FragmentBlock()
        cmd.add_text("; Parallel block - placeholder")
        return cmd
    
    def visitComando_bloco(self, ctx):
        """Visit block command (if, while, for)"""
        cmd = FragmentBlock()
        cmd.add_text(f"; Block command: {ctx.getText()}")
        return cmd
    
    def get_llvm_type_from_minipar_type(self, tipo_ctx):
        """Convert MiniPar type to LLVM type"""
        if not tipo_ctx:
            return 'i32'
            
        tipo_text = tipo_ctx.getText()
        type_map = {
            'number': 'double',    # MiniPar number -> LLVM double
            'bool': 'i1',          # MiniPar bool -> LLVM i1
            'string': 'i8*',       # MiniPar string -> LLVM i8*
            'list': '%list*',      # MiniPar list -> custom struct
            'dict': '%dict*',      # MiniPar dict -> custom struct
            'void': 'void',        # MiniPar void -> LLVM void
            'any': 'i8*'          # MiniPar any -> generic pointer
        }
        return type_map.get(tipo_text, 'i32')
    
    def visit_programa(self, ctx):
        """Alternative method name for compatibility"""
        return self.visitPrograma(ctx)