import time
class Processor(object):
    def __init__(self, cycleTime):
        self.cycleTime = cycleTime #Tiempo de ciclo
        self.registerFile = [0]*32 #Register File
        self.memory = [None]*500 #Memory
        self.registerFileDict = {}
        self.registerFileDict["zero"] = 0
        self.registerFileDict["ra"] = 1
        self.registerFileDict["sp"] = 2
        self.registerFileDict["gp"] = 3
        self.registerFileDict["tp"] = 4
        self.registerFileDict["t0"] = 5
        self.registerFileDict["t1"] = 6
        self.registerFileDict["t2"] = 7
        self.registerFileDict["s0"] = 8
        self.registerFileDict["s1"] = 9
        self.registerFileDict["a0"] = 10
        self.registerFileDict["a1"] = 11
        self.registerFileDict["a2"] = 12
        self.registerFileDict["a3"] = 13
        self.registerFileDict["a4"] = 14
        self.registerFileDict["a5"] = 15
        self.registerFileDict["a6"] = 16
        self.registerFileDict["a7"] = 17
        self.registerFileDict["s2"] = 18
        self.registerFileDict["s3"] = 19
        self.registerFileDict["s4"] = 20
        self.registerFileDict["s5"] = 21
        self.registerFileDict["s6"] = 22
        self.registerFileDict["s7"] = 23
        self.registerFileDict["s8"] = 24
        self.registerFileDict["s9"] = 25
        self.registerFileDict["s10"] = 26
        self.registerFileDict["s11"] = 27
        self.registerFileDict["t3"] = 28
        self.registerFileDict["t4"] = 29
        self.registerFileDict["t5"] = 30
        self.registerFileDict["t6"] = 31
        self.labels = {}
        self.pc = 0 #PC
        self.hlt = False
        self.memory[0] = "li, s4, 30"
        self.memory[1] = "li, a3, 2"
        self.memory[2] = "li, a4, 49"
        self.memory[3] = "li, s5, 6"
        self.memory[4] = "li, s7, 1"
        self.memory[5] = ""
        self.memory[6] = "#fill the initial array [0,sieveSize-1]"
        self.memory[7] = "li, t0, 0"
        self.memory[8] = "add, t1, t1, zero"
        self.memory[9] = "add, t1, t1, a4"
        self.memory[10] = "add, t0,t0,zero"
        self.memory[11] = "add, t0, t0, a3"
        self.memory[12] = "addi, s4, s4, 1"
        self.memory[13] = ""
        self.memory[14] = "fill:"
        self.memory[15] = "sw, t0, 0,t1"
        self.memory[16] = "addi, t1, t1, 1"
        self.memory[17] = "addi, t0, t0, 1"
        self.memory[18] = "beq, t0, s4, eliminate"
        self.memory[19] = "j, fill"
        self.memory[20] = ""
        self.memory[21] = ""
        self.memory[22] = "eliminate:"
        self.memory[23] = "addi, t3, a4, -1"
        self.memory[24] = "add, s1, zero, zero"
        self.memory[25] = "nextPrime:"
        self.memory[26] = "addi, s1, s1, 1"
        self.memory[27] = "addi, t3,t3,1"
        self.memory[28] = "lw, t5, 0,t3"
        self.memory[29] = ""
        self.memory[30] = "#calcula el tamano del salto"
        self.memory[31] = "mul, s6, t5, s7"
        self.memory[32] = "add, t6, zero, t3"
        self.memory[33] = "beq, t5, zero, nextPrime"
        self.memory[34] = "bge, s1, s5, end"
        self.memory[35] = "add, s11, zero, zero"
        self.memory[36] = ""
        self.memory[37] = "#loop with step size lesser than sqrt of N"
        self.memory[38] = "#makes zero what arrives in the step "
        self.memory[39] = "loopSieve:"
        self.memory[40] = "addi, s11, s11, 1"
        self.memory[41] = "add, t6, t6, s6"
        self.memory[42] = "sw, zero, 0,t6"
        self.memory[43] = "bge, s11, s4, nextPrime"
        self.memory[44] = "j, loopSieve"
        self.memory[45] = "end:"
        self.memory[46] = "call, 10"
        
    def li(self, rd, imm):
        pass

    def add(self, rd, rs1, rs2):
        pass

    def sw(self, rs1, offset, rs2):
        pass

    def addi(self, rd, rs2, imm):
        pass

    def beq(self, rs1, rs2, addr):
        pass
    
    def j(self, addr):
        pass

    def mul(self, rd, rs1, rs2):
        pass

    def lw(self, rd, offset, rs1):
        pass

    def bge(self, rs1, rs2, addr):
        pass

    def call(self, code):
        pass

    def runAll(self):
        pass

    def run(self, instruction:str):
        pass