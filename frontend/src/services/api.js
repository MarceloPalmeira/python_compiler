import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

class CompilerAPI {
  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      headers: {
        'Content-Type': 'application/json',
      },
    });
  }

  /**
   * Faz upload do código e retorna o code_id
   * @param {string} code - Código fonte MiniPar
   * @returns {Promise<string>} - code_id gerado
   */
  async uploadCode(code) {
    try {
      const response = await this.client.post('/compiler/upload', { code });
      return response.data.code_id;
    } catch (error) {
      console.error('Erro ao fazer upload do código:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao fazer upload do código'
      );
    }
  }

  /**
   * Obtém o código original pelo ID
   * @param {string} codeId - ID do código
   * @returns {Promise<string>} - Código fonte original
   */
  async getCode(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}`);
      return response.data.code;
    } catch (error) {
      console.error('Erro ao obter código:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter código'
      );
    }
  }

  /**
   * Obtém a lista de tokens (análise léxica)
   * @param {string} codeId - ID do código
   * @returns {Promise<Array>} - Lista de tokens
   */
  async getTokens(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}/token`, {
        responseType: 'text',
        transformResponse: [(data) => data],
      });

      const raw = typeof response.data === 'string' ? response.data : String(response.data || '');
      return parseTokensTextToArray(raw);
    } catch (error) {
      console.error('Erro ao obter tokens:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter tokens'
      );
    }
  }

  /**
   * Obtém a árvore sintática
   * @param {string} codeId - ID do código
   * @returns {Promise<string>} - Árvore sintática
   */
  async getSyntaxTree(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}/syntax`, {
        responseType: 'text',
        transformResponse: [(data) => data],
      });

      if (typeof response.data === 'string') {
        return response.data;
      }

      return response.data?.syntax_tree || '';
    } catch (error) {
      console.error('Erro ao obter árvore sintática:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter árvore sintática'
      );
    }
  }

  /**
   * Obtém o código LLVM IR
   * @param {string} codeId - ID do código
   * @returns {Promise<string>} - Código LLVM IR
   */
  async getLLVMIR(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}/llvm/ir`);
      return response.data.llvm_ir;
    } catch (error) {
      console.error('Erro ao obter LLVM IR:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter LLVM IR'
      );
    }
  }

  /**
   * Obtém a tabela de símbolos
   * @param {string} codeId - ID do código
   * @returns {Promise<object>} - Tabela de símbolos
   */
  async getSymbolsTable(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}/symbols`, {
        responseType: 'text',
        transformResponse: [(data) => data],
      });

      const raw = typeof response.data === 'string' ? response.data : String(response.data || '');
      return parseSymbolsTextToObject(raw);
    } catch (error) {
      console.error('Erro ao obter tabela de símbolos:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter tabela de símbolos'
      );
    }
  }

  /**
   * Obtém análise de complexidade
   * @param {string} codeId - ID do código
   * @returns {Promise<object>} - Análise de complexidade
   */
  async getComplexityAnalysis(codeId) {
    try {
      const response = await this.client.get(`/compiler/${codeId}/complexity`);
      return response.data.complexity_analysis;
    } catch (error) {
      console.error('Erro ao obter análise de complexidade:', error);
      throw new Error(
        error.response?.data?.detail || 'Erro ao obter análise de complexidade'
      );
    }
  }
}

export default new CompilerAPI();

// Helpers

function normalizePythonish(input) {
  if (!input || typeof input !== 'string') return '';
  let s = input.trim();
  // Remove leading/trailing quotes if the whole payload was quoted
  if ((s.startsWith('"') && s.endsWith('"')) || (s.startsWith("'") && s.endsWith("'"))) {
    s = s.slice(1, -1);
  }
  // Normalize booleans and nulls
  s = s.replace(/\bTrue\b/g, 'true').replace(/\bFalse\b/g, 'false').replace(/\bNone\b/g, 'null');
  // Convert set() to []
  s = s.replace(/set\(\)/g, '[]');
  // Convert single-quoted strings to JSON strings
  s = s.replace(/'((?:[^'\\]|\\.)*)'/g, (_m, content) => {
    const unescaped = content.replace(/\\'/g, "'");
    return JSON.stringify(unescaped);
  });
  return s;
}

function safeEvalToObject(expr) {
  try {
    // eslint-disable-next-line no-new-func
    const fn = Function; 
    return fn(`"use strict"; return (${expr});`)();
  } catch (_e) {
    return null;
  }
}

function parseTokensTextToArray(raw) {
  const normalized = normalizePythonish(raw);

  // Try JSON first
  try {
    const parsed = JSON.parse(normalized);
    return mapTokens(parsed);
  } catch (_) {
    // Fallback: try permissive eval
    const obj = safeEvalToObject(normalized);
    if (Array.isArray(obj)) {
      return mapTokens(obj);
    }
  }

  // Last resort: empty list
  return [];
}

function mapTokens(arr) {
  if (!Array.isArray(arr)) return [];
  return arr.map((t, idx) => {
    const type = t?.type || t?.Type || t?.TOKEN || 'UNKNOWN';
    const text = t?.text ?? t?.value ?? t?.lexeme ?? '';
    const line = t?.line ?? t?.Line ?? t?.linha ?? null;
    const column = t?.column ?? t?.col ?? t?.coluna ?? null;
    return { type, text, line, column, _i: idx };
  });
}

function parseSymbolsTextToObject(raw) {
  let s = normalizePythonish(raw);

  // Special-case: variables printed as a Python set literal inside the object
  // Replace "'variables': { ... }" with an array when there are no colons inside
  s = s.replace(/("variables"\s*:\s*)\{([^:{}]|:(?!\s))*?\}/g, (match) => {
    // If there is a ':' inside the braces, it's a dict, not a set
    const inner = match.slice(match.indexOf('{') + 1, match.lastIndexOf('}'));
    if (/:/.test(inner)) return match; // keep as-is
    return match.replace('{', '[').replace(/}$/, ']');
  });

  // Another heuristic: top-level {...} without keys could be a set; not expected here, but guard anyway
  // Try JSON.parse, else fallback to eval
  try {
    const parsed = JSON.parse(s);
    return coerceSymbols(parsed);
  } catch (_) {
    const obj = safeEvalToObject(s);
    return coerceSymbols(obj);
  }
}

function coerceSymbols(obj) {
  if (!obj || typeof obj !== 'object') return { functions: {}, variables: [] };
  const variables = Array.isArray(obj.variables)
    ? obj.variables
    : Array.isArray(obj?.symbols?.variables)
      ? obj.symbols.variables
      : (obj.variables && typeof obj.variables === 'object' && !('0' in obj.variables))
        ? Object.values(obj.variables)
        : [];

  // functions may be an object map name->node/true
  const functionsMap = obj.functions || obj?.symbols?.functions || {};
  const functionNames = [];
  const functions = [];
  if (functionsMap && typeof functionsMap === 'object') {
    for (const [name, node] of Object.entries(functionsMap)) {
      functionNames.push(name);
      const params = Array.isArray(node?.params) ? node.params : [];
      functions.push({ name, paramsCount: params.length, params });
    }
  }

  return {
    raw: obj,
    variables,
    functions,
    functionNames,
  };
}

