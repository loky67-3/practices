import datetime
import time


def mostrar_fecha():
    ahora = datetime.datetime.now()

    print("Fecha actual:", ahora.strftime("%d/%m/%Y"))
    print("Hora actual:", ahora.strftime("%H:%M:%S"))


def cuenta_regresiva():
    while True:
        ahora = datetime.datetime.now()

        objetivo = datetime.datetime(2026, 12, 31, 23, 59, 59)

        diferencia = objetivo - ahora

        if diferencia.total_seconds() <= 0:
            print("¡Llegó la fecha!")
            break

        print(
            f"Faltan: {diferencia.days} días "
            f"y {diferencia.seconds // 3600} horas"
        )

        time.sleep(1)


def programa():
    while True:
        print("\n===== FECHAS =====")
        print("1. Mostrar fecha y hora")
        print("2. Cuenta regresiva")
        print("3. Salir")

        opcion = input("Selecciona: ")

        if opcion == "1":
            mostrar_fecha()

        elif opcion == "2":
            cuenta_regresiva()

        elif opcion == "3":
            print("Programa terminado.")
            break

        else:
            print("Opción incorrecta.")


programa()