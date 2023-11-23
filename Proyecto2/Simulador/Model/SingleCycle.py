import time 
from Processor import Processor

class SingleCycle(Processor):
    def __init__(self, cycleTime):
        Processor.__init__(self,cycleTime)

    def li(self, rd:str, imm:int):
        self.registerFile[self.registerFileDict[rd]] = imm
        print("loaded %d into %s"%(imm, rd))
    
    def add(self, rd:str, rs1:str, rs2:str):
        value1 = self.registerFile[self.registerFileDict[rs1]]
        value2 = self.registerFile[self.registerFileDict[rs2]]
        self.registerFile[self.registerFileDict[rd]] = value1+value2
        print("loaded sum result: %d in %s"%(value1+value2,rd))

    def sw(self, rs1:str, offset:int, rs2:str):
        offset = int(offset)
        addr = self.registerFile[self.registerFileDict[rs2]] + offset
        value = self.registerFile[self.registerFileDict[rs1]]
        self.memory[addr] = value
        print("stored %d in address %d"%(value, addr))

    def addi(self, rd:str, rs2:str, imm:int):
        value  = self.registerFile[self.registerFileDict[rs2]]+imm
        self.registerFile[self.registerFileDict[rd]] = value

        print("loaded sum result: %d in %s"%(value, rd))

    def beq(self, rs1:str, rs2:str, addr:int):
        value1 = self.registerFile[self.registerFileDict[rs1]]
        value2 = self.registerFile[self.registerFileDict[rs2]]
        if value1 == value2:
            self.pc = addr
            self.run(self.memory[addr])
            print("jumped to %d"%(addr))
            return
        print("did not make the jump")
    
    def j(self, addr:int):
        self.run(self.memory[addr])
        self.pc = addr
        print("jumped to %d"%(addr))

    def mul(self, rd:str, rs1:str, rs2:str):
        value1 = self.registerFile[self.registerFileDict[rs1]]
        value2 = self.registerFile[self.registerFileDict[rs2]]
        self.registerFile[self.registerFileDict[rd]] = value1*value2
        print("loaded mul result: %d in %s"%(value1*value2, rd))
    
    def lw(self, rd:str, offset:int, rs1:str):
        offset = int(offset)
        addr = self.registerFile[self.registerFileDict[rs1]]+offset
        value = self.memory[addr]
        self.registerFile[self.registerFileDict[rd]] = value
        print("loaded %d into %s"%(value, rd))

    def bge(self, rs1:str, rs2:str, addr:int):
        value1 = self.registerFile[self.registerFileDict[rs1]]
        value2 = self.registerFile[self.registerFileDict[rs2]]
        if value1 >= value2:
            self.pc = addr
            self.run(self.memory[addr])
            print("jumped to %d"%(addr))
            return
        print("did not make the jump")
    
    def run(self, instruction:str):
        instruction = instruction.replace(" ","")
        operation = instruction.split(",")
        opNem = operation[0]
        if opNem == "li":
            self.li(operation[1],int(operation[2]))
        elif opNem == "add":
            self.add(operation[1],operation[2],operation[3])
        elif opNem == "sw":
            self.sw(operation[1],operation[2],operation[3])
        elif opNem == "addi":
            self.addi(operation[1],operation[2],int(operation[3]))
        elif opNem == "beq":
            addr = self.labels[operation[3]]
            self.beq(operation[1],operation[2],addr)
        elif opNem == "j":
            addr = self.labels[operation[1]]
            self.j(addr)
        elif opNem == "mul":
            self.mul(operation[1],operation[2],operation[3])
        elif opNem == "lw":
            self.lw(operation[1],operation[2],operation[3])
        elif opNem == "bge":
            addr = self.labels[operation[3]]
            self.bge(operation[1],operation[2],addr)
        elif opNem == "call":
            self.hlt = True
        print(opNem)
    def runAll(self):
        for i in range(50):
            try:
                if self.memory[i][-1:]:
                    self.labels[self.memory[i][:-1]] = i
            except:
                break
        while self.pc < 50 and not(self.hlt):
            self.run(self.memory[self.pc])
            self.pc+=1
            time.sleep(self.cycleTime)
            print(self.pc)
            print(self.registerFile)
    def runSteps(self):
        for i in range(50):
            try:
                if self.memory[i][-1:]:
                    self.labels[self.memory[i][:-1]] = i
            except:
                break
        while self.pc < 50 and not(self.hlt):
            input()
            self.run(self.memory[self.pc])
            self.pc+=1
            print(self.pc)
            print(self.registerFile)
singleCycleProc = SingleCycle(0.005)

singleCycleProc.memory[0] = "li, s4, 30"
singleCycleProc.memory[1] = "li, a3, 2"
singleCycleProc.memory[2] = "li, a4, 49"
singleCycleProc.memory[3] = "li, s5, 6"
singleCycleProc.memory[4] = "li, s7, 1"
singleCycleProc.memory[5] = ""
singleCycleProc.memory[6] = "#fill the initial array [0,sieveSize-1]"
singleCycleProc.memory[7] = "li, t0, 0"
singleCycleProc.memory[8] = "add, t1, t1, zero"
singleCycleProc.memory[9] = "add, t1, t1, a4"
singleCycleProc.memory[10] = "add, t0,t0,zero"
singleCycleProc.memory[11] = "add, t0, t0, a3"
singleCycleProc.memory[12] = "addi, s4, s4, 1"
singleCycleProc.memory[13] = ""
singleCycleProc.memory[14] = "fill:"
singleCycleProc.memory[15] = "sw, t0, 0,t1"
singleCycleProc.memory[16] = "addi, t1, t1, 1"
singleCycleProc.memory[17] = "addi, t0, t0, 1"
singleCycleProc.memory[18] = "beq, t0, s4, eliminate"
singleCycleProc.memory[19] = "j, fill"
singleCycleProc.memory[20] = ""
singleCycleProc.memory[21] = ""
singleCycleProc.memory[22] = "eliminate:"
singleCycleProc.memory[23] = "addi, t3, a4, -1"
singleCycleProc.memory[24] = "add, s1, zero, zero"
singleCycleProc.memory[25] = "nextPrime:"
singleCycleProc.memory[26] = "addi, s1, s1, 1"
singleCycleProc.memory[27] = "addi, t3,t3,1"
singleCycleProc.memory[28] = "lw, t5, 0,t3"
singleCycleProc.memory[29] = ""
singleCycleProc.memory[30] = "#calcula el tamano del salto"
singleCycleProc.memory[31] = "mul, s6, t5, s7"
singleCycleProc.memory[32] = "add, t6, zero, t3"
singleCycleProc.memory[33] = "beq, t5, zero, nextPrime"
singleCycleProc.memory[34] = "bge, s1, s5, end"
singleCycleProc.memory[35] = "add, s11, zero, zero"
singleCycleProc.memory[36] = ""
singleCycleProc.memory[37] = "#loop with step size lesser than sqrt of N"
singleCycleProc.memory[38] = "#makes zero what arrives in the step "
singleCycleProc.memory[39] = "loopSieve:"
singleCycleProc.memory[40] = "addi, s11, s11, 1"
singleCycleProc.memory[41] = "add, t6, t6, s6"
singleCycleProc.memory[42] = "sw, zero, 0,t6"
singleCycleProc.memory[43] = "bge, s11, s4, nextPrime"
singleCycleProc.memory[44] = "j, loopSieve"
singleCycleProc.memory[45] = "end:"
singleCycleProc.memory[46] = "call, 10"


singleCycleProc.runAll()


print(singleCycleProc.memory)