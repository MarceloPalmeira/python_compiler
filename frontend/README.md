# MiniPar Compiler - Frontend

Interface React moderna com design inspirado na Apple para o compilador MiniPar.

## 🚀 Funcionalidades

- **Editor de Código**: Editor Monaco com syntax highlighting
- **Análise Léxica**: Visualização interativa de tokens
- **Análise Sintática**: Representação da árvore sintática
- **Design Apple**: Interface elegante e minimalista
- **Animações Suaves**: Transições fluidas com Framer Motion

## 📦 Tecnologias

- React 18
- Vite
- Tailwind CSS
- Framer Motion
- Monaco Editor
- Axios
- Lucide React (ícones)

## 🛠️ Instalação

```bash
# Instalar dependências
npm install

# Iniciar servidor de desenvolvimento
npm run dev

# Build para produção
npm run build
```

## 🎨 Design

O frontend segue as diretrizes de design da Apple:

- Tipografia: SF Pro Display / System fonts
- Cores: Paleta minimalista com tons de cinza e azul
- Sombras suaves e blur effects (glass morphism)
- Animações suaves e responsivas
- Scrollbars customizadas

## 🔗 API

O frontend se conecta ao backend FastAPI em `http://127.0.0.1:8000`

Endpoints utilizados:

- `POST /compiler/upload` - Upload de código
- `GET /compiler/{code_id}/token` - Obter tokens
- `GET /compiler/{code_id}/syntax` - Obter árvore sintática

## 📱 Uso

1. Escreva ou cole seu código MiniPar no editor
2. Clique em "Compilar e Analisar"
3. Navegue pelas abas para ver:
   - **Editor**: Código fonte
   - **Tokens**: Lista de tokens da análise léxica
   - **Sintaxe**: Árvore sintática abstrata (AST)

## 🎯 Exemplos

```minipar
# Exemplo básico
var x: number = 10
var y: number = 20
var resultado: number = x + y

print("Resultado:", resultado)

func somar(a: number, b: number) -> number {
    return a + b
}
```

## 📄 Licença

MIT
