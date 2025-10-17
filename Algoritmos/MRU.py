#Most Recently Used
def MRU(sequencia, quadros):
    memoria = []
    falhas = 0
    
    for pagina in sequencia:
        
        if pagina in memoria:
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            falhas += 1
            if len(memoria) >= quadros:
                memoria.pop()
            memoria.append(pagina)
            
    return memoria, falhas