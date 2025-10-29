import React, { useState } from 'react';
import { motion } from 'framer-motion';
import CodeEditor from '../components/CodeEditor';

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

function EditorPage() {
  const [code, setCode] = useState(EXAMPLE_CODE);

  return (
    <div className="space-y-8">
      {/* Editor Principal */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="glass-morphism rounded-3xl apple-shadow-lg overflow-hidden p-6"
      >
        <CodeEditor code={code} setCode={setCode} />
      </motion.div>

      {/* Informações adicionais */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3, duration: 0.5 }}
        className="grid grid-cols-1 md:grid-cols-3 gap-4"
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
    </div>
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

export default EditorPage;

