# NAS Processor Emulator

## Overview
NAS (Not A Standard) Processor Emulator is a software project aimed at simulating the behavior of a theoretical processor named the NAS processor. The project consists of various components including an interpreter, processor modules, utility functions, and an example NAS processor assembly language.

## Features
- Interpretation and execution of NAS assembly language instructions.
- Processor modules including registers, ALU (Arithmetic Logic Unit), and clock cycle control.
- Error handling for invalid instructions or syntax errors.
- Support for label-based program execution.

## Components
1. **Interpreter**: Interprets the NAS assembly language code, performs lexical analysis, parsing, and execution of instructions.
2. **Processor Modules**:
   - **Registers**: AX, BX, CX, and DX 4 bit registers with corresponding operations like storing, loading, and clearing.
   - **ALU (Arithmetic Logic Unit)**: Performs arithmetic operations like addition and subtraction.
   - **Clock Cycle Control**: Controls the execution flow based on the clock cycle.
3. **Utilities**: Utility functions for error handling, data conversion, and code splitting.
4. **Example Assembly Language**: An example assembly language file demonstrating various NAS instructions and program structure.

## Getting Started
To run the NAS Processor Emulator, follow these steps:
1. Clone the repository: `git clone https://github.com/N2MGAMING/NAS-Processor.git`
2. Navigate to the project directory: `cd NAS-Processor`
3. Execute the main script: `python emulator.py`
4. Follow the prompts to load and execute NAS assembly language programs.

## Usage
- **Help Command**: Use the `help` command to display available commands and usage information.
- **Configuration**: Use the `config` command to change configuration settings such as enabling verbose mode.
- **Execution**: Load and execute NAS assembly language programs using the `run` command.

## Example
An example of a NAS assembly language source file is present in the code.nas file.

## License
This project is licensed under the [MIT License](LICENSE).