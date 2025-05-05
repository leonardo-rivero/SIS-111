def suma_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            suma += numero
    return suma

# Ejemplo de uso

resultado = suma_pares(numeros)
print(f"La suma de los números pares es: {resultado}")