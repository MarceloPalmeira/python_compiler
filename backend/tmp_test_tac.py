from services.compiler_service import compiler_service

code = '''var x: number = 1
var y: number = 2
var z: number = x + y
print(z)'''

cid = compiler_service.upload_code(code)
print('code id:', cid)

tac = compiler_service.compile_to_tac(cid)
print('TAC output:')
print('\n'.join(tac))
