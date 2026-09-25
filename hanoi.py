# ============================================================
# TORRES DE HANOI
# Ejemplo de RECURSIVIDAD
# ============================================================


def hanoi(n, origen, auxiliar, destino):

    # --------------------------------------------------------
    # CASO BASE
    # --------------------------------------------------------
    #
    # Si solamente queda 1 disco, ya no necesitamos
    # volver a llamar a la función.
    #
    # Simplemente lo movemos.
    #
    if n == 1:
        print(f"Mover disco de {origen} -> {destino}")
        return


    # --------------------------------------------------------
    # PASO 1
    # --------------------------------------------------------
    #
    # Tenemos que quitar los discos que están encima
    # del disco más grande.
    #
    # Para hacerlo:
    #
    # movemos n-1 discos:
    #
    # ORIGEN -> AUXILIAR
    #
    hanoi(
        n - 1,
        origen,
        destino,
        auxiliar
    )


    # --------------------------------------------------------
    # PASO 2
    # --------------------------------------------------------
    #
    # Ahora el disco más grande queda libre.
    #
    # Lo movemos:
    #
    # ORIGEN -> DESTINO
    #
    print(f"Mover disco de {origen} -> {destino}")


    # --------------------------------------------------------
    # PASO 3
    # --------------------------------------------------------
    #
    # Finalmente movemos los n-1 discos que dejamos
    # en la torre auxiliar.
    #
    # AUXILIAR -> DESTINO
    #
    hanoi(
        n - 1,
        auxiliar,
        origen,
        destino
    )


# ============================================================
# PROGRAMA
# ============================================================

# Número de discos.
discos = 3

# Llamamos a la función.
#
# A = origen
# B = auxiliar
# C = destino
#
hanoi(discos, "A", "B", "C")