from services.compiler_service import compiler_service

examples = {
    'dict_literal': '''var d: dict = {"a": 1, "b": 2}
print(d)''',

    'slicing': '''var arr: list = [1,2,3,4,5]
var s: list = arr[1:3]
print(s)''',

    'chained_index': '''var mat: list = [[1,2],[3,4]]
var x: number = mat[1][0]
print(x)'''
}

for name, code in examples.items():
    print('\n--- TEST:', name, '---')
    cid = compiler_service.upload_code(code)
    print('code id:', cid)

    ast = compiler_service.get_syntax_tree(cid)
    print('\nAST:')
    print(ast)

    tac = compiler_service.compile_to_tac(cid)
    print('\nTAC:')
    print('\n'.join(tac))
