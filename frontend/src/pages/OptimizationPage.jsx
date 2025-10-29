import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { useCodeContext } from '../contexts/CodeContext';
import { Settings, Zap } from 'lucide-react';

function OptimizationPage() {
  const { currentCodeId } = useCodeContext();
  const [optimizationLevel, setOptimizationLevel] = useState('O0');

  const levels = [
    { value: 'O0', name: 'Sem otimização', description: 'Compilação rápida, sem otimizações' },
    { value: 'O1', name: 'Otimização básica', description: 'Otimizações simples e rápidas' },
    { value: 'O2', name: 'Otimização moderada', description: 'Maioria das otimizações sem trade-offs' },
    { value: 'O3', name: 'Otimização máxima', description: 'Todas as otimizações, pode aumentar tamanho do código' },
  ];

  if (!currentCodeId) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-morphism rounded-3xl apple-shadow-lg p-12 text-center"
      >
        <div className="text-6xl mb-4">⚡</div>
        <h2 className="text-2xl font-bold text-apple-gray-800 mb-2">
          Nenhum código carregado
        </h2>
        <p className="text-apple-gray-600">
          Faça upload de um código na página do Editor primeiro
        </p>
      </motion.div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      className="glass-morphism rounded-3xl apple-shadow-lg overflow-hidden p-6"
    >
      <div className="flex items-center gap-2 mb-6">
        <Settings className="w-6 h-6 text-apple-gray-600" />
        <h2 className="text-2xl font-semibold text-apple-gray-800">
          Níveis de Otimização
        </h2>
      </div>

      <div className="space-y-4">
        {levels.map((level) => (
          <motion.div
            key={level.value}
            whileHover={{ scale: 1.01 }}
            onClick={() => setOptimizationLevel(level.value)}
            className={`
              p-6 rounded-xl border-2 cursor-pointer transition-all
              ${optimizationLevel === level.value
                ? 'border-apple-blue bg-blue-50'
                : 'border-apple-gray-200 hover:border-apple-gray-300'
              }
            `}
          >
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <code className="text-lg font-bold text-apple-gray-800">
                    -{level.value}
                  </code>
                  {optimizationLevel === level.value && (
                    <Zap className="w-5 h-5 text-apple-blue" />
                  )}
                </div>
                <h3 className="font-semibold text-apple-gray-800 mb-1">
                  {level.name}
                </h3>
                <p className="text-sm text-apple-gray-600">
                  {level.description}
                </p>
              </div>
              <div className={`
                w-6 h-6 rounded-full border-2 flex items-center justify-center
                ${optimizationLevel === level.value
                  ? 'border-apple-blue bg-apple-blue'
                  : 'border-apple-gray-300'
                }
              `}>
                {optimizationLevel === level.value && (
                  <div className="w-3 h-3 rounded-full bg-white"></div>
                )}
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      <div className="mt-6 bg-apple-gray-50 rounded-xl p-4 border border-apple-gray-200">
        <h3 className="text-sm font-semibold text-apple-gray-700 mb-2">
          💡 Nível atual selecionado
        </h3>
        <p className="text-sm text-apple-gray-600">
          Você está usando o nível de otimização:{' '}
          <code className="bg-white px-2 py-1 rounded font-bold text-apple-blue">
            -{optimizationLevel}
          </code>
        </p>
        <p className="text-xs text-apple-gray-500 mt-2">
          🚧 A funcionalidade de compilação com diferentes níveis de otimização estará disponível em breve
        </p>
      </div>
    </motion.div>
  );
}

export default OptimizationPage;

