import React from 'react';
import { motion } from 'framer-motion';
import { FileCode, Clock, Trash2, RotateCcw } from 'lucide-react';
import { useCodeContext } from '../contexts/CodeContext';

function CodeStatus() {
  const { currentCodeId, codeHistory, clearCurrentCodeId, clearHistory, hasCodeLoaded, updateCurrentCodeId } = useCodeContext();

  if (!hasCodeLoaded && codeHistory.length === 0) {
    return null;
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="mt-6 glass-morphism rounded-2xl p-6 apple-shadow"
    >
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-apple-gray-800 flex items-center gap-2">
          <FileCode className="w-5 h-5" />
          Status do Código
        </h3>
        {codeHistory.length > 0 && (
          <button
            onClick={clearHistory}
            className="text-sm text-red-600 hover:text-red-700 flex items-center gap-1"
          >
            <Trash2 className="w-4 h-4" />
            Limpar Histórico
          </button>
        )}
      </div>

      {hasCodeLoaded && (
        <div className="bg-green-50 border border-green-200 rounded-xl p-4 mb-4">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-green-800">Código Atual Carregado</p>
              <code className="text-xs text-green-600 font-mono bg-white px-2 py-1 rounded mt-1 inline-block">
                {currentCodeId}
              </code>
            </div>
            <button
              onClick={clearCurrentCodeId}
              className="text-sm text-green-700 hover:text-green-800 underline"
            >
              Limpar
            </button>
          </div>
        </div>
      )}

      {codeHistory.length > 0 && (
        <div>
          <h4 className="text-sm font-semibold text-apple-gray-700 mb-2 flex items-center gap-2">
            <Clock className="w-4 h-4" />
            Histórico de Uploads ({codeHistory.length})
          </h4>
          <div className="space-y-2 max-h-60 overflow-y-auto">
            {codeHistory.map((item, index) => (
              <div
                key={item.id}
                className={`
                  flex items-center justify-between p-3 rounded-lg border
                  ${item.id === currentCodeId
                    ? 'bg-blue-50 border-blue-200'
                    : 'bg-white border-apple-gray-200'
                  }
                `}
              >
                <div className="flex-1">
                  <code className="text-xs font-mono text-apple-gray-700">
                    {item.id}
                  </code>
                  <p className="text-xs text-apple-gray-500 mt-1">
                    {item.uploadedAt}
                  </p>
                </div>
                <div className="flex items-center gap-2">
                  {item.id === currentCodeId ? (
                    <span className="text-xs bg-blue-500 text-white px-2 py-1 rounded-full">
                      Atual
                    </span>
                  ) : (
                    <motion.button
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                      onClick={() => updateCurrentCodeId(item.id)}
                      className="flex items-center gap-1 text-xs bg-purple-500 hover:bg-purple-600 text-white px-3 py-1.5 rounded-lg transition-colors"
                      title="Usar este código"
                    >
                      <RotateCcw className="w-3 h-3" />
                      Usar
                    </motion.button>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </motion.div>
  );
}

export default CodeStatus;

