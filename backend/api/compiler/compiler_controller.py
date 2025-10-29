"""
Compiler Controller - FastAPI equivalent of Spring Boot CompilerController
"""

from fastapi import APIRouter, HTTPException, Path, Response
from pydantic import BaseModel, Field
from typing import Optional
import sys
from pathlib import Path as PathLib

# Add project root to path  
project_root = PathLib(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from services.compiler_service import compiler_service

router = APIRouter()

# Request/Response models
class CodeUploadRequest(BaseModel):
    """Modelo para upload de código MiniPar"""
    code: str = Field(
        ..., 
        description="Código fonte MiniPar para compilar",
        example="""# Exemplo MiniPar
var x: number = 10
var y: number = 20
var resultado: number = x + y

print("Resultado:", resultado)

func somar(a: number, b: number) -> number {
    return a + b
}

var total: number = somar(x, y)
print("Total:", total)"""
    )

class CodeResponse(BaseModel):
    """Resposta com ID do código"""
    code_id: str = Field(..., description="ID único gerado para o código", example="a1b2c3d4e5f6")

class CompilationResponse(BaseModel):
    """Resposta de compilação (TAC)"""
    tac: str = Field(..., description="Código TAC gerado")


@router.post("/upload", 
            response_model=CodeResponse,
            summary="Upload de Código",
            description="""
            **Faz upload do código fonte e retorna um ID único.**
            
            O código será:
            1. Validado sintaticamente
            2. Armazenado com ID único
            3. Compilado para verificar erros
            
            **Linguagem suportada: MiniPar 2025.1**
            - Sintaxe moderna: `var nome: tipo = valor`
            - Tipos: `number`, `bool`, `string`, `list`, `dict`, `void`, `any`
            - Funções: `func nome(param: tipo) -> tipo { ... }`
            - Estruturas: `if/else`, `while`, `for`, `par` (paralelo)
            - Built-ins: `print()`, `input()`, `sleep()`
            """,
            responses={
                200: {"description": "Upload realizado com sucesso"},
                400: {"description": "Erro de compilação ou sintaxe"}
            })
async def upload_code(request: CodeUploadRequest):
    """Upload código fonte - Envia código e recebe ID único"""
    try:
        code_trimmed = request.code.strip()
        print(f"Received code upload request: {len(code_trimmed)} characters")
        
        # Save code and get ID
        code_id = compiler_service.upload_code(code_trimmed)
        print(f"Generated code ID: {code_id}")
        
        return CodeResponse(code_id=code_id)
    except Exception as e:
        print(f"Error in upload_code: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@router.get("/{code_id}",
           summary="Obter Código Original",
           description="**Retorna apenas o código fonte original - copy/paste direto**",
           responses={
               200: {"description": "Código fonte puro"},
               404: {"description": "Código não encontrado"}
           })
async def get_code(code_id: str):
    """📖 **Código original** - Recupera código fonte pelo ID"""
    try:
        code = compiler_service.get_code(code_id)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return Response(content=code, media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





@router.get("/{code_id}/asm",
           summary="Código Assembly ARM",
           description="""
           **Gera código assembly ARM compatível com CPULator**
           
           **Retorna apenas o código assembly puro para copy/paste direto no CPULator**
           """,
           responses={
               200: {"description": "Código assembly ARM puro"},
               404: {"description": "Código não encontrado"}
           })
async def get_asm_code(code_id: str):
    """Get ARM assembly code compatible with CPULator"""
    try:
        # Prefer TAC->ARM pipeline
        asm_code = compiler_service.compile_tac_to_arm(code_id)
        if asm_code is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")

        return Response(content=asm_code,
                        media_type="text/plain",
                        headers={"Content-Disposition": 'attachment; filename="program.s"'})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def _generate_cpulator_arm_assembly(code: str) -> str:
    """Generate ARM assembly for CPULator (https://cpulator.01xz.net/?sys=arm)"""
    asm = []
    
    # ARM assembly header for CPULator
    asm.append(".text")
    asm.append(".global _start")
    asm.append("")
    asm.append("_start:")
    
    # Parse variables and operations
    variables = {}
    operations = []
    lines = code.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('var ') and ':' in line and '=' in line:
            # Extract variable: var name: type = value
            parts = line.replace('var ', '').split(':')
            if len(parts) >= 2:
                var_name = parts[0].strip()
                type_and_value = parts[1].strip()
                if '=' in type_and_value:
                    var_type = type_and_value.split('=')[0].strip()
                    var_value = type_and_value.split('=')[1].strip()
                    
                    # Handle numeric values
                    if var_value.replace('-', '').isdigit():
                        variables[var_name] = int(var_value)
                    # Handle expressions like "a + b"
                    elif '+' in var_value or '-' in var_value or '*' in var_value:
                        operations.append((var_name, var_value))
        elif line.startswith('print('):
            operations.append(('print', line))
    
    # Generate ARM code
    if variables:
        asm.append("    @ Initialize variables")
        reg_map = {}
        reg_counter = 0
        
        for var_name, var_value in variables.items():
            if reg_counter < 12:  # r0-r11
                asm.append(f"    mov r{reg_counter}, #{var_value}     @ {var_name} = {var_value}")
                reg_map[var_name] = f"r{reg_counter}"
                reg_counter += 1
    
    # Handle operations
    if operations:
        asm.append("")
        asm.append("    @ Process operations")
        
        for op_target, op_expr in operations:
            if op_target == 'print':
                asm.append("    @ Print operation")
                asm.append("    mov r7, #4          @ sys_write system call")
                asm.append("    mov r0, #1          @ file descriptor (stdout)")
                asm.append("    ldr r1, =output_msg @ message address")
                asm.append("    mov r2, #15         @ message length")
                asm.append("    swi 0               @ software interrupt")
            elif '+' in op_expr:
                # Handle addition: result = a + b
                parts = op_expr.split('+')
                if len(parts) == 2:
                    var1 = parts[0].strip()
                    var2 = parts[1].strip()
                    asm.append(f"    add r{reg_counter}, r0, r1  @ {op_target} = {var1} + {var2}")
                    reg_counter += 1
    
    # Program termination
    asm.append("")
    asm.append("    @ Exit program")
    asm.append("    mov r7, #1          @ sys_exit system call")
    asm.append("    mov r0, #0          @ exit status")
    asm.append("    swi 0               @ software interrupt")
    
    # Data section for print messages
    if any('print' in str(op) for op in operations):
        asm.append("")
        asm.append(".data")
        asm.append("output_msg: .ascii \"MiniPar Output\\n\"")
    
    return '\n'.join(asm)



@router.get("/{code_id}/syntax",
           summary="Árvore Sintática",
           description="**Retorna apenas a árvore sintática - copy/paste direto**",
           responses={
               200: {"description": "Árvore sintática pura"},
               404: {"description": "Código não encontrado"}
           })
async def get_syntax_tree(code_id: str):
    """Get syntax tree representation"""
    try:
        syntax_tree = compiler_service.get_syntax_tree(code_id)
        if syntax_tree is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return Response(content=str(syntax_tree), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/tac",
           summary="Código Intermediário (TAC)",
           description="""
           Retorna o código intermediário em Three-Address Code (TAC) gerado a partir da AST.
           Útil para inspeção, otimizações e como passo intermediário na pipeline de compilação.
           """,
           responses={
               200: {"description": "Código TAC puro"},
               404: {"description": "Código não encontrado"},
               500: {"description": "Erro ao gerar TAC"}
           })
async def get_tac_code(code_id: str):
    """Retorna TAC (three-address code) gerado pelo backend"""
    try:
        tac = compiler_service.compile_to_tac(code_id)
        if tac is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")

        # tac é uma lista de instruções (strings) — retornamos como texto puro
        tac_text = "\n".join(tac)
        return Response(content=tac_text, media_type="text/plain")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/token",
           summary="Lista de Tokens",
           description="**Retorna apenas a lista de tokens - copy/paste direto**",
           responses={
               200: {"description": "Lista de tokens pura"},
               404: {"description": "Código não encontrado"}
           })
async def get_token_list(code_id: str):
    """Get token list representation"""
    try:
        token_list = compiler_service.get_tokens(code_id)
        if token_list is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return Response(content=str(token_list), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/symbols",
           summary="Tabela de Símbolos",
           description="**Retorna apenas a tabela de símbolos - copy/paste direto**",
           responses={
               200: {"description": "Tabela de símbolos pura"},
               404: {"description": "Código não encontrado"}
           })
async def get_symbols_table(code_id: str):
    """Get symbols table"""
    try:
        symbols_table = compiler_service.get_symbols_table(code_id)
        if symbols_table is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return Response(content=str(symbols_table), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
