import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { useCodeContext } from '../contexts/CodeContext';
import { Cpu } from 'lucide-react';

function AssemblyPage() {
  const { currentCodeId } = useCodeContext();
  const [activeTab, setActiveTab] = useState('normal');

  if (!currentCodeId) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-morphism rounded-3xl apple-shadow-lg p-12 text-center"
      >
        <div className="text-6xl mb-4">💻</div>
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
      className="glass-morphism rounded-3xl apple-shadow-lg overflow-hidden"
    >
      {/* Tabs */}
      <div className="flex border-b border-apple-gray-200">
        <button
          onClick={() => setActiveTab('normal')}
          className={`flex-1 px-6 py-4 font-medium transition-colors ${
            activeTab === 'normal'
              ? 'bg-white text-apple-blue border-b-2 border-apple-blue'
              : 'text-apple-gray-600 hover:bg-apple-gray-50'
          }`}
        >
          Assembly Normal
        </button>
        <button
          onClick={() => setActiveTab('optimized')}
          className={`flex-1 px-6 py-4 font-medium transition-colors ${
            activeTab === 'optimized'
              ? 'bg-white text-apple-blue border-b-2 border-apple-blue'
              : 'text-apple-gray-600 hover:bg-apple-gray-50'
          }`}
        >
          Assembly Otimizado
        </button>
      </div>

      {/* Content */}
      <div className="p-6">
        <div className="flex items-center gap-2 mb-4">
          <Cpu className="w-5 h-5 text-apple-gray-600" />
          <h2 className="text-xl font-semibold text-apple-gray-800">
            {activeTab === 'normal' ? 'Assembly' : 'Assembly Otimizado'}
          </h2>
        </div>
        
        <div className="bg-apple-gray-50 rounded-xl p-8 text-center">
          <p className="text-apple-gray-600">
            🚧 Funcionalidade em desenvolvimento
          </p>
          <p className="text-sm text-apple-gray-500 mt-2">
            Em breve você poderá visualizar o código Assembly aqui
          </p>
        </div>
      </div>
    </motion.div>
  );
}

export default AssemblyPage;

