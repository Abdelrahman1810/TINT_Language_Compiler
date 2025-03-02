# TINY Compiler

This repository contains a compiler for the TINY programming language, developed as part of a compiler design course project. The TINY language is a simplified programming language used primarily for educational purposes to illustrate fundamental concepts in compiler construction. [TINY_resource](https://a7medayman6.github.io/Tiny-Compiler/?utm_source=chatgpt.com)

## Features

- **Lexical Analysis (Scanner):** Tokenizes the input source code into a sequence of tokens, identifying keywords, identifiers, literals, and symbols.

- **Syntax Analysis (Parser):** Analyzes the token sequence to construct a parse tree based on the TINY language grammar, ensuring the source code adheres to the language's syntactic rules.

- **Semantic Analysis:** Performs checks for semantic correctness, such as type checking and scope resolution.

- **Code Generation:** Translates the parse tree into intermediate code or target code for execution.

## Repository Structure

- **`Scanner.py`:** Contains the implementation of the lexical analyzer.

- **`Parser.py`:** Implements the syntax analyzer.

- **`Tokens.py`:** Defines the token types and related utilities.

- **`grammer.py`:** Contains the grammar definitions for the TINY language.

- **`Tiny_compiler.py`:** Integrates the scanning and parsing processes to compile TINY source code.

- **`Correct_Codes/`:** Directory containing sample TINY programs that are syntactically and semantically correct.

- **`Wrong_Codes/`:** Directory containing sample TINY programs that contain errors, used for testing the compiler's error detection capabilities.

- **`Report.pdf` and `Report.docx`:** Documentation detailing the design and implementation of the compiler.

## Getting Started

To use the TINY compiler:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Abdelrahman1810/TINT_Language_Compiler.git
   ```


2. **Navigate to the Repository Directory:**

   ```bash
   cd TINY_Compiler
   ```


3. **Run the Compiler:**

   ```bash
   python Tiny_compiler.py <path_to_tiny_source_code>
   ```


   Replace `<path_to_tiny_source_code>` with the path to your TINY language source file.

## Prerequisites

- Python 3.x

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your changes.

## Acknowledgments

Special thanks to the contributors and the academic community for their support and resources in compiler design. 

## Contact info 💜
<a href="https://linktr.ee/A_Hassanen" target="_blank">
  <img align="left" alt="Linktree" width="150px" src="https://app.ashbyhq.com/api/images/org-theme-wordmark/b3f78683-a307-4014-b236-373f18850e2c/d54b020a-ff53-455a-9d52-c90c0f4f2081.png" />
</a>