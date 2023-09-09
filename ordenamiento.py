# Se crea un objeto tipo escáner que recibe ingresos del sistema
print("Ingrese la cantidad de números: ")
n = int(input())

numeros = []

print("Ingrese los números:")
for i in range(n):
    numeros.append(int(input()))

# Ordenar utilizando el algoritmo de selección (Selection Sort)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if numeros[j] < numeros[min_index]:
            min_index = j

    # Intercambiar números
    numeros[i], numeros[min_index] = numeros[min_index], numeros[i]

print("Números ordenados de menor a mayor:")
for num in numeros:
    print(num, end=" ")