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
    description="""Compilador MiniPar desenvolvido em Python utilizando FastAPI.""",
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
            "Compilação MiniPar para TAC (three-address code)",
            "Análise sintática",
            "Análise lexical",
            "Tabela de símbolos",
            "Análise de complexidade",
            "Otimização do TAC",
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