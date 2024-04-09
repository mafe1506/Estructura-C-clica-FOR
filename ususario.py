# Solicitar al usuario que ingrese una palabra o frase
palabra_frase = input("Por favor, ingresa una palabra o frase: ")

# Inicializar contadores para cada vocal
conteo_a = 0
conteo_e = 0
conteo_i = 0
conteo_o = 0
conteo_u = 0

# Utilizar un ciclo for para contar cuántas vocales contiene la palabra o frase
for letra in palabra_frase:
    if letra.lower() == 'a':
        conteo_a += 1
    elif letra.lower() == 'e':
        conteo_e += 1
    elif letra.lower() == 'i':
        conteo_i += 1
    elif letra.lower() == 'o':
        conteo_o += 1
    elif letra.lower() == 'u':
        conteo_u += 1

# Mostrar el conteo de cada vocal por separado
print(f"La palabra o frase ingresada contiene:")
print(f"{conteo_a} vocales 'a'")
print(f"{conteo_e} vocales 'e'")
print(f"{conteo_i} vocales 'i'")
print(f"{conteo_o} vocales 'o'")
print(f"{conteo_u} vocales 'u'")
