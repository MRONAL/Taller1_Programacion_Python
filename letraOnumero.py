# Se crea un objeto tipo escáner que recibe ingresos del sistema
print("Ingrese un valor: ")
input_value = input()

# Obtener el valor ASCII del primer carácter ingresado
ascii_value = ord(input_value[0])

if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
    print("Es una letra.")

    if ascii_value >= 65 and ascii_value <= 90:
        print("Es una letra mayúscula.")
    else:
        print("Es una letra minúscula.")
elif ascii_value >= 48 and ascii_value <= 57:
    print("Es un número.")
else:
    print("No es ni una letra ni un número.")

print("Valor ASCII/numérico:", ascii_value)