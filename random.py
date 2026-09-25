# ============================================================
# APRENDIENDO RANDOM EN PYTHON
# Generador y simulador
# ============================================================

# random es una librería incluida en Python.
#
# Sirve para generar valores pseudoaleatorios.
#
# Algunos usos:
#
# - números aleatorios
# - elegir elementos de una lista
# - mezclar listas
# - simulaciones
# - juegos
#
import random

# datetime solamente lo utilizaremos para registrar
# cuándo realizamos una operación.
import datetime

# time nos permitirá hacer una pequeña pausa.
import time


# ============================================================
# CLASE PRINCIPAL
# ============================================================

class GeneradorAleatorio:

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self):

        # Lista que utilizaremos en varios métodos.
        self.opciones = [
            "Python",
            "C++",
            "JavaScript",
            "Flask",
            "SQL"
        ]


    # ========================================================
    # RANDOM.RANDINT()
    # ========================================================

    def numero_entero(self):

        print("\n========== NÚMERO ALEATORIO ==========")

        minimo = int(input("Número mínimo: "))
        maximo = int(input("Número máximo: "))

        # randint(a, b)
        #
        # Genera un número entero aleatorio
        # entre a y b.
        #
        # IMPORTANTE:
        #
        # Tanto el mínimo como el máximo
        # están incluidos.
        #
        numero = random.randint(minimo, maximo)

        print(f"Número generado: {numero}")


    # ========================================================
    # RANDOM.RANDRANGE()
    # ========================================================

    def numero_rango(self):

        print("\n========== RANGE ALEATORIO ==========")

        # randrange() funciona parecido a range().
        #
        # Aquí puede generar:
        #
        # 0, 1, 2, 3 o 4
        #
        numero = random.randrange(0, 5)

        print(f"Número: {numero}")


    # ========================================================
    # RANDOM.CHOICE()
    # ========================================================

    def elegir_elemento(self):

        print("\n========== ELECCIÓN ==========")

        # choice() selecciona UN elemento
        # aleatoriamente de una secuencia.
        #
        elegido = random.choice(self.opciones)

        print(f"Elemento elegido: {elegido}")


    # ========================================================
    # RANDOM.SHUFFLE()
    # ========================================================

    def mezclar(self):

        print("\n========== MEZCLAR ==========")

        # Creamos una copia de la lista.
        lista = self.opciones.copy()

        print("Antes:")
        print(lista)

        # shuffle() mezcla la lista.
        #
        # IMPORTANTE:
        #
        # shuffle() modifica directamente
        # la lista original que recibe.
        #
        random.shuffle(lista)

        print("\nDespués:")
        print(lista)


    # ========================================================
    # RANDOM.SAMPLE()
    # ========================================================

    def seleccionar_varios(self):

        print("\n========== SELECCIÓN MÚLTIPLE ==========")

        # sample() permite seleccionar varios
        # elementos SIN repetirlos.
        #
        # k = cantidad de elementos.
        #
        seleccion = random.sample(
            self.opciones,
            k=3
        )

        print("Seleccionados:")

        for elemento in seleccion:

            print(f"- {elemento}")


    # ========================================================
    # RANDOM.RANDOM()
    # ========================================================

    def numero_decimal(self):

        print("\n========== DECIMAL ==========")

        # random() devuelve un número decimal
        # entre 0.0 y 1.0.
        #
        numero = random.random()

        print(f"Número: {numero}")


    # ========================================================
    # RANDOM.UNIFORM()
    # ========================================================

    def decimal_rango(self):

        print("\n========== DECIMAL EN RANGO ==========")

        minimo = float(input("Mínimo: "))
        maximo = float(input("Máximo: "))

        # uniform() genera un número decimal
        # dentro del rango indicado.
        #
        numero = random.uniform(
            minimo,
            maximo
        )

        print(f"Número generado: {numero}")


    # ========================================================
    # SIMULADOR DE DADO
    # ========================================================

    def dado(self):

        print("\n========== DADO ==========")

        # Simulamos un dado de 6 caras.
        #
        resultado = random.randint(1, 6)

        print("Lanzando dado...")

        time.sleep(1)

        print(f"Resultado: {resultado}")


    # ========================================================
    # SIMULACIÓN DE LANZAMIENTOS
    # ========================================================

    def muchos_dados(self):

        print("\n========== SIMULACIÓN ==========")

        cantidad = int(
            input("¿Cuántas veces lanzar?: ")
        )

        resultados = []

        # Repetimos el lanzamiento.
        for i in range(cantidad):

            resultado = random.randint(1, 6)

            resultados.append(resultado)


        print("\nResultados:")

        print(resultados)


        # ----------------------------------------------------
        # CONTAMOS CUÁNTAS VECES SALIÓ CADA CARA
        # ----------------------------------------------------

        for cara in range(1, 7):

            cantidad_cara = resultados.count(cara)

            print(
                f"El {cara} salió "
                f"{cantidad_cara} veces."
            )


    # ========================================================
    # FECHA
    # ========================================================

    def fecha(self):

        ahora = datetime.datetime.now()

        print("\n========== FECHA ==========")

        print(
            ahora.strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )


    # ========================================================
    # MENÚ
    # ========================================================

    def ejecutar(self):

        while True:

            print("\n")
            print("==========================================")
            print("       GENERADOR ALEATORIO")
            print("==========================================")
            print("1. Número entero")
            print("2. Número con randrange")
            print("3. Elegir elemento")
            print("4. Mezclar lista")
            print("5. Seleccionar varios")
            print("6. Número decimal")
            print("7. Decimal en rango")
            print("8. Lanzar dado")
            print("9. Simular muchos dados")
            print("10. Fecha y hora")
            print("11. Salir")
            print("==========================================")


            opcion = input(
                "Selecciona: "
            )


            if opcion == "1":

                self.numero_entero()


            elif opcion == "2":

                self.numero_rango()


            elif opcion == "3":

                self.elegir_elemento()


            elif opcion == "4":

                self.mezclar()


            elif opcion == "5":

                self.seleccionar_varios()


            elif opcion == "6":

                self.numero_decimal()


            elif opcion == "7":

                self.decimal_rango()


            elif opcion == "8":

                self.dado()


            elif opcion == "9":

                self.muchos_dados()


            elif opcion == "10":

                self.fecha()


            elif opcion == "11":

                print("\nPrograma terminado.")

                break


            else:

                print("\nOpción incorrecta.")


            time.sleep(1)


# ============================================================
# CREAR OBJETO
# ============================================================

generador = GeneradorAleatorio()


# ============================================================
# EJECUTAR
# ============================================================

generador.ejecutar()