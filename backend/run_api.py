#!/usr/bin/env python3
"""
API Launcher - Inicia a API FastAPI diretamente
"""

import sys
import uvicorn
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

if __name__ == "__main__":
    print("Iniciando API do Compilador ...")
    print("📖 Documentação Swagger: http://127.0.0.1:8000/docs")
    print("ReDoc: http://127.0.0.1:8000/redoc")
    print("OpenAPI JSON: http://127.0.0.1:8000/openapi.json")
    print("Para parar: Ctrl+C")
    print("-" * 50)
    
    uvicorn.run(
        "api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        access_log=True
    )