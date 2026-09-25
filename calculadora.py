operaciones = {
    "+":lambda a, b: a + b,
    "-":lambda a, b: a - b,
    "*":lambda a, b: a * b,
    "/":lambda a, b: a / b,
}


def calcular():
    try:
        a = float(input("Num1: "))
        ope = input("Operaciones: (+-*/): ")
        b = float(input("Num2: "))

        resultado = operaciones[ope](a, b)
        print(f"resultado: {resultado}")
    except ValueError:
        print("Ingresa un numero entero")
    except KeyError:
        print("Operacion no valida")
    except ZeroDivisionError:
        print("Error de Divicion por Cero")

while True:
    calcular()
    salir = input("Selecciona una opcion para salir o continuar: (n/s): ")
    if salir == "s":
        print("saliendo del programa...")
        break
    