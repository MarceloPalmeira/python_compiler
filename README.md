# Projeto Compiladores - Python Version

Este é a versão Python do projeto de compiladores do IFSC, convertido do projeto Java original.

## 🚀 Setup Rápido

### Windows
```batch
setup.bat
```

### Linux/Mac
```bash
chmod +x setup.sh
./setup.sh
```

## 📁 Estrutura do Projeto

```
python_compiler/
├── requirements.txt          # Dependências Python
├── main.py                  # CLI principal (equivalente ao Main.java)
├── setup.sh / setup.bat     # Scripts de instalação
├── grammar/                 # Gramáticas ANTLR4
│   ├── LexerGrammar.g4
│   └── ParserGrammar.g4
├── compiler/                # Módulo do compilador
│   ├── generated/          # Arquivos gerados pelo ANTLR
│   ├── llvm/              # Geração de código LLVM IR
│   ├── complexity/        # Análise de complexidade
│   ├── symbols/           # Tabela de símbolos
│   ├── syntax/            # Análise sintática
│   └── tokens/            # Análise lexical
├── api/                    # API REST (equivalente ao Spring Boot)
│   ├── main.py
│   ├── compiler/          # Controllers e services
│   └── models/            # Modelos de dados
└── common/                # Utilitários comuns
```

## 🛠️ Instalação Manual

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

## 🎯 Uso

### CLI (Interface de Linha de Comando)

```bash
# Ajuda
python main.py --help
python main.py compiler --help

# Compilar arquivo
python main.py compiler test_simple.txt

# Compilar e salvar saída
python main.py compiler test_simple.txt -o output.ll

# Modo interativo
python main.py compiler

# Mostrar árvore sintática (quando implementado)
python main.py compiler test_simple.txt -t
```

### API REST

```bash
# Iniciar servidor
python main.py api

# Com opções personalizadas
python main.py api --host 0.0.0.0 --port 8080 --reload
```

A API estará disponível em:
- **Servidor**: http://localhost:8000
- **Documentação**: http://localhost:8000/docs
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Endpoints da API

```
POST /compiler/upload              # Upload de código
GET  /compiler/{code_id}          # Obter código original
GET  /compiler/{code_id}/llvm/ir  # Obter LLVM IR
GET  /compiler/{code_id}/llvm/ir/opt/{level} # LLVM IR otimizado
GET  /compiler/{code_id}/asm      # Código assembly
GET  /compiler/{code_id}/asm/opt/{level}     # Assembly otimizado
GET  /compiler/{code_id}/syntax   # Árvore sintática
GET  /compiler/{code_id}/token    # Lista de tokens
GET  /compiler/{code_id}/symbols  # Tabela de símbolos
GET  /compiler/{code_id}/complexity # Análise de complexidade
```

## 📝 Exemplos de Código

### Programa Simples
```c
main() {
    int x;
    x = 42;
    println("Hello, World! The answer is:", x);
}
```

### Programa com Função
```c
int soma(int a, int b) {
    return a + b;
}

main() {
    int resultado;
    resultado = func soma(10, 20);
    println("Resultado:", resultado);
}
```

## 🔧 Estado de Implementação

### ✅ Implementado
- [x] Estrutura básica do projeto
- [x] CLI com Click
- [x] API REST com FastAPI
- [x] Sistema de cache de código
- [x] Gramáticas ANTLR4 copiadas
- [x] Scripts de setup automático
- [x] Estrutura de serviços
- [x] Sistema de fragmentos LLVM

### 🚧 Em Desenvolvimento
- [ ] Gerador de LLVM IR completo
- [ ] Visitor para análise sintática
- [ ] Sistema de tipos completo
- [ ] Análise semântica
- [ ] Gerenciamento de escopo

### 📋 Pendente
- [ ] Análise de complexidade
- [ ] Tabela de símbolos
- [ ] Análise de tokens
- [ ] Árvore sintática
- [ ] Otimizações LLVM
- [ ] Compilação para assembly
- [ ] Interface gráfica para árvore sintática

## 🤝 Equivalências Java → Python

| Java | Python |
|------|--------|
| Spring Boot | FastAPI |
| Maven | pip + requirements.txt |
| JUnit | pytest |
| Picocli | Click |
| ArrayList | list |
| HashMap | dict |
| Optional | Optional (typing) |

## 🐞 Solução de Problemas

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

## 📄 Licença

Mesmo projeto original do IFSC, convertido para Python.

## 🤝 Contribuição

1. Mantenha a estrutura equivalente ao projeto Java
2. Use type hints em Python
3. Documente as funções
4. Mantenha compatibilidade com a API existente