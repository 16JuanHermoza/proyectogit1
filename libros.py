def totalPaginas(Libros):
    if len(Libros) == 1:
        return Libros[0]
    else:
        return Libros[0] + totalPaginas(Libros[1:])

print(totalPaginas([10, 20, 30, 40]))
