# ============================================================
# APRENDIENDO SOCKET EN PYTHON
# Monitor básico de red LOCAL
# ============================================================

# Importamos socket.
#
# socket es un módulo incluido en Python que permite trabajar
# con comunicaciones de red.
#
# Entre otras cosas podemos:
#
# - Obtener el nombre de nuestro equipo.
# - Obtener una IP.
# - Resolver nombres de dominio.
# - Crear conexiones TCP/UDP.
# - Trabajar con direcciones de red.
#
import socket

# datetime lo utilizaremos solamente para mostrar
# la fecha y hora actual.
import datetime

# time nos permitirá hacer pequeñas pausas.
import time


# ============================================================
# CLASE
# ============================================================

class MonitorRed:

    # --------------------------------------------------------
    # __init__
    # --------------------------------------------------------
    #
    # Este método se ejecuta AUTOMÁTICAMENTE cuando creamos
    # un objeto de la clase.
    #
    # Por ejemplo:
    #
    # monitor = MonitorRed()
    #
    # En ese momento Python ejecuta __init__().
    #
    def __init__(self):

        # socket.gethostname()
        #
        # Obtiene el nombre que tiene nuestro equipo en la red.
        #
        # Ejemplo:
        #
        # DESKTOP-ABC123
        #
        self.nombre = socket.gethostname()


    # ========================================================
    # 1. GETHOSTNAME
    # ========================================================

    def mostrar_nombre(self):

        print("\n========== NOMBRE DEL EQUIPO ==========")

        # Mostramos el nombre que guardamos anteriormente.
        print(f"Nombre del equipo: {self.nombre}")


    # ========================================================
    # 2. GETHOSTBYNAME
    # ========================================================

    def mostrar_ip(self):

        print("\n========== IP ==========")

        try:

            # socket.gethostbyname()
            #
            # Esta función recibe un nombre de host.
            #
            # En nuestro caso:
            #
            # self.nombre
            #
            # y devuelve una dirección IPv4.
            #
            # Ejemplo:
            #
            # "192.168.1.25"
            #
            ip = socket.gethostbyname(self.nombre)

            print(f"Nombre: {self.nombre}")
            print(f"IPv4: {ip}")

        except socket.gaierror:

            # gaierror aparece cuando Python no puede
            # resolver el nombre.
            #
            print("No se pudo obtener la IP.")


    # ========================================================
    # 3. GETADDRINFO
    # ========================================================

    def informacion_red(self):

        print("\n========== INFORMACIÓN DE RED ==========")

        try:

            # getaddrinfo() es mucho más completa que
            # gethostbyname().
            #
            # Puede devolver información sobre diferentes
            # tipos de direcciones y protocolos.
            #
            # Los parámetros:
            #
            # self.nombre
            #     -> nombre del equipo
            #
            # None
            #     -> no estamos especificando un puerto.
            #
            informacion = socket.getaddrinfo(
                self.nombre,
                None
            )

            # Recorremos los resultados utilizando un bucle.
            for resultado in informacion:

                # resultado contiene varios datos.
                #
                # Aquí nos interesa principalmente la dirección.
                #
                familia = resultado[0]
                direccion = resultado[4]

                print("--------------------------------")
                print(f"Familia: {familia}")
                print(f"Dirección: {direccion}")

        except socket.gaierror:

            print("No se pudo obtener información.")


    # ========================================================
    # 4. RESOLVER DOMINIO
    # ========================================================

    def resolver_dominio(self):

        print("\n========== RESOLVER DOMINIO ==========")

        # Pedimos al usuario un dominio.
        #
        # Ejemplo:
        #
        # google.com
        #
        dominio = input("Escribe un dominio: ")

        try:

            # gethostbyname() también puede utilizarse
            # con nombres de dominio.
            #
            # Python pregunta al sistema de resolución DNS
            # por la dirección IPv4 correspondiente.
            #
            ip = socket.gethostbyname(dominio)

            print(f"\nDominio: {dominio}")
            print(f"IPv4: {ip}")

        except socket.gaierror:

            print("No se pudo resolver el dominio.")


    # ========================================================
    # 5. GETHOSTBYADDR
    # ========================================================

    def buscar_nombre_por_ip(self):

        print("\n========== REVERSE DNS ==========")

        ip = input("Escribe una IP: ")

        try:

            # gethostbyaddr()
            #
            # Hace el proceso contrario a gethostbyname().
            #
            # Tenemos:
            #
            # IP -> buscamos un nombre asociado.
            #
            nombre, alias, direcciones = socket.gethostbyaddr(ip)

            print(f"\nNombre: {nombre}")
            print(f"Alias: {alias}")
            print(f"Direcciones: {direcciones}")

        except socket.herror:

            print("No se encontró un nombre asociado.")


    # ========================================================
    # 6. COMPROBAR CONEXIÓN
    # ========================================================

    def comprobar_internet(self):

        print("\n========== CONEXIÓN ==========")

        try:

            # Intentamos resolver un dominio.
            #
            # Si el sistema puede resolverlo correctamente,
            # tenemos conectividad DNS.
            #
            socket.gethostbyname("example.com")

            print("Se pudo resolver example.com.")

        except socket.gaierror:

            print("No se pudo resolver el dominio.")


    # ========================================================
    # 7. INFORMACIÓN DEL SOCKET
    # ========================================================

    def ejemplo_socket(self):

        print("\n========== SOCKET ==========")

        # socket.socket() crea un objeto socket.
        #
        # AF_INET
        #     -> utilizaremos IPv4.
        #
        # SOCK_STREAM
        #     -> utilizaremos TCP.
        #
        conexion = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        print("Socket TCP creado correctamente.")

        # Cerramos el socket porque solamente lo
        # estamos utilizando para aprender.
        conexion.close()

        print("Socket cerrado.")


    # ========================================================
    # 8. FECHA Y HORA
    # ========================================================

    def fecha_hora(self):

        print("\n========== FECHA Y HORA ==========")

        # datetime.now() obtiene la fecha y hora
        # actual del equipo.
        ahora = datetime.datetime.now()

        print(
            ahora.strftime("%d/%m/%Y %H:%M:%S")
        )


    # ========================================================
    # MENÚ
    # ========================================================

    def ejecutar(self):

        # while True crea un bucle infinito.
        #
        # El menú continuará apareciendo hasta que
        # utilicemos break.
        #
        while True:

            print("\n")
            print("======================================")
            print("          APRENDIENDO SOCKET")
            print("======================================")
            print("1. Nombre del equipo")
            print("2. Obtener IP")
            print("3. Información de red")
            print("4. Resolver dominio")
            print("5. Buscar nombre por IP")
            print("6. Comprobar conexión")
            print("7. Crear socket TCP")
            print("8. Fecha y hora")
            print("9. Salir")
            print("======================================")

            opcion = input("Selecciona una opción: ")


            # ------------------------------------------------
            # OPCIÓN 1
            # ------------------------------------------------

            if opcion == "1":

                self.mostrar_nombre()


            # ------------------------------------------------
            # OPCIÓN 2
            # ------------------------------------------------

            elif opcion == "2":

                self.mostrar_ip()


            # ------------------------------------------------
            # OPCIÓN 3
            # ------------------------------------------------

            elif opcion == "3":

                self.informacion_red()


            # ------------------------------------------------
            # OPCIÓN 4
            # ------------------------------------------------

            elif opcion == "4":

                self.resolver_dominio()


            # ------------------------------------------------
            # OPCIÓN 5
            # ------------------------------------------------

            elif opcion == "5":

                self.buscar_nombre_por_ip()


            # ------------------------------------------------
            # OPCIÓN 6
            # ------------------------------------------------

            elif opcion == "6":

                self.comprobar_internet()


            # ------------------------------------------------
            # OPCIÓN 7
            # ------------------------------------------------

            elif opcion == "7":

                self.ejemplo_socket()


            # ------------------------------------------------
            # OPCIÓN 8
            # ------------------------------------------------

            elif opcion == "8":

                self.fecha_hora()


            # ------------------------------------------------
            # OPCIÓN 9
            # ------------------------------------------------

            elif opcion == "9":

                print("\nPrograma terminado.")

                # break rompe el while True.
                break


            # ------------------------------------------------
            # OPCIÓN INCORRECTA
            # ------------------------------------------------

            else:

                print("\nOpción incorrecta.")


            # Esperamos un segundo antes de mostrar
            # nuevamente el menú.
            time.sleep(1)


# ============================================================
# CREAR EL OBJETO
# ============================================================

# Aquí creamos una instancia de nuestra clase.
#
# Python ejecutará automáticamente:
#
# MonitorRed.__init__()
#
monitor = MonitorRed()


# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

# Llamamos al método ejecutar().
#
# Esto inicia nuestro menú.
#
monitor.ejecutar()