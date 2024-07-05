def palindroma(lista):
    while(len(lista)> 0):
        if lista[0] == lista [-1]:
            lista = lista[1:-1]
            print(lista)
        else:
            print("no es palindroma")
            break
    if(len(lista)==0):
        print("es palindroma")
mi_lista = [1,2,3,3,2,1]
print(palindroma(mi_lista))

 
def palindorma_recursiva(lista):
    #caso base  
    if len(lista) <=1:
        return "es palindrome"
    #recursividad
    elif lista[0] == lista [-1]:
        return palindorma_recursiva(lista[1:-1])
    else:
        return "no es palindrome"
    
mi_lista = [1,2,3,3,2,1]
print(palindorma_recursiva(mi_lista))


