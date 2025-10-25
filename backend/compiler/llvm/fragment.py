"""
LLVM IR Fragment system - Python equivalent of Java Fragment classes
"""

from abc import ABC, abstractmethod
from typing import List


class Fragment(ABC):
    """Abstract base class for LLVM IR fragments"""
    
    @abstractmethod
    def get_text(self) -> str:
        """Get the text representation of this fragment"""
        pass


class SimpleFragment(Fragment):
    """Simple text fragment"""
    
    def __init__(self, text: str):
        self.text = text
    
    def get_text(self) -> str:
        return self.text


class FragmentBlock(Fragment):
    """Block of fragments - equivalent to Java FragmentBlock"""
    
    INDENT_CHAR = ' '
    INDENT_SIZE = 4
    
    def __init__(self):
        self.fragments: List[Fragment] = []
    
    def add(self, fragment: Fragment):
        """Add a fragment to this block"""
        self.fragments.append(fragment)
        return self
    
    def add_text(self, text: str):
        """Add simple text as a fragment"""
        self.fragments.append(SimpleFragment(text))
        return self
    
    def extend(self, fragments: List[Fragment]):
        """Add multiple fragments"""
        self.fragments.extend(fragments)
        return self
    
    def get_text(self) -> str:
        """Get concatenated text of all fragments"""
        return '\n'.join(fragment.get_text() for fragment in self.fragments)
    
    def get_indented_text(self, indentation: int = 1) -> str:
        """Get indented text representation"""
        indent = self.INDENT_CHAR * (self.INDENT_SIZE * max(0, indentation))
        return '\n'.join(
            indent + fragment.get_text() 
            for fragment in self.fragments
        )
    
    def __len__(self):
        return len(self.fragments)
    
    def __bool__(self):
        return len(self.fragments) > 0


class LabeledFragmentBlock(FragmentBlock):
    """Fragment block with a label - equivalent to Java LabeledFragmentBlock"""
    
    def __init__(self, label: str):
        super().__init__()
        self.label = label
    
    def get_text(self) -> str:
        if not self.fragments:
            return f"{self.label}:"
        
        result = f"{self.label}:\n"
        result += self.get_indented_text()
        return result


class ReturnableFragment(Fragment):
    """Fragment that can have a return value - equivalent to Java ReturnableFragment"""
    
    def __init__(self, fragment: Fragment, return_value: str = None):
        self.fragment = fragment
        self.return_value = return_value
    
    def get_text(self) -> str:
        return self.fragment.get_text()
    
    def get_return_value(self) -> str:
        return self.return_value
    
    def set_return_value(self, return_value: str):
        self.return_value = return_value


class ReturnableFragmentBlock(FragmentBlock):
    """Fragment block with return value - equivalent to Java ReturnableFragmentBlock"""
    
    def __init__(self, return_value: str = None):
        super().__init__()
        self.return_value = return_value
    
    def get_return_value(self) -> str:
        return self.return_value
    
    def set_return_value(self, return_value: str):
        self.return_value = return_value