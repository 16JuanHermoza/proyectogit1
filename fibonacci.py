def fibonacci(x):
    #caso base 
    if (x == 0 ):
        return 0
    elif(x == 1):
        return 1
    #recursividad
    else: 
        return fibonacci(x - 1) + fibonacci(x - 2)
    

print(fibonacci(5))