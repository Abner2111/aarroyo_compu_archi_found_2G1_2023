from Model.SingleCycle import SingleCycle


while True:

    tipo = input("Ingrese A para Step by step o B para ejecución continua o B para step by step: ")
    cycleTime = float(input("Ingrese el periodo de reloj en segundos: "))
    singleCycleProc = SingleCycle(cycleTime)
    tipo = tipo.lower()
    if tipo.replace(" ","") == "a":
        singleCycleProc.runSteps()
    elif tipo.replace(" ","") =="b":
        singleCycleProc.runAll()
