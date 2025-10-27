import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Tag, Hash, Type, Search, Download } from 'lucide-react';

const TOKEN_COLORS = {
  KEYWORD: 'bg-purple-100 text-purple-700 border-purple-200',
  IDENTIFIER: 'bg-blue-100 text-blue-700 border-blue-200',
  NUMBER: 'bg-green-100 text-green-700 border-green-200',
  STRING: 'bg-orange-100 text-orange-700 border-orange-200',
  OPERATOR: 'bg-pink-100 text-pink-700 border-pink-200',
  PUNCTUATION: 'bg-gray-100 text-gray-700 border-gray-200',
  COMMENT: 'bg-slate-100 text-slate-600 border-slate-200',
  DEFAULT: 'bg-apple-gray-100 text-apple-gray-700 border-apple-gray-200',
};

const TOKEN_ICONS = {
  KEYWORD: '🔑',
  IDENTIFIER: '🏷️',
  NUMBER: '🔢',
  STRING: '📝',
  OPERATOR: '➕',
  PUNCTUATION: '⚫',
  COMMENT: '💬',
};

function TokenViewer({ tokens, codeId }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredTokens, setFilteredTokens] = useState([]);
  const [stats, setStats] = useState({});

  useEffect(() => {
    if (tokens && Array.isArray(tokens)) {
      // Filtrar tokens por termo de busca
      const filtered = tokens.filter((token) => {
        const text = token.text?.toLowerCase() || '';
        const type = token.type?.toLowerCase() || '';
        const search = searchTerm.toLowerCase();
        return text.includes(search) || type.includes(search);
      });
      setFilteredTokens(filtered);

      // Calcular estatísticas
      const tokenStats = tokens.reduce((acc, token) => {
        const type = token.type || 'UNKNOWN';
        acc[type] = (acc[type] || 0) + 1;
        return acc;
      }, {});
      setStats(tokenStats);
    }
  }, [tokens, searchTerm]);

  const downloadTokens = () => {
    const data = JSON.stringify(tokens, null, 2);
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `tokens-${codeId}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (!tokens) {
    return (
      <div className="text-center py-20">
        <Tag className="w-16 h-16 text-apple-gray-300 mx-auto mb-4" />
        <h3 className="text-xl font-semibold text-apple-gray-800 mb-2">
          Nenhum Token Disponível
        </h3>
        <p className="text-apple-gray-500">
          Compile seu código primeiro para ver os tokens
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Cabeçalho */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-apple-gray-800 mb-1">
            Análise Léxica - Tokens
          </h2>
          <p className="text-sm text-apple-gray-500">
            {filteredTokens.length} token{filteredTokens.length !== 1 ? 's' : ''} encontrado
            {filteredTokens.length !== 1 ? 's' : ''}
          </p>
        </div>

        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={downloadTokens}
          className="flex items-center gap-2 px-4 py-2 bg-apple-gray-100 hover:bg-apple-gray-200 
                     text-apple-gray-700 rounded-xl transition-colors apple-shadow"
        >
          <Download className="w-4 h-4" />
          Baixar JSON
        </motion.button>
      </div>

      {/* Estatísticas */}
      <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-3">
        {Object.entries(stats).map(([type, count], index) => (
          <motion.div
            key={type}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className="bg-white rounded-xl p-4 border border-apple-gray-200 apple-shadow"
          >
            <div className="text-2xl mb-1">{TOKEN_ICONS[type] || '🏷️'}</div>
            <div className="text-2xl font-bold text-apple-gray-800">{count}</div>
            <div className="text-xs text-apple-gray-500 mt-1">{type}</div>
          </motion.div>
        ))}
      </div>

      {/* Barra de pesquisa */}
      <div className="relative">
        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-apple-gray-400" />
        <input
          type="text"
          placeholder="Buscar tokens por texto ou tipo..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="w-full pl-12 pr-4 py-3 border border-apple-gray-200 rounded-xl 
                     focus:outline-none focus:ring-2 focus:ring-apple-blue focus:border-transparent
                     bg-white apple-shadow transition-all"
        />
      </div>

      {/* Lista de tokens */}
      <div className="bg-white rounded-2xl border border-apple-gray-200 overflow-hidden apple-shadow">
        <div className="overflow-x-auto max-h-[600px] overflow-y-auto">
          <table className="w-full">
            <thead className="bg-apple-gray-50 sticky top-0 z-10">
              <tr>
                <th className="px-6 py-4 text-left text-xs font-semibold text-apple-gray-600 uppercase tracking-wider">
                  <div className="flex items-center gap-2">
                    <Hash className="w-4 h-4" />
                    #
                  </div>
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-apple-gray-600 uppercase tracking-wider">
                  <div className="flex items-center gap-2">
                    <Type className="w-4 h-4" />
                    Tipo
                  </div>
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-apple-gray-600 uppercase tracking-wider">
                  <div className="flex items-center gap-2">
                    <Tag className="w-4 h-4" />
                    Texto
                  </div>
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-apple-gray-600 uppercase tracking-wider">
                  Linha
                </th>
                <th className="px-6 py-4 text-left text-xs font-semibold text-apple-gray-600 uppercase tracking-wider">
                  Coluna
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-apple-gray-100">
              <AnimatePresence>
                {filteredTokens.map((token, index) => {
                  const type = token.type || 'DEFAULT';
                  const colorClass = TOKEN_COLORS[type] || TOKEN_COLORS.DEFAULT;
                  
                  return (
                    <motion.tr
                      key={`${index}-${token.text}`}
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: 20 }}
                      transition={{ delay: index * 0.02 }}
                      className="hover:bg-apple-gray-50 transition-colors"
                    >
                      <td className="px-6 py-4 text-sm text-apple-gray-500">
                        {index + 1}
                      </td>
                      <td className="px-6 py-4">
                        <span className={`inline-flex items-center gap-1 px-3 py-1 rounded-lg text-xs font-medium border ${colorClass}`}>
                          {TOKEN_ICONS[type] || '🏷️'}
                          {type}
                        </span>
                      </td>
                      <td className="px-6 py-4">
                        <code className="px-3 py-1 bg-apple-gray-50 rounded-lg text-sm font-mono text-apple-gray-800">
                          {token.text || '(vazio)'}
                        </code>
                      </td>
                      <td className="px-6 py-4 text-sm text-apple-gray-600">
                        {token.line || '-'}
                      </td>
                      <td className="px-6 py-4 text-sm text-apple-gray-600">
                        {token.column || '-'}
                      </td>
                    </motion.tr>
                  );
                })}
              </AnimatePresence>
            </tbody>
          </table>
        </div>
      </div>

      {filteredTokens.length === 0 && tokens.length > 0 && (
        <div className="text-center py-12">
          <Search className="w-12 h-12 text-apple-gray-300 mx-auto mb-3" />
          <p className="text-apple-gray-500">
            Nenhum token encontrado com "{searchTerm}"
          </p>
        </div>
      )}
    </div>
  );
}

export default TokenViewer;

