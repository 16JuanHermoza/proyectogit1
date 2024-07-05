def palindroma(lista):
    while(len(lista)> 0):
        if lista[0] == lista [-1]:
            lista = lista[1:-1]
            print(lista)
        else:
            print("no es palindroma")
    if(len(lista)==0):
        print("es palindroma")

mi_lista = [1,2,3,3,2,1]
print(palindroma(mi_lista))

 

