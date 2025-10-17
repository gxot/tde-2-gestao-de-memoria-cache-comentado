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
            
def LRU(sequencia, quadros):
    memoria = []
    falhas = 0
    
    for pagina in sequencia:
        if pagina in memoria:
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            falhas += 1
            if len(memoria) >= quadros:
                memoria.pop(0)
            memoria.append(pagina)
    
    return memoria, falhas
    
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

quadros = 8

print("="*40)
print("TESTE A")
print("="*40)


sequencia_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]

memoria_a_fifo, falhas_a_fifo = FIFO(sequencia_a, quadros)
memoria_a_lru, falhas_a_lru = LRU(sequencia_a, quadros)
memoria_a_mru, falhas_a_mru = MRU(sequencia_a, quadros)

print("\nFIFO")
print(f"Memória final: {memoria_a_fifo}")
print(f"Falhas: {falhas_a_fifo}")
if 7 in memoria_a_fifo:
    print(f"Página 7 está no QUADRO {memoria_a_fifo.index(7)}")
else:
    print("Página 7 NÃO está na memória")

print("\nLRU")
print(f"Memória final: {memoria_a_lru}")
print(f"Falhas: {falhas_a_lru}")
if 7 in memoria_a_lru:
    print(f"Página 7 está no QUADRO {memoria_a_lru.index(7)}")
else:
    print("Página 7 NÃO está na memória")

print("\nMRU")
print(f"Memória final: {memoria_a_mru}")
print(f"Falhas: {falhas_a_mru}")
if 7 in memoria_a_mru:
    print(f"Página 7 está no QUADRO {memoria_a_mru.index(7)}")
else:
    print("Página 7 NÃO está na memória")
    
# ===============================================================================================

print("\n" + "="*40)
print("TESTE B")
print("="*40)


sequencia_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]

memoria_b_fifo, falhas_b_fifo = FIFO(sequencia_b, quadros)
memoria_b_lru, falhas_b_lru = LRU(sequencia_b, quadros)
memoria_b_mru, falhas_b_mru = MRU(sequencia_b, quadros)

print("\nFIFO")
print(f"Memória final: {memoria_b_fifo}")
print(f"Falhas: {falhas_b_fifo}")
if 11 in memoria_b_fifo:
    print(f"Página 11 está no QUADRO {memoria_b_fifo.index(11)})")
else:
    print("Página 11 NÃO está na memória")

print("\nLRU")
print(f"Memória final: {memoria_b_lru}")
print(f"Falhas: {falhas_b_lru}")
if 11 in memoria_b_lru:
    print(f"Página 11 está no QUADRO {memoria_b_lru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

print("\nMRU")
print(f"Memória final: {memoria_b_mru}")
print(f"Falhas: {falhas_b_mru}")
if 11 in memoria_b_mru:
    print(f"Página 11 está no QUADRO {memoria_b_mru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

# ===============================================================================================

print("\n" + "="*40)
print("TESTE C")
print("="*40)


sequencia_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

memoria_c_fifo, falhas_c_fifo = FIFO(sequencia_c, quadros)
memoria_c_lru, falhas_c_lru = LRU(sequencia_c, quadros)
memoria_c_mru, falhas_c_mru = MRU(sequencia_c, quadros)

print("\nFIFO")
print(f"Memória final: {memoria_c_fifo}")
print(f"Falhas: {falhas_c_fifo}")
if 11 in memoria_c_fifo:
    print(f"Página 11 está no QUADRO {memoria_c_fifo.index(11)})")
else:
    print("Página 11 NÃO está na memória")

print("\nLRU")
print(f"Memória final: {memoria_c_lru}")
print(f"Falhas: {falhas_c_lru}")
if 11 in memoria_c_lru:
    print(f"Página 11 está no QUADRO {memoria_c_lru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

print("\nMRU")
print(f"Memória final: {memoria_c_mru}")
print(f"Falhas: {falhas_c_mru}")
if 11 in memoria_c_mru:
    print(f"Página 11 está no QUADRO {memoria_c_mru.index(11)})")
else:
    print("Página 11 NÃO está na memória")


def media (falha_a, falha_b, falha_c): 
    soma_falhas = falha_a + falha_b + falha_c 
    
    media = soma_falhas / 3

    return media

media_falhas_fifo = media(falhas_a_fifo, falhas_b_fifo, falhas_c_fifo)
media_falhas_lru = media(falhas_a_lru, falhas_b_lru, falhas_c_lru)
media_falhas_mru = media(falhas_a_mru, falhas_b_mru, falhas_c_mru)

print("\n" + "="*40)
print("Méida final de Page Faults")
print("="*40)

print("\nFIFO")
print(f"Falhas: {media_falhas_fifo}")

print("\nLRU")
print(f"Falhas: {media_falhas_lru}")

print("\nMRU")
print(f"Falhas: {media_falhas_mru}")



