# Definimos una lista con los nombres y apellidos
integrantes = [
    "José Luis Barría",
    "Marcela Orellana"
]

# Imprimimos la lista
for i, integrante in enumerate(integrantes, start=1):
    print(f"{i}.- {integrante}\n")
