# MiniPar Compiler Module

This folder contains the **unified functional compiler** for the MiniPar language.

## Core Components

### `simple_minipar_compiler.py` - **Primary Implementation**
Complete standalone MiniPar compiler with:
- **Lexer**: Tokenizes MiniPar source code
- **Parser**: Generates AST from tokens using recursive descent
- **Semantic Analysis**: Basic type checking and symbol resolution
- **TAC Generator**: Produces Three-Address Code

### `tac_to_arm.py` - **ARM Assembly Generator**
Functional TAC->ARM translator that converts TAC to ARM assembly.

## Compiler Pipeline

```
MiniPar Source → Tokens → AST → TAC → ARM Assembly
```

### TAC Contract
**Input**: List of TAC lines (List[str]). Each TAC line is a textual instruction:
- `"param x"` - Function parameter
- `"t1 = a + b"` - Binary operation
- `"t2 = call foo, 3"` - Function call with assignment
- `"call print, 2"` - Function call statement
- `"func foo"` / `"endfunc foo"` - Function boundaries
- `"return t1"` - Return statement

**Output**: Single ARM assembly string for CPULator simulator.

### ARM Generation Notes
- **r0-r3**: Argument passing and return values
- **r4-r11**: Temporaries, saved across function calls
- **r12**: Spill/temp register for literals
- **Stack**: Extra args (>4) pushed right-to-left with cleanup
- **Functions**: Conservative prologue/epilogue with full register saving

## Usage

```python
from compiler.simple_minipar_compiler import parse, generate_tac
from compiler.tac_to_arm import tac_to_arm

# Complete pipeline
source = "var x = 5; func add(a, b) { return a + b; } print(add(x, 3));"
ast = parse(source)
tac = generate_tac(ast)
arm = tac_to_arm(tac)
```

## API Integration

The compiler service (`services/compiler_service.py`) uses this unified implementation
and expects the `tac_to_arm(tac: List[str]) -> str` interface.
