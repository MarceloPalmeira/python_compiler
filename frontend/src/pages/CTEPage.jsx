import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { useCodeContext } from '../contexts/CodeContext';
import TACViewer from '../components/TACViewer';
import compilerAPI from '../services/api';

function CTEPage() {
  const { currentCodeId } = useCodeContext();
  const [tacCode, setTacCode] = useState(null);
  const [tacLoading, setTacLoading] = useState(false);
  const [tacError, setTacError] = useState(null);

  useEffect(() => {
    if (!currentCodeId) {
      setTacCode(null);
      return;
    }

    setTacLoading(true);
    setTacError(null);
    
    compilerAPI.getTAC(currentCodeId)
      .then(setTacCode)
      .catch(err => setTacError(err.message))
      .finally(() => setTacLoading(false));
  }, [currentCodeId]);

  if (!currentCodeId) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-morphism rounded-3xl apple-shadow-lg p-12 text-center"
      >
        <div className="text-6xl mb-4">⚙️</div>
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
      <TACViewer
        tacCode={tacCode}
        codeId={currentCodeId}
        loading={tacLoading}
        error={tacError}
      />
    </motion.div>
  );
}

export default CTEPage;

