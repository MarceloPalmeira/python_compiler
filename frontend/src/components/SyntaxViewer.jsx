import React from 'react';
import { motion } from 'framer-motion';
import { TreePine, Download, FileJson } from 'lucide-react';

function SyntaxViewer({ syntaxTree, codeId }) {
  const downloadSyntaxTree = () => {
    const data = typeof syntaxTree === 'string' ? syntaxTree : JSON.stringify(syntaxTree, null, 2);
    const blob = new Blob([data], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `syntax-tree-${codeId}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (!syntaxTree) {
    return (
      <div className="text-center py-20">
        <TreePine className="w-16 h-16 text-apple-gray-300 mx-auto mb-4" />
        <h3 className="text-xl font-semibold text-apple-gray-800 mb-2">
          Nenhuma Árvore Sintática Disponível
        </h3>
        <p className="text-apple-gray-500">
          Compile seu código primeiro para ver a árvore sintática
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
            Análise Sintática
          </h2>
          <p className="text-sm text-apple-gray-500">
            Representação em árvore da estrutura sintática
          </p>
        </div>

        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={downloadSyntaxTree}
          className="flex items-center gap-2 px-4 py-2 bg-apple-gray-100 hover:bg-apple-gray-200 
                     text-apple-gray-700 rounded-xl transition-colors apple-shadow"
        >
          <Download className="w-4 h-4" />
          Baixar
        </motion.button>
      </div>

      {/* Visualização da árvore */}
      <motion.div
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.3 }}
        className="bg-white rounded-2xl border border-apple-gray-200 overflow-hidden apple-shadow"
      >
        <div className="bg-apple-gray-50 px-6 py-3 border-b border-apple-gray-200 flex items-center gap-2">
          <FileJson className="w-4 h-4 text-apple-gray-600" />
          <span className="text-sm font-medium text-apple-gray-700">
            Árvore Sintática Abstrata (AST)
          </span>
        </div>
        
        <div className="p-6 max-h-[600px] overflow-auto">
          <pre className="text-sm font-mono text-apple-gray-800 whitespace-pre-wrap break-words leading-relaxed">
            {typeof syntaxTree === 'string' 
              ? syntaxTree 
              : JSON.stringify(syntaxTree, null, 2)
            }
          </pre>
        </div>
      </motion.div>

      {/* Informações adicionais */}
      <div className="bg-blue-50 rounded-xl p-4 border border-blue-200">
        <h3 className="text-sm font-semibold text-blue-900 mb-2 flex items-center gap-2">
          <TreePine className="w-4 h-4" />
          Sobre a Árvore Sintática
        </h3>
        <p className="text-sm text-blue-800">
          A árvore sintática abstrata (AST) representa a estrutura hierárquica do seu código.
          Cada nó representa uma construção sintática como expressões, declarações e comandos.
        </p>
      </div>
    </div>
  );
}

export default SyntaxViewer;

