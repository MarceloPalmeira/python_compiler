import React from 'react';
import { motion } from 'framer-motion';
import {
  Cpu,
  Download,
  Loader2,
  AlertCircle,
  FileCode,
  Copy,
  Check,
} from 'lucide-react';

function AssemblyViewer({ asmCode, codeId, loading, error }) {
  const [copied, setCopied] = React.useState(false);

  const copyToClipboard = () => {
    if (asmCode) {
      navigator.clipboard.writeText(asmCode);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const downloadASM = () => {
    const blob = new Blob([asmCode || ''], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `assembly-code-${codeId || 'untitled'}.s`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Parse Assembly code to identify different instruction types
  const parseAssemblyLine = (line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith(';') || trimmed.startsWith('@')) {
      return { type: 'comment', content: line };
    }

    // Match labels (ending with :)
    if (/^\w+\s*:/.test(trimmed)) {
      return { type: 'label', content: line };
    }
    
    // Match directives (.text, .data, .global, etc)
    if (/^\.\w+/.test(trimmed)) {
      return { type: 'directive', content: line };
    }
    
    // Match instructions (mov, add, sub, ldr, str, etc)
    if (/^\s*\w+\s+(r\d+|#|\[|sp|lr|pc)/i.test(trimmed)) {
      return { type: 'instruction', content: line };
    }

    return { type: 'other', content: line };
  };

  // Estado de loading
  if (loading) {
    return (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-center py-20 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl border border-blue-200"
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
        >
          <Loader2 className="w-16 h-16 text-blue-500 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent mb-2">
          Gerando Código Assembly
        </h3>
        <p className="text-apple-gray-600">
          Aguarde enquanto compilamos o código para Assembly ARM...
        </p>
        <motion.div
          className="mt-4 flex justify-center gap-2"
          animate={{ opacity: [0.3, 1, 0.3] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          <div className="w-2 h-2 rounded-full bg-blue-500" />
          <div className="w-2 h-2 rounded-full bg-indigo-500" />
          <div className="w-2 h-2 rounded-full bg-purple-500" />
        </motion.div>
      </motion.div>
    );
  }

  // Estado de erro
  if (error) {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center py-20 bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl border border-red-200"
      >
        <motion.div
          animate={{ scale: [1, 1.1, 1] }}
          transition={{ duration: 2, repeat: Infinity }}
        >
          <AlertCircle className="w-16 h-16 text-red-500 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold bg-gradient-to-r from-red-600 to-orange-600 bg-clip-text text-transparent mb-2">
          Erro ao Gerar Código Assembly
        </h3>
        <p className="text-red-600 mb-4 font-medium">
          {error}
        </p>
        <p className="text-sm text-apple-gray-600 bg-white/50 px-4 py-2 rounded-lg inline-block">
          Verifique se o código foi compilado corretamente
        </p>
      </motion.div>
    );
  }

  // Sem dados
  if (!asmCode) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center py-20 bg-gradient-to-br from-slate-50 to-gray-100 rounded-2xl border border-slate-200"
      >
        <motion.div
          animate={{ y: [0, -10, 0] }}
          transition={{ duration: 2, repeat: Infinity, repeatDelay: 1 }}
        >
          <Cpu className="w-16 h-16 text-slate-400 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold text-apple-gray-800 mb-2">
          Nenhum Código Assembly Disponível
        </h3>
        <p className="text-apple-gray-600 mb-4">
          Compile seu código primeiro para ver o código Assembly ARM
        </p>
      </motion.div>
    );
  }

  const lines = asmCode.split('\n');
  const parsedLines = lines.map(parseAssemblyLine);
  const instructionCount = parsedLines.filter(l => l.type === 'instruction').length;
  const labelCount = parsedLines.filter(l => l.type === 'label').length;
  const directiveCount = parsedLines.filter(l => l.type === 'directive').length;
  const commentCount = parsedLines.filter(l => l.type === 'comment').length;

  return (
    <div className="space-y-6">
      {/* Cabeçalho */}
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="flex items-center justify-between"
      >
        <div className="space-y-2">
          <div className="flex items-center gap-3">
            <motion.div
              animate={{ rotate: [0, 10, -10, 0] }}
              transition={{ duration: 2, repeat: Infinity, repeatDelay: 3 }}
            >
              <Cpu className="w-8 h-8 text-blue-500" />
            </motion.div>
            <h2 className="text-3xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              Assembly ARM
            </h2>
          </div>
          <p className="text-sm text-apple-gray-500 ml-11">
            Código de máquina gerado a partir do CTE
          </p>
        </div>

        <div className="flex items-center gap-2">
          <motion.button
            whileHover={{ scale: 1.05, y: -2 }}
            whileTap={{ scale: 0.95 }}
            onClick={copyToClipboard}
            className="flex items-center gap-2 px-4 py-2 bg-white hover:bg-gray-50 
                     text-apple-gray-700 rounded-xl border border-apple-gray-300
                     transition-all apple-shadow font-medium"
          >
            {copied ? (
              <>
                <Check className="w-4 h-4 text-green-600" />
                <span className="text-green-600">Copiado!</span>
              </>
            ) : (
              <>
                <Copy className="w-4 h-4" />
                Copiar
              </>
            )}
          </motion.button>
          
          <motion.button
            whileHover={{ scale: 1.05, y: -2 }}
            whileTap={{ scale: 0.95 }}
            onClick={downloadASM}
            className="flex items-center gap-2 px-5 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 
                     hover:from-blue-600 hover:to-indigo-700 text-white rounded-xl 
                     transition-all apple-shadow font-medium"
          >
            <Download className="w-4 h-4" />
            Baixar (.s)
          </motion.button>
        </div>
      </motion.div>

      {/* Estatísticas */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="grid grid-cols-2 md:grid-cols-4 gap-4"
      >
        <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-4 border border-blue-200">
          <div className="flex items-center gap-2 mb-2">
            <FileCode className="w-5 h-5 text-blue-600" />
            <span className="text-sm font-semibold text-blue-900">Instruções</span>
          </div>
          <p className="text-2xl font-bold text-blue-700">{instructionCount}</p>
        </div>
        <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-4 border border-purple-200">
          <div className="flex items-center gap-2 mb-2">
            <Cpu className="w-5 h-5 text-purple-600" />
            <span className="text-sm font-semibold text-purple-900">Diretivas</span>
          </div>
          <p className="text-2xl font-bold text-purple-700">{directiveCount}</p>
        </div>
        <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-xl p-4 border border-emerald-200">
          <div className="flex items-center gap-2 mb-2">
            <FileCode className="w-5 h-5 text-emerald-600" />
            <span className="text-sm font-semibold text-emerald-900">Rótulos</span>
          </div>
          <p className="text-2xl font-bold text-emerald-700">{labelCount}</p>
        </div>
        <div className="bg-gradient-to-br from-amber-50 to-orange-50 rounded-xl p-4 border border-amber-200">
          <div className="flex items-center gap-2 mb-2">
            <FileCode className="w-5 h-5 text-amber-600" />
            <span className="text-sm font-semibold text-amber-900">Comentários</span>
          </div>
          <p className="text-2xl font-bold text-amber-700">{commentCount}</p>
        </div>
      </motion.div>

      {/* Visualização do código */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="bg-white rounded-2xl border border-blue-200 overflow-hidden apple-shadow"
      >
        <div className="bg-gradient-to-r from-blue-50 via-indigo-50 to-purple-50 px-6 py-4 border-b border-blue-200 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
            >
              <FileCode className="w-5 h-5 text-blue-600" />
            </motion.div>
            <div>
              <span className="text-sm font-semibold text-blue-900">
                Código Assembly ARM
              </span>
              <p className="text-xs text-blue-700 mt-0.5">
                Compatível com CPULator
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs text-blue-700 bg-white px-3 py-1 rounded-md border border-blue-200 font-medium">
              {lines.length} linhas
            </span>
          </div>
        </div>

        <div className="relative">
          {/* Números de linha e código */}
          <div className="flex bg-gradient-to-br from-white via-gray-50/30 to-blue-50/20">
            {/* Números de linha */}
            <div className="select-none bg-gray-100 border-r border-gray-300 px-4 py-3 text-right text-xs text-gray-500 font-mono">
              {lines.map((_, index) => (
                <div key={index} className="leading-relaxed">
                  {index + 1}
                </div>
              ))}
            </div>
            
            {/* Código Assembly */}
            <div className="flex-1 overflow-x-auto">
              <div className="p-3">
                {parsedLines.map((lineObj, index) => {
                  const { type, content } = lineObj;
                  const baseClasses = 'py-1 px-4 font-mono text-sm leading-relaxed';
                  
                  let lineElement;
                  switch (type) {
                    case 'comment':
                      lineElement = (
                        <div className={`${baseClasses} text-gray-500 italic`}>
                          {content}
                        </div>
                      );
                      break;
                    case 'label':
                      lineElement = (
                        <div className={`${baseClasses} text-emerald-700 font-semibold`}>
                          {content}
                        </div>
                      );
                      break;
                    case 'directive':
                      lineElement = (
                        <div className={`${baseClasses} text-purple-700 font-medium`}>
                          {content}
                        </div>
                      );
                      break;
                    case 'instruction':
                      lineElement = (
                        <div className={`${baseClasses} text-blue-700`}>
                          {content}
                        </div>
                      );
                      break;
                    default:
                      lineElement = (
                        <div className={`${baseClasses} text-gray-800`}>
                          {content}
                        </div>
                      );
                  }

                  return (
                    <motion.div
                      key={index}
                      initial={{ opacity: 0, x: -10 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ duration: 0.2, delay: index * 0.01 }}
                      className="flex items-start"
                    >
                      {lineElement}
                    </motion.div>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Informações sobre Assembly */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
        className="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl p-5 border border-indigo-200 apple-shadow"
      >
        <h3 className="text-sm font-semibold text-indigo-900 mb-3 flex items-center gap-2">
          <Cpu className="w-4 h-4" />
          Sobre Assembly ARM
        </h3>
        <p className="text-sm text-indigo-800 leading-relaxed mb-3">
          Assembly ARM é uma linguagem de baixo nível que representa instruções diretamente executáveis pelo processador ARM. 
          O código gerado é compatível com o CPULator, um simulador online de arquitetura ARM, permitindo visualizar e testar 
          a execução do programa em tempo real. Cada instrução corresponde diretamente a uma operação da CPU.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-4">
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Instruções</span>
            <p className="text-xs text-indigo-600 mt-1">Operações básicas do processador (mov, add, sub, ldr, str, etc)</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Diretivas</span>
            <p className="text-xs text-indigo-600 mt-1">Comandos do assembler (.text, .data, .global)</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Rótulos</span>
            <p className="text-xs text-indigo-600 mt-1">Marcadores de endereço para controle de fluxo</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Comentários</span>
            <p className="text-xs text-indigo-600 mt-1">Anotações explicativas (iniciados com ; ou @)</p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default AssemblyViewer;


