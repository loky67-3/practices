# ============================================================
# APRENDIENDO PATHLIB
# Administrador básico de archivos y carpetas
# ============================================================

# pathlib sirve para trabajar con:
#
# - archivos
# - carpetas
# - rutas
# - extensiones
# - nombres de archivos
#
# Es una librería incluida en Python.
#
from pathlib import Path

import datetime
import time


# ============================================================
# CLASE PRINCIPAL
# ============================================================

class AdministradorArchivos:

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self):

        # Path.cwd()
        #
        # cwd significa:
        # Current Working Directory
        #
        # Devuelve la carpeta desde donde se está ejecutando
        # el programa.
        #
        self.carpeta = Path.cwd()


    # ========================================================
    # MOSTRAR RUTA ACTUAL
    # ========================================================

    def mostrar_ruta(self):

        print("\n========== RUTA ACTUAL ==========")

        print(self.carpeta)


    # ========================================================
    # LISTAR CONTENIDO
    # ========================================================

    def listar(self):

        print("\n========== CONTENIDO ==========")

        # iterdir() recorre todos los elementos
        # que existen dentro de la carpeta.
        #
        for elemento in self.carpeta.iterdir():

            # is_dir() comprueba si es una carpeta.
            if elemento.is_dir():

                print(
                    f"[CARPETA] {elemento.name}"
                )

            # is_file() comprueba si es un archivo.
            elif elemento.is_file():

                print(
                    f"[ARCHIVO] {elemento.name}"
                )


    # ========================================================
    # BUSCAR ARCHIVOS
    # ========================================================

    def buscar(self):

        print("\n========== BUSCAR ==========")

        extension = input(
            "Extensión que quieres buscar (ej: .py): "
        )

        # glob() permite buscar archivos
        # utilizando patrones.
        #
        # Por ejemplo:
        #
        # *.py
        #
        # significa:
        #
        # cualquier archivo que termine en .py
        #
        archivos = self.carpeta.glob(f"*{extension}")


        encontrados = False


        for archivo in archivos:

            print(
                f"Encontrado: {archivo.name}"
            )

            encontrados = True


        if not encontrados:

            print("No se encontraron archivos.")


    # ========================================================
    # INFORMACIÓN DE UN ARCHIVO
    # ========================================================

    def informacion_archivo(self):

        print("\n========== INFORMACIÓN ==========")

        nombre = input(
            "Nombre del archivo: "
        )


        archivo = self.carpeta / nombre


        # exists() comprueba si existe.
        if not archivo.exists():

            print("El archivo no existe.")

            return


        # is_file() comprueba que realmente sea archivo.
        if archivo.is_file():

            print(f"Nombre: {archivo.name}")

            print(f"Extensión: {archivo.suffix}")

            print(f"Ruta: {archivo}")

            # stat() obtiene información del archivo.
            informacion = archivo.stat()

            print(
                f"Tamaño: {informacion.st_size} bytes"
            )


    # ========================================================
    # CREAR CARPETA
    # ========================================================

    def crear_carpeta(self):

        print("\n========== CREAR CARPETA ==========")

        nombre = input(
            "Nombre de la carpeta: "
        )


        nueva_carpeta = self.carpeta / nombre


        try:

            # mkdir() crea la carpeta.
            nueva_carpeta.mkdir()

            print("Carpeta creada correctamente.")


        except FileExistsError:

            print("La carpeta ya existe.")


    # ========================================================
    # FECHA Y HORA
    # ========================================================

    def fecha(self):

        ahora = datetime.datetime.now()

        print(
            "\nFecha:",
            ahora.strftime("%d/%m/%Y")
        )

        print(
            "Hora:",
            ahora.strftime("%H:%M:%S")
        )


    # ========================================================
    # MENÚ
    # ========================================================

    def ejecutar(self):

        while True:

            print("\n")
            print("======================================")
            print("       ADMINISTRADOR DE ARCHIVOS")
            print("======================================")
            print("1. Mostrar ruta")
            print("2. Listar archivos")
            print("3. Buscar por extensión")
            print("4. Información de archivo")
            print("5. Crear carpeta")
            print("6. Fecha y hora")
            print("7. Salir")
            print("======================================")


            opcion = input(
                "Selecciona: "
            )


            if opcion == "1":

                self.mostrar_ruta()


            elif opcion == "2":

                self.listar()


            elif opcion == "3":

                self.buscar()


            elif opcion == "4":

                self.informacion_archivo()


            elif opcion == "5":

                self.crear_carpeta()


            elif opcion == "6":

                self.fecha()


            elif opcion == "7":

                print("Programa terminado.")

                break


            else:

                print("Opción incorrecta.")


            time.sleep(1)


# ============================================================
# CREAR OBJETO
# ============================================================

administrador = AdministradorArchivos()


# ============================================================
# EJECUTAR
# ============================================================

administrador.ejecutar()