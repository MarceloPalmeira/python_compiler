"""
Models for API data structures
"""

from enum import Enum
from typing import Optional


class OptLevel(Enum):
    """Optimization levels"""
    O0 = "O0"
    O1 = "O1" 
    O2 = "O2"
    O3 = "O3"
    
    @classmethod
    def from_string(cls, opt_str: str) -> Optional['OptLevel']:
        """Get optimization level from string"""
        try:
            return cls(opt_str)
        except ValueError:
            return None
    
    def __str__(self):
        return self.value