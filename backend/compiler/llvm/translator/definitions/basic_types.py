"""
Basic definitions for LLVM IR generation
"""

from enum import Enum
from typing import List, Optional
from ..fragment import Fragment, SimpleFragment, FragmentBlock


class BaseType(Enum):
    """Basic types supported by the compiler"""
    VOID = "void"
    CHAR = "i8"
    INT = "i32"
    FLOAT = "float"
    BOOLEAN = "i1"


class Type:
    """Type representation for LLVM IR"""
    
    def __init__(self, base_type: BaseType, dimensions: List[int] = None):
        self.base_type = base_type
        self.dimensions = dimensions or []
    
    def get_llvm_type(self) -> str:
        """Get LLVM IR type string"""
        type_str = self.base_type.value
        
        # Add array dimensions
        for dim in reversed(self.dimensions):
            type_str = f"[{dim} x {type_str}]"
        
        return type_str
    
    def get_pointer_type(self) -> str:
        """Get pointer to this type"""
        return f"{self.get_llvm_type()}*"
    
    def get_new_reference_pointer_to_this(self) -> 'Type':
        """Create a new type that is a pointer to this type"""
        new_type = Type(self.base_type, self.dimensions.copy())
        new_type.is_pointer = True
        return new_type
    
    def is_array(self) -> bool:
        """Check if this is an array type"""
        return len(self.dimensions) > 0
    
    def __str__(self):
        return self.get_llvm_type()


class Variable:
    """Variable representation"""
    
    def __init__(self, var_type: Type, name: str, is_constant: bool = False):
        self.type = var_type
        self.name = name
        self.is_constant = is_constant
        self._llvm_name = None
    
    def get_llvm_name(self) -> str:
        """Get LLVM IR variable name"""
        if self._llvm_name:
            return self._llvm_name
        
        if self.is_constant:
            return self.name
        else:
            return f"%{self.name}"
    
    def set_llvm_name(self, name: str):
        """Set custom LLVM name"""
        self._llvm_name = name
    
    def get_raw_name_without_conflict(self) -> str:
        """Get raw name without scope conflicts"""
        return self.name
    
    @staticmethod
    def as_constant(var_type: Type, value: str) -> 'Variable':
        """Create a constant variable"""
        return Variable(var_type, value, is_constant=True)
    
    def __str__(self):
        return f"{self.type.get_llvm_type()} {self.get_llvm_name()}"


class Label:
    """Label for LLVM IR basic blocks"""
    
    def __init__(self, name: str):
        self.name = name
    
    def get_label_name(self) -> str:
        return self.name
    
    def __str__(self):
        return self.name


class Alloca(Fragment):
    """LLVM alloca instruction"""
    
    def __init__(self, var_name: str, var_type: Type):
        self.var_name = var_name
        self.var_type = var_type
        self.return_variable = Variable(var_type.get_new_reference_pointer_to_this(), var_name)
    
    def get_return_variable(self) -> Variable:
        return self.return_variable
    
    def get_text(self) -> str:
        return f"{self.return_variable.get_llvm_name()} = alloca {self.var_type.get_llvm_type()}"


class Store(Fragment):
    """LLVM store instruction"""
    
    def __init__(self, source: Variable, dest: Variable):
        self.source = source
        self.dest = dest
    
    def get_text(self) -> str:
        return f"store {self.source}, {self.dest.type.get_llvm_type()}* {self.dest.get_llvm_name()}"


class Load(Fragment):
    """LLVM load instruction"""
    
    def __init__(self, source: Variable, dest_name: str):
        self.source = source
        self.dest_name = dest_name
        # The loaded value has the type that the pointer points to
        if hasattr(source.type, 'base_type'):
            loaded_type = Type(source.type.base_type, source.type.dimensions)
        else:
            loaded_type = source.type
        self.return_variable = Variable(loaded_type, dest_name)
    
    def get_return_variable(self) -> Variable:
        return self.return_variable
    
    def get_text(self) -> str:
        return f"{self.return_variable.get_llvm_name()} = load {self.return_variable.type.get_llvm_type()}, {self.source.type.get_llvm_type()} {self.source.get_llvm_name()}"


class Constant(Variable):
    """Constant value"""
    
    def __init__(self, var_type: Type, value: str):
        super().__init__(var_type, value, is_constant=True)
        self.value = value
    
    def get_llvm_name(self) -> str:
        return self.value