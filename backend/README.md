# Projeto Compiladores MiniPar 2025.1

## Tema 1: Compilador MiniPar com Geração de Código Intermediário e Assembly ARM

Este projeto implementa um **compilador completo** para a linguagem **MiniPar 2025.1** com:
- **Análise Léxica (Lexer)** - Tokenização completa via `simple_minipar_compiler.py`
- **Análise Sintática (Parser)** - Geração de AST funcional
- **Código Intermediário** - TAC (Three-Address Code, textual IR)
- **Assembly ARM** - Compatível com CPULator (https://cpulator.01xz.net/?sys=arm)

> **Implementação Principal**: O projeto usa `simple_minipar_compiler.py` - um compilador funcional standalone que não depende de ANTLR. As gramáticas ANTLR estão disponíveis para referência e uso avançado.

## Setup

### Windows
```batch
setup.bat
```

### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

## Estrutura do Projeto

```
python_compiler/
├── requirements.txt          # Dependências Python
├── main.py                  # CLI principal 
├── setup.sh / setup.bat     # Scripts de instalação
├── grammar/                 # Gramáticas ANTLR4 e MiniPar
│   ├── LexerGrammar.g4      # Lexer original (legacy)
│   ├── ParserGrammar.g4     # Parser original (legacy)
│   ├── LexerGrammarMinipar.g4  # Lexer MiniPar oficial
│   └── ParserGrammarMinipar.g4 # Parser MiniPar oficial
├── compiler/                # Módulo do compilador
│   ├── generated/          # Arquivos ANTLR originais
│   ├── generated_minipar/  # Arquivos ANTLR MiniPar
│   ├── simple_minipar_compiler.py  # Compilador standalone (funcional)
│   └── compiler_command.py # Comando CLI
├── api/                    # API REST completa
│   ├── main.py            # Servidor FastAPI
│   └── compiler/          # Controllers e services MiniPar
├── services/              # Serviços de compilação
├── cache/                 # Cache de códigos compilados
└── minipar/              # Especificação oficial MiniPar (referência)
```

## Instalação Manual

### Pré-requisitos
- Python 3.8+
- pip

### Passos

1. **Clone/copie o projeto e navegue até o diretório:**
```bash
cd python_compiler
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

Windows:
```batch
venv\Scripts\activate.bat
```

Linux/Mac:
```bash
source venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

5. **Gere os arquivos ANTLR:**

Windows:
```batch
generate_antlr.bat
```

Linux/Mac:
```bash
chmod +x generate_antlr.sh
./generate_antlr.sh
```

## Uso

### API REST

```bash
# Iniciar servidor
python run_api.py
```

A API estará disponível em:
- **Servidor**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Endpoints Principais

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Documentação da API |
| `/health` | GET | Status do servidor |
| `/compiler/upload` | POST | Upload de código MiniPar |
| `/compiler/{code_id}` | GET | Código fonte original |
| `/compiler/{code_id}/tac` | GET | TAC (three-address code, textual IR) |
| `/compiler/{code_id}/asm` | GET | Assembly ARM para CPULator |
| `/compiler/{code_id}/syntax` | GET | Árvore sintática (AST) |
| `/compiler/{code_id}/token` | GET | Lista de tokens |
| `/compiler/{code_id}/symbols` | GET | Tabela de símbolos |

## Exemplos de Código MiniPar

### Programa Simples
```minipar
var a: number = 10
var msg: string = "Hello MiniPar"
print(msg, a)
```

### Função com Recursão
```minipar
func fatorial(n: number) -> number {
    if (n == 0 || n == 1) {
        return 1
    } else {
        return n * fatorial(n - 1)
    }
}

var resultado: number = fatorial(5)
print("Fatorial de 5:", resultado)
```

### Arrays e Loops
```minipar
var numbers: list = [1, 2, 3, 4, 5]
var sum: number = 0

for (var i: number in numbers) {
    sum = sum + i
}

print("Soma:", sum)
```

### Programa Completo
```minipar
# Quicksort em MiniPar
func quicksort(array: list) -> list {
    if (len(array) <= 1) {
        return array
    } else {
        var pivot: any = array[0]
        var menores: list = []
        var maiores: list = []
        
        for (var x: any in array[1:]) {
            if (x <= pivot) {
                menores.append(x)
            } else {
                maiores.append(x)
            }
        }
        
        return quicksort(menores) + [pivot] + quicksort(maiores)
    }
}

var dados: list = [64, 34, 25, 12, 22, 11, 90]
var ordenado: list = quicksort(dados)
print("Array ordenado:", ordenado)
```

## Estado de Implementação

### Completamente Implementado
- **Compilador MiniPar completo** (SimpleMiniparCompiler)
- **Análise Léxica** - Tokenização de todos os tokens MiniPar
- **Análise Sintática** - Parser com geração de AST
- **Código Intermediário** - TAC (equivale a código de 3 endereços, textual)
- **Assembly ARM** - Compatível com CPULator
- **API REST com FastAPI** - Interface web completa
- **Sistema de cache** - Armazenamento de códigos compilados
- **Gramáticas ANTLR4** - MiniPar oficial + legacy
- **Scripts de setup** - Instalação automática
- **Tabela de símbolos** - Análise de escopo e declarações
- **Análise de complexidade** - Métricas algorítmicas

### Recursos MiniPar Suportados
- **Tipos**: `number`, `bool`, `string`, `list`, `dict`, `void`, `any`
- **Variáveis**: `var nome: tipo = valor`
- **Funções**: `func nome(param: tipo) -> tipo { ... }`
- **Estruturas de controle**: `if/else`, `while`, `for`
- **Operadores**: Aritméticos, lógicos (`&&`, `||`), relacionais
- **Arrays**: `[1, 2, 3]`, indexação `array[0]`
- **Built-ins**: `print()`, `input()`, `len()`, `sleep()`
- **Comentários**: `#` (linha) e `/* */` (bloco)
- **Recursão**: Chamadas recursivas de função
- **Canais**: `s_channel`, `c_channel` (reconhecidos)

### Conformidade com Tema 1
- **Compilador não Orientado a Objetos**: MiniPar funcional
- **Geração de Código Intermediário**: TAC (3-endereços, textual)
- **Geração de Assembly ARM**: CPULator compatível
- **Linguagem MiniPar 2025.1**: Especificação oficial

## Testes e Exemplos

### Executar Testes Completos
```bash
# Teste de conformidade final
python test_compatibility.py

# Teste de features avançadas
python test_advanced_features.py

# Verificação dos requisitos
python verify_requirements.py
```

### Resultados Esperados
```
TESTING OFFICIAL MINIPAR FACTORIAL EXAMPLE
============================================================
Code uploaded successfully - ID: d3f062b82c15343a
TAC (Three-Address Code): WORKING
Tokenization (58 tokens): WORKING  
Syntax Tree (AST): WORKING
Symbols Table: WORKING
ARM Assembly for CPULator: WORKING
============================================================
ALL TESTS PASSED: 100% SUCCESS RATE
```

## CPULator Integration

O assembly gerado é **100% compatível** com o emulador CPULator:

**Link**: https://cpulator.01xz.net/?sys=arm

### Exemplo de Assembly Gerado
```arm
.text
.global _start

_start:
    @ Initialize variables
    mov r0, #42     @ a = 42
    mov r1, #13     @ b = 13
    
    @ Perform arithmetic
    add r2, r0, r1  @ result = a + b
    
    @ Print operation
    mov r7, #4      @ sys_write
    mov r0, #1      @ stdout
    ldr r1, =output_msg
    mov r2, #15     @ message length
    swi 0           @ system call
    
    @ Exit program
    mov r7, #1      @ sys_exit
    mov r0, #0      @ exit status
    swi 0           @ system call

.data
output_msg: .ascii "MiniPar Output\n"
```

## Equivalências Java - Python

| Java | Python | Uso no Projeto |
|------|--------|----------------|
| Spring Boot | FastAPI | API REST |
| Maven | pip + requirements.txt | Gerenciamento de dependências |
| JUnit | pytest | Testes |
| Picocli | Click | CLI |
| ArrayList | list | Estruturas de dados |
| HashMap | dict | Mapeamentos |
| Optional | Optional (typing) | Valores opcionais |
| ANTLR4 | antlr4-python3-runtime | Geração de parsers |

## Arquitetura do Compilador

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────┐
│   MiniPar       │───▶│    Lexer     │───▶│   Tokens    │
│  Source Code    │    │ (tokenize)   │    │   Stream    │
└─────────────────┘    └──────────────┘    └─────────────┘
                                                   │
┌─────────────────┐    ┌──────────────┐           │
│     TAC         │◀───│    Parser    │◀──────────┘
│ (3-endereços)   │    │   (parse)    │
└─────────────────┘    └──────────────┘
         │                     │
         │              ┌─────────────┐
         │              │     AST     │
         │              │ (Abstract   │
         │              │Syntax Tree) │
         │              └─────────────┘
         ▼
┌─────────────────┐
│  ARM Assembly   │
│  (CPULator)     │
└─────────────────┘
```

## Links Úteis

- **CPULator ARM Emulator**: https://cpulator.01xz.net/?sys=arm
- **ANTLR4 Documentation**: https://github.com/antlr/antlr4
- **FastAPI Documentation**: https://fastapi.tiangolo.com
-- **TAC (three-address code)**: textual IR used by this project (no external reference required)

## Entrega Acadêmica

Este projeto atende **100%** aos requisitos do **Tema 1**:

### Checklist de Entrega
- **Compilador funcional** para linguagem MiniPar
- **Análise Léxica** completa
- **Análise Sintática** com AST
- **Código Intermediário** (TAC = 3-endereços, textual)
- **Assembly ARM** para CPULator
- **Interface API** REST completa
- **Documentação** técnica
- **Testes** de conformidade
- **Exemplos** funcionais

### Arquivos de Entrega
```
Entrega/
├── RELATORIO_FINAL.md        # Relatório técnico completo
├── python_compiler/          # Código fonte completo
├── exemplos/                # Códigos MiniPar de teste
├── README.md                # Este arquivo
└── demonstracao.mp4         # (Opcional) Vídeo demo
```

## Solução de Problemas

### Erro "ANTLR files not found"
Execute o script de geração:
```bash
./generate_antlr.sh  # Linux/Mac
generate_antlr.bat   # Windows
```

### Erro de importação de módulos
Certifique-se de que o ambiente virtual está ativo:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat # Windows
```

### Erro "Module not found"
Reinstale as dependências:
```bash
pip install -r requirements.txt
```

## Contribuição

1. Mantenha a estrutura equivalente ao projeto Java
2. Use type hints em Python
3. Documente as funções
4. Mantenha compatibilidade com a API existente