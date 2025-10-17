#First In First Out
def FIFO(sequencia, quadros):
    memoria = []
    falhas = 0
    
    for pagina in sequencia:
        
        if pagina not in memoria:
            falhas +=1
            if len(memoria) >= quadros:
                memoria.pop(0)
            memoria.append(pagina)
    
    return memoria, falhas