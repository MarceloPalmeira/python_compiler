"""
FastAPI main application - Python equivalent of Spring Boot APIMain
"""

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from .compiler.compiler_controller import router as compiler_router

app = FastAPI(
    title="Projeto Compiladores MiniPar - API",
    description="""
    **Compilador MiniPar para LLVM IR**
    
    Esta API permite compilar código da linguagem **MiniPar** para LLVM IR e realizar várias análises.
    
    ## Linguagem MiniPar
    
    A linguagem MiniPar possui sintaxe moderna e recursos avançados:
    
    * **Tipos**: `number`, `bool`, `string`, `list`, `dict`, `void`, `any`
    * **Declarações**: `var nome: tipo = valor`
    * **Funções**: `func nome(param: tipo) -> tipo { ... }`
    * **Estruturas**: `if/else`, `while`, `for`, `par` (paralelo)
    * **Built-ins**: `print()`, `input()`, `sleep()`
    
    ## Funcionalidades
    
    * **Compilação**: Converte código MiniPar para LLVM IR
    * **Análise Sintática**: Gera árvore sintática do código
    * **Tokens**: Lista todos os tokens lexicais
    * **Símbolos**: Tabela de símbolos e escopo
    * **Complexidade**: Análise de complexidade algorítmica
    * **Otimização**: Diferentes níveis de otimização LLVM
    * **Assembly ARM**: Geração de código assembly para CPULator
    
    ## Como usar
    
    1. **Upload**: Faça POST em `/compiler/upload` com seu código MiniPar
    2. **Compile**: Use o `code_id` retornado nos outros endpoints
    3. **Explore**: Use os endpoints de análise para estudar o código
    
    ## Exemplo de código MiniPar
    
    ```minipar
    # Exemplo básico MiniPar
    var x: number = 10
    var y: number = 20
    var resultado: number = x + y
    
    print("Resultado:", resultado)
    
    func somar(a: number, b: number) -> number {
        return a + b
    }
    
    var total: number = somar(x, y)
    print("Total:", total)
    ```
    """,
    version="0.0.1",
    contact={
        "name": "Compiladores",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "compiler",
            "description": "Operações de compilação e análise de código",
        },
        {
            "name": "health",
            "description": "Verificação de saúde da API",
        }
    ]
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(compiler_router, prefix="/compiler", tags=["compiler"])

@app.get("/", tags=["health"])
async def root():
    """Root endpoint - Informações básicas da API"""
    return {
        "message": "Projeto Compiladores MiniPar - Python API",
        "version": "0.0.1",
        "language": "MiniPar",
        "docs": "/docs",
        "swagger": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json",
        "features": [
            "Compilação MiniPar para LLVM IR",
            "Análise sintática",
            "Análise lexical",
            "Tabela de símbolos",
            "Análise de complexidade",
            "Otimização LLVM",
            "Geração de assembly ARM para CPULator"
        ]
    }


@app.get("/health", tags=["health"])
async def health():
    """Health check - Verifica se a API está funcionando"""
    return {
        "status": "healthy",
        "service": "Compilador",
        "timestamp": "2025-10-06",
        "features_available": True
    }


def run_api(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Run the FastAPI application"""
    print(f"Starting API server on http://{host}:{port}")
    print("API Documentation available at http://127.0.0.1:8000/docs")
    uvicorn.run(
        "api.main:app",
        host=host,
        port=port,
        reload=reload
    )


if __name__ == "__main__":
    run_api()