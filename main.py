import re

# Set of C Programming  keywords
keywords = {
    # Basic Types
    'int', 'char', 'float', 'double', 'void',

    # Type Qualifiers
    'const', 'restrict', 'volatile',

    # Storage Class Specifiers
    'auto', 'extern', 'register', 'static', 'typedef',

    # Control Flow Statements
    'if', 'else', 'switch', 'case', 'default', 'for', 'do', 'while', 'break', 'continue', 'goto', 'return',

    # Data Types and Modifiers
    'short', 'long', 'signed', 'unsigned',

    # Structure and Union
    'struct', 'union', 'enum',

    # Special Keywords for C11 Standard
    '_Alignas', '_Alignof', '_Atomic', '_Bool', '_Complex', '_Generic', '_Imaginary', '_Noreturn', '_Static_assert', '_Thread_local',

    # Miscellaneous
    'sizeof', 'inline',

    # C++ Specific (for compatibility)
    'namespace', 'using', 'main'
}


# Define regular expressions for token types==> C language
token_specification = [
    ('PREPROCESSOR', r'#include\s*<\w+>'),             # Preprocessor directive=> #include <...>
    ('COMMENT', r'//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'),  # Single-line or multi-line comment=> //... or /*...*/
    ('STRING', r'"[^"]*"'),                            # String literals=> "..."
    ('CONSTANTFLOAT', r'\b\d+\.\d+\b'),               # Floating-point constant=> 0.5, 1.0, 3.14, etc.
    ('CONSTANTINT', r'\b\d+\b'),                      # Integer constant=> 0, 1, 2, 3, etc.
    ('ASSIGNMENT', r'='),                             # Assignment operator=> =
    ('OPERATOR', r'[+\-*/]'),                         # Arithmetic operators=> + - * /
    ('PUNCTUATOR', r'[{}();,]'),                      # Punctuators (braces, commas, semicolons)=> {}();,
    ('IDENTIFIER', r'\b[a-zA-Z_]\w*\b'),              # Identifiers (we’ll check against keywords)=> main, printf, etc.
    ('WHITESPACE', r'\s+'),                           # Whitespace (to skip)=> spaces, tabs, newlines
]

# Compile the token regular expressions into a master pattern=> for tokenizing
master_pattern = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification))

# Function to check if basic C syntax is followed==> braces, semicolons, etc.
def check_c_syntax(tokens, code_lines):
    syntax_errors = []
    brace_stack = []
    has_main = False
    
    for i, (token_type, token_value, line_number) in enumerate(tokens):
        # Ensure #include <...> is at the top
        if token_type == 'PREPROCESSOR' and i != 0:
            syntax_errors.append(f"Error: #include directive should be at the beginning. ===> in line #{line_number}")

        # Check for main function
        if token_type == 'KEYWORD' and token_value == 'main':
            has_main = True

        # Check for unbalanced braces
        if token_value == '{':
            brace_stack.append(token_value)
        elif token_value == '}':
            if brace_stack:
                brace_stack.pop()
            else:
                syntax_errors.append(f"Error: Unmatched '}}' found. ===> in line #{line_number}")
        
        # Check for missing semicolon at the end of statements
        if token_type == 'IDENTIFIER' and i < len(tokens) - 1:
            next_token = tokens[i + 1]
            if next_token[0] == 'IDENTIFIER' and next_token[1] not in {'main'} and next_token[1] not in keywords:
                continue
            if next_token[1] not in {';', '{', '}'}:
                syntax_errors.append(f"Error: Missing ';' after '{token_value}'. ===> in line #{line_number}")

    # Final checks
    if brace_stack:
        unmatched_brace_line = [line_number for _, _, line_number in tokens if '{' in brace_stack]
        syntax_errors.append(f"Error: Unmatched '{{' found. ===> in line #{unmatched_brace_line[0]}")
    if len(code_lines) > 1 and not has_main:
        syntax_errors.append("Error: 'main' function not found.")

    return syntax_errors

# Function to tokenize input C code
def tokenize(code):
    tokens = []
    error_flag = False
    code_lines = code.splitlines()

    for line_number, line in enumerate(code_lines, start=1):
        for match in master_pattern.finditer(line):
            token_type = match.lastgroup
            token_value = match.group(token_type)
            
            # Skip whitespace
            if token_type == 'WHITESPACE':
                continue
            
            # Check if the token is a keyword
            if token_type == 'IDENTIFIER' and token_value in keywords:
                tokens.append(('KEYWORD', token_value, line_number))
            elif token_type == 'IDENTIFIER':
                tokens.append((token_type, token_value, line_number))
            else:
                tokens.append((token_type, token_value, line_number))
            
            # Error check: keyword used as identifier
            if token_type == 'IDENTIFIER' and token_value in keywords:
                print(f"Error: '{token_value}' is a keyword and cannot be used as an identifier. ===> in line #{line_number}")
                error_flag = True

    return tokens, error_flag, code_lines

# Prompt user for input
print("Enter C code (type 'perform' to analyze the input):")
code_input = []
while True:
    line = input()
    if line.strip().lower() == 'perform':
        break
    code_input.append(line)

# Join the input lines into a single string
code = "\n".join(code_input)

# Tokenize the user input code
tokens, error_flag, code_lines = tokenize(code)

# Check for syntax errors
syntax_errors = check_c_syntax(tokens, code_lines)

# Print formatted output
print("\nTokenized Output:\n" + "="*40)
for token_type, token_value, line_number in tokens:
    print(f"Token Type: {token_type:<12} | Token Value: {token_value} | Line: {line_number}")
print("="*40)

# Print error message if there!!
if error_flag:
    print("\nError detected: Keywords cannot be used as identifiers.")

# Display syntax errors ==> with line numbers
if syntax_errors:
    print("\nConclusion:\n" + "-"*20)
    print("Syntax Errors:\n")
    for error in syntax_errors:
        print(error)
else:
    print("\nConclusion:\nNo syntax errors detected.")
