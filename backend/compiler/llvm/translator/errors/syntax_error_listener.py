"""
Syntax Error Listener - Python equivalent of Java SyntaxErrorListener
"""

from antlr4.error.ErrorListener import ErrorListener
from typing import List, Any


class SyntaxErrorListener(ErrorListener):
    """Custom error listener for ANTLR syntax errors"""
    
    def __init__(self):
        super().__init__()
        self.syntax_errors: List[str] = []
    
    def syntaxError(self, recognizer, offending_symbol, line: int, column: int, 
                   msg: str, e: Any):
        """Handle syntax error"""
        error_msg = f"Line {line}:{column} - {msg}"
        self.syntax_errors.append(error_msg)
    
    def get_syntax_errors(self) -> List[str]:
        """Get list of syntax errors"""
        return self.syntax_errors
    
    def has_errors(self) -> bool:
        """Check if there are any syntax errors"""
        return len(self.syntax_errors) > 0
    
    def __str__(self) -> str:
        """String representation of all errors"""
        if not self.syntax_errors:
            return "No syntax errors"
        
        return "Syntax errors:\n" + "\n".join(self.syntax_errors)