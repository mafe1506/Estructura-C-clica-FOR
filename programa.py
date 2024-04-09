# Leer una lista de palabras separadas por espacios
palabras = input("Por favor, ingresa una lista de palabras separadas por espacios: ")

# Convertir la cadena de entrada en una lista separada por espacios
lista_palabras = palabras.split()

# Solicitar al usuario que ingrese la letra por la que desea filtrar las palabras
letra = input("Por favor, ingresa la letra por la que quieres filtrar las palabras: ")

# Crear una lista para almacenar las palabras que comienzan con la letra especificada
palabras_con_letra = []

# Iterar sobre la lista de palabras y agregar las que comiencen con la letra especificada a la nueva lista
for palabra in lista_palabras:
    if palabra.lower().startswith(letra.lower()):
        palabras_con_letra.append(palabra)

# Imprimir la lista de palabras que comienzan con la letra especificada
print(f"Las palabras que comienzan con la letra '{letra}' son:")
for palabra in palabras_con_letra:
    print(palabra)