# MOHAMED NASRAOUI
# Define a function to convert data to bits

def decimalToBinary(Value): 
    binary = "{0:b}".format(Value)
    while len(binary)!=4:
        binary = "0" + binary
    return binary

def ConvertDataToBit(data):
    """
    Convert data to a list of bits.

    Parameters:
        data (str): Data to be converted.

    Returns:
        list: List of bits representing the data.
        int: Error code (0 if successful, -1 otherwise).
    """
    if data[0:3] == "INT" and data[3:].isnumeric() == True:
        Value = int(data[3:])
        data = decimalToBinary(Value)
    BitData = []
    ERRORCODE = -1
    ValidBitValue = True 
    if len(data) == 4 and data.isnumeric() == True:
        for i in range(4):
            if int(data[i])!=0 and int(data[i])!=1:# Verify that the value to store are 0 or 1
                ValidBitValue = False
            BitData.append(int(data[i]))
        if ValidBitValue == True:
            ERRORCODE = 0

    return BitData, ERRORCODE

# Define a function to convert register names to processor registers
def ConvertREG(Reg, PROC):
    """
    Convert register name to corresponding processor register.

    Parameters:
        Reg (str): Register name to be converted.
        PROC (Processor): Processor object containing registers.

    Returns:
        Register: Processor register corresponding to the given name.
        int: Error code (0 if successful, -2 otherwise).
    """
    PREG = 0
    ERRORCODE = -2
    if Reg == "AX":
        PREG = PROC.AX
        ERRORCODE = 0
    elif Reg == "BX":
        PREG = PROC.BX
        ERRORCODE = 0
    elif Reg == "CX":
        PREG = PROC.CX
        ERRORCODE = 0
    elif Reg == "DX":
        PREG = PROC.DX
        ERRORCODE = 0
    elif Reg == "CARRY":
        PREG = PROC.carry
        ERRORCODE = 0
    elif Reg == "ZEROFLAG":
        PREG = PROC.ZEROFLAG
        ERRORCODE = 0
    return PREG, ERRORCODE

# Define a function to handle error messages
def ERRORDICT(ERRORCODE, line, src):
    """
    Print error message based on error code.

    Parameters:
        ERRORCODE (int): Error code indicating the type of error.
        line (int): Line number where the error occurred.
        src (str): Source file where the error occurred.
    """
    if ERRORCODE == -1:
        print(f">>>InterpreterError at line {line} in {src}: Invalid data format in the STO command.")
    if ERRORCODE == -2:
        print(f">>>InterpreterError at line {line} in {src}: Invalid Register name in the STO command.")
    if ERRORCODE == -3:
        print(f">>>InterpreterError at line {line} in {src}: Invalid syntax, unknown command.")
    if ERRORCODE == -4:
        print(f">>>InterpreterError at line {line} in {src}: Unexpected START label found. When using START, commands must be written inside labels.")
    if ERRORCODE == -5:
        print(f">>>InterpreterError at line {line} in {src}: Invalid module format in the INCLUDE header.")
    if ERRORCODE == -6:
        print(f">>>InterpreterError at line {line} in {src}: Invalid module, module not found.")

# Define a function to handle errors during interpretation
def ERRORHANDLER(ERRORCODE, line, src, errornum):
    """
    Handle errors encountered during interpretation.

    Parameters:
        ERRORCODE (int): Error code indicating the type of error.
        line (int): Line number where the error occurred.
        src (str): Source file where the error occurred.
        errornum (int): Current count of errors.

    Returns:
        int: Updated count of errors.
    """
    ERRORDICT(ERRORCODE, line, src)
    if ERRORCODE != 0:
        errornum += 1
    return errornum

# Define a function to split code into sections
def SplitCode(code):
    """
    Split code into sections based on END markers.

    Parameters:
        code (list): List of code lines.

    Returns:
        list: List of code sections.
    """
    result = []
    section = []
    for i in range(len(code)):
        section.append(code[i])
        if code[i][1] == "END" or i == len(code) - 1 or code[i][1][0] == "#":
            result.append(section)
            section = []
    return result

def returnsrc(module, line, src, errors):
    modulesrc = ""
    if module[0] == '<':
        module = module.replace("<", "").replace(">", "")
        modulesrc = "./Libraries/"+module+".nas"
        try:
            with open(modulesrc, 'r') as file:
                pass
        except Exception:
            errors = ERRORHANDLER(-6, line, src, errors)
    elif module[0] == '"':
        module = module.replace('"', "")
        modulesrc = module
        try:
            with open(modulesrc, 'r') as file:
                pass
        except Exception:
            errors = ERRORHANDLER(-6, line, src, errors)
    else:
        errors = ERRORHANDLER(-5, line, src, errors)

    return modulesrc, errors
