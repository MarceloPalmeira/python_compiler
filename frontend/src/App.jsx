import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Header from './components/Header';
import CodeEditor from './components/CodeEditor';
import TokenViewer from './components/TokenViewer';
import SyntaxViewer from './components/SyntaxViewer';
import TabNavigation from './components/TabNavigation';
import CodeStatus from './components/CodeStatus';
import compilerAPI from './services/api';
import { CodeProvider } from './contexts/CodeContext';

const EXAMPLE_CODE = `# Exemplo MiniPar
var x: number = 10
var y: number = 20
var resultado: number = x + y

print("Resultado:", resultado)

func somar(a: number, b: number) -> number {
    return a + b
}

var total: number = somar(x, y)
print("Total:", total)`;

function App() {
  const [code, setCode] = useState(EXAMPLE_CODE);
  const [codeId, setCodeId] = useState(null);
  const [tokens, setTokens] = useState(null);
  const [syntaxTree, setSyntaxTree] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('editor');

  const handleCompile = async () => {
    setLoading(true);
    setError(null);
    
    try {
      // 1. Upload do código
      const id = await compilerAPI.uploadCode(code);
      setCodeId(id);
      
      // 2. Obter tokens (análise léxica)
      const tokensData = await compilerAPI.getTokens(id);
      setTokens(tokensData);
      
      // 3. Obter árvore sintática
      const syntaxData = await compilerAPI.getSyntaxTree(id);
      setSyntaxTree(syntaxData);
      
      // Mudar para a aba de tokens automaticamente
      setActiveTab('tokens');
    } catch (err) {
      setError(err.message);
      console.error('Erro na compilação:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <CodeProvider>
      <div className="min-h-screen bg-gradient-to-br from-apple-gray-50 via-white to-blue-50">
        <Header />
        
        <main className="container mx-auto px-4 py-8 max-w-7xl">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="glass-morphism rounded-3xl apple-shadow-lg overflow-hidden"
        >
          {/* Navegação por abas */}
          <TabNavigation 
            activeTab={activeTab} 
            setActiveTab={setActiveTab}
            hasResults={!!tokens}
          />

          {/* Mensagem de erro */}
          <AnimatePresence>
            {error && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: 'auto' }}
                exit={{ opacity: 0, height: 0 }}
                className="mx-6 mt-6"
              >
                <div className="bg-red-50 border border-red-200 text-red-800 px-6 py-4 rounded-xl">
                  <p className="font-medium">❌ Erro</p>
                  <p className="text-sm mt-1">{error}</p>
                </div>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Conteúdo das abas */}
          <div className="p-6">
            <AnimatePresence mode="wait">
              {activeTab === 'editor' && (
                <motion.div
                  key="editor"
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 20 }}
                  transition={{ duration: 0.3 }}
                >
                  <CodeEditor
                    code={code}
                    setCode={setCode}
                  />
                </motion.div>
              )}

              {activeTab === 'tokens' && (
                <motion.div
                  key="tokens"
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 20 }}
                  transition={{ duration: 0.3 }}
                >
                  <TokenViewer tokens={tokens} codeId={codeId} />
                </motion.div>
              )}

              {activeTab === 'syntax' && (
                <motion.div
                  key="syntax"
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: 20 }}
                  transition={{ duration: 0.3 }}
                >
                  <SyntaxViewer syntaxTree={syntaxTree} codeId={codeId} />
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        </motion.div>

        {/* Status do código carregado */}
        <CodeStatus />

        {/* Informações adicionais */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5, duration: 0.5 }}
          className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4"
        >
          <InfoCard
            icon="📝"
            title="Editor de Código"
            description="Escreva seu código MiniPar com syntax highlighting"
          />
          <InfoCard
            icon="🏷️"
            title="Análise Léxica"
            description="Visualize todos os tokens identificados pelo compilador"
          />
          <InfoCard
            icon="🌳"
            title="Árvore Sintática"
            description="Explore a estrutura sintática do seu código"
          />
        </motion.div>
      </main>
      </div>
    </CodeProvider>
  );
}

function InfoCard({ icon, title, description }) {
  return (
    <motion.div
      whileHover={{ scale: 1.02, y: -2 }}
      className="glass-morphism rounded-2xl p-6 apple-shadow cursor-default"
    >
      <div className="text-4xl mb-3">{icon}</div>
      <h3 className="font-semibold text-lg text-apple-gray-800 mb-2">{title}</h3>
      <p className="text-sm text-apple-gray-500">{description}</p>
    </motion.div>
  );
}

export default App;

