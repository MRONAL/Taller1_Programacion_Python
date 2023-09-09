# Se crea un objeto tipo escáner que recibe ingresos del sistema
print("Ingrese el valor del lado A:")
ladoA = float(input())
print("Ingrese el valor del lado B:")
ladoB = float(input())
print("Ingrese el valor del lado C:")
ladoC = float(input())

# Para identificar qué tipo de triángulo es, debemos verificar si se puede formar un triángulo
if ladoC + ladoB <= ladoA or ladoB + ladoA <= ladoC or ladoA + ladoC <= ladoB:
    print("Triángulo Inválido")
elif (ladoA + ladoB > ladoC and ladoA == ladoB and ladoA != ladoC) or \
        (ladoA + ladoC > ladoB and ladoA == ladoC and ladoA != ladoB) or \
        (ladoC + ladoB > ladoA and ladoB == ladoC and ladoB != ladoA):
    print("Es un triángulo isósceles")
elif (ladoA + ladoB > ladoC and ladoA != ladoB) and \
        (ladoB + ladoC > ladoA and ladoB != ladoC) and \
        (ladoA + ladoC > ladoB and ladoA != ladoC):
    print("Es un triángulo escaleno")
elif ladoA + ladoB > ladoC and ladoA == ladoB and ladoA + ladoC > ladoB and ladoA == ladoC and ladoB + ladoC > ladoA and ladoB == ladoC:
    print("Es un triángulo equilátero")