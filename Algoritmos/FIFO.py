#First In First Out

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