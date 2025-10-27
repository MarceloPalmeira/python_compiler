# 📤 Funcionalidade de Upload de Código

## Visão Geral

Esta funcionalidade permite fazer upload de código MiniPar para o backend, salvando o token (code_id) no localStorage e compartilhando-o entre todas as telas da aplicação através de um Context React.

## Estrutura Implementada

### 1. **Context API - CodeContext**
📁 `src/contexts/CodeContext.jsx`

Gerencia o estado global do código carregado na aplicação:

#### Funcionalidades:
- ✅ Armazena o `currentCodeId` atual
- ✅ Mantém histórico de códigos enviados (últimos 20)
- ✅ Persiste dados no localStorage
- ✅ Compartilha estado entre todos os componentes

#### Hooks disponíveis:
```javascript
const {
  currentCodeId,      // ID do código atual
  codeHistory,        // Array com histórico de uploads
  updateCurrentCodeId, // Atualiza o ID atual
  clearCurrentCodeId,  // Limpa o ID atual
  clearHistory,        // Limpa todo o histórico
  hasCodeLoaded       // Boolean indicando se há código carregado
} = useCodeContext();
```

### 2. **Componente CodeEditor Atualizado**
📁 `src/components/CodeEditor.jsx`

Agora inclui:

#### Novo Botão de Upload
- 🟣 Botão roxo "Fazer Upload"
- ⏳ Estados de loading durante upload
- ✅ Feedback visual de sucesso/erro
- 🆔 Exibe o code_id gerado

#### Indicadores Visuais
- Badge "Código Carregado" quando há código ativo
- Mensagens animadas de status
- Exibição do code_id completo após upload

### 3. **Componente CodeStatus (Novo)**
📁 `src/components/CodeStatus.jsx`

Widget para exibir status e histórico:

#### Features:
- 📊 Status do código atual
- 🕐 Histórico de uploads com timestamps
- 🗑️ Opção de limpar histórico
- ✨ Destaque visual para código atual

### 4. **App.jsx Atualizado**
📁 `src/App.jsx`

- Envolvido pelo `CodeProvider`
- Inclui componente `CodeStatus` na página

## Como Funciona

### Fluxo de Upload

1. **Usuário escreve código** no editor
2. **Clica no botão "Fazer Upload"** (roxo)
3. **POST para `/compiler/upload`** é realizado
4. **Backend retorna `code_id`**
5. **`code_id` é salvo no Context** e localStorage
6. **Mensagem de sucesso** é exibida
7. **Badge "Código Carregado"** aparece

### Persistência no localStorage

Os dados são salvos automaticamente:

```javascript
localStorage.setItem('minipar_current_code_id', codeId);
localStorage.setItem('minipar_code_history', JSON.stringify(history));
```

**Chaves utilizadas:**
- `minipar_current_code_id` - ID do código atual
- `minipar_code_history` - Array JSON com histórico

## Usando em Outros Componentes

Para acessar o código carregado em qualquer componente:

```jsx
import { useCodeContext } from '../contexts/CodeContext';

function MeuComponente() {
  const { currentCodeId, hasCodeLoaded } = useCodeContext();
  
  if (!hasCodeLoaded) {
    return <p>Nenhum código carregado</p>;
  }
  
  return (
    <div>
      Código atual: {currentCodeId}
    </div>
  );
}
```

## Exemplos de Uso

### Exemplo 1: Verificar se há código carregado
```jsx
const { hasCodeLoaded } = useCodeContext();

{hasCodeLoaded && (
  <button>Processar código atual</button>
)}
```

### Exemplo 2: Obter o ID atual
```jsx
const { currentCodeId } = useCodeContext();

const processarCodigo = async () => {
  if (currentCodeId) {
    const tokens = await compilerAPI.getTokens(currentCodeId);
    // processar tokens...
  }
};
```

### Exemplo 3: Atualizar após novo upload
```jsx
const { updateCurrentCodeId } = useCodeContext();

const fazerUpload = async (code) => {
  const codeId = await compilerAPI.uploadCode(code);
  updateCurrentCodeId(codeId); // Atualiza o context
};
```

## API Backend Utilizada

### POST /compiler/upload

**Request:**
```json
{
  "code": "var x: number = 10"
}
```

**Response:**
```json
{
  "code_id": "a1b2c3d4e5f6"
}
```

## Estrutura de Dados

### CodeHistory Item
```typescript
{
  id: string,           // code_id
  timestamp: string,    // ISO timestamp
  uploadedAt: string    // Formatado para exibição (pt-BR)
}
```

## Estilos e UX

### Botão de Upload
- Cor: Roxo (`bg-purple-500`)
- Ícone: Upload (lucide-react)
- Estados: Normal, Hover, Disabled, Loading

### Mensagens de Status
- ✅ Sucesso: Verde (`bg-green-50`)
- ❌ Erro: Vermelho (`bg-red-50`)
- Auto-dismiss após 5 segundos

### Badge "Código Carregado"
- Verde (`bg-green-100`)
- Aparece ao lado do título do editor

## Melhorias Futuras Possíveis

- [ ] Sincronização com backend para recuperar histórico
- [ ] Opção de carregar código do histórico
- [ ] Exportar/importar histórico
- [ ] Integração com sistema de autenticação
- [ ] Compartilhamento de códigos via link
- [ ] Versionamento de códigos
- [ ] Tags e categorias para códigos

## Debugging

### Verificar localStorage no DevTools

```javascript
// Console do navegador
localStorage.getItem('minipar_current_code_id')
JSON.parse(localStorage.getItem('minipar_code_history'))
```

### Limpar dados

```javascript
// Console do navegador
localStorage.removeItem('minipar_current_code_id')
localStorage.removeItem('minipar_code_history')
```

## Troubleshooting

### O código não é salvo
- Verifique se o backend está rodando
- Confira as permissões do localStorage
- Verifique o console para erros de rede

### Context não está disponível
- Certifique-se de que o componente está dentro do `<CodeProvider>`
- Verifique a importação do `useCodeContext`

### Histórico não aparece
- Verifique se há dados no localStorage
- Limpe o cache do navegador
- Recarregue a página

## Compatibilidade

- ✅ React 18+
- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ localStorage habilitado
- ✅ JavaScript habilitado

---

**Desenvolvido para o Compilador MiniPar 2025.1**

