import React from 'react';
import { NavLink } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Code2, Sparkles } from 'lucide-react';

function Header() {
  const navItems = [
    { path: '/', label: '📝 Editor', exact: true },
    { path: '/lexical', label: '🏷️ Análise Léxica' },
    { path: '/syntax', label: '🌳 Análise Sintática' },
    { path: '/cte', label: '⚙️ CTE -> Geração de Código Intermediário' },
    { path: '/assembly', label: '💻 Assembly -> Geração de Código de Máquina' },
  ];

  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="sticky top-0 z-50 backdrop-blur-xl bg-white/80 border-b border-apple-gray-50"
    >
      <div className="container mx-auto px-4 py-3 max-w-7xl">
        <div className="flex items-center justify-between mb-3">
          <NavLink to="/" className="flex items-center gap-3 group">
            <div className="relative">
              <div className="absolute inset-0 bg-apple-blue rounded-2xl blur-lg opacity-30 animate-pulse-soft"></div>
              <div className="relative bg-gradient-to-br from-apple-blue to-blue-600 p-3 rounded-2xl group-hover:scale-105 transition-transform">
                <Code2 className="w-7 h-7 text-white" />
              </div>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-apple-gray-800 tracking-tight">
                MiniPar Compiler
              </h1>
              <p className="text-sm text-apple-gray-500 flex items-center gap-1">
                <Sparkles className="w-3 h-3" />
              </p>
            </div>
          </NavLink>

          <div className="flex items-center gap-4">
            <motion.a
              href="http://127.0.0.1:8000/docs"
              target="_blank"
              rel="noopener noreferrer"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-4 py-2 text-sm font-medium text-apple-gray-700 hover:text-apple-blue transition-colors"
            >
              📚 API Docs
            </motion.a>
            <motion.div
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              className="px-4 py-2 bg-apple-gray-100 rounded-full"
            >
              <span className="text-sm font-medium text-apple-gray-700">
                v1.0.0
              </span>
            </motion.div>
          </div>
        </div>

        {/* Navigation */}
        <nav className="flex gap-2 overflow-x-auto pb-1">
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.exact}
              className={({ isActive }) => `
                px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap
                transition-all duration-200
                ${
                  isActive
                    ? 'bg-apple-blue text-cyan-800 shadow-xl'
                    : 'text-apple-gray-600 hover:bg-apple-gray-100'
                }
              `}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </div>
    </motion.header>
  );
}

export default Header;
