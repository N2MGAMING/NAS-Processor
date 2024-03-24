# MOHAMED NASRAOUI
from processor import *
from utilities import *
from datetime import datetime


# Define a class named Interpreter
class Interpreter():
    """
    Class responsible for interpreting and executing instructions.
    """

    # Constructor method to initialize an Interpreter object
    def __init__(self, src, verbose):
        """
        Initialize the Interpreter object with the provided source file and verbosity setting.

        Parameters:
            src (str): Path to the source file containing instructions.
            verbose (bool): Indicates whether verbose mode is enabled or not.
        """
        self.src = src  # Store the path to the source file
        self.lexer = Lexer(src)  # Create a Lexer object for tokenization
        self.parser = Parser()  # Create a Parser object for parsing
        self.PROC = Processor()  # Create a Processor object for execution
        self.verbose = verbose  # Store the verbosity setting
        self.errors = 0  # Initialize error count to 0
        self.labels = []  # Initialize a list to store encountered labels

    # Method to execute the instructions
    def run(self):
        """
        Execute the instructions from the source file.
        """
        code = self.lexer.lex()  # Tokenize the source code
        code = self.parser.pars(code)  # Parse the tokenized code
        for i in range(len(code)):
            for j in range(len(code[i][3])):
                if code[i][3][j][1]=='START':
                    # Check for unexpected START label
                    self.errors = ERRORHANDLER(-4, code[i][3][j-1][0], self.src, self.errors)
        # If no errors occurred during parsing
        if self.errors == 0:
            if self.verbose == True:  # If verbose mode is enabled
                print(code)  # Print the parsed code
            # Get current timestamp
            current_time = datetime.now().strftime("%b %-d %Y, %H:%M:%S:%f")
            print(f"\nExecuting started at {current_time}\n--------------------------------------------------")
            for i in range(len(code)):
                if self.errors == 0:  # If no errors occurred
                    self.labelize(code[i])  # Labelize the code section
            current_time = datetime.now().strftime("%b %-d %Y, %H:%M:%S:%f")
            print(f"--------------------------------------------------\nExecution Ended at {current_time}\n")

    # Method to process labels in the code
    def labelize(self, code):
        """
        Process labels in the code section.

        Parameters:
            code (list): List representing a section of code from the source file.
        """
        if code[2] == 'MAIN':  # If the code section is the main program
            print("-------------------------")
            print("$$$(ExecutionInfo 'MAIN') Started")
            for j in range(len(code[3])):
                if self.errors == 0:  # If no errors occurred
                    self.execute(code[3][j])  # Execute each instruction
            print("$$$(ExecutionInfo 'MAIN') Ended")
        else:
            print(f"$$$(ExecutionInfo 'LABEL') Storing the Label {code[2]}")
            self.labels.append([code[2], code[3]])  # Store label and corresponding instructions

    # Method to execute individual instructions
    def execute(self, code):
        """
        Execute individual instructions.

        Parameters:
            code (list): List representing an instruction.
        """
        if code[1] == "CC":  # Clock Cycle
            print("$$$(ExecutionInfo 'CC') Clock Cycle")
            self.PROC.CLOCK_CYCLE()
        elif code[1] == "RES":  # Display Result
            print("$$$(ExecutionInfo 'RES') Displaying the value in CX")
            print("CX: "+str(self.PROC.P_GET(self.PROC.CX)))
        elif code[1] == "STAT":  # Display Registers
            print("$$$(ExecutionInfo 'STAT') Displaying the value in the registers")
            AX, BX, CX, DX, carry, ZEROFLAG = self.PROC.GET_ALL()
            print(f"AX: {str(AX)}")
            print(f"BX: {str(BX)}")
            print(f"CX: {str(CX)}")
            print(f"DX: {str(DX)}")
            print(f"Carry: {str(carry)}")
            print(f"ZEROFLAG: {str(ZEROFLAG)}")
        elif code[1] == "STO":  # Store value in the specified register
            Reg, ERRORCODE = ConvertREG(code[3], self.PROC)
            self.errors = ERRORHANDLER(ERRORCODE, code[0], self.src, self.errors)
            BitData, ERRORCODE = ConvertDataToBit(code[2])
            self.errors = ERRORHANDLER(ERRORCODE, code[0], self.src, self.errors)
            Value = code[2].replace("INT", "") # Removing INT from the shown string	
            if self.errors == 0:
                self.PROC.P_STORE(BitData, Reg)
                print(f"$$$(ExecutionInfo 'STO') Storing {Value} in {code[3]}")
        elif code[1] == "MOV":  # Move the value of a register to another
            RegIn, ERRORCODE = ConvertREG(code[2], self.PROC)
            self.errors = ERRORHANDLER(ERRORCODE, code[0], self.src, self.errors)
            RegOut, ERRORCODE = ConvertREG(code[3], self.PROC)
            self.errors = ERRORHANDLER(ERRORCODE, code[0], self.src, self.errors)
            if self.errors == 0:
                self.PROC.P_STORE(self.PROC.P_GET(RegIn), RegOut)
                print(f"$$$(ExecutionInfo 'MOV') Storing the value of {code[2]} in {code[3]}")
        elif code[1] == "DO":  # Execute the specified Label
            ExecLabel = 0
            for label in self.labels:
                if label[0] == code[2]:
                    ExecLabel = label
            print(f"\n$$$(ExecutionInfo 'DO') Execution of Label {ExecLabel[0]} started")
            if self.errors == 0:
                cmds = ExecLabel[1]
                for cmd in cmds:
                    self.execute(cmd)  # Execute each instruction in the labeled section
            print(f"$$$(ExecutionInfo 'DO') Execution of Label {ExecLabel[0]} ended\n")
        else:
            print(code)
            self.errors = ERRORHANDLER(-3, code[0], self.src, self.errors)  # Handle unknown syntax error


# Define a class named Lexer
class Lexer():
    """
    Class responsible for lexical analysis of the source code.
    """

    # Constructor method to initialize a Lexer object
    def __init__(self, src):
        """
        Initialize the Lexer object with the provided source file.

        Parameters:
            src (str): Path to the source file.
        """
        self.src = src  # Store the path to the source file
        self.code = []  # Initialize a list to store tokenized code

    # Method to perform lexical analysis
    def lex(self):
        """
        Perform lexical analysis on the source code.

        Returns:
            list: List containing tokenized code.
        """
        with open(self.src, 'r+') as file:  # Open the source file
            unlexed_code = file.readlines()  # Read lines from the file
        lines_count = len(unlexed_code)  # Get the number of lines
        for i in range(lines_count):
            unlexed_code[i] = unlexed_code[i].replace("\n", "")  # Remove newline characters
            if unlexed_code[i] != "":  # If the line is not empty
                if unlexed_code[i][0] != "$":  # If it's not a comment line
                    self.code.append([i+1, unlexed_code[i]])  # Append line number and code to the tokenized list
        return self.code  # Return the tokenized code


# Define a class named Parser
class Parser():
    """
    Class responsible for parsing tokenized code.
    """

    # Constructor method to initialize a Parser object
    def __init__(self):
        """
        Initialize the Parser object.
        """
        self.parsed_code = []  # Initialize a list to store parsed code

    # Method to parse the tokenized code
    def pars(self, code):
        """
        Parse the tokenized code.

        Parameters:
            code (list): List containing tokenized code.

        Returns:
            list: List containing parsed code.
        """
        code = SplitCode(code)  # Split the tokenized code into sections
        labels_count = len(code)  # Get the number of sections
        for i in range(labels_count):
            label = code[i][0][1].split(" ")  # Split the label line into tokens
            if label[0] == "START":  # If it's a START label
                code[i].pop()  # Remove the 'END' label line
                labelcmd = [code[i][0][0], 'LABEL', label[1], []]  # Create a label command to define the label
                for j in range(1, len(code[i])):
                    line = code[i][j][0]
                    cmd = code[i][j][1].split(" ")  # Split the command line into tokens
                    cmd.insert(0, line)  # Insert the line number at the beginning
                    labelcmd[3].append(cmd)  # Append the command to the label command list
                self.parsed_code.append(labelcmd)  # Append the label command to the parsed code
            else:
                cmds = []
                for j in range(len(code[i])):
                    line = code[i][j][0]
                    cmd = code[i][j][1].split(" ")  # Split the command line into tokens
                    cmd.insert(0, line)  # Insert the line number at the beginning
                    cmds.append(cmd)  # Append the command to the command list
                self.parsed_code.append([code[i][0][0], 'LABEL', 'MAIN', cmds])  # Append the MAIN Label to the parsed code
        return self.parsed_code  # Return the parsed code
