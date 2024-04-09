# Leer una lista de números separados por espacios
numeros = input("Por favor, ingresa una lista de números separados por espacios: ")

# Convertir la cadena de entrada en una lista de números
lista_numeros = list(map(int, numeros.split()))

# Inicializar la variable para almacenar la suma de los números pares
suma_pares = 0

# Iterar sobre la lista de números y sumar los números pares
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares += numero

# Imprimir la suma de los números pares
print(f"La suma de los números pares es: {suma_pares}")