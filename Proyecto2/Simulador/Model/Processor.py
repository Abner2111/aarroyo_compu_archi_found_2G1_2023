import time
class Processor(object):
    def __init__(self, cycleTime):
        self.cycleTime = cycleTime
        self.registerFile = [0]*32
        self.memory = [None]*80
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
        self.pc = 0
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