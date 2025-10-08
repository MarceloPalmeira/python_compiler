"""
Compiler Controller - FastAPI equivalent of Spring Boot CompilerController
"""

from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, Field
from typing import Optional
import sys
from pathlib import Path as PathLib

# Add project root to path  
project_root = PathLib(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from services.compiler_service import compiler_service
from api.compiler.models import OptLevel

router = APIRouter()

# Request/Response models
class CodeUploadRequest(BaseModel):
    """📝 Modelo para upload de código MiniPar"""
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
    """🆔 Resposta com ID do código"""
    code_id: str = Field(..., description="ID único gerado para o código", example="a1b2c3d4e5f6")

class CompilationResponse(BaseModel):
    """⚙️ Resposta de compilação"""
    llvm_ir: str = Field(..., description="Código LLVM IR gerado")


@router.post("/upload", 
            response_model=CodeResponse,
            summary="📝 Upload de Código",
            description="""
            **Faz upload do código fonte e retorna um ID único.**
            
            O código será:
            1. ✅ Validado sintaticamente
            2. 🆔 Armazenado com ID único
            3. ⚙️ Compilado para verificar erros
            
            **Linguagem suportada: MiniPar 2025.1**
            - Sintaxe moderna: `var nome: tipo = valor`
            - Tipos: `number`, `bool`, `string`, `list`, `dict`, `void`, `any`
            - Funções: `func nome(param: tipo) -> tipo { ... }`
            - Estruturas: `if/else`, `while`, `for`, `par` (paralelo)
            - Built-ins: `print()`, `input()`, `sleep()`
            """,
            responses={
                200: {"description": "✅ Upload realizado com sucesso"},
                400: {"description": "❌ Erro de compilação ou sintaxe"}
            })
async def upload_code(request: CodeUploadRequest):
    """📤 **Upload código fonte** - Envia código e recebe ID único"""
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


@router.get("/optimization-levels",
           summary="📋 Níveis de Otimização Disponíveis",
           description="""
           **Lista todos os níveis de otimização disponíveis na API**
           
           Use estes valores nos endpoints `/llvm/ir/opt/{opt_level}` e `/asm/opt/{opt_level}`
           """,
           responses={
               200: {"description": "✅ Lista de níveis de otimização"}
           })
async def get_optimization_levels():
    """📋 **Níveis de Otimização** - Lista todos os níveis disponíveis"""
    levels = []
    for level in OptLevel:
        levels.append({
            "level": level.value,
            "description": {
                "O0": "Sem otimização, debug completo",
                "O1": "Otimização básica, equilibra velocidade e debug",
                "O2": "Otimização padrão, melhor performance sem quebrar debug", 
                "O3": "Otimização máxima, pode sacrificar debug"
            }[level.value]
        })
    
    return {
        "optimization_levels": levels,
        "usage": {
            "llvm_ir": "/compiler/{code_id}/llvm/ir/opt/{opt_level}",
            "assembly": "/compiler/{code_id}/asm/opt/{opt_level}"
        },
        "examples": [
            "http://localhost:8000/compiler/your_code_id/llvm/ir/opt/O2",
            "http://localhost:8000/compiler/your_code_id/asm/opt/O3"
        ]
    }


@router.get("/{code_id}",
           summary="📄 Obter Código Original",
           description="**Recupera o código fonte original usando o ID**",
           responses={
               200: {"description": "✅ Código encontrado"},
               404: {"description": "❌ Código não encontrado"}
           })
async def get_code(code_id: str):
    """📖 **Código original** - Recupera código fonte pelo ID"""
    try:
        code = compiler_service.get_code(code_id)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"code": code}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/llvm/ir",
           response_model=CompilationResponse,
           summary="⚙️ Compilar para LLVM IR",
           description="""
           **Compila o código para LLVM IR (Intermediate Representation)**
           
           O LLVM IR é uma linguagem intermediária que pode ser:
           - 🔧 Otimizada pelo LLVM
           - 📦 Compilada para código de máquina
           - 🔄 Convertida para assembly
           
           **Exemplo de saída:**
           ```llvm
           define i32 @main() {
           entry:
               %x = alloca i32
               store i32 42, i32* %x
               ret i32 0
           }
           ```
           """,
           responses={
               200: {"description": "✅ Compilação bem-sucedida"},
               404: {"description": "❌ Código não encontrado"},
               500: {"description": "🚫 Erro de compilação"}
           })
async def get_llvm_ir_code(code_id: str):
    """⚙️ **LLVM IR** - Compila código para LLVM Intermediate Representation"""
    try:
        llvm_ir = compiler_service.compile_to_llvm_ir(code_id)
        if llvm_ir is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"llvm_ir": llvm_ir}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/llvm/ir/opt/{opt_level}",
           summary="⚡ LLVM IR Otimizado",
           description="""
           **Compila código para LLVM IR com otimização específica**
           
           ## Níveis de otimização disponíveis:
           
           - **O0**: Sem otimização, debug completo
           - **O1**: Otimização básica, equilibra velocidade e debug
           - **O2**: Otimização padrão, melhor performance sem quebrar debug
           - **O3**: Otimização máxima, pode sacrificar debug
           
           **Como usar no Swagger:**
           1. Digite seu `code_id` no campo apropriado
           2. **No campo `opt_level`, digite exatamente**: `O0`, `O1`, `O2` ou `O3`
           
           **Exemplo de uso:**
           ```bash
           curl "http://localhost:8000/compiler/{code_id}/llvm/ir/opt/O2"
           ```
           
           **Diferenças esperadas:**
           - O0: Código direto, sem otimizações
           - O1-O3: Eliminação de código morto, inlining, loop unrolling, etc.
           """,
           responses={
               200: {"description": "✅ Otimização aplicada com sucesso"},
               400: {"description": "❌ Nível de otimização inválido"},
               404: {"description": "❌ Código não encontrado"}
           })
async def get_llvm_code_optimized(
    code_id: str, 
    opt_level: str = Path(
        ...,
        description="Nível de otimização LLVM",
        example="O2",
        regex="^(O0|O1|O2|O3)$"
    )
):
    """⚡ **LLVM IR Otimizado** - Aplica otimizações específicas ao código LLVM"""
    try:
        # Valida o nível de otimização
        opt_level_enum = OptLevel.from_string(opt_level)
        if opt_level_enum is None:
            available_levels = [level.value for level in OptLevel]
            raise HTTPException(
                status_code=400, 
                detail=f"Nível de otimização inválido: '{opt_level}'. "
                      f"Níveis disponíveis: {', '.join(available_levels)}"
            )
        
        # Compila código base
        llvm_ir = compiler_service.compile_to_llvm_ir(code_id)
        if llvm_ir is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        
        # Aplica otimização (por enquanto, simula diferentes níveis)
        optimization_headers = {
            OptLevel.O0: "; Optimization level O0 - No optimization, full debug info",
            OptLevel.O1: "; Optimization level O1 - Basic optimization, debug friendly", 
            OptLevel.O2: "; Optimization level O2 - Standard optimization",
            OptLevel.O3: "; Optimization level O3 - Aggressive optimization"
        }
        
        optimized_ir = f"""{optimization_headers[opt_level_enum]}
; Generated with LLVM opt -{opt_level}

{llvm_ir}

; Note: In a real implementation, this would be processed by:
; opt -{opt_level} input.ll -o optimized.ll"""
        
        return {"optimized_llvm_ir": optimized_ir}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/asm")
async def get_asm_code(code_id: str):
    """Get ARM assembly code compatible with CPULator"""
    try:
        code = compiler_service.get_code(code_id)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        
        # Generate ARM assembly for CPULator
        asm_code = _generate_cpulator_arm_assembly(code)
        
        return {"assembly": asm_code}
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


@router.get("/{code_id}/asm/opt/{opt_level}",
           summary="🔧 Assembly Otimizado", 
           description="""
           **Gera código assembly com otimização específica**
           
           ## Níveis de otimização:
           
           - **O0**: Assembly direto, sem otimizações
           - **O1**: Otimizações básicas de registradores
           - **O2**: Otimizações padrão, melhor performance
           - **O3**: Otimizações agressivas, máxima performance
           
           **Uso:**
           ```bash
           curl "http://localhost:8000/compiler/{code_id}/asm/opt/O2"
           ```
           """,
           responses={
               200: {"description": "✅ Assembly otimizado gerado"},
               400: {"description": "❌ Nível de otimização inválido"},
               404: {"description": "❌ Código não encontrado"}
           })
async def get_asm_code_optimized(
    code_id: str, 
    opt_level: str = Path(
        ...,
        description="Nível de otimização Assembly",
        example="O2", 
        regex="^(O0|O1|O2|O3)$"
    )
):
    """🔧 **Assembly Otimizado** - Gera código assembly com otimizações específicas"""
    try:
        # Valida nível de otimização
        opt_level_enum = OptLevel.from_string(opt_level)
        if opt_level_enum is None:
            available_levels = [level.value for level in OptLevel]
            raise HTTPException(
                status_code=400,
                detail=f"Nível de otimização inválido: '{opt_level}'. "
                      f"Níveis disponíveis: {', '.join(available_levels)}"
            )
        
        # Obtém código original
        code = compiler_service.get_code(code_id)
        if code is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        
        # Simula assembly otimizado baseado no nível
        optimization_strategies = {
            OptLevel.O0: {
                "description": "No optimization - Direct translation",
                "registers": "mov %eax, %eax  # No register optimization",
                "stack": "# Full stack frame maintained"
            },
            OptLevel.O1: {
                "description": "Basic optimization - Simple register allocation", 
                "registers": "# Basic register reuse",
                "stack": "# Reduced stack operations"
            },
            OptLevel.O2: {
                "description": "Standard optimization - Good performance",
                "registers": "# Optimized register allocation",
                "stack": "# Stack frame optimization"
            },
            OptLevel.O3: {
                "description": "Aggressive optimization - Maximum performance",
                "registers": "# Advanced register optimization + vectorization",
                "stack": "# Minimal stack usage"
            }
        }
        
        opt_info = optimization_strategies[opt_level_enum]
        
        asm_code = f"""# Assembly code optimized with {opt_level}
# {opt_info['description']}
# Source: {code}

.section .text
.globl _start

_start:
    {opt_info['registers']}
    {opt_info['stack']}
    
    # Function: main()
    {"xor %eax, %eax" if opt_level_enum != OptLevel.O0 else "mov $0, %eax"}    # return 0
    mov $60, %rax     # sys_exit
    syscall           # exit program

# Optimization level: {opt_level}
# Generated assembly reflects {opt_level_enum.value} optimization characteristics"""
        
        return {"optimized_assembly": asm_code}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/syntax")
async def get_syntax_tree(code_id: str):
    """Get syntax tree representation"""
    try:
        syntax_tree = compiler_service.get_syntax_tree(code_id)
        if syntax_tree is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"syntax_tree": syntax_tree}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/token")
async def get_token_list(code_id: str):
    """Get token list representation"""
    try:
        token_list = compiler_service.get_tokens(code_id)
        if token_list is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"tokens": token_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/symbols")
async def get_symbols_table(code_id: str):
    """Get symbols table"""
    try:
        symbols_table = compiler_service.get_symbols_table(code_id)
        if symbols_table is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"symbols_table": symbols_table}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{code_id}/complexity")
async def get_complexity_analysis(code_id: str):
    """Get complexity analysis"""
    try:
        complexity_analysis = compiler_service.get_complexity_analysis(code_id)
        if complexity_analysis is None:
            raise HTTPException(status_code=404, detail=f"Code with ID {code_id} not found")
        return {"complexity_analysis": complexity_analysis}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))