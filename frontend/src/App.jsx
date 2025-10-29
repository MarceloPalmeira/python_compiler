import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import Header from './components/Header';
import CodeStatus from './components/CodeStatus';
import EditorPage from './pages/EditorPage';
import LexicalPage from './pages/LexicalPage';
import SyntaxPage from './pages/SyntaxPage';
import LLVMPage from './pages/LLVMPage';
import AssemblyPage from './pages/AssemblyPage';
import OptimizationPage from './pages/OptimizationPage';
import { CodeProvider } from './contexts/CodeContext';

function App() {
  return (
    <CodeProvider>
      <div className="min-h-screen bg-gray-300 from-apple-gray-50 via-white to-blue-50">
        <Header />
        
        <main className="container mx-auto px-4 py-8 max-w-7xl">
          <Routes>
            <Route path="/" element={<EditorPage />} />
            <Route path="/editor" element={<Navigate to="/" replace />} />
            <Route path="/lexical" element={<LexicalPage />} />
            <Route path="/syntax" element={<SyntaxPage />} />
            <Route path="/llvm" element={<LLVMPage />} />
            <Route path="/assembly" element={<AssemblyPage />} />
            <Route path="/optimization" element={<OptimizationPage />} />
          </Routes>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5 }}
            className="mt-8"
          >
            <CodeStatus />
          </motion.div>
        </main>
      </div>
    </CodeProvider>
  );
}

export default App;
