#Define a função e seus parâmetros
def FIFO(sequencia, quadros):

    #Inicia a variável "memoria"(array) e "falhas"(inteiro)
    memoria = []
    falhas = 0
    
    #Itera sobre sequencia, cada iteração vira uma "página"
    for pagina in sequencia:
        
        #Confere se a "pagina" não está no array "memoria"
        if pagina not in memoria:
            #Incrementa 1 na contagem de Page Fault
            falhas +=1
            #Confere se a quantidade de itens no array "memoria" é maior que a quantidade de quadros definidos
            if len(memoria) >= quadros:
                #Remove a primeira pagina do array "memoria" devido ao index estar setado como 0
                memoria.pop(0)
            #Adiciona a "pagina" ao final do array "memoria"
            memoria.append(pagina)
    #Retorna os dados obtidos
    return memoria, falhas
            


#Define a função e seus parâmetros
def LRU(sequencia, quadros):

    #Inicia a variável "memoria"(array) e "falhas"(inteiro)
    memoria = []
    falhas = 0
    
    #Itera sobre sequencia, cada iteração vira uma "página"
    for pagina in sequencia:

        #Confere se a "pagina" está no array "memoria"
        if pagina in memoria:

            #Remove a "pagina" de onde ela estiver no array "memoria"
            #e realoca ela no final do array
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            #Incrementa 1 na contagem de Page Fault
            falhas += 1
            #Confere se a quantidade de itens no array "memoria" é maior que a quantidade de quadros definidos
            if len(memoria) >= quadros:
                #Remove a primeira "pagina" do array "memoria" devido ao index estar setado como 0
                memoria.pop(0)
            #Adiciona a "pagina" ao final do array "memoria"    
            memoria.append(pagina)
    #Retorna os dados obtidos
    return memoria, falhas




#Define a função e seus parâmetros
def MRU(sequencia, quadros):

    #Inicia a variável "memoria"(array) e "falhas"(inteiro)
    memoria = []
    falhas = 0
    
    #Itera sobre sequencia, cada iteração vira uma "página"
    for pagina in sequencia:
        
        #Confere se a "pagina" está no array "memoria"
        if pagina in memoria:

            #Remove a "pagina" de onde ela estiver no array "memoria"
            #e realoca ela no final do array
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            #Incrementa 1 na contagem de Page Fault
            falhas += 1
            #Confere se a quantidade de itens no array "memoria" é maior que a quantidade de quadros definidos
            if len(memoria) >= quadros:
                #Remove a útima "pagina" do array "memoria"
                memoria.pop()
            #Adiciona a "pagina" ao final do array "memoria" 
            memoria.append(pagina)
    #Retorna os dados obtidos        
    return memoria, falhas

#Define a quantidade fixa de quadros (dada no enunciado)
quadros = 8

#Separador de testes
print("="*40)
print("TESTE A")
print("="*40)

#Define a sequência A (dada no enunciado)
sequencia_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]

#Dados retornados das funções são passados para suas devidas variáveis
memoria_a_fifo, falhas_a_fifo = FIFO(sequencia_a, quadros)
memoria_a_lru, falhas_a_lru = LRU(sequencia_a, quadros)
memoria_a_mru, falhas_a_mru = MRU(sequencia_a, quadros)

#Teste A FIFO
print("\nFIFO")
print(f"Memória final: {memoria_a_fifo}")
print(f"Falhas: {falhas_a_fifo}")
if 7 in memoria_a_fifo:
    print(f"Página 7 está no QUADRO {memoria_a_fifo.index(7)}")
else:
    print("Página 7 NÃO está na memória")

#Teste A LRU
print("\nLRU")
print(f"Memória final: {memoria_a_lru}")
print(f"Falhas: {falhas_a_lru}")
if 7 in memoria_a_lru:
    print(f"Página 7 está no QUADRO {memoria_a_lru.index(7)}")
else:
    print("Página 7 NÃO está na memória")

#Teste A MRU
print("\nMRU")
print(f"Memória final: {memoria_a_mru}")
print(f"Falhas: {falhas_a_mru}")
if 7 in memoria_a_mru:
    print(f"Página 7 está no QUADRO {memoria_a_mru.index(7)}")
else:
    print("Página 7 NÃO está na memória")
    
# ===============================================================================================

#Separador de testes
print("\n" + "="*40)
print("TESTE B")
print("="*40)

#Define a sequência B (dada no enunciado)
sequencia_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]

#Dados retornados das funções são passados para suas devidas variáveis
memoria_b_fifo, falhas_b_fifo = FIFO(sequencia_b, quadros)
memoria_b_lru, falhas_b_lru = LRU(sequencia_b, quadros)
memoria_b_mru, falhas_b_mru = MRU(sequencia_b, quadros)

#Teste B FIFO
print("\nFIFO")
print(f"Memória final: {memoria_b_fifo}")
print(f"Falhas: {falhas_b_fifo}")
if 11 in memoria_b_fifo:
    print(f"Página 11 está no QUADRO {memoria_b_fifo.index(11)})")
else:
    print("Página 11 NÃO está na memória")

#Teste B LRU
print("\nLRU")
print(f"Memória final: {memoria_b_lru}")
print(f"Falhas: {falhas_b_lru}")
if 11 in memoria_b_lru:
    print(f"Página 11 está no QUADRO {memoria_b_lru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

#Teste B MRU
print("\nMRU")
print(f"Memória final: {memoria_b_mru}")
print(f"Falhas: {falhas_b_mru}")
if 11 in memoria_b_mru:
    print(f"Página 11 está no QUADRO {memoria_b_mru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

# ===============================================================================================

#Separador de testes
print("\n" + "="*40)
print("TESTE C")
print("="*40)

#Define a sequência C (dada no enunciado)
sequencia_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

#Dados retornados das funções são passados para suas devidas variáveis
memoria_c_fifo, falhas_c_fifo = FIFO(sequencia_c, quadros)
memoria_c_lru, falhas_c_lru = LRU(sequencia_c, quadros)
memoria_c_mru, falhas_c_mru = MRU(sequencia_c, quadros)

#Teste C FIFO
print("\nFIFO")
print(f"Memória final: {memoria_c_fifo}")
print(f"Falhas: {falhas_c_fifo}")
if 11 in memoria_c_fifo:
    print(f"Página 11 está no QUADRO {memoria_c_fifo.index(11)})")
else:
    print("Página 11 NÃO está na memória")

#Teste C LRU
print("\nLRU")
print(f"Memória final: {memoria_c_lru}")
print(f"Falhas: {falhas_c_lru}")
if 11 in memoria_c_lru:
    print(f"Página 11 está no QUADRO {memoria_c_lru.index(11)})")
else:
    print("Página 11 NÃO está na memória")

#Teste C MRU
print("\nMRU")
print(f"Memória final: {memoria_c_mru}")
print(f"Falhas: {falhas_c_mru}")
if 11 in memoria_c_mru:
    print(f"Página 11 está no QUADRO {memoria_c_mru.index(11)})")
else:
    print("Página 11 NÃO está na memória")


#Função para descobri a média de Page Faults por política de substituição
def media (falha_a, falha_b, falha_c): 
    soma_falhas = falha_a + falha_b + falha_c 
    
    media = soma_falhas / 3

    return media

#Dados retornados da função são passados para suas devidas variáveis
media_falhas_fifo = media(falhas_a_fifo, falhas_b_fifo, falhas_c_fifo)
media_falhas_lru = media(falhas_a_lru, falhas_b_lru, falhas_c_lru)
media_falhas_mru = media(falhas_a_mru, falhas_b_mru, falhas_c_mru)

#Separador
print("\n" + "="*40)
print("Méida final de Page Faults")
print("="*40)

#Média de Page faults FIFO
print("\nFIFO")
print(f"Falhas: {media_falhas_fifo}")

#Média de Page faults LRU
print("\nLRU")
print(f"Falhas: {media_falhas_lru}")

#Média de Page faults MRU
print("\nMRU")
print(f"Falhas: {media_falhas_mru}")



