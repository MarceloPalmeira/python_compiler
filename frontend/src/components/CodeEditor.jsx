import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Loader2, FileCode, Upload, Check, X } from 'lucide-react';
import Editor from '@monaco-editor/react';
import { useCodeContext } from '../contexts/CodeContext';
import compilerAPI from '../services/api';

function CodeEditor({ code, setCode }) {
  const { currentCodeId, updateCurrentCodeId, hasCodeLoaded } =
    useCodeContext();
  const [uploading, setUploading] = useState(false);
  const [uploadStatus, setUploadStatus] = useState(null); // 'success' | 'error' | null
  const [uploadMessage, setUploadMessage] = useState('');

  const handleUpload = async () => {
    if (!code.trim()) {
      setUploadStatus('error');
      setUploadMessage('O código está vazio');
      setTimeout(() => setUploadStatus(null), 3000);
      return;
    }

    setUploading(true);
    setUploadStatus(null);

    try {
      const codeId = await compilerAPI.uploadCode(code);
      updateCurrentCodeId(codeId);
      setUploadStatus('success');
      setUploadMessage(`Código enviado! ID: ${codeId.substring(0, 8)}...`);

      // Limpa a mensagem após 5 segundos
      setTimeout(() => setUploadStatus(null), 5000);
    } catch (error) {
      setUploadStatus('error');
      setUploadMessage(error.message || 'Erro ao fazer upload');
      setTimeout(() => setUploadStatus(null), 5000);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="space-y-4">
      {/* Cabeçalho com título */}
      <div className="flex items-center gap-2">
        <FileCode className="w-5 h-5 text-apple-gray-600" />
        <h2 className="text-xl font-semibold text-apple-gray-800">
          Editor de Código MiniPar
        </h2>
        {hasCodeLoaded && (
          <span className="text-xs bg-green-100 text-green-700 px-2 py-1 rounded-full">
            Código Carregado
          </span>
        )}
      </div>

      {/* Editor de código */}
      <motion.div
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.3 }}
        className="rounded-2xl overflow-hidden apple-shadow border border-apple-gray-200"
      >
        <Editor
          height="500px"
          defaultLanguage="python"
          value={code}
          onChange={(value) => setCode(value || '')}
          theme="vs-light"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            fontFamily: "'Fira Code', 'Consolas', 'Monaco', monospace",
            lineNumbers: 'on',
            roundedSelection: true,
            scrollBeyondLastLine: false,
            automaticLayout: true,
            padding: { top: 16, bottom: 16 },
            smoothScrolling: true,
            cursorBlinking: 'smooth',
            cursorSmoothCaretAnimation: 'on',
            renderLineHighlight: 'all',
            lineHeight: 24,
          }}
        />
      </motion.div>

      {/* Botão de Upload - Canto inferior direito */}
      <div className="flex justify-end">
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={handleUpload}
          disabled={uploading || !code.trim()}
          className={`
            flex items-center gap-2 px-8 py-3 rounded-xl font-medium
            transition-all duration-200 apple-shadow
            ${
              uploading || !code.trim()
                ? 'bg-apple-gray-200 text-apple-gray-400 cursor-not-allowed'
                : 'bg-purple-500 text-white hover:bg-purple-600'
            }
          `}
        >
          {uploading ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              Enviando código...
            </>
          ) : (
            <>
              <Upload className="w-5 h-5" />
              Fazer Upload do Código
            </>
          )}
        </motion.button>
      </div>

      {/* Mensagem de status do upload */}
      <AnimatePresence>
        {uploadStatus && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className={`
              flex items-center gap-2 px-4 py-3 rounded-xl border
              ${
                uploadStatus === 'success'
                  ? 'bg-green-50 border-green-200 text-green-800'
                  : 'bg-red-50 border-red-200 text-red-800'
              }
            `}
          >
            {uploadStatus === 'success' ? (
              <Check className="w-5 h-5" />
            ) : (
              <X className="w-5 h-5" />
            )}
            <span className="text-sm font-medium">{uploadMessage}</span>
            {uploadStatus === 'success' && currentCodeId && (
              <code className="ml-auto text-xs bg-white px-2 py-1 rounded border border-green-300">
                {currentCodeId}
              </code>
            )}
          </motion.div>
        )}
      </AnimatePresence>

      <div className="bg-apple-gray-50 rounded-xl p-4 border border-apple-gray-200">
        <h3 className="text-sm font-semibold text-apple-gray-700 mb-2">
          💡 Dicas de Sintaxe MiniPar
        </h3>
        <ul className="text-sm text-apple-gray-600 space-y-1">
          <li>
            • Declarações:{' '}
            <code className="bg-white px-2 py-0.5 rounded">
              var nome: tipo = valor
            </code>
          </li>
          <li>
            • Tipos:{' '}
            <code className="bg-white px-2 py-0.5 rounded">number</code>,{' '}
            <code className="bg-white px-2 py-0.5 rounded">bool</code>,{' '}
            <code className="bg-white px-2 py-0.5 rounded">string</code>
          </li>
          <li>
            • Funções:{' '}
            <code className="bg-white px-2 py-0.5 rounded">
              func nome(param: tipo) -&gt; tipo &#123; ... &#125;
            </code>
          </li>
          <li>
            • Estruturas:{' '}
            <code className="bg-white px-2 py-0.5 rounded">if/else</code>,{' '}
            <code className="bg-white px-2 py-0.5 rounded">while</code>,{' '}
            <code className="bg-white px-2 py-0.5 rounded">for</code>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default CodeEditor;
