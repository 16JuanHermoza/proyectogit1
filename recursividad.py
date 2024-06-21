def mostrar_numero(numero):
    #caso base 
    if numero <= 0:
        return
    #caso recursivo
    else:
        print( numero, end=" ,")
        return mostrar_numero(numero-1)

mostrar_numero(6)
    

#https://pythontutor.com/visualize.html#mode=edit
