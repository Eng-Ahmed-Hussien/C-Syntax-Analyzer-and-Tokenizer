# C Syntax Analyzer and Tokenizer

## Description

This Python script analyzes C code for syntax errors and tokenizes it into various components. It uses regular expressions to identify different types of tokens such as keywords, operators, identifiers, and comments, while also performing syntax checks to ensure the code adheres to basic C syntax rules.

## Features

- **Tokenization**: Breaks down the input C code into tokens based on defined specifications.
- **Syntax Checking**: Validates the C code for:
  - Correct placement of `#include` directives
  - Presence of the `main` function
  - Balanced braces
  - Proper termination of statements with semicolons
- **Error Detection**: Identifies and reports any keyword usage errors and syntax errors with line numbers.

## Usage

1. Run the script in a Python environment.
2. Input C code line by line.
3. Type `done` when you finish inputting your code to analyze it.
4. The script will output the tokenized results and any detected syntax errors.

### Example Input

```c
#include <stdio.h>
int main() {
    int x = 10;
    printf("Hello World");
    return 0;
}
```

### Example Output

```Elixir
Tokenized Output:
========================================
Token Type: PREPROCESSOR  | Token Value: #include <stdio.h> | Line: 1
Token Type: KEYWORD       | Token Value: int                | Line: 2
Token Type: IDENTIFIER    | Token Value: main               | Line: 2
Token Type: PUNCTUATOR    | Token Value: {                  | Line: 2
Token Type: KEYWORD       | Token Value: int                | Line: 3
Token Type: IDENTIFIER    | Token Value: x                  | Line: 3
Token Type: ASSIGNMENT    | Token Value: =                  | Line: 3
Token Type: CONSTANTINT   | Token Value: 10                 | Line: 3
Token Type: PUNCTUATOR    | Token Value: ;                  | Line: 3
Token Type: FUNCTION      | Token Value: printf             | Line: 4
Token Type: STRING        | Token Value: "Hello World"      | Line: 4
Token Type: PUNCTUATOR    | Token Value: ;                  | Line: 4
Token Type: KEYWORD       | Token Value: return             | Line: 5
Token Type: CONSTANTINT   | Token Value: 0                  | Line: 5
Token Type: PUNCTUATOR    | Token Value: ;                  | Line: 5
Token Type: PUNCTUATOR    | Token Value: }                  | Line: 6
========================================

Conclusion:
No syntax errors detected.
```

## Team Members

- **[Eng/ Ahmed Hesham]** - Supervisor | Compiler Design Assistant Lecturer
- **Ahmed Hussien El Sayed** - Project Lead | Developer | Documentation Specialist.
- **[Ahmed Ebrahim El Sayed ]** - Developer | Tester.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by educational projects focused on C programming language syntax analysis.
- Special thanks to Eng / Ahmed Hesham for His explanation and support.
- Special thanks to the Python community for their resources and support.
