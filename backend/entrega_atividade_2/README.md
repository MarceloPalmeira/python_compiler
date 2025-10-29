# 📋 Entrega Atividade 2 - Compilador MiniPar

Este diretório contém todos os materiais relacionados à **Atividade 2** do curso de Compiladores.

## 📁 Estrutura dos Arquivos

### 📋 Relatórios
- `RELATORIO_FINAL.md` - Relatório técnico completo da implementação
- `RESUMO_EXECUTIVO.md` - Resumo executivo do projeto

### 🔤 Gramáticas MiniPar
- `grammar_minipar/`
  - `LexerGrammarMinipar.g4` - Gramática do analisador léxico
  - `ParserGrammarMinipar.g4` - Gramática do analisador sintático

### 🧪 Exemplos de Teste
- `exemplos_minipar/`
  - `ex1.minipar` - Exemplo 1 oficial MiniPar
  - `ex3.minipar` - Exemplo 3 oficial MiniPar
  - `exemplo_minipar.txt` - Exemplo adicional

## 🎯 Requisitos Atendidos

✅ **Analisador Léxico (Lexer)** - Tokenização completa do MiniPar
✅ **Analisador Sintático (Parser)** - Geração de AST estruturada
✅ **Geração de Código Intermediário** - TAC (three-address code, textual IR)
✅ **Interface Textual** - API REST completa
✅ **Conformidade com Tema 1** - Compilador MiniPar 2025.1

## 🚀 Demonstração

Para demonstrar os componentes implementados, use os seguintes endpoints da API:

1. **Upload**: `POST /compiler/upload` - Envio do código MiniPar
2. **Lexer**: `GET /compiler/{id}/token` - Análise léxica
3. **Parser**: `GET /compiler/{id}/syntax` - Análise sintática
4. **Código Intermediário**: `GET /compiler/{id}/tac` - TAC (three-address code)

## 📖 Documentação

Consulte os relatórios inclusos para detalhes técnicos da implementação e conformidade com os requisitos da Atividade 2.