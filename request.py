# ============================================================
# APRENDIENDO REQUESTS EN PYTHON
# Cliente HTTP básico
# ============================================================

# requests permite que Python haga peticiones HTTP.
#
# Por ejemplo:
#
# Python
#   ↓
# requests
#   ↓
# Internet
#   ↓
# servidor
#   ↓
# respuesta
#
import requests

# datetime solamente lo utilizaremos para mostrar
# cuándo realizamos la petición.
import datetime

# time nos permite hacer una pequeña pausa
# entre las opciones del menú.
import time


# ============================================================
# CLASE PRINCIPAL
# ============================================================

class ClienteHTTP:

    # --------------------------------------------------------
    # CONSTRUCTOR
    # --------------------------------------------------------

    def __init__(self):

        # Guardamos una URL de prueba.
        #
        # JSONPlaceholder es una API pública diseñada
        # para practicar peticiones HTTP.
        #
        self.url = "https://jsonplaceholder.typicode.com"


    # ========================================================
    # MÉTODO GET
    # ========================================================

    def obtener_post(self):

        print("\n========== GET ==========")

        # Pedimos al usuario el número del post.
        numero = input("Número del post (1-100): ")

        # Construimos la URL.
        #
        # Por ejemplo:
        #
        # https://jsonplaceholder.typicode.com/posts/1
        #
        url = f"{self.url}/posts/{numero}"

        try:

            # ------------------------------------------------
            # requests.get()
            # ------------------------------------------------
            #
            # GET significa:
            #
            # "Quiero obtener información del servidor."
            #
            respuesta = requests.get(
                url,
                timeout=10
            )

            # ------------------------------------------------
            # STATUS_CODE
            # ------------------------------------------------
            #
            # El servidor devuelve un código HTTP.
            #
            # 200 = OK
            # 404 = No encontrado
            # 500 = Error del servidor
            #
            print(f"Código HTTP: {respuesta.status_code}")


            # ------------------------------------------------
            # RAISE_FOR_STATUS()
            # ------------------------------------------------
            #
            # Si el servidor devuelve un error HTTP,
            # esta función genera una excepción.
            #
            respuesta.raise_for_status()


            # ------------------------------------------------
            # JSON()
            # ------------------------------------------------
            #
            # La respuesta de la API viene en formato JSON.
            #
            # .json() convierte ese JSON en estructuras
            # que Python puede manejar, normalmente
            # diccionarios y listas.
            #
            datos = respuesta.json()


            print("\nTítulo:")
            print(datos["title"])

            print("\nContenido:")
            print(datos["body"])


        # Error de conexión, DNS, timeout, etc.
        except requests.exceptions.RequestException as error:

            print(f"\nError en la petición: {error}")


    # ========================================================
    # MÉTODO PARA LISTAR POSTS
    # ========================================================

    def listar_posts(self):

        print("\n========== LISTA DE POSTS ==========")

        try:

            # Hacemos una petición GET.
            respuesta = requests.get(
                f"{self.url}/posts",
                timeout=10
            )

            # Comprobamos si hubo error HTTP.
            respuesta.raise_for_status()

            # Convertimos la respuesta JSON
            # en una lista de diccionarios.
            posts = respuesta.json()


            # ------------------------------------------------
            # BUCLE
            # ------------------------------------------------
            #
            # Recorremos los primeros 10 elementos.
            #
            for post in posts[:10]:

                print("\n------------------------")

                print(
                    f"ID: {post['id']}"
                )

                print(
                    f"Título: {post['title']}"
                )


        except requests.exceptions.RequestException as error:

            print(f"Error: {error}")


    # ========================================================
    # MÉTODO CON PARÁMETROS
    # ========================================================

    def buscar_usuario(self):

        print("\n========== PARÁMETROS ==========")

        # Pedimos un ID.
        usuario = input("ID del usuario (1-10): ")


        # ----------------------------------------------------
        # params
        # ----------------------------------------------------
        #
        # requests puede enviar parámetros en la URL.
        #
        # Ejemplo conceptual:
        #
        # ?userId=1
        #
        parametros = {
            "userId": usuario
        }


        try:

            respuesta = requests.get(
                f"{self.url}/posts",
                params=parametros,
                timeout=10
            )


            respuesta.raise_for_status()


            datos = respuesta.json()


            print(
                f"\nResultados encontrados: {len(datos)}"
            )


            for post in datos:

                print("\n----------------")

                print(
                    f"Post: {post['id']}"
                )

                print(
                    f"Título: {post['title']}"
                )


        except requests.exceptions.RequestException as error:

            print(f"Error: {error}")


    # ========================================================
    # HEADERS
    # ========================================================

    def mostrar_headers(self):

        print("\n========== HEADERS ==========")

        try:

            respuesta = requests.get(
                self.url,
                timeout=10
            )

            print(
                f"Código: {respuesta.status_code}"
            )


            # .headers contiene los encabezados HTTP
            # que devolvió el servidor.
            #
            # Es parecido a un diccionario.
            #
            for nombre, valor in respuesta.headers.items():

                print(
                    f"{nombre}: {valor}"
                )


        except requests.exceptions.RequestException as error:

            print(f"Error: {error}")


    # ========================================================
    # INFORMACIÓN DE LA PETICIÓN
    # ========================================================

    def informacion(self):

        print("\n========== INFORMACIÓN ==========")

        ahora = datetime.datetime.now()

        print(
            "Fecha:",
            ahora.strftime("%d/%m/%Y")
        )

        print(
            "Hora:",
            ahora.strftime("%H:%M:%S")
        )

        print(
            "Servidor:",
            self.url
        )


    # ========================================================
    # MENÚ
    # ========================================================

    def ejecutar(self):

        while True:

            print("\n")
            print("======================================")
            print("          CLIENTE HTTP")
            print("======================================")
            print("1. Obtener un post")
            print("2. Listar posts")
            print("3. Buscar por usuario")
            print("4. Mostrar headers")
            print("5. Información")
            print("6. Salir")
            print("======================================")

            opcion = input("Selecciona: ")


            if opcion == "1":

                self.obtener_post()


            elif opcion == "2":

                self.listar_posts()


            elif opcion == "3":

                self.buscar_usuario()


            elif opcion == "4":

                self.mostrar_headers()


            elif opcion == "5":

                self.informacion()


            elif opcion == "6":

                print("\nPrograma terminado.")

                break


            else:

                print("\nOpción incorrecta.")


            time.sleep(1)


# ============================================================
# CREAR OBJETO
# ============================================================

cliente = ClienteHTTP()


# ============================================================
# INICIAR PROGRAMA
# ============================================================

cliente.ejecutar()