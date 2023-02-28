import json

with open("data/amazon.books.json","r") as f:
    listaLibros = json.load(f)

def listaTitulosLibros(listaLibros):
    for libro in listaLibros["books"]:
        print(libro["title"])

def numAutores(listaLibros):
    listaAutores = []
    for libro in listaLibros["books"]:
        for autor in libro["authors"]:
            if autor not in listaAutores:
                listaAutores.append(autor)
    
    print(f"Hay un total de {len(listaAutores)} autores en todo el catálogo")
    opcionAutores = input("¿Quieres listar todos los autores? [Y/N]: ")
    if opcionAutores == "Y":
        for autor in listaAutores:
            print(autor)

def busquedaTituloLimite(listaLibros):
    aux = []
    textoBusqueda = input("Introduzca el texto del título para buscar: ")
    limitePaginas = int(input("Introduzca el límite de páginas: "))
    for libro in listaLibros["books"]:
        if textoBusqueda in libro["title"] and libro["pageCount"] < limitePaginas:
            aux.append(libro["title"])
    for libro in aux:
        print(libro)

def librosPorAutor(listaLibros):
    aux = []
    autorBusqueda = input("Introduzca el autor para obtener sus libros: ")
    for libro in listaLibros["books"]:
        for autor in libro["authors"]:
            if autorBusqueda == autor:
                aux.append(libro["title"])
    print("\nLos libros escritos por el autor son: ")
    for libro in aux:
        print(libro)

def actualizacionPorISBN(listaLibros):
    isbnBusqueda = input("Introduzca el ISBN del libro a buscar: ")
    for libro in listaLibros["books"]:
        if isbnBusqueda in libro["isbn"]:
                print("Hemos encontrado el siguiente libro: ", libro["title"])