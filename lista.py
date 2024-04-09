# Leer una lista de nombres separados por espacios
nombres = input("Por favor, ingresa una lista de nombres separados por espacios: ")

# Convertir la cadena de entrada en una lista separada por espacios
lista_nombres = nombres.split()

# Ordenar la lista alfabéticamente
lista_nombres.sort()

# Imprimir la lista en orden alfabético
print("La lista de nombres en orden alfabético es:")
for nombre in lista_nombres:
    print(nombre)