# MOHAMED NASRAOUI
# Global variable storing register indices in reverse order
global RegIndex
RegIndex = [3, 2, 1, 0]

# Register class representing a generic register
class Register():
    def __init__(self):
        self.data = [0]*4

    # Method to store values into the register
    def STORE(self, Value):
        for i in RegIndex:
            self.data[i] = Value[i]

    # Method to clear the register
    def CLEAR(self):
        for i in RegIndex:
            self.data[i] = 0

# Arithmetic Logic Unit class representing the ALU component
class ALU():
    def __init__(self):
        self.carry = 0
        self.result = [0]*4
        self.ZEROFLAG = 0

    # Method to perform addition operation
    def ADD(self, a, b):
        for i in RegIndex:
            SumBit = a[i] + b[i] + self.carry
            self.result[i] = SumBit%2
            self.carry = SumBit//2

    # Method to perform subtraction operation
    def SUBTRACT(self, a, b):
        for i in RegIndex:
            SumBit = a[i] - b[i] + self.carry
            self.result[i] = SumBit%2
            self.carry = SumBit//2
    
    # Method to perform comparison
    def COMPARE(self, a, b):
    	self.SUBTRACT(a, b)
    	if self.result != [0]*4:
    		self.ZEROFLAG = 1

    # Method to clear the ALU
    def CLEAR(self):
        for i in RegIndex:
            self.result[i] = 0
        self.carry = 0
        self.ZEROFLAG = 0

# Processor class representing the main processor
class Processor():
    def __init__(self):
        self.AX = Register()
        self.BX = Register()
        self.CX = Register()
        self.DX = Register()
        self.carry = 0
        self.ZEROFLAG = 0
        self.ALU = ALU()

    # Method to clear all registers and ALU
    def CLEAR_ALL(self):
        self.AX.CLEAR()
        self.BX.CLEAR()
        self.CX.CLEAR()
        self.DX.CLEAR()
        self.carry = 0
        self.ZEROFLAG = 0
        self.ALU.CLEAR()

    # Method to perform addition operation
    def P_ADD(self):
        self.ALU.ADD(self.AX.data, self.BX.data)
        self.CX.STORE(self.ALU.result)
        self.carry = self.ALU.carry

    # Method to perform subtraction operation
    def P_SUBTRACT(self):
        self.ALU.SUBTRACT(self.AX.data, self.BX.data)
        self.CX.STORE(self.ALU.result)
        self.carry = self.ALU.carry

    # Method to perform comparison
    def P_CMP(self):
    	self.ALU.COMPARE(self.AX.data, self.BX.data)
    	self.CX.STORE(self.ALU.result)
    	self.carry = self.ALU.carry
    	self.ZEROFLAG = self.ALU.ZEROFLAG

    # Method to store values into a register
    def P_STORE(self, Value, Reg):
        for i in RegIndex:
            Reg.data[i] = Value[i]

    # Method to get values from a register
    def P_GET(self, Reg):
        return Reg.data

    # Method representing a clock cycle
    def CLOCK_CYCLE(self):
        if self.DX.data == [0]*4 :
            self.CLEAR_ALL()
        elif self.DX.data == [0, 0, 0, 1] :
            self.P_ADD()
        elif self.DX.data == [0, 0, 1, 0] :
            self.P_SUBTRACT()
        elif self.DX.data == [0, 0, 1, 1] :
            self.P_CMP()

    # Method to get data from all registers
    def GET_ALL(self):
        return self.AX.data, self.BX.data, self.CX.data, self.DX.data, self.carry, self.ZEROFLAG