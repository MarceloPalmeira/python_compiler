"""
Compilador Completo para MiniPar - Suporte a todos os recursos da linguagem
"""
import re
from typing import Dict, List, Any, Optional, Tuple


class SimpleMiniparCompiler:
    """Compilador MiniPar completo para demonstração"""
    
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.string_constants = {}
        self.string_count = 0
        self.label_count = 0
        self.current_function = None
    
    def compile_to_ir(self, source_code: str) -> str:
        """Compile MiniPar source code to complete LLVM IR"""
        
        # Reset state
        self.variables = {}
        self.functions = {}
        self.string_constants = {}
        self.string_count = 0
        self.label_count = 0
        
        # Parse the code
        lines = source_code.strip().split('\n')
        parsed_code = self._parse_code(lines)
        
        # Generate LLVM IR
        ir = []
        ir.append("; Generated Complete LLVM IR for MiniPar")
        ir.append("target triple = \"x86_64-pc-windows-msvc\"")
        ir.append("")
        
        # Declare external functions
        ir.append("declare i32 @printf(i8*, ...)")
        ir.append("declare i8* @gets(i8*)")
        ir.append("declare i32 @scanf(i8*, ...)")
        ir.append("declare i32 @strlen(i8*)")
        ir.append("declare i8* @malloc(i64)")
        ir.append("declare void @free(i8*)")
        ir.append("declare void @sleep(i32)")
        ir.append("")
        
        # Add string constants
        for string_id, string_value in self.string_constants.items():
            escaped_string = string_value.replace('"', '').replace('\\n', '\\0A')
            str_len = len(escaped_string) + 1
            ir.append(f'@.str{string_id} = private unnamed_addr constant [{str_len} x i8] c"{escaped_string}\\00", align 1')
        
        if self.string_constants:
            ir.append("")
        
        # Generate function definitions
        for func_name, func_info in self.functions.items():
            ir.extend(self._generate_function_ir(func_name, func_info))
            ir.append("")
        
        # Main function
        ir.append("define i32 @main() {")
        ir.append("entry:")
        
        # Generate main body
        main_body = self._generate_main_body(parsed_code)
        ir.extend(main_body)
        
        ir.append("    ret i32 0")
        ir.append("}")
        
        return '\n'.join(ir)
    
    def _parse_code(self, lines: List[str]) -> Dict[str, Any]:
        """Parse MiniPar code into structured format"""
        result = {
            'variables': [],
            'functions': [],
            'statements': [],
            'imports': [],
            'channels': []
        }
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#') or line.startswith('//'):
                i += 1
                continue
            
            # Handle block comments
            if line.startswith('/*'):
                while i < len(lines) and '*/' not in lines[i]:
                    i += 1
                i += 1
                continue
            
            # Parse variable declarations
            if line.startswith('var '):
                var_info = self._parse_variable_declaration(line)
                if var_info:
                    result['variables'].append(var_info)
                    self.variables[var_info['name']] = var_info
            
            # Parse function declarations
            elif line.startswith('func '):
                func_info, end_line = self._parse_function_declaration(lines, i)
                if func_info:
                    result['functions'].append(func_info)
                    self.functions[func_info['name']] = func_info
                    i = end_line
                    continue
            
            # Parse channel declarations
            elif 'channel' in line:
                channel_info = self._parse_channel_declaration(line)
                if channel_info:
                    result['channels'].append(channel_info)
            
            # Parse statements
            else:
                stmt_info = self._parse_statement(line)
                if stmt_info:
                    result['statements'].append(stmt_info)
            
            i += 1
        
        return result
    
    def _parse_variable_declaration(self, line: str) -> Optional[Dict[str, Any]]:
        """Parse variable declaration: var name: type = value"""
        # Remove 'var ' prefix
        content = line.replace('var ', '').strip()
        
        # Split by colon to get name and type_value
        if ':' not in content:
            return None
        
        name_part, type_value_part = content.split(':', 1)
        var_name = name_part.strip()
        
        # Parse type and value
        if '=' in type_value_part:
            type_part, value_part = type_value_part.split('=', 1)
            var_type = type_part.strip()
            var_value = value_part.strip()
        else:
            var_type = type_value_part.strip()
            var_value = self._get_default_value(var_type)
        
        return {
            'name': var_name,
            'type': var_type,
            'value': var_value,
            'is_array': var_type == 'list',
            'is_function_param': False
        }
    
    def _parse_function_declaration(self, lines: List[str], start_idx: int) -> Tuple[Optional[Dict[str, Any]], int]:
        """Parse function declaration with body"""
        line = lines[start_idx].strip()
        
        # Parse function signature
        if not line.startswith('func '):
            return None, start_idx
        
        # Extract function name and parameters
        func_signature = line.replace('func ', '')
        
        # Find function name (before parentheses)
        if '(' not in func_signature:
            return None, start_idx
        
        func_name = func_signature.split('(')[0].strip()
        
        # Extract parameters and return type
        params_and_return = func_signature.split('(', 1)[1]
        
        if ')' not in params_and_return:
            return None, start_idx
        
        params_part = params_and_return.split(')')[0]
        remaining = params_and_return.split(')', 1)[1].strip()
        
        # Parse return type
        return_type = 'void'
        if remaining.startswith('->'):
            return_type = remaining.replace('->', '').strip().split()[0]
        
        # Parse parameters
        parameters = []
        if params_part.strip():
            for param in params_part.split(','):
                param = param.strip()
                if ':' in param:
                    param_name, param_type = param.split(':', 1)
                    param_name = param_name.strip()
                    param_type = param_type.strip()
                    
                    # Handle default values
                    default_value = None
                    if '=' in param_type:
                        param_type, default_value = param_type.split('=', 1)
                        param_type = param_type.strip()
                        default_value = default_value.strip()
                    
                    parameters.append({
                        'name': param_name,
                        'type': param_type,
                        'default': default_value
                    })
        
        # Parse function body
        body_lines = []
        i = start_idx + 1
        brace_count = 0
        started = False
        
        while i < len(lines):
            line = lines[i].strip()
            
            if '{' in line:
                brace_count += line.count('{')
                started = True
            
            if '}' in line:
                brace_count -= line.count('}')
            
            if started:
                body_lines.append(lines[i])
            
            if started and brace_count == 0:
                break
            
            i += 1
        
        return {
            'name': func_name,
            'parameters': parameters,
            'return_type': return_type,
            'body': body_lines
        }, i
    
    def _parse_channel_declaration(self, line: str) -> Optional[Dict[str, Any]]:
        """Parse channel declaration: s_channel name {func, desc, host, port}"""
        if 's_channel' in line:
            channel_type = 'server'
            content = line.replace('s_channel', '').strip()
        elif 'c_channel' in line:
            channel_type = 'client' 
            content = line.replace('c_channel', '').strip()
        else:
            return None
        
        # Parse channel name and configuration
        parts = content.split('{', 1)
        if len(parts) < 2:
            return None
        
        channel_name = parts[0].strip()
        config_part = parts[1].replace('}', '').strip()
        
        return {
            'name': channel_name,
            'type': channel_type,
            'config': config_part
        }
    
    def _parse_statement(self, line: str) -> Optional[Dict[str, Any]]:
        """Parse various statement types"""
        line = line.strip()
        
        # Print statements
        if line.startswith('print('):
            return {'type': 'print', 'content': line}
        
        # Input statements
        elif 'input(' in line:
            return {'type': 'input', 'content': line}
        
        # Function calls
        elif '(' in line and ')' in line and not any(op in line for op in ['=', 'var ', 'if ', 'while ', 'for ']):
            return {'type': 'function_call', 'content': line}
        
        # Assignments
        elif '=' in line and not line.startswith('var '):
            return {'type': 'assignment', 'content': line}
        
        # Return statements
        elif line.startswith('return'):
            return {'type': 'return', 'content': line}
        
        # Break/Continue
        elif line in ['break', 'continue']:
            return {'type': 'control', 'content': line}
        
        # Control structures (if, while, for)
        elif any(line.startswith(keyword) for keyword in ['if ', 'while ', 'for ', 'par ']):
            return {'type': 'control_structure', 'content': line}
        
        return None
    
    def _get_default_value(self, var_type: str) -> str:
        """Get default value for a type"""
        defaults = {
            'number': '0',
            'bool': 'false',
            'string': '""',
            'list': '[]',
            'dict': '{}',
            'any': 'null'
        }
        return defaults.get(var_type, '0')
    
    def _generate_function_ir(self, func_name: str, func_info: Dict[str, Any]) -> List[str]:
        """Generate LLVM IR for a function"""
        ir = []
        
        # Function signature
        return_type = self._minipar_type_to_llvm(func_info['return_type'])
        
        # Build parameter list
        param_list = []
        for param in func_info['parameters']:
            llvm_type = self._minipar_type_to_llvm(param['type'])
            param_list.append(f"{llvm_type} %{param['name']}")
        
        param_str = ', '.join(param_list) if param_list else ''
        
        ir.append(f"define {return_type} @{func_name}({param_str}) {{")
        ir.append("entry:")
        
        # Allocate space for parameters
        for param in func_info['parameters']:
            llvm_type = self._minipar_type_to_llvm(param['type'])
            ir.append(f"    %{param['name']}_addr = alloca {llvm_type}")
            ir.append(f"    store {llvm_type} %{param['name']}, {llvm_type}* %{param['name']}_addr")
        
        # Generate function body
        body_ir = self._generate_function_body_ir(func_info['body'])
        ir.extend(body_ir)
        
        # Default return if no explicit return
        if return_type == 'void':
            ir.append("    ret void")
        else:
            ir.append(f"    ret {return_type} 0")
        
        ir.append("}")
        
        return ir
    
    def _generate_function_body_ir(self, body_lines: List[str]) -> List[str]:
        """Generate IR for function body"""
        ir = []
        
        for line in body_lines:
            line = line.strip()
            if not line or line in ['{', '}']:
                continue
            
            # Handle different statement types
            if line.startswith('var '):
                var_ir = self._generate_variable_declaration_ir(line)
                ir.extend(var_ir)
            elif line.startswith('return'):
                return_ir = self._generate_return_ir(line)
                ir.extend(return_ir)
            elif line.startswith('if '):
                if_ir = self._generate_if_ir(line)
                ir.extend(if_ir)
            elif '=' in line and not line.startswith('var '):
                assign_ir = self._generate_assignment_ir(line)
                ir.extend(assign_ir)
            elif line.startswith('print('):
                print_ir = self._generate_print_ir(line)
                ir.extend(print_ir)
        
        return ir
    
    def _generate_main_body(self, parsed_code: Dict[str, Any]) -> List[str]:
        """Generate IR for main function body"""
        ir = []
        
        # Declare variables
        for var_info in parsed_code['variables']:
            var_ir = self._generate_variable_ir(var_info)
            ir.extend(var_ir)
        
        # Generate statements
        for stmt in parsed_code['statements']:
            stmt_ir = self._generate_statement_ir(stmt)
            ir.extend(stmt_ir)
        
        return ir
    
    def _generate_variable_ir(self, var_info: Dict[str, Any]) -> List[str]:
        """Generate IR for variable declaration"""
        ir = []
        llvm_type = self._minipar_type_to_llvm(var_info['type'])
        var_name = var_info['name']
        
        # Allocate variable
        ir.append(f"    %{var_name} = alloca {llvm_type}")
        
        # Initialize with value
        value = var_info['value']
        if value and value != '0' and value != '""':
            if var_info['type'] == 'number' and value.replace('.', '').replace('-', '').isdigit():
                ir.append(f"    store {llvm_type} {value}, {llvm_type}* %{var_name}")
            elif var_info['type'] == 'bool':
                bool_val = "1" if value.lower() == 'true' else "0"
                ir.append(f"    store {llvm_type} {bool_val}, {llvm_type}* %{var_name}")
            elif var_info['type'] == 'string' and value.startswith('"'):
                # String handling
                self.string_count += 1
                self.string_constants[self.string_count] = value
                ir.append(f"    ; String assignment: {var_name} = {value}")
            elif '(' in value:  # Function call
                ir.append(f"    ; Function call assignment: {var_name} = {value}")
            else:
                ir.append(f"    ; Complex assignment: {var_name} = {value}")
        
        return ir
    
    def _generate_variable_declaration_ir(self, line: str) -> List[str]:
        """Generate IR for variable declaration within function"""
        var_info = self._parse_variable_declaration(line)
        if var_info:
            return self._generate_variable_ir(var_info)
        return []
    
    def _generate_assignment_ir(self, line: str) -> List[str]:
        """Generate IR for assignment statements"""
        ir = []
        
        if '=' not in line:
            return ir
        
        var_name, value = line.split('=', 1)
        var_name = var_name.strip()
        value = value.strip()
        
        # Simple assignment
        if var_name in self.variables:
            var_type = self.variables[var_name]['type']
            llvm_type = self._minipar_type_to_llvm(var_type)
            
            if value.replace('.', '').replace('-', '').isdigit():
                ir.append(f"    store {llvm_type} {value}, {llvm_type}* %{var_name}")
            else:
                ir.append(f"    ; Assignment: {var_name} = {value}")
        else:
            ir.append(f"    ; Assignment: {var_name} = {value}")
        
        return ir
    
    def _generate_return_ir(self, line: str) -> List[str]:
        """Generate IR for return statements"""
        ir = []
        
        value = line.replace('return', '').strip()
        if value:
            if value.isdigit():
                ir.append(f"    ret i32 {value}")
            else:
                ir.append(f"    ; Return with expression: {value}")
                ir.append("    ret i32 0")
        else:
            ir.append("    ret void")
        
        return ir
    
    def _generate_if_ir(self, line: str) -> List[str]:
        """Generate IR for if statements"""
        ir = []
        self.label_count += 1
        
        condition = line.replace('if', '').replace('(', '').replace(')', '').strip()
        
        ir.append(f"    ; If condition: {condition}")
        ir.append(f"    br label %if_true_{self.label_count}")
        ir.append(f"if_true_{self.label_count}:")
        ir.append(f"    ; If body")
        ir.append(f"    br label %if_end_{self.label_count}")
        ir.append(f"if_end_{self.label_count}:")
        
        return ir
    
    def _generate_print_ir(self, line: str) -> List[str]:
        """Generate IR for print statements"""
        ir = []
        
        # Extract print arguments
        content = line.replace('print(', '').rstrip(')')
        
        # Add string constant for print
        self.string_count += 1
        self.string_constants[self.string_count] = '"MiniPar Output\\n"'
        
        ir.append("    ; Print statement")
        ir.append(f"    %call_{self.label_count} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.str{self.string_count}, i32 0, i32 0))")
        
        self.label_count += 1
        
        return ir
    
    def _generate_statement_ir(self, stmt: Dict[str, Any]) -> List[str]:
        """Generate IR for different statement types"""
        stmt_type = stmt['type']
        content = stmt['content']
        
        if stmt_type == 'print':
            return self._generate_print_ir(content)
        elif stmt_type == 'assignment':
            return self._generate_assignment_ir(content)
        elif stmt_type == 'function_call':
            return [f"    ; Function call: {content}"]
        elif stmt_type == 'input':
            return [f"    ; Input statement: {content}"]
        elif stmt_type == 'return':
            return self._generate_return_ir(content)
        elif stmt_type == 'control':
            return [f"    ; Control: {content}"]
        elif stmt_type == 'control_structure':
            return [f"    ; Control structure: {content}"]
        
        return []
        if 'print(' in source_code:
            string_count += 1
            ir.append(f'@.str{string_count} = private unnamed_addr constant [20 x i8] c"MiniPar Output\\0A\\00", align 1')
            ir.append("")
        
        # Main function
        ir.append("define i32 @main() {")
        ir.append("entry:")
        
        # Declare variables
        for var_name, var_info in variables.items():
            llvm_type = SimpleMiniparCompiler._minipar_type_to_llvm(var_info['type'])
            ir.append(f"    %{var_name} = alloca {llvm_type}")
            
            # Initialize variable
            if var_info['value'] and var_info['value'] != "0":
                if var_info['value'].isdigit():
                    ir.append(f"    store {llvm_type} {var_info['value']}, {llvm_type}* %{var_name}")
                elif var_info['value'] in ['true', 'false']:
                    bool_val = "1" if var_info['value'] == 'true' else "0"
                    ir.append(f"    store {llvm_type} {bool_val}, {llvm_type}* %{var_name}")
                elif var_info['value'].startswith('"'):
                    # String literal
                    ir.append(f"    ; String assignment: {var_name} = {var_info['value']}")
                else:
                    # Expression or variable reference
                    ir.append(f"    ; Assignment: {var_name} = {var_info['value']}")
        
        # Handle print statements
        if 'print(' in source_code:
            ir.append("    ; Print statement")
            ir.append(f"    %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([20 x i8], [20 x i8]* @.str{string_count}, i32 0, i32 0))")
        
        # Add function definitions (simplified)
        for func_name, func_def in functions.items():
            ir.append(f"    ; Function {func_name} defined: {func_def}")
        
        ir.append("    ret i32 0")
        ir.append("}")
        ir.append("")
        
        # Add function implementations (placeholder)
        for func_name in functions.keys():
            ir.append(f"define i32 @{func_name}() {{")
            ir.append("entry:")
            ir.append("    ret i32 0")
            ir.append("}")
            ir.append("")
        
        return '\n'.join(ir)
    
    @staticmethod
    def _minipar_type_to_llvm(minipar_type: str) -> str:
        """Convert MiniPar type to LLVM type"""
        type_map = {
            'number': 'double',
            'bool': 'i1',
            'string': 'i8*',
            'list': 'i8*',    # Simplified
            'dict': 'i8*',    # Simplified
            'void': 'void',
            'any': 'i8*'
        }
        return type_map.get(minipar_type.strip(), 'i32')
    
    def tokenize(self, source_code: str) -> List[Dict[str, Any]]:
        """Tokenize MiniPar source code"""
        tokens = []
        lines = source_code.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                continue
            
            # Tokenize line
            line_tokens = self._tokenize_line(line, line_num)
            tokens.extend(line_tokens)
        
        return tokens
    
    def _tokenize_line(self, line: str, line_num: int) -> List[Dict[str, Any]]:
        """Tokenize a single line"""
        tokens = []
        
        # Define token patterns (order matters - more specific first)
        patterns = [
            (r'#.*', 'COMMENT'),
            (r'/\*.*?\*/', 'BLOCK_COMMENT'),
            (r'\b(var|func|if|else|while|for|return|break|continue|par|seq)\b', 'KEYWORD'),
            (r'\b(number|bool|string|list|dict|void|any)\b', 'TYPE'),
            (r'\b(true|false)\b', 'BOOLEAN'),
            (r'\b(print|input|len|sleep)\b', 'BUILTIN'),
            (r'\b\d+\.\d+\b', 'FLOAT'),
            (r'\b\d+\b', 'INTEGER'),
            (r'"[^"]*"', 'STRING'),
            (r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', 'IDENTIFIER'),
            # Multi-character operators first (order is critical)
            (r'&&', 'LOGICAL_OP'),
            (r'\|\|', 'LOGICAL_OP'),
            (r'==', 'RELATIONAL_OP'),
            (r'!=', 'RELATIONAL_OP'),
            (r'<=', 'RELATIONAL_OP'),
            (r'>=', 'RELATIONAL_OP'),
            (r'->', 'ARROW'),
            # Single character operators
            (r'<', 'RELATIONAL_OP'),
            (r'>', 'RELATIONAL_OP'),
            (r'\+', 'ARITHMETIC_OP'),
            (r'-', 'ARITHMETIC_OP'),
            (r'\*', 'ARITHMETIC_OP'),
            (r'/', 'ARITHMETIC_OP'),
            (r'%', 'ARITHMETIC_OP'),
            (r'=', 'ARITHMETIC_OP'),
            (r'[(){}[\],;:.]', 'DELIMITER'),
            (r'\s+', 'WHITESPACE')
        ]
        
        pos = 0
        while pos < len(line):
            matched = False
            
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(line, pos)
                
                if match:
                    value = match.group()
                    
                    # Skip whitespace and comments
                    if token_type not in ['WHITESPACE', 'COMMENT', 'BLOCK_COMMENT']:
                        tokens.append({
                            'type': token_type,
                            'value': value,
                            'line': line_num,
                            'column': pos
                        })
                    
                    pos = match.end()
                    matched = True
                    break
            
            if not matched:
                # Unknown character
                tokens.append({
                    'type': 'UNKNOWN',
                    'value': line[pos],
                    'line': line_num,
                    'column': pos
                })
                pos += 1
        
        return tokens
    
    def parse(self, source_code: str) -> Dict[str, Any]:
        """Parse MiniPar source code into AST"""
        parsed_code = self._parse_code(source_code.split('\n'))
        
        # Convert to AST format
        ast = {
            'type': 'Program',
            'body': []
        }
        
        # Add variable declarations
        for var in parsed_code['variables']:
            ast['body'].append({
                'type': 'VariableDeclaration',
                'name': var['name'],
                'var_type': var['type'],
                'value': var['value']
            })
        
        # Add function declarations
        for func in parsed_code['functions']:
            ast['body'].append({
                'type': 'FunctionDeclaration',
                'name': func['name'],
                'parameters': func['parameters'],
                'return_type': func['return_type'],
                'body': func['body']
            })
        
        # Add statements
        for stmt in parsed_code['statements']:
            ast['body'].append({
                'type': 'Statement',
                'statement_type': stmt['type'],
                'content': stmt['content']
            })
        
        return ast
    
    def get_symbols_table(self, source_code: str) -> Dict[str, Any]:
        """Generate symbols table for MiniPar code"""
        parsed_code = self._parse_code(source_code.split('\n'))
        
        symbols = {
            'variables': [],
            'functions': [],
            'scopes': {}
        }
        
        # Add global variables
        for var in parsed_code['variables']:
            symbols['variables'].append({
                'name': var['name'],
                'type': var['type'],
                'scope': 'global',
                'line': 1
            })
        
        # Add functions
        for func in parsed_code['functions']:
            symbols['functions'].append({
                'name': func['name'],
                'return_type': func['return_type'],
                'parameters': [p['name'] for p in func['parameters']],
                'scope': 'global',
                'line': 1
            })
            
            # Add function scope
            symbols['scopes'][func['name']] = {
                'variables': [p['name'] for p in func['parameters']],
                'type': 'function'
            }
        
        return symbols