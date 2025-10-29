import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { motion } from 'framer-motion';
import {
  TreePine,
  Download,
  FileJson,
  Loader2,
  AlertCircle,
  ChevronRight,
  ChevronDown,
  FileCode,
  GitBranch,
} from 'lucide-react';

function SyntaxViewer({ syntaxTree, codeId, loading, error }) {
  const { treeData, parseError } = useMemo(() => parseSyntaxTreeInput(syntaxTree), [syntaxTree]);

  const [expandedNodes, setExpandedNodes] = useState(() => new Set(['root']));

  useEffect(() => {
    setExpandedNodes(new Set(['root']));
  }, [treeData]);

  const toggleNode = useCallback((path) => {
    setExpandedNodes((prev) => {
      const next = new Set(prev);
      if (next.has(path)) {
        next.delete(path);
      } else {
        next.add(path);
      }
      return next;
    });
  }, []);

  const downloadSyntaxTree = () => {
    const data = typeof syntaxTree === 'string' ? syntaxTree : JSON.stringify(syntaxTree, null, 2);
    const blob = new Blob([data], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `syntax-tree-${codeId}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Estado de loading
  if (loading) {
    return (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-center py-20 bg-gradient-to-br from-blue-50 to-purple-50 rounded-2xl border border-blue-200"
      >
        <motion.div
          animate={{ rotate: 360 }}
          transition={{ duration: 1, repeat: Infinity, ease: "linear" }}
        >
          <Loader2 className="w-16 h-16 text-blue-500 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2">
          Carregando Árvore Sintática
        </h3>
        <p className="text-apple-gray-600">
          Aguarde enquanto processamos o código...
        </p>
        <motion.div
          className="mt-4 flex justify-center gap-2"
          animate={{ opacity: [0.3, 1, 0.3] }}
          transition={{ duration: 1.5, repeat: Infinity }}
        >
          <div className="w-2 h-2 rounded-full bg-blue-500" />
          <div className="w-2 h-2 rounded-full bg-purple-500" />
          <div className="w-2 h-2 rounded-full bg-pink-500" />
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
          Erro ao Carregar Árvore Sintática
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
  if (!syntaxTree) {
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
          <TreePine className="w-16 h-16 text-slate-400 mx-auto mb-4" />
        </motion.div>
        <h3 className="text-xl font-semibold text-apple-gray-800 mb-2">
          Nenhuma Árvore Sintática Disponível
        </h3>
        <p className="text-apple-gray-600 mb-4">
          Compile seu código primeiro para ver a árvore sintática
        </p>
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-emerald-500 to-blue-500 text-white rounded-lg font-medium"
        >
          <FileCode className="w-4 h-4" />
          Compilar Código
        </motion.div>
      </motion.div>
    );
  }

  const syntaxTreeString = typeof syntaxTree === 'string'
    ? syntaxTree
    : JSON.stringify(syntaxTree, null, 2);

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
              <TreePine className="w-8 h-8 text-emerald-500" />
            </motion.div>
            <h2 className="text-3xl font-bold bg-gradient-to-r from-emerald-600 to-blue-600 bg-clip-text text-transparent">
              Análise Sintática
            </h2>
          </div>
          <p className="text-sm text-apple-gray-500 ml-11">
            Explore a árvore sintática como uma estrutura de pastas interativa
          </p>
        </div>

        <motion.button
          whileHover={{ scale: 1.05, y: -2 }}
          whileTap={{ scale: 0.95 }}
          onClick={downloadSyntaxTree}
          className="flex items-center gap-2 px-5 py-3 bg-gradient-to-r from-blue-500 to-blue-600 
                     hover:from-blue-600 hover:to-blue-700 text-white rounded-xl 
                     transition-all apple-shadow font-medium"
        >
          <Download className="w-4 h-4" />
          Baixar
        </motion.button>
      </motion.div>

      {/* Visualização em árvore */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
        className="bg-white rounded-2xl border border-emerald-200 overflow-hidden apple-shadow"
      >
        <div className="bg-gradient-to-r from-emerald-50 via-teal-50 to-cyan-50 px-6 py-4 border-b border-emerald-200 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <motion.div
              whileHover={{ rotate: 360 }}
              transition={{ duration: 0.5 }}
            >
              <GitBranch className="w-5 h-5 text-emerald-600" />
            </motion.div>
            <div>
              <span className="text-sm font-semibold text-emerald-900">
                Navegação pela Árvore Sintática
              </span>
              <p className="text-xs text-emerald-700 mt-0.5">
                Clique nos nós para expandir ou recolher
              </p>
            </div>
          </div>
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => {
              if (expandedNodes.size > 1) {
                setExpandedNodes(new Set(['root']));
              } else {
                const allPaths = new Set(['root']);
                const collectPaths = (obj, parentPath = 'root') => {
                  if (obj && typeof obj === 'object') {
                    if (Array.isArray(obj)) {
                      obj.forEach((_, index) => {
                        const path = `${parentPath}.${index}`;
                        allPaths.add(path);
                        collectPaths(obj[index], path);
                      });
                    } else {
                      Object.keys(obj).forEach((key) => {
                        const path = `${parentPath}.${key}`;
                        allPaths.add(path);
                        collectPaths(obj[key], path);
                      });
                    }
                  }
                };
                collectPaths(treeData);
                setExpandedNodes(allPaths);
              }
            }}
            className="flex items-center gap-2 px-3 py-1.5 bg-white hover:bg-emerald-100 
                       text-emerald-700 rounded-lg transition-colors text-xs font-medium border border-emerald-200"
          >
            {expandedNodes.size > 1 ? 'Recolher Todos' : 'Expandir Todos'}
          </motion.button>
        </div>

        <div className="p-6 bg-gradient-to-br from-white via-emerald-50/20 to-blue-50/20">
          {treeData ? (
            <SyntaxTreeExplorer
              data={treeData}
              expandedNodes={expandedNodes}
              toggleNode={toggleNode}
            />
          ) : (
            <div className="text-sm text-apple-gray-500 bg-red-50 border border-red-200 rounded-lg p-4">
              {parseError
                ? (
                  <>
                    <div className="flex items-center gap-2 mb-2">
                      <AlertCircle className="w-4 h-4 text-red-500" />
                      <span className="font-semibold text-red-700">
                        Não foi possível exibir a árvore sintática
                      </span>
                    </div>
                    <span className="text-red-600 text-xs">
                      {parseError}
                    </span>
                  </>
                )
                : 'A árvore sintática está vazia.'}
            </div>
          )}
        </div>
      </motion.div>

      {/* Visualização raw */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.05 }}
        className="bg-white rounded-2xl border border-apple-gray-200 overflow-hidden apple-shadow"
      >
        <div className="bg-gradient-to-r from-apple-gray-50 to-slate-100 px-6 py-3 border-b border-apple-gray-200 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <FileJson className="w-4 h-4 text-apple-gray-600" />
            <span className="text-sm font-medium text-apple-gray-700">
              Representação Bruta (texto)
            </span>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-xs text-apple-gray-500 bg-white px-2 py-1 rounded-md border border-apple-gray-200">
              {syntaxTreeString.split('\n').length} linhas
            </span>
            <span className="text-xs text-apple-gray-500 bg-white px-2 py-1 rounded-md border border-apple-gray-200">
              {(syntaxTreeString.length / 1024).toFixed(1)} KB
            </span>
          </div>
        </div>

        <div className="p-6 max-h-[400px] overflow-auto bg-gradient-to-br from-slate-50 to-gray-50">
          <pre className="text-sm font-mono text-apple-gray-800 whitespace-pre leading-relaxed">
            {syntaxTreeString}
          </pre>
        </div>
      </motion.div>

      {/* Legenda de Cores */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.1 }}
        className="bg-gradient-to-br from-purple-50 to-blue-50 rounded-2xl p-5 border border-purple-200 apple-shadow"
      >
        <h3 className="text-sm font-semibold text-purple-900 mb-3 flex items-center gap-2">
          <TreePine className="w-4 h-4" />
          Legenda de Cores
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
          <ColorLegendItem color="violet" label="Declarações" />
          <ColorLegendItem color="blue" label="Statements" />
          <ColorLegendItem color="emerald" label="Expressões" />
          <ColorLegendItem color="fuchsia" label="Literais" />
          <ColorLegendItem color="orange" label="Operadores" />
          <ColorLegendItem color="cyan" label="Funções" />
          <ColorLegendItem color="amber" label="Identificadores" />
          <ColorLegendItem color="red" label="Controle" />
          <ColorLegendItem color="lime" label="Blocos" />
          <ColorLegendItem color="teal" label="Loops" />
          <ColorLegendItem color="pink" label="Parâmetros" />
          <ColorLegendItem color="indigo" label="Tipos" />
        </div>
      </motion.div>

      {/* Informações adicionais */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3, delay: 0.15 }}
        className="bg-gradient-to-br from-blue-50 to-cyan-50 rounded-2xl p-5 border border-blue-200 apple-shadow"
      >
        <h3 className="text-sm font-semibold text-blue-900 mb-2 flex items-center gap-2">
          <TreePine className="w-4 h-4" />
          Sobre a Árvore Sintática
        </h3>
        <p className="text-sm text-blue-800 leading-relaxed">
          A árvore sintática abstrata (AST) representa a estrutura hierárquica do seu código.
          Cada nó representa uma construção sintática como expressões, declarações e comandos.
          Use as cores para identificar rapidamente diferentes tipos de elementos no código.
        </p>
      </motion.div>
    </div>
  );
}

function ColorLegendItem({ color, label }) {
  const colorConfig = {
    violet: {
      bg: 'bg-violet-100',
      text: 'text-violet-700',
      border: 'border-violet-300',
      dot: 'bg-violet-500',
      shadow: 'shadow-violet-200',
    },
    blue: {
      bg: 'bg-blue-100',
      text: 'text-blue-700',
      border: 'border-blue-300',
      dot: 'bg-blue-500',
      shadow: 'shadow-blue-200',
    },
    emerald: {
      bg: 'bg-emerald-100',
      text: 'text-emerald-700',
      border: 'border-emerald-300',
      dot: 'bg-emerald-500',
      shadow: 'shadow-emerald-200',
    },
    fuchsia: {
      bg: 'bg-fuchsia-100',
      text: 'text-fuchsia-700',
      border: 'border-fuchsia-300',
      dot: 'bg-fuchsia-500',
      shadow: 'shadow-fuchsia-200',
    },
    orange: {
      bg: 'bg-orange-100',
      text: 'text-orange-700',
      border: 'border-orange-300',
      dot: 'bg-orange-500',
      shadow: 'shadow-orange-200',
    },
    cyan: {
      bg: 'bg-cyan-100',
      text: 'text-cyan-700',
      border: 'border-cyan-300',
      dot: 'bg-cyan-500',
      shadow: 'shadow-cyan-200',
    },
    amber: {
      bg: 'bg-amber-100',
      text: 'text-amber-700',
      border: 'border-amber-300',
      dot: 'bg-amber-500',
      shadow: 'shadow-amber-200',
    },
    red: {
      bg: 'bg-red-100',
      text: 'text-red-700',
      border: 'border-red-300',
      dot: 'bg-red-500',
      shadow: 'shadow-red-200',
    },
    lime: {
      bg: 'bg-lime-100',
      text: 'text-lime-700',
      border: 'border-lime-300',
      dot: 'bg-lime-500',
      shadow: 'shadow-lime-200',
    },
    teal: {
      bg: 'bg-teal-100',
      text: 'text-teal-700',
      border: 'border-teal-300',
      dot: 'bg-teal-500',
      shadow: 'shadow-teal-200',
    },
    pink: {
      bg: 'bg-pink-100',
      text: 'text-pink-700',
      border: 'border-pink-300',
      dot: 'bg-pink-500',
      shadow: 'shadow-pink-200',
    },
    indigo: {
      bg: 'bg-indigo-100',
      text: 'text-indigo-700',
      border: 'border-indigo-300',
      dot: 'bg-indigo-500',
      shadow: 'shadow-indigo-200',
    },
  };

  const config = colorConfig[color];

  return (
    <motion.div
      whileHover={{ scale: 1.05, y: -2 }}
      transition={{ duration: 0.2 }}
      className={`flex items-center gap-2 px-3 py-2 rounded-lg border ${config.bg} ${config.text} ${config.border} ${config.shadow} shadow-sm text-xs font-medium cursor-pointer`}
    >
      <motion.div
        whileHover={{ scale: 1.3, rotate: 180 }}
        transition={{ duration: 0.3 }}
        className={`w-3 h-3 rounded-full ${config.dot} shadow-md`}
      />
      {label}
    </motion.div>
  );
}

export default SyntaxViewer;

function parseSyntaxTreeInput(rawSyntaxTree) {
  if (!rawSyntaxTree) {
    return { treeData: null, parseError: null };
  }

  if (typeof rawSyntaxTree !== 'string') {
    return { treeData: rawSyntaxTree, parseError: null };
  }

  const strategies = [
    () => JSON.parse(rawSyntaxTree),
    () => {
      const normalized = normalizeSingleQuotedJson(rawSyntaxTree);
      return JSON.parse(normalized);
    },
    () => {
      const trimmed = rawSyntaxTree.trim();
      if (!/^[\[{]/.test(trimmed)) {
        throw new Error('Formato inesperado para a árvore sintática.');
      }
      const fn = Function;
      return fn(`"use strict"; return (${trimmed});`)();
    },
  ];

  let lastError = null;

  for (const parseStrategy of strategies) {
    try {
      const parsed = parseStrategy();
      if (parsed && typeof parsed === 'object') {
        return { treeData: parsed, parseError: null };
      }
    } catch (err) {
      lastError = err instanceof Error ? err.message : String(err);
    }
  }

  return {
    treeData: null,
    parseError: lastError || 'Erro desconhecido ao interpretar a árvore sintática.',
  };
}

function normalizeSingleQuotedJson(input) {
  return input.replace(/'((?:[^'\\]|\\.)*)'/g, (_match, content) => {
    const unescaped = content.replace(/\\'/g, "'");
    return JSON.stringify(unescaped);
  });
}

function getNodeStyles({ nodeKey, isBranch, isArray, value }) {
  if (isArray) {
    return {
      accent: '#a855f7',
      iconClass: 'text-purple-500',
      badgeBg: 'bg-purple-100',
      badgeText: 'text-purple-700',
      badgeLabel: 'Array',
      valueColor: 'text-purple-600',
      metaText: 'text-purple-600',
      rowHover: 'hover:bg-purple-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-purple-100 text-purple-500/70',
    };
  }

  if (isBranch) {
    const typeName = value && typeof value === 'object' && typeof value.type === 'string'
      ? value.type
      : null;

    if (typeName) {
      return {
        ...getTypeColorTokens(typeName),
        badgeLabel: typeName,
      };
    }

    return {
      accent: '#0ea5e9',
      iconClass: 'text-sky-500',
      badgeBg: 'bg-sky-100',
      badgeText: 'text-sky-700',
      badgeLabel: 'Objeto',
      valueColor: 'text-sky-600',
      metaText: 'text-sky-600',
      rowHover: 'hover:bg-sky-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-sky-100 text-sky-500/70',
    };
  }

  if (value === null) {
    return {
      accent: '#6b7280',
      iconClass: 'text-slate-400',
      badgeBg: 'bg-slate-200',
      badgeText: 'text-slate-600',
      badgeLabel: 'Null',
      valueColor: 'text-slate-600',
      metaText: 'text-slate-500',
      rowHover: 'hover:bg-slate-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-slate-100 text-slate-500',
    };
  }

  const valueType = typeof value;

  if (valueType === 'string') {
    return {
      accent: '#10b981',
      iconClass: 'text-emerald-500',
      badgeBg: 'bg-emerald-100',
      badgeText: 'text-emerald-700',
      badgeLabel: 'String',
      valueColor: 'text-emerald-600',
      metaText: 'text-emerald-600',
      rowHover: 'hover:bg-emerald-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-emerald-100 text-emerald-500',
    };
  }

  if (valueType === 'number') {
    return {
      accent: '#f59e0b',
      iconClass: 'text-amber-500',
      badgeBg: 'bg-amber-100',
      badgeText: 'text-amber-700',
      badgeLabel: 'Number',
      valueColor: 'text-amber-600',
      metaText: 'text-amber-600',
      rowHover: 'hover:bg-amber-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-amber-100 text-amber-500',
    };
  }

  if (valueType === 'boolean') {
    return {
      accent: '#f97316',
      iconClass: 'text-orange-500',
      badgeBg: 'bg-orange-100',
      badgeText: 'text-orange-700',
      badgeLabel: 'Boolean',
      valueColor: 'text-orange-600',
      metaText: 'text-orange-600',
      rowHover: 'hover:bg-orange-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-orange-100 text-orange-500',
    };
  }

  if (valueType === 'undefined') {
    return {
      accent: '#94a3b8',
      iconClass: 'text-slate-400',
      badgeBg: 'bg-slate-200',
      badgeText: 'text-slate-600',
      badgeLabel: 'Undefined',
      valueColor: 'text-slate-600',
      metaText: 'text-slate-500',
      rowHover: 'hover:bg-slate-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-slate-100 text-slate-500',
    };
  }

  return {
    accent: '#6366f1',
    iconClass: 'text-indigo-500',
    badgeBg: 'bg-indigo-100',
    badgeText: 'text-indigo-700',
    badgeLabel: nodeKey === 'type' ? 'Tipo' : 'Valor',
    valueColor: 'text-indigo-600',
    metaText: 'text-indigo-600',
    rowHover: 'hover:bg-indigo-50',
    rowBackground: 'bg-white',
    toggleButtonClasses: 'hover:bg-indigo-100 text-indigo-500',
  };
}

function getTypeColorTokens(typeName) {
  const normalized = typeName.toLowerCase();
  const palette = {
    // Declarations - Roxo
    declaration: {
      accent: '#7c3aed',
      iconClass: 'text-violet-500',
      badgeBg: 'bg-violet-100',
      badgeText: 'text-violet-700',
      valueColor: 'text-violet-600',
      metaText: 'text-violet-600',
      rowHover: 'hover:bg-violet-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-violet-100 text-violet-500',
    },
    // Statements - Azul
    statement: {
      accent: '#2563eb',
      iconClass: 'text-blue-500',
      badgeBg: 'bg-blue-100',
      badgeText: 'text-blue-700',
      valueColor: 'text-blue-600',
      metaText: 'text-blue-600',
      rowHover: 'hover:bg-blue-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-blue-100 text-blue-500',
    },
    // Expressions - Verde
    expression: {
      accent: '#10b981',
      iconClass: 'text-emerald-500',
      badgeBg: 'bg-emerald-100',
      badgeText: 'text-emerald-700',
      valueColor: 'text-emerald-600',
      metaText: 'text-emerald-600',
      rowHover: 'hover:bg-emerald-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-emerald-100 text-emerald-500',
    },
    // Literals - Rosa/Fúcsia
    literal: {
      accent: '#d946ef',
      iconClass: 'text-fuchsia-500',
      badgeBg: 'bg-fuchsia-100',
      badgeText: 'text-fuchsia-700',
      valueColor: 'text-fuchsia-600',
      metaText: 'text-fuchsia-600',
      rowHover: 'hover:bg-fuchsia-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-fuchsia-100 text-fuchsia-500',
    },
    // Operators - Laranja
    operator: {
      accent: '#f97316',
      iconClass: 'text-orange-500',
      badgeBg: 'bg-orange-100',
      badgeText: 'text-orange-700',
      valueColor: 'text-orange-600',
      metaText: 'text-orange-600',
      rowHover: 'hover:bg-orange-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-orange-100 text-orange-500',
    },
    // Functions - Ciano
    function: {
      accent: '#06b6d4',
      iconClass: 'text-cyan-500',
      badgeBg: 'bg-cyan-100',
      badgeText: 'text-cyan-700',
      valueColor: 'text-cyan-600',
      metaText: 'text-cyan-600',
      rowHover: 'hover:bg-cyan-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-cyan-100 text-cyan-500',
    },
    // Identifiers - Âmbar
    identifier: {
      accent: '#f59e0b',
      iconClass: 'text-amber-500',
      badgeBg: 'bg-amber-100',
      badgeText: 'text-amber-700',
      valueColor: 'text-amber-600',
      metaText: 'text-amber-600',
      rowHover: 'hover:bg-amber-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-amber-100 text-amber-500',
    },
    // Types - Índigo
    type: {
      accent: '#6366f1',
      iconClass: 'text-indigo-500',
      badgeBg: 'bg-indigo-100',
      badgeText: 'text-indigo-700',
      valueColor: 'text-indigo-600',
      metaText: 'text-indigo-600',
      rowHover: 'hover:bg-indigo-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-indigo-100 text-indigo-500',
    },
    // Control Flow - Vermelho
    control: {
      accent: '#ef4444',
      iconClass: 'text-red-500',
      badgeBg: 'bg-red-100',
      badgeText: 'text-red-700',
      valueColor: 'text-red-600',
      metaText: 'text-red-600',
      rowHover: 'hover:bg-red-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-red-100 text-red-500',
    },
    // Blocks - Verde-limão
    block: {
      accent: '#84cc16',
      iconClass: 'text-lime-500',
      badgeBg: 'bg-lime-100',
      badgeText: 'text-lime-700',
      valueColor: 'text-lime-600',
      metaText: 'text-lime-600',
      rowHover: 'hover:bg-lime-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-lime-100 text-lime-500',
    },
    // Loops - Teal
    loop: {
      accent: '#14b8a6',
      iconClass: 'text-teal-500',
      badgeBg: 'bg-teal-100',
      badgeText: 'text-teal-700',
      valueColor: 'text-teal-600',
      metaText: 'text-teal-600',
      rowHover: 'hover:bg-teal-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-teal-100 text-teal-500',
    },
    // Parameters - Rosa
    parameter: {
      accent: '#ec4899',
      iconClass: 'text-pink-500',
      badgeBg: 'bg-pink-100',
      badgeText: 'text-pink-700',
      valueColor: 'text-pink-600',
      metaText: 'text-pink-600',
      rowHover: 'hover:bg-pink-50',
      rowBackground: 'bg-white',
      toggleButtonClasses: 'hover:bg-pink-100 text-pink-500',
    },
  };

  // Mapeamento específico por palavras-chave
  if (normalized.includes('declaration') || normalized.includes('decl')) {
    return palette.declaration;
  }

  if (normalized.includes('statement') || normalized.includes('stmt')) {
    return palette.statement;
  }

  if (normalized.includes('expression') || normalized.includes('expr')) {
    return palette.expression;
  }

  if (normalized.includes('literal')) {
    return palette.literal;
  }

  if (normalized.includes('operator') || normalized.includes('binary') || normalized.includes('unary')) {
    return palette.operator;
  }

  if (normalized.includes('function') || normalized.includes('method') || normalized.includes('call')) {
    return palette.function;
  }

  if (normalized.includes('identifier') || normalized.includes('name') || normalized.includes('variable')) {
    return palette.identifier;
  }

  if (normalized.includes('type') || normalized.includes('class')) {
    return palette.type;
  }

  if (normalized.includes('if') || normalized.includes('else') || normalized.includes('switch') || 
      normalized.includes('case') || normalized.includes('return') || normalized.includes('break') || 
      normalized.includes('continue')) {
    return palette.control;
  }

  if (normalized.includes('block') || normalized.includes('body')) {
    return palette.block;
  }

  if (normalized.includes('while') || normalized.includes('for') || normalized.includes('loop')) {
    return palette.loop;
  }

  if (normalized.includes('param') || normalized.includes('argument') || normalized.includes('arg')) {
    return palette.parameter;
  }

  // Fallback para cores baseadas em hash
  const paletteArray = Object.values(palette);
  const hash = [...typeName].reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return paletteArray[hash % paletteArray.length];
}

function SyntaxTreeExplorer({ data, expandedNodes, toggleNode }) {
  return (
    <div className="font-mono text-sm text-apple-gray-800 space-y-1">
      <TreeNode
        nodeKey="AST"
        value={data}
        path="root"
        depth={0}
        expandedNodes={expandedNodes}
        toggleNode={toggleNode}
      />
    </div>
  );
}

function TreeNode({ nodeKey, value, path, depth, expandedNodes, toggleNode }) {
  const isBranch = value !== null && typeof value === 'object';
  const isArray = Array.isArray(value);
  const isExpanded = expandedNodes.has(path);

  const handleToggle = () => {
    if (isBranch) {
      toggleNode(path);
    }
  };

  const branchSummary = isArray
    ? `${value.length} item${value.length === 1 ? '' : 's'}`
    : formatObjectSummary(value);

  const primitiveSummary = formatPrimitive(value);
  const secondaryText = isBranch ? branchSummary : primitiveSummary;
  const nodeStyles = getNodeStyles({ nodeKey, isBranch, isArray, value });
  const SecondaryIcon = isBranch ? GitBranch : FileCode;
  const ToggleIcon = isExpanded ? ChevronDown : ChevronRight;
  const rowHoverClass = nodeStyles.rowHover || (isBranch ? 'hover:bg-apple-gray-50' : '');
  const rowBackgroundClass = nodeStyles.rowBackground || 'bg-white';
  const iconClass = nodeStyles.iconClass || (isBranch ? 'text-apple-blue' : 'text-apple-gray-400');
  const metaTextClass = nodeStyles.metaText || (isBranch ? 'text-apple-gray-500' : 'text-apple-gray-400');
  const valueColorClass = nodeStyles.valueColor || 'text-apple-gray-500';
  const badgeLabel = nodeStyles.badgeLabel;
  const badgeBgClass = nodeStyles.badgeBg || 'bg-apple-gray-100';
  const badgeTextClass = nodeStyles.badgeText || 'text-apple-gray-600';
  const toggleButtonClasses = nodeStyles.toggleButtonClasses || 'hover:bg-slate-100 text-slate-500';

  return (
    <motion.div
      initial={{ opacity: 0, x: -10 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.2, delay: depth * 0.02 }}
    >
      <div
        style={{ 
          marginLeft: depth * 16, 
          borderLeftColor: nodeStyles.accent || 'rgba(148, 163, 184, 0.5)',
          boxShadow: isExpanded && isBranch ? `0 0 0 1px ${nodeStyles.accent}15` : 'none'
        }}
        className={`flex items-start gap-2 rounded-xl border-l-2 px-3 py-2 transition-all duration-200 ${rowBackgroundClass} ${rowHoverClass}`}
      >
        {isBranch ? (
          <motion.button
            type="button"
            onClick={handleToggle}
            className={`mt-0.5 flex h-5 w-5 items-center justify-center rounded transition-all duration-200 ${toggleButtonClasses}`}
            aria-label={isExpanded ? 'Recolher nó' : 'Expandir nó'}
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
          >
            <motion.div
              animate={{ rotate: isExpanded ? 0 : -90 }}
              transition={{ duration: 0.2 }}
            >
              <ChevronDown className="h-4 w-4" />
            </motion.div>
          </motion.button>
        ) : (
          <span className="mt-0.5 h-5 w-5" />
        )}

        <div className="flex flex-1 items-start gap-2 min-w-0">
          <motion.div
            whileHover={{ scale: 1.1, rotate: 5 }}
            transition={{ duration: 0.2 }}
          >
            <SecondaryIcon className={`h-4 w-4 flex-shrink-0 mt-0.5 ${iconClass}`} />
          </motion.div>
          <div className="min-w-0">
            <div className="flex flex-wrap items-baseline gap-2">
              <span className="font-semibold text-apple-gray-700 break-all">
                {nodeKey}
              </span>
              {badgeLabel && (
                <motion.span 
                  className={`rounded-full px-2 py-0.5 text-[11px] font-medium ${badgeBgClass} ${badgeTextClass}`}
                  whileHover={{ scale: 1.05 }}
                  transition={{ duration: 0.15 }}
                >
                  {badgeLabel}
                </motion.span>
              )}
              <span className={`text-xs font-medium ${metaTextClass}`}>
                {secondaryText}
              </span>
            </div>
            {!isBranch && (
              <div className={`text-xs break-all ${valueColorClass} mt-1`}>
                {primitiveSummary}
              </div>
            )}
          </div>
        </div>
      </div>

      {isBranch && isExpanded && (
        <motion.div 
          className="space-y-1"
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          exit={{ opacity: 0, height: 0 }}
          transition={{ duration: 0.2 }}
        >
          {(isArray ? value : Object.entries(value || {})).length === 0 && (
            <div className="text-xs text-apple-gray-400 italic" style={{ paddingLeft: (depth + 1) * 16 + 12 }}>
              (vazio)
            </div>
          )}

          {isArray
            ? value.map((item, index) => (
                <TreeNode
                  key={`${path}.${index}`}
                  nodeKey={`[${index}]`}
                  value={item}
                  path={`${path}.${index}`}
                  depth={depth + 1}
                  expandedNodes={expandedNodes}
                  toggleNode={toggleNode}
                />
              ))
            : Object.entries(value || {}).map(([childKey, childValue]) => (
                <TreeNode
                  key={`${path}.${childKey}`}
                  nodeKey={childKey}
                  value={childValue}
                  path={`${path}.${childKey}`}
                  depth={depth + 1}
                  expandedNodes={expandedNodes}
                  toggleNode={toggleNode}
                />
              ))}
        </motion.div>
      )}
    </motion.div>
  );
}

function formatPrimitive(value) {
  if (value === null) {
    return 'null';
  }

  if (value === undefined) {
    return 'undefined';
  }

  if (typeof value === 'string') {
    const trimmed = value.length > 60 ? `${value.slice(0, 57)}...` : value;
    return `"${trimmed}"`;
  }

  if (typeof value === 'number' || typeof value === 'boolean' || typeof value === 'bigint') {
    return String(value);
  }

  if (typeof value === 'function') {
    return 'function()';
  }

  if (Array.isArray(value)) {
    return `[${value.length} itens]`;
  }

  if (typeof value === 'object') {
    return '{...}';
  }

  return String(value);
}

function formatObjectSummary(obj) {
  if (!obj || typeof obj !== 'object') {
    return '{vazio}';
  }

  const keys = Object.keys(obj);
  if (keys.length === 0) {
    return '{vazio}';
  }

  if (keys.length === 1) {
    return `{${keys[0]}}`;
  }

  if (keys.length <= 3) {
    return `{${keys.join(', ')}}`;
  }

  return `{${keys.slice(0, 2).join(', ')}, +${keys.length - 2}}`;
}

