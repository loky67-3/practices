import random

tipos = ["papel", "tijera", "piedra"]

def escoger():
    while True:
        opcion = input("Elige papel, tijera o piedra: ").lower()

        if opcion not in tipos:
            print("Opción inválida")
            continue

        computadora = random.choice(tipos)

        gana = {
            "papel": "piedra",
            "tijera": "papel",
            "piedra": "tijera"
        }

        print(f"Tú: {opcion}")
        print(f"Computadora: {computadora}")

        if opcion == computadora:
            print("Empate")
        elif gana[opcion] == computadora:
            print("Ganaste")
        else:
            print("Perdiste")

escoger()