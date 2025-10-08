from compiler.llvm.simple_minipar_compiler import SimpleMiniparCompiler

compiler = SimpleMiniparCompiler()

# Teste do fluxo completo
code = 'var x: number = 42'
print('=== FLUXO COMPLETO MINIPAR ===')
print('1. Código fonte:', repr(code))

print('\n2. TOKENIZAÇÃO (LEXER):')
tokens = compiler.tokenize(code)
for token in tokens:
    print(f'   {token["type"]:15s}: {token["value"]}')

print('\n3. PARSING (PARSER → AST):')
ast = compiler.parse(code)
print(f'   Tipo: {ast["type"]}')
print(f'   Body items: {len(ast["body"])}')
for item in ast['body']:
    print(f'   - {item["type"]}: {item["name"]} ({item["var_type"]})')

print('\n4. CÓDIGO INTERMEDIÁRIO (LLVM IR):')
ir = compiler.compile_to_ir(code)
print(ir[:300] + '...')

print('\n=== RESPOSTA DA PERGUNTA ===')
print('✅ SIM! Nossa implementação possui:')
print('   Source Code → TOKENIZE → PARSE → AST → LLVM IR')
print('   📝 Lexer: método tokenize()')
print('   🌳 Parser: método parse() que gera AST')
print('   🔧 Code Gen: método compile_to_ir()')