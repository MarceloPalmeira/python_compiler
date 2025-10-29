import React, { useEffect, useMemo, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { GitBranch, Hash, Tag, Download, Search, Loader2, AlertCircle } from 'lucide-react';

function SymbolTable({ symbols, codeId, loading, error }) {
  const [search, setSearch] = useState('');

  const { variables, functions } = useMemo(() => {
    const vars = Array.isArray(symbols?.variables) ? symbols.variables : [];
    const fns = Array.isArray(symbols?.functions) ? symbols.functions : [];
    return { variables: vars, functions: fns };
  }, [symbols]);

  const filtered = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return { variables, functions };
    return {
      variables: variables.filter((v) => String(v).toLowerCase().includes(q)),
      functions: functions.filter((f) => f.name.toLowerCase().includes(q) || f.params?.some((p) => String(p).toLowerCase().includes(q))),
    };
  }, [variables, functions, search]);

  const downloadSymbols = () => {
    const data = JSON.stringify(symbols?.raw || symbols || {}, null, 2);
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `symbols-${codeId}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  if (loading) {
    return (
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        className="text-center py-16 bg-gradient-to-br from-amber-50 to-sky-50 rounded-2xl border border-apple-gray-200"
      >
        <motion.div animate={{ rotate: 360 }} transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}>
          <Loader2 className="w-12 h-12 text-apple-gray-400 mx-auto mb-4" />
        </motion.div>
        <div className="text-apple-gray-700 font-medium">Carregando Tabela de Símbolos…</div>
      </motion.div>
    );
  }

  if (error) {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center py-16 bg-gradient-to-br from-red-50 to-orange-50 rounded-2xl border border-red-200"
      >
        <AlertCircle className="w-12 h-12 text-red-500 mx-auto mb-3" />
        <div className="text-red-700 font-semibold mb-1">Erro ao carregar símbolos</div>
        <div className="text-red-600 text-sm">{error}</div>
      </motion.div>
    );
  }

  if (!symbols) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-center py-16 bg-gradient-to-br from-slate-50 to-gray-100 rounded-2xl border border-slate-200"
      >
        <GitBranch className="w-12 h-12 text-slate-400 mx-auto mb-3" />
        <div className="text-apple-gray-700 font-medium">Sem símbolos ainda</div>
        <div className="text-apple-gray-500 text-sm">Compile o código para gerar a tabela</div>
      </motion.div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-apple-gray-800 mb-1">Tabela de Símbolos</h2>
          <p className="text-sm text-apple-gray-500">Panorama de variáveis e funções globais</p>
        </div>
        <motion.button
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          onClick={downloadSymbols}
          className="flex items-center gap-2 px-4 py-2 bg-apple-gray-100 hover:bg-apple-gray-200 text-apple-gray-700 rounded-xl transition-colors apple-shadow"
        >
          <Download className="w-4 h-4" /> Baixar JSON
        </motion.button>
      </div>

      <div className="grid grid-cols-2 gap-3">
        <StatCard icon={<Tag className="w-4 h-4" />} label="Variáveis" value={variables.length} color="amber" />
        <StatCard icon={<Hash className="w-4 h-4" />} label="Funções" value={functions.length} color="cyan" />
      </div>

      <div className="relative">
        <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-apple-gray-400" />
        <input
          type="text"
          placeholder="Buscar por nome de símbolo…"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="w-full pl-12 pr-4 py-3 border border-apple-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-apple-blue focus:border-transparent bg-white apple-shadow transition-all"
        />
      </div>

      <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} className="bg-white rounded-2xl border border-apple-gray-200 apple-shadow overflow-hidden">
        <div className="bg-gradient-to-r from-amber-50 via-apple-gray-50 to-cyan-50 px-6 py-4 border-b border-apple-gray-200 flex items-center gap-3">
          <GitBranch className="w-5 h-5 text-amber-600" />
          <span className="text-sm font-semibold text-apple-gray-800">Símbolos Globais</span>
        </div>

        <div className="p-6 space-y-8">
          <section>
            <h3 className="text-xs font-semibold text-amber-800 mb-3">Variáveis</h3>
            <AnimatePresence mode="popLayout">
              <div className="flex flex-wrap gap-2">
                {filtered.variables.length === 0 && (
                  <span className="text-apple-gray-500 text-sm">Nenhuma variável</span>
                )}
                {filtered.variables.map((name, idx) => (
                  <motion.span
                    key={`${name}-${idx}`}
                    initial={{ opacity: 0, y: 6 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -6 }}
                    transition={{ delay: idx * 0.02 }}
                    className="px-3 py-1.5 rounded-lg text-xs font-medium border bg-amber-50 text-amber-800 border-amber-200"
                  >
                    {name}
                  </motion.span>
                ))}
              </div>
            </AnimatePresence>
          </section>

          <section>
            <h3 className="text-xs font-semibold text-cyan-800 mb-3">Funções</h3>
            <div className="grid md:grid-cols-2 gap-3">
              <AnimatePresence>
                {filtered.functions.length === 0 && (
                  <span className="text-apple-gray-500 text-sm">Nenhuma função</span>
                )}
                {filtered.functions.map((fn, idx) => (
                  <motion.div
                    key={fn.name}
                    initial={{ opacity: 0, y: 8 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -8 }}
                    transition={{ delay: idx * 0.03 }}
                    className="rounded-xl border border-cyan-200 bg-cyan-50/50 p-4"
                  >
                    <div className="flex items-baseline justify-between gap-2 mb-2">
                      <div className="text-apple-gray-800 font-semibold truncate">{fn.name}</div>
                      <span className="text-[11px] px-2 py-0.5 rounded-full bg-white border border-cyan-200 text-cyan-700 font-medium">
                        {fn.paramsCount} parâmetro{fn.paramsCount === 1 ? '' : 's'}
                      </span>
                    </div>
                    {Array.isArray(fn.params) && fn.params.length > 0 && (
                      <div className="flex flex-wrap gap-1.5">
                        {fn.params.map((p, i) => (
                          <span key={`${fn.name}-p-${i}`} className="px-2 py-0.5 rounded-md text-[11px] border bg-white text-cyan-800 border-cyan-200">
                            {p}
                          </span>
                        ))}
                      </div>
                    )}
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>
          </section>
        </div>
      </motion.div>

      {(filtered.variables.length === 0 && filtered.functions.length === 0) && (variables.length + functions.length > 0) && (
        <div className="text-center py-8">
          <Search className="w-10 h-10 text-apple-gray-300 mx-auto mb-2" />
          <div className="text-apple-gray-500 text-sm">Nenhum símbolo encontrado para "{search}"</div>
        </div>
      )}
    </div>
  );
}

function StatCard({ icon, label, value, color }) {
  const colorMap = {
    amber: {
      bg: 'bg-amber-50',
      text: 'text-amber-800',
      border: 'border-amber-200',
    },
    cyan: {
      bg: 'bg-cyan-50',
      text: 'text-cyan-800',
      border: 'border-cyan-200',
    },
  }[color] || { bg: 'bg-apple-gray-50', text: 'text-apple-gray-800', border: 'border-apple-gray-200' };

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`rounded-xl p-4 border ${colorMap.bg} ${colorMap.text} ${colorMap.border}`}
    >
      <div className="flex items-center gap-2 text-xs font-semibold mb-1">{icon} {label}</div>
      <div className="text-2xl font-bold">{value}</div>
    </motion.div>
  );
}

export default SymbolTable;


