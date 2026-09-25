import os
import datetime


class AnalizadorSistema:

    def __init__(self):
        self.carpeta_actual = os.getcwd()

    # Método para mostrar información básica
    def informacion(self):
        print("\n========== INFORMACIÓN ==========")
        print(f"Carpeta actual: {self.carpeta_actual}")
        print(f"Sistema operativo: {os.name}")
        print(f"Usuario: {os.getlogin()}")

    # Método para mostrar la fecha y hora
    def fecha_hora(self):
        ahora = datetime.datetime.now()

        print("\n========== FECHA Y HORA ==========")
        print(ahora.strftime("%d/%m/%Y"))
        print(ahora.strftime("%H:%M:%S"))

    # Método para mostrar archivos y carpetas
    def listar(self):
        print("\n========== CONTENIDO ==========")

        archivos = os.listdir(self.carpeta_actual)

        for numero, archivo in enumerate(archivos, start=1):
            ruta = os.path.join(self.carpeta_actual, archivo)

            if os.path.isdir(ruta):
                tipo = "CARPETA"
            else:
                tipo = "ARCHIVO"

            print(f"{numero}. [{tipo}] {archivo}")

    # Método para buscar un archivo
    def buscar(self):
        nombre = input("\nNombre del archivo: ")

        if os.path.exists(nombre):
            print("El archivo o carpeta existe.")

            if os.path.isfile(nombre):
                print("Tipo: archivo")

            elif os.path.isdir(nombre):
                print("Tipo: carpeta")

        else:
            print("No se encontró.")

    # Método para crear una carpeta
    def crear_carpeta(self):
        nombre = input("\nNombre de la carpeta: ")

        try:
            os.mkdir(nombre)
            print("Carpeta creada correctamente.")

        except FileExistsError:
            print("Esa carpeta ya existe.")

    # Menú principal
    def ejecutar(self):

        while True:

            print("\n================================")
            print("       ANALIZADOR OSINT LOCAL")
            print("================================")
            print("1. Información del sistema")
            print("2. Fecha y hora")
            print("3. Listar archivos")
            print("4. Buscar archivo")
            print("5. Crear carpeta")
            print("6. Salir")

            opcion = input("\nSelecciona: ")

            if opcion == "1":
                self.informacion()

            elif opcion == "2":
                self.fecha_hora()

            elif opcion == "3":
                self.listar()

            elif opcion == "4":
                self.buscar()

            elif opcion == "5":
                self.crear_carpeta()

            elif opcion == "6":
                print("Programa terminado.")
                break

            else:
                print("Opción incorrecta.")


# Crear el objeto
programa = AnalizadorSistema()

# Ejecutar el programa
programa.ejecutar()