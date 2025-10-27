import React, { createContext, useContext, useState, useEffect } from 'react';

const CodeContext = createContext();

export const useCodeContext = () => {
  const context = useContext(CodeContext);
  if (!context) {
    throw new Error('useCodeContext deve ser usado dentro de um CodeProvider');
  }
  return context;
};

export const CodeProvider = ({ children }) => {
  const [currentCodeId, setCurrentCodeId] = useState(() => {
    // Carrega o code_id do localStorage ao inicializar
    const saved = localStorage.getItem('minipar_current_code_id');
    return saved || null;
  });

  const [codeHistory, setCodeHistory] = useState(() => {
    // Carrega o histórico de códigos do localStorage
    const saved = localStorage.getItem('minipar_code_history');
    return saved ? JSON.parse(saved) : [];
  });

  // Salva o code_id atual no localStorage sempre que mudar
  useEffect(() => {
    if (currentCodeId) {
      localStorage.setItem('minipar_current_code_id', currentCodeId);
    } else {
      localStorage.removeItem('minipar_current_code_id');
    }
  }, [currentCodeId]);

  // Salva o histórico no localStorage sempre que mudar
  useEffect(() => {
    localStorage.setItem('minipar_code_history', JSON.stringify(codeHistory));
  }, [codeHistory]);

  const updateCurrentCodeId = (codeId) => {
    setCurrentCodeId(codeId);
    
    // Adiciona ao histórico se não existir
    if (codeId && !codeHistory.some(item => item.id === codeId)) {
      const newHistoryItem = {
        id: codeId,
        timestamp: new Date().toISOString(),
        uploadedAt: new Date().toLocaleString('pt-BR')
      };
      
      // Mantém apenas os últimos 20 itens
      setCodeHistory(prev => [newHistoryItem, ...prev].slice(0, 20));
    }
  };

  const clearCurrentCodeId = () => {
    setCurrentCodeId(null);
  };

  const clearHistory = () => {
    setCodeHistory([]);
    localStorage.removeItem('minipar_code_history');
  };

  const value = {
    currentCodeId,
    codeHistory,
    updateCurrentCodeId,
    clearCurrentCodeId,
    clearHistory,
    hasCodeLoaded: !!currentCodeId
  };

  return (
    <CodeContext.Provider value={value}>
      {children}
    </CodeContext.Provider>
  );
};

