import React from 'react';
import { motion } from 'framer-motion';
import {
  Code2,
  Download,
  Loader2,
  AlertCircle,
  FileCode,
  Copy,
  Check,
} from 'lucide-react';

function TACViewer({ tacCode, codeId, loading, error }) {
  const [copied, setCopied] = React.useState(false);

  const copyToClipboard = () => {
    if (tacCode) {
      navigator.clipboard.writeText(tacCode);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  const downloadCTE = () => {
    const blob = new Blob([tacCode || ''], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `cte-code-${codeId || 'untitled'}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Parse CTE code to identify different instruction types
  const parseCTELine = (line) => {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith(';')) {
      return { type: 'comment', content: line };
    }

    // Match common CTE patterns
    if (/^\w+\s*:/.test(trimmed)) {
      return { type: 'label', content: line };
    }
    
    if (/^\w+\s*=\s*/.test(trimmed)) {
      return { type: 'assignment', content: line };
    }
    
    if (/^(if|goto|call|param|return)\b/.test(trimmed)) {
      return { type: 'control', content: line };
    }

    return { type: 'instruction', content: line };
  };


  // Estado de loading
  if (loading) {
    return (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-center py-20 bg-gradient-to-br from-cyan-50 to-blue-50 rounded-2xl border border-cyan-200"
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
        >
          <Loader2 className="w-16 h-16 text-cyan-500 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold bg-gradient-to-r from-cyan-600 to-blue-600 bg-clip-text text-transparent mb-2">
          Gerando Código CTE
        </h3>
        <p className="text-apple-gray-600">
          Aguarde enquanto compilamos o código para Código de Três Endereços...
        </p>
        <motion.div
          className="mt-4 flex justify-center gap-2"
          animate={{ opacity: [0.3, 1, 0.3] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          <div className="w-2 h-2 rounded-full bg-cyan-500" />
          <div className="w-2 h-2 rounded-full bg-blue-500" />
          <div className="w-2 h-2 rounded-full bg-indigo-500" />
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
          Erro ao Gerar Código CTE
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
  if (!tacCode) {
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
          <Code2 className="w-16 h-16 text-slate-400 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold text-apple-gray-800 mb-2">
          Nenhum Código CTE Disponível
        </h3>
        <p className="text-apple-gray-600 mb-4">
          Compile seu código primeiro para ver o código intermediário CTE
        </p>
      </motion.div>
    );
  }

  const lines = tacCode.split('\n');
  const parsedLines = lines.map(parseCTELine);
  const instructionCount = parsedLines.filter(l => l.type !== 'comment').length;
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
              <Code2 className="w-8 h-8 text-cyan-500" />
            </motion.div>
            <h2 className="text-3xl font-bold bg-gradient-to-r from-cyan-600 to-blue-600 bg-clip-text text-transparent">
              Código de Três Endereços (CTE)
            </h2>
          </div>
          <p className="text-sm text-apple-gray-500 ml-11">
            Código intermediário gerado a partir da AST
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
            onClick={downloadCTE}
            className="flex items-center gap-2 px-5 py-3 bg-gradient-to-r from-cyan-500 to-blue-600 
                     hover:from-cyan-600 hover:to-blue-700 text-white rounded-xl 
                     transition-all apple-shadow font-medium"
          >
            <Download className="w-4 h-4" />
            Baixar
          </motion.button>
        </div>
      </motion.div>

      {/* Estatísticas */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-4"
      >
        <div className="bg-gradient-to-br from-cyan-50 to-blue-50 rounded-xl p-4 border border-cyan-200">
          <div className="flex items-center gap-2 mb-2">
            <FileCode className="w-5 h-5 text-cyan-600" />
            <span className="text-sm font-semibold text-cyan-900">Instruções</span>
          </div>
          <p className="text-2xl font-bold text-cyan-700">{instructionCount}</p>
        </div>
        <div className="bg-gradient-to-br from-purple-50 to-pink-50 rounded-xl p-4 border border-purple-200">
          <div className="flex items-center gap-2 mb-2">
            <Code2 className="w-5 h-5 text-purple-600" />
            <span className="text-sm font-semibold text-purple-900">Linhas</span>
          </div>
          <p className="text-2xl font-bold text-purple-700">{lines.length}</p>
        </div>
        <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-xl p-4 border border-emerald-200">
          <div className="flex items-center gap-2 mb-2">
            <FileCode className="w-5 h-5 text-emerald-600" />
            <span className="text-sm font-semibold text-emerald-900">Comentários</span>
          </div>
          <p className="text-2xl font-bold text-emerald-700">{commentCount}</p>
        </div>
      </motion.div>

      {/* Visualização do código */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="bg-white rounded-2xl border border-cyan-200 overflow-hidden apple-shadow"
      >
        <div className="bg-gradient-to-r from-cyan-50 via-blue-50 to-indigo-50 px-6 py-4 border-b border-cyan-200 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
            >
              <FileCode className="w-5 h-5 text-cyan-600" />
            </motion.div>
            <div>
              <span className="text-sm font-semibold text-cyan-900">
                Código CTE
              </span>
              <p className="text-xs text-cyan-700 mt-0.5">
                Código intermediário de Três Endereços
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs text-cyan-700 bg-white px-3 py-1 rounded-md border border-cyan-200 font-medium">
              {lines.length} linhas
            </span>
          </div>
        </div>

        <div className="relative">
          {/* Números de linha e código */}
          <div className="flex bg-gradient-to-br from-white via-gray-50/30 to-cyan-50/20">
            {/* Números de linha */}
            <div className="select-none bg-gray-100 border-r border-gray-300 px-4 py-3 text-right text-xs text-gray-500 font-mono">
              {lines.map((_, index) => (
                <div key={index} className="leading-relaxed">
                  {index + 1}
                </div>
              ))}
            </div>
            
            {/* Código CTE */}
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
                    case 'assignment':
                      lineElement = (
                        <div className={`${baseClasses} text-blue-700`}>
                          {content}
                        </div>
                      );
                      break;
                    case 'control':
                      lineElement = (
                        <div className={`${baseClasses} text-purple-700 font-medium`}>
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

      {/* Informações sobre CTE */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
        className="bg-gradient-to-br from-indigo-50 to-purple-50 rounded-2xl p-5 border border-indigo-200 apple-shadow"
      >
        <h3 className="text-sm font-semibold text-indigo-900 mb-3 flex items-center gap-2">
          <Code2 className="w-4 h-4" />
          Sobre Código de Três Endereços (CTE)
        </h3>
        <p className="text-sm text-indigo-800 leading-relaxed mb-3">
          Código de Três Endereços (CTE) é uma representação intermediária do código que usa no máximo três endereços (operandos) por instrução. 
          Esta representação facilita a geração de código otimizado e é um passo crucial na pipeline de compilação.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mt-4">
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Rótulos</span>
            <p className="text-xs text-indigo-600 mt-1">Marcadores de linha para controle de fluxo</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Atribuições</span>
            <p className="text-xs text-indigo-600 mt-1">Instruções de atribuição com até 3 operandos</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Controle</span>
            <p className="text-xs text-indigo-600 mt-1">Instruções de controle de fluxo (if, goto, call)</p>
          </div>
          <div className="bg-white/60 rounded-lg p-3 border border-indigo-200">
            <span className="text-xs font-semibold text-indigo-700">Comentários</span>
            <p className="text-xs text-indigo-600 mt-1">Comentários e anotações explicativas</p>
          </div>
        </div>
      </motion.div>
    </div>
  );
}

export default TACViewer;
