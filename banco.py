# ==========================================
# 🏦 BANCO SIMPLE - PRÁCTICA DE PYTHON
# ==========================================

import random
from datetime import datetime


# ------------------------------------------
# DATOS DEL BANCO
# ------------------------------------------

cuentas = []


# ------------------------------------------
# FUNCIÓN PARA CREAR UNA CUENTA
# ------------------------------------------

def crear_cuenta():

    print("\n===== CREAR CUENTA =====")

    nombre = input("Nombre: ")

    # Generamos un número de cuenta aleatorio
    numero = random.randint(1000, 9999)

    cuenta = {
        "nombre": nombre,
        "numero": numero,
        "saldo": 0,
        "historial": []
    }

    cuentas.append(cuenta)

    print(f"\nCuenta creada.")
    print(f"Número de cuenta: {numero}")


# ------------------------------------------
# FUNCIÓN PARA BUSCAR UNA CUENTA
# ------------------------------------------

def buscar_cuenta(numero):

    # Recorremos todas las cuentas
    for cuenta in cuentas:

        # Si encontramos el número
        if cuenta["numero"] == numero:
            return cuenta

    # Si no encontramos nada
    return None


# ------------------------------------------
# FUNCIÓN PRINCIPAL DEL BANCO
# ------------------------------------------

def banco(cuenta):

    # Este while mantiene abierto el menú
    while True:

        print("\n========== BANCO ==========")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Historial")
        print("5. Salir")

        opcion = input("Selecciona: ")


        # ----------------------------------
        # CONSULTAR SALDO
        # ----------------------------------

        if opcion == "1":

            print(f"\nSaldo: ${cuenta['saldo']}")


        # ----------------------------------
        # DEPOSITAR
        # ----------------------------------

        elif opcion == "2":

            try:
                dinero = float(input("Cantidad a depositar: "))

                if dinero > 0:

                    cuenta["saldo"] += dinero

                    cuenta["historial"].append(
                        f"Depósito ${dinero} - {datetime.now()}"
                    )

                    print("Depósito realizado.")

                else:
                    print("La cantidad debe ser mayor que 0.")

            except ValueError:
                print("Debes escribir un número.")


        # ----------------------------------
        # RETIRAR
        # ----------------------------------

        elif opcion == "3":

            try:
                dinero = float(input("Cantidad a retirar: "))

                if dinero <= 0:

                    print("Cantidad inválida.")

                elif dinero > cuenta["saldo"]:

                    print("Saldo insuficiente.")

                else:

                    cuenta["saldo"] -= dinero

                    cuenta["historial"].append(
                        f"Retiro ${dinero} - {datetime.now()}"
                    )

                    print("Retiro realizado.")

            except ValueError:
                print("Debes escribir un número.")


        # ----------------------------------
        # HISTORIAL
        # ----------------------------------

        elif opcion == "4":

            print("\n===== HISTORIAL =====")

            if len(cuenta["historial"]) == 0:

                print("No hay movimientos.")

            else:

                # FOR dentro del menú
                for movimiento in cuenta["historial"]:
                    print(movimiento)


        # ----------------------------------
        # SALIR
        # ----------------------------------

        elif opcion == "5":

            print("Sesión terminada.")
            break


        else:

            print("Opción incorrecta.")


# ------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------

while True:

    print("\n========== SISTEMA BANCARIO ==========")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Selecciona: ")


    if opcion == "1":

        crear_cuenta()


    elif opcion == "2":

        try:

            numero = int(input("Número de cuenta: "))

            cuenta = buscar_cuenta(numero)

            if cuenta:

                print(f"\nBienvenido {cuenta['nombre']}")

                banco(cuenta)

            else:

                print("Cuenta no encontrada.")

        except ValueError:

            print("Debes escribir un número.")


    elif opcion == "3":

        print("Banco cerrado.")
        break


    else:

        print("Opción incorrecta.")