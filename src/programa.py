from funciones import *

print("Bienvenido al proyecto JSON")

menu='''
    1 - Lista los títulos de los libros
    2 - Número de autores
    3 - Búsqueda por título y límite de páginas
    4 - Libros escritos por autor
    5 - Modificación de datos del libro
    6 - Salir
    '''

opcion = 0

while opcion !=6:
    print(menu)
    opcion = int(input("Introduce una opción: "))

    if opcion==1:
        listaTitulosLibros(listaLibros)

    if opcion==2:
        numAutores(listaLibros)

    if opcion==3:
        busquedaTituloLimite(listaLibros)

    if opcion==4:
        librosPorAutor(listaLibros)

    if opcion==5:
        actualizacionPorISBN(listaLibros)
