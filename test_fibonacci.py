import requests
import json

# Upload new MiniPar code
code = """func fibonacci(n: number) -> number {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

var result: number = fibonacci(10)
print(result)
"""

# Upload code
response = requests.post('http://localhost:8000/compiler/upload', 
                        json={'source_code': code})
print('Upload Status:', response.status_code)
code_id = response.json()['code_id']
print('Code ID:', code_id)

# Test LLVM IR generation
ir_response = requests.get(f'http://localhost:8000/compiler/{code_id}/llvm/ir')
print('\nLLVM IR Status:', ir_response.status_code)
print('LLVM IR (first 500 chars):')
print(ir_response.json()['llvm_ir'][:500])

# Test tokens
tokens_response = requests.get(f'http://localhost:8000/compiler/{code_id}/token')
print('\nTokens Status:', tokens_response.status_code)
print('First 5 tokens:')
tokens = tokens_response.json()['tokens'][:5]
for token in tokens:
    print(f"  {token['type']}: {token['value']}")

# Test assembly
asm_response = requests.get(f'http://localhost:8000/compiler/{code_id}/asm')
print('\nAssembly Status:', asm_response.status_code)
print('Assembly (first 200 chars):')
print(asm_response.json()['assembly'][:200])