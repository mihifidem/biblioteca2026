libros = [ 
    ("El principito", 1943, True), 
    ("Dune", 1965, False), 
    ("Python para todos", 2022, True), 
    ("Aprende Django", 2024, True)
    ]

print(libros) #1
print(len(libros)) #2
print(libros[1]) #3 ("Dune", 1965, False)
print(libros[2][2]) #4 True 


for libro in libros:
    print(libro)


for titulo,anio,disponible in libros:
    
    print(titulo)
    print(anio)
    print(disponible)
    print() # Separador entre libros
    print("-----") # Línea separadora entre libros

frutas= ["manzana golden", "banana canarias", "naranja valenciana"]
for fruta in frutas:
    print(fruta)
# EJERCICIO 1
# Modificad el programa para mostrar exclusivamente los títulos de los libros disponibles.
#1
for libro in libros:
    if libro[2]:  # Verifica si el libro está disponible
       # ("titulo",anio,disponible)
        print(libro[0])
#2
for titulo,anio,disponible in libros:
    if disponible:
        print(titulo)

#3
print([libro[0] for libro in libros if libro[2]])

# EJERCICIO 2
cont=0
#1
for libro in libros:
    if libro[2]:  # Verifica si el libro está disponible
       # ("titulo",anio,disponible)
        print(libro[0])
        cont += 1
print(cont)

#2
for titulo,anio,disponible in libros:
    if disponible:
        print(titulo)
        cont += 1
print(cont)

#3
print(len([libro[0] for libro in libros if libro[2]]))

libros.append(("Nuevo libro", 2024, True))
print(libros) # Verificar que se ha añadido el nuevo libro
print(len(libros)) # Verificar el número total de libros después de añadir el nuevo libro
print([libro[0] for libro in libros if libro[2]]) # Verificar los títulos de los libros disponibles después de añadir el nuevo libro    


print([libro[0] for libro in libros if libro[2]]) # Verificar los títulos de los libros disponibles después de añadir el nuevo libro
#("En un ligar de La Mancha", 1605, True)

titulos =[] 
for titulo,anio, disponible in libros:
    if disponible:
        titulos.append(titulo)
print(titulos)