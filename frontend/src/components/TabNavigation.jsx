import React from 'react';
import { motion } from 'framer-motion';
import { Code, Tag, TreePine } from 'lucide-react';

const tabs = [
  { id: 'editor', label: 'Editor', icon: Code },
  { id: 'tokens', label: 'Tokens', icon: Tag },
  { id: 'syntax', label: 'Sintaxe', icon: TreePine },
];

function TabNavigation({ activeTab, setActiveTab, hasResults }) {
  return (
    <div className="flex border-b border-apple-gray-200/50 px-6">
      {tabs.map((tab) => {
        const Icon = tab.icon;
        const isActive = activeTab === tab.id;
        const isDisabled = !hasResults && tab.id !== 'editor';

        return (
          <button
            key={tab.id}
            onClick={() => !isDisabled && setActiveTab(tab.id)}
            disabled={isDisabled}
            className={`
              relative px-6 py-4 font-medium text-sm transition-all duration-200
              flex items-center gap-2
              ${isActive 
                ? 'text-apple-blue' 
                : isDisabled 
                  ? 'text-apple-gray-300 cursor-not-allowed'
                  : 'text-apple-gray-600 hover:text-apple-gray-800'
              }
            `}
          >
            <Icon className="w-4 h-4" />
            {tab.label}
            
            {/* Indicador de aba ativa */}
            {isActive && (
              <motion.div
                layoutId="activeTab"
                className="absolute bottom-0 left-0 right-0 h-0.5 bg-apple-blue"
                transition={{ type: 'spring', stiffness: 380, damping: 30 }}
              />
            )}
          </button>
        );
      })}
    </div>
  );
}

export default TabNavigation;

