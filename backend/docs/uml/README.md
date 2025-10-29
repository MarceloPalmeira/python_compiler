# Diagramas UML - Compilador MiniPar 2025.1

Este diretório contém os diagramas UML do projeto do Compilador MiniPar 2025.1, criados em PlantUML.

## 📋 Diagramas Disponíveis

### 1. **Diagrama de Casos de Uso** (`casos_de_uso.puml`)
Representa as funcionalidades do sistema do ponto de vista dos usuários:
- **Atores**: Desenvolvedor, Usuário Final, Sistema Externo, CPULator
- **Casos de Uso Principais**: Compilação, Análises (Léxica, Sintática, Semântica)
- **Funcionalidades Avançadas**: PAR/SEQ, Canais de Comunicação, Threads
- **Interfaces**: Web, API REST, CLI
- **Programas de Teste**: 8 programas especificados no projeto

### 2. **Arquitetura de Componentes** (`arquitetura_componentes.puml`)
Mostra a arquitetura de software baseada em componentes:
- **Frontend Layer**: Web Editor, CLI, REST API
- **Compiler Core**: Lexer, Parser, Semantic, TAC Generator, ARM Generator
- **Runtime Layer**: Interpreter, Thread Manager, Socket Manager
- **Support Components**: AST Builder, Error Handler, Utils
- **External Systems**: CPULator, ANTLR, Python Threading

### 3. **Diagrama de Classes** (`diagrama_classes.puml`)
Detalha a estrutura orientada a objetos do sistema:
- **AST Nodes**: Hierarquia de nós da árvore sintática
- **Compiler Components**: Classes dos analisadores
- **Symbol Management**: Gerenciamento de símbolos e variáveis
- **Runtime Component**: Execução e interpretação
- **Code Generation**: Geração de TAC e Assembly ARM

## 🔧 Como Visualizar

### PlantUML Online
1. Acesse: http://www.plantuml.com/plantuml/uml/
2. Copie e cole o conteúdo de qualquer arquivo `.puml`
3. Clique em "Submit" para gerar o diagrama

### PlantUML Local
```bash
# Instalar PlantUML
npm install -g plantuml

# Gerar PNG
plantuml casos_de_uso.puml
plantuml arquitetura_componentes.puml  
plantuml diagrama_classes.puml
```

### VS Code Extension
1. Instale a extensão "PlantUML"
2. Abra qualquer arquivo `.puml`
3. Use `Ctrl+Shift+P` → "PlantUML: Preview Current Diagram"

## 📊 Conformidade com Requisitos

Estes diagramas atendem aos requisitos especificados no documento do projeto:

✅ **Requisito 12**: Diagrama de Casos de Uso segundo a notação da UML  
✅ **Requisito 13**: Arquitetura utilizando Componentes de Software segundo a notação da UML  
✅ **Requisito 14**: Modelagem dos Componentes de Software via Diagrama de Classes segundo a notação da UML  

## 🎯 Características dos Diagramas

- **Padrão UML**: Notação oficial da UML 2.0
- **PlantUML**: Sintaxe textual para versionamento
- **Documentação Técnica**: Notas explicativas em cada diagrama
- **Rastreabilidade**: Mapeamento direto com o código fonte
- **Componentização**: Arquitetura baseada em componentes reutilizáveis

## 📝 Notas Técnicas

### Casos de Uso
- Demonstra interação entre atores e sistema
- Inclui relacionamentos `<<include>>`, `<<extend>>` e generalização
- Cobre todos os 8 programas de teste especificados

### Arquitetura de Componentes  
- Mostra separação em camadas (Frontend, Core, Runtime, Support)
- Interfaces bem definidas entre componentes
- Dependências externas explícitas

### Diagrama de Classes
- Hierarquia completa dos nós AST
- Padrões de design: Visitor, Abstract Factory
- Composição e agregação entre classes
- Métodos principais de cada classe