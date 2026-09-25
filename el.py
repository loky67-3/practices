import tkinter as tk


class Calculadora:
    def __init__(self, ventana):
        # ==========================================================
        # CONFIGURACIÓN PRINCIPAL DE LA VENTANA
        # ==========================================================

        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("380x600")
        self.ventana.resizable(False, False)

        # ==========================================================
        # VARIABLES DE LA CALCULADORA
        # ==========================================================

        # Número que estamos escribiendo actualmente
        self.numero_actual = ""

        # Primer número de una operación
        self.primer_numero = None

        # Operador seleccionado: +, -, ×, ÷
        self.operador = None

        # Guarda si acabamos de obtener un resultado
        self.nuevo_resultado = False

        # ==========================================================
        # PANTALLA
        # ==========================================================

        self.pantalla = tk.Entry(
            ventana,
            font=("Arial", 32),
            justify="right",
            bd=0,
            relief="flat"
        )

        self.pantalla.grid(
            row=0,
            column=0,
            columnspan=4,
            padx=15,
            pady=(20, 10),
            sticky="nsew"
        )

        # ==========================================================
        # HISTORIAL
        # ==========================================================

        self.historial = tk.Label(
            ventana,
            text="",
            font=("Arial", 11),
            anchor="e"
        )

        self.historial.grid(
            row=1,
            column=0,
            columnspan=4,
            padx=20,
            pady=(0, 10),
            sticky="ew"
        )

        # ==========================================================
        # BOTONES
        # ==========================================================

        botones = [
            ("C", 2, 0),
            ("⌫", 2, 1),
            ("%", 2, 2),
            ("÷", 2, 3),

            ("7", 3, 0),
            ("8", 3, 1),
            ("9", 3, 2),
            ("×", 3, 3),

            ("4", 4, 0),
            ("5", 4, 1),
            ("6", 4, 2),
            ("-", 4, 3),

            ("1", 5, 0),
            ("2", 5, 1),
            ("3", 5, 2),
            ("+", 5, 3),

            ("+/-", 6, 0),
            ("0", 6, 1),
            (".", 6, 2),
            ("=", 6, 3),
        ]

        for texto, fila, columna in botones:

            boton = tk.Button(
                ventana,
                text=texto,
                font=("Arial", 18),
                bd=0,
                command=lambda valor=texto: self.presionar(valor)
            )

            boton.grid(
                row=fila,
                column=columna,
                padx=5,
                pady=5,
                sticky="nsew"
            )

        # ==========================================================
        # CONFIGURACIÓN DEL GRID
        # ==========================================================

        for columna in range(4):
            ventana.grid_columnconfigure(
                columna,
                weight=1
            )

        for fila in range(7):
            ventana.grid_rowconfigure(
                fila,
                weight=1
            )

        # ==========================================================
        # TECLADO FÍSICO
        # ==========================================================

        ventana.bind("<Key>", self.teclado)

        # Permitimos que la ventana reciba el teclado
        ventana.focus_set()

    # ==============================================================
    # FUNCIÓN PRINCIPAL DE LOS BOTONES
    # ==============================================================

    def presionar(self, valor):

        # Números
        if valor.isdigit():
            self.numero(valor)

        # Punto decimal
        elif valor == ".":
            self.decimal()

        # Operadores
        elif valor in ["+", "-", "×", "÷"]:
            self.operacion(valor)

        # Igual
        elif valor == "=":
            self.calcular()

        # Borrar todo
        elif valor == "C":
            self.limpiar()

        # Borrar último carácter
        elif valor == "⌫":
            self.borrar()

        # Porcentaje
        elif valor == "%":
            self.porcentaje()

        # Cambiar signo
        elif valor == "+/-":
            self.cambiar_signo()

    # ==============================================================
    # ESCRIBIR NÚMEROS
    # ==============================================================

    def numero(self, numero):

        # Si acabamos de obtener un resultado,
        # empezar una nueva operación.
        if self.nuevo_resultado:
            self.numero_actual = ""
            self.pantalla.delete(0, tk.END)
            self.nuevo_resultado = False

        self.numero_actual += numero

        self.actualizar_pantalla()

    # ==============================================================
    # DECIMALES
    # ==============================================================

    def decimal(self):

        # Si acabamos de obtener un resultado,
        # empezamos un nuevo número.
        if self.nuevo_resultado:
            self.numero_actual = ""
            self.pantalla.delete(0, tk.END)
            self.nuevo_resultado = False

        # Evita cosas como:
        #
        # 5.2.8
        #
        if "." not in self.numero_actual:

            # Si escribimos "." directamente,
            # se convierte en "0."
            if self.numero_actual == "":
                self.numero_actual = "0"

            self.numero_actual += "."

            self.actualizar_pantalla()

    # ==============================================================
    # SELECCIONAR OPERACIÓN
    # ==============================================================

    def operacion(self, operador):

        # Si no hemos escrito ningún número,
        # no hacemos nada.
        if self.numero_actual == "":
            return

        try:
            numero = float(self.numero_actual)

        except ValueError:
            self.mostrar_error()
            return

        # Si ya había una operación pendiente,
        # primero calculamos.
        if self.primer_numero is not None and self.operador is not None:

            resultado = self.realizar_operacion(
                self.primer_numero,
                numero,
                self.operador
            )

            if resultado is None:
                return

            self.primer_numero = resultado

        else:
            self.primer_numero = numero

        self.operador = operador
        self.numero_actual = ""
        self.nuevo_resultado = False

    # ==============================================================
    # REALIZAR OPERACIÓN
    # ==============================================================

    def realizar_operacion(self, numero1, numero2, operador):

        if operador == "+":
            return numero1 + numero2

        elif operador == "-":
            return numero1 - numero2

        elif operador == "×":
            return numero1 * numero2

        elif operador == "÷":

            # Evitamos dividir entre cero
            if numero2 == 0:
                self.mostrar_error()
                return None

            return numero1 / numero2

        return None

    # ==============================================================
    # CALCULAR RESULTADO
    # ==============================================================

    def calcular(self):

        # Debemos tener:
        #
        # primer número
        # operador
        # segundo número

        if (
            self.primer_numero is None
            or self.operador is None
            or self.numero_actual == ""
        ):
            return

        try:
            segundo_numero = float(self.numero_actual)

        except ValueError:
            self.mostrar_error()
            return

        resultado = self.realizar_operacion(
            self.primer_numero,
            segundo_numero,
            self.operador
        )

        if resultado is None:
            return

        # Guardamos la operación para el historial
        operacion_texto = (
            f"{self.formatear(self.primer_numero)} "
            f"{self.operador} "
            f"{self.formatear(segundo_numero)} = "
            f"{self.formatear(resultado)}"
        )

        self.historial.config(
            text=operacion_texto
        )

        # Mostramos el resultado
        self.numero_actual = self.formatear(resultado)

        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.numero_actual)

        # Limpiamos la operación pendiente
        self.primer_numero = None
        self.operador = None

        # Indicamos que tenemos un resultado nuevo
        self.nuevo_resultado = True

    # ==============================================================
    # FORMATEAR NÚMEROS
    # ==============================================================

    def formatear(self, numero):

        # Si el resultado es entero,
        # quitamos ".0"
        if numero.is_integer():
            return str(int(numero))

        # Si es decimal, lo dejamos como decimal
        return str(numero)

    # ==============================================================
    # LIMPIAR
    # ==============================================================

    def limpiar(self):

        self.numero_actual = ""
        self.primer_numero = None
        self.operador = None
        self.nuevo_resultado = False

        self.pantalla.delete(0, tk.END)

        self.historial.config(
            text=""
        )

    # ==============================================================
    # BORRAR ÚLTIMO CARÁCTER
    # ==============================================================

    def borrar(self):

        if self.numero_actual:

            self.numero_actual = self.numero_actual[:-1]

            self.actualizar_pantalla()

    # ==============================================================
    # PORCENTAJE
    # ==============================================================

    def porcentaje(self):

        if self.numero_actual == "":
            return

        try:

            numero = float(self.numero_actual)

            numero = numero / 100

            self.numero_actual = self.formatear(numero)

            self.actualizar_pantalla()

        except ValueError:

            self.mostrar_error()

    # ==============================================================
    # CAMBIAR SIGNO
    # ==============================================================

    def cambiar_signo(self):

        if self.numero_actual == "":
            return

        try:

            numero = float(self.numero_actual)

            numero *= -1

            self.numero_actual = self.formatear(numero)

            self.actualizar_pantalla()

        except ValueError:

            self.mostrar_error()

    # ==============================================================
    # ACTUALIZAR PANTALLA
    # ==============================================================

    def actualizar_pantalla(self):

        self.pantalla.delete(0, tk.END)

        self.pantalla.insert(
            0,
            self.numero_actual
        )

    # ==============================================================
    # MOSTRAR ERROR
    # ==============================================================

    def mostrar_error(self):

        self.pantalla.delete(0, tk.END)

        self.pantalla.insert(
            0,
            "Error"
        )

        self.numero_actual = ""
        self.primer_numero = None
        self.operador = None
        self.nuevo_resultado = True

    # ==============================================================
    # TECLADO
    # ==============================================================

    def teclado(self, evento):

        tecla = evento.keysym

        # Números
        if evento.char.isdigit():

            self.numero(evento.char)

        # Punto
        elif evento.char == ".":

            self.decimal()

        # Operadores del teclado
        elif evento.char in ["+", "-"]:

            self.operacion(evento.char)

        # Multiplicación
        elif evento.char == "*":

            self.operacion("×")

        # División
        elif evento.char == "/":

            self.operacion("÷")

        # Enter
        elif tecla in ["Return", "KP_Enter"]:

            self.calcular()

        # Backspace
        elif tecla == "BackSpace":

            self.borrar()

        # Escape
        elif tecla == "Escape":

            self.limpiar()

        # Porcentaje
        elif evento.char == "%":

            self.porcentaje()


# ==============================================================
# PROGRAMA PRINCIPAL
# ==============================================================

if __name__ == "__main__":

    ventana = tk.Tk()

    calculadora = Calculadora(ventana)

    ventana.mainloop()