import unittest
from backend.compiler import simple_minipar_compiler as comp
from backend.services.compiler_service import CompilerService


class TestSimpleMiniParCompiler(unittest.TestCase):
    def test_tokenize_basic(self):
        src = "var x = 10;"
        tokens = comp.tokenize(src)
        # should contain VAR, ID, ASSIGN/OP, NUMBER
        types = [t['type'] for t in tokens]
        self.assertIn('VAR', types)
        self.assertIn('ID', types)
        self.assertIn('NUMBER', types)

    def test_parse_basic(self):
        src = "var x = 10;"
        ast = comp.parse(src)
        self.assertEqual(ast['type'], 'Program')
        self.assertGreaterEqual(len(ast['body']), 1)
        first = ast['body'][0]
        self.assertEqual(first['type'], 'VariableDeclaration')
        self.assertEqual(first['name'], 'x')

    def test_generate_tac(self):
        src = "var x = 10;"
        ast = comp.parse(src)
        tac = comp.generate_tac(ast)
        # Expect at least two lines: temp assignment and x = t
        self.assertIsInstance(tac, list)
        self.assertGreaterEqual(len(tac), 1)
        # basic sanity: contains '='
        self.assertTrue(any('=' in line for line in tac))

    def test_end_to_end_pipeline(self):
        src = "var a = 5; func inc(x) { return x + 1; } var b = inc(a); print(b);"
        service = CompilerService()
        code_id = service.upload_code(src)
        tac = service.compile_to_tac(code_id)
        self.assertIsNotNone(tac)
        self.assertIsInstance(tac, list)
        asm = service.compile_tac_to_arm(code_id)
        self.assertIsNotNone(asm)
        self.assertIsInstance(asm, str)

    def test_function_calls_with_typed_params_and_spilling(self):
        # function with 5 parameters (one more than 4), typed params ignored by parser
        src = (
            "func sum(a: number, b: number, c: number, d: number, e: number) -> number { "
            "return a + b + c + d + e; } var r = sum(1,2,3,4,5); print(r);"
        )
        service = CompilerService()
        code_id = service.upload_code(src)
        tac = service.compile_to_tac(code_id)
        self.assertIsInstance(tac, list)
        asm = service.compile_tac_to_arm(code_id)
        self.assertIsInstance(asm, str)
        # asm should contain a call to sum and a push (spilling extra arg)
        self.assertIn('bl sum', asm)
        # expect either a push instruction for the 5th arg or cleanup add sp
        self.assertTrue(('push' in asm) or ('add sp, sp' in asm))


if __name__ == '__main__':
    unittest.main()
