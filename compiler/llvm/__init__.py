"""
LLVM module - Python equivalent of Java LLVM package
"""

from .fragment import *

try:
    from .llvm_compiler import LLVMCompiler
except ImportError:
    # Skip if ANTLR files not generated
    pass

try:
    from .simple_minipar_compiler import SimpleMiniparCompiler
except ImportError:
    pass