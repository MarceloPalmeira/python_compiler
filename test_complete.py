import requests

# Test new code LLVM IR
response = requests.get('http://localhost:8000/compiler/110f11c819316db9/llvm/ir')
print('LLVM IR Status:', response.status_code)
print('LLVM IR:')
print(response.json()['llvm_ir'])

print('\n' + '='*50)

# Test tokens
tokens_response = requests.get('http://localhost:8000/compiler/110f11c819316db9/token')
print('Tokens Status:', tokens_response.status_code)
print('Tokens:')
for token in tokens_response.json()['tokens']:
    print(f"  {token['type']}: '{token['value']}'")

print('\n' + '='*50)

# Test assembly
asm_response = requests.get('http://localhost:8000/compiler/110f11c819316db9/asm')
print('Assembly Status:', asm_response.status_code)
print('Assembly:')
print(asm_response.json()['assembly'])