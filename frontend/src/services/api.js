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
      const response = await this.client.get(`/compiler/${codeId}/token`);
      return response.data.tokens;
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
      const response = await this.client.get(`/compiler/${codeId}/symbols`);
      return response.data.symbols_table;
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

