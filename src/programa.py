import json
from funciones import *

with open("data/amazon.books.json","r") as f:
    datos = json.load(f)

print(datos)
# listaTitulosLibros(data)