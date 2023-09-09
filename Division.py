# Pedir al usuario que ingrese dos números enteros
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Verificar si el segundo número es diferente de cero
if num2 != 0:
    # Realizar la división y calcular el residuo
    division = num1 // num2
    resto = num1 % num2

    # Mostrar el resultado de la división y el residuo
    print("Resultado de la división:", division)
    print("Residuo de la división:", resto)

    # Verificar si la división es exacta
    if resto == 0:
        print("La división es exacta.")
    else:
        print("La división no es exacta.")
else:
    print("El segundo número debe ser distinto de cero para realizar la división.")