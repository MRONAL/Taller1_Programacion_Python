# Se crea un objeto tipo escáner que recibe ingresos del sistema
print("Juegos ganados por A: ")
jugadorA = int(input())

print("Juegos ganados por B: ")
jugadorB = int(input())

# Cantidad máxima de juegos
maxJuegos = 7
juegos = 6
ganador = False
invalido = True

# JugadorA gana si: hace 6 juegos o llega a 7,
# JugadorB gana si: hace 6 juegos o llega a 7,
# Aún no se acaba el set si jugadorA o jugadorB no pasan de 6,
# El set es inválido cuando un jugador llega a 7 y el otro no llega a 5
if (jugadorA < 0 or jugadorB < 0) or \
        (jugadorB == maxJuegos and jugadorA < juegos) or \
        (jugadorA == maxJuegos and jugadorB < juegos):
    print("invalido")

else:
    if jugadorA >= juegos and jugadorA > jugadorB + 1:
        ganador = True
        print("Gana jugador A")

    if jugadorB >= juegos and jugadorB > jugadorA + 1:
        ganador = True
        print("Gana jugador B")

    if not ganador:
        print("El set aún no termina")