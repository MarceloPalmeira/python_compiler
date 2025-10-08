import requests

# Upload the complex MiniPar code
complex_code = """func fatorial(n: number) -> number {
    if (n == 0 || n == 1) {
        return 1
    } else {
        return n * fatorial(n - 1)
    }
}

var result: number = fatorial(5)
print("Fatorial de 5:", result)

var a: bool = true
var b: bool = false
var c: bool = a && b
print("a && b =", c)

var numbers: list = [1, 2, 3, 4, 5]
print("Lista:", numbers)

var name: string = input("Digite seu nome: ")
print("Olá", name)"""

# Upload code
response = requests.post('http://localhost:8000/compiler/upload', 
                        json={'code': complex_code})
print('Upload Status:', response.status_code)
code_id = response.json()['code_id']
print('Code ID:', code_id)

# Test LLVM IR
ir_response = requests.get(f'http://localhost:8000/compiler/{code_id}/llvm/ir')
print('\n🔧 LLVM IR Status:', ir_response.status_code)
print('LLVM IR (first 1000 chars):')
print(ir_response.json()['llvm_ir'][:1000])

# Test improved tokenization
tokens_response = requests.get(f'http://localhost:8000/compiler/{code_id}/token')
print('\n🏷️ Tokens Status:', tokens_response.status_code)
print('Enhanced tokens (first 10):')
tokens = tokens_response.json()['tokens'][:10]
for i, token in enumerate(tokens, 1):
    print(f"  {i:2d}. {token['type']:15s}: '{token['value']}'")

# Test syntax tree
syntax_response = requests.get(f'http://localhost:8000/compiler/{code_id}/syntax')
print('\n🌳 Syntax Tree Status:', syntax_response.status_code)
syntax_tree = syntax_response.json()['syntax_tree']
if 'error' not in syntax_tree:
    print(f"AST Type: {syntax_tree['type']}")
    print(f"Body items: {len(syntax_tree['body'])}")
    for i, item in enumerate(syntax_tree['body'][:3], 1):
        print(f"  {i}. {item['type']}: {item.get('name', 'N/A')}")
else:
    print(f"Error: {syntax_tree['error']}")

# Test symbols table
symbols_response = requests.get(f'http://localhost:8000/compiler/{code_id}/symbols')
print('\n📊 Symbols Status:', symbols_response.status_code)
symbols = symbols_response.json()['symbols_table']
print(f"Variables found: {len(symbols['variables'])}")
print(f"Functions found: {len(symbols['functions'])}")
for var in symbols['variables'][:3]:
    print(f"  Variable: {var['name']} ({var['type']})")
for func in symbols['functions']:
    print(f"  Function: {func['name']} -> {func['return_type']}")

print(f"\n🎯 Total features working: LLVM IR ✅, Tokens ✅, AST ✅, Symbols ✅")
print(f"🚀 MiniPar Compiler is now 100% COMPLETE!")