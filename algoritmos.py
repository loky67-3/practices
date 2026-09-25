# ============================================================
# 1. VARIABLES
# ============================================================

nombre = "chatt"
edad = 20
altura = 1.75
estudiante = True

print(nombre)
print(edad)
print(altura)
print(estudiante)


# ============================================================
# 2. CONCATENAR CADENAS
# ============================================================

nombre = "Abner"
apellido = "García"

# Concatenar = unir textos
nombre_completo = nombre + " " + apellido

print(nombre_completo)


# También podemos usar f-strings
edad = 20

print(f"Me llamo {nombre_completo} y tengo {edad} años.")


# ============================================================
# 3. MÉTODOS DE STRINGS
# ============================================================

texto = "Hola Python"

print(texto.upper())       # MAYÚSCULAS
print(texto.lower())       # minúsculas
print(texto.capitalize())  # Primera letra
print(texto.replace("Python", "Mundo"))

print(len(texto))          # Cantidad de caracteres


# ============================================================
# 4. INPUT
# ============================================================

nombre = input("Tu nombre: ")

print(f"Hola {nombre}")


# ============================================================
# 5. CONVERSIONES
# ============================================================

edad = int(input("Edad: "))
precio = float(input("Precio: "))

print(edad)
print(precio)


# ============================================================
# 6. OPERADORES
# ============================================================

a = 10
b = 3

print(a + b)   # suma
print(a - b)   # resta
print(a * b)   # multiplicación
print(a / b)   # división
print(a // b)  # división entera
print(a % b)   # residuo
print(a ** b)  # potencia


# ============================================================
# 7. CONDICIONALES
# ============================================================

edad = 20

if edad >= 18:
    print("Mayor de edad")

elif edad >= 13:
    print("Adolescente")

else:
    print("Menor")


# ============================================================
# 8. OPERADORES LÓGICOS
# ============================================================

edad = 20
tiene_credencial = True

if edad >= 18 and tiene_credencial:
    print("Puede entrar")


if edad < 18 or tiene_credencial:
    print("Se cumple una condición")


if not tiene_credencial:
    print("No tiene credencial")


# ============================================================
# 9. WHILE
# ============================================================

contador = 1

while contador <= 5:

    print(contador)

    contador += 1


# ============================================================
# 10. FOR
# ============================================================

for numero in range(1, 6):

    print(numero)


# ============================================================
# 11. FOR CON STRING
# ============================================================

nombre = "Python"

for letra in nombre:

    print(letra)


# ============================================================
# 12. TRIÁNGULO DE ASTERISCOS
# ============================================================

for fila in range(1, 6):

    print("*" * fila)

# Resultado:
#
# *
# **
# ***
# ****
# *****


# ============================================================
# 13. TRIÁNGULO CON BUCLES DENTRO DE BUCLES
# ============================================================

for fila in range(1, 6):

    for columna in range(fila):

        print("*", end="")

    print()


# ============================================================
# 14. CUADRADO
# ============================================================

for fila in range(5):

    for columna in range(5):

        print("*", end="")

    print()


# ============================================================
# 15. RECTÁNGULO
# ============================================================

for fila in range(3):

    for columna in range(7):

        print("*", end="")

    print()


# ============================================================
# 16. TRIÁNGULO INVERTIDO
# ============================================================

for fila in range(5, 0, -1):

    print("*" * fila)


# ============================================================
# 17. TRIÁNGULO CENTRADO
# ============================================================

for fila in range(1, 6):

    espacios = 5 - fila
    estrellas = 2 * fila - 1

    print(" " * espacios + "*" * estrellas)


# ============================================================
# 18. TABLA DE MULTIPLICAR
# ============================================================

numero = 5

for i in range(1, 11):

    print(f"{numero} x {i} = {numero * i}")


# ============================================================
# 19. SUMAR NÚMEROS
# ============================================================

suma = 0

for numero in range(1, 11):

    suma += numero

print(suma)


# ============================================================
# 20. CONTAR PARES
# ============================================================

for numero in range(1, 21):

    if numero % 2 == 0:

        print(numero)


# ============================================================
# 21. LISTAS
# ============================================================

frutas = ["manzana", "pera", "uva"]

print(frutas[0])

frutas.append("mango")

frutas.remove("pera")

for fruta in frutas:

    print(fruta)


# ============================================================
# 22. DICCIONARIOS
# ============================================================

persona = {
    "nombre": "Abner",
    "edad": 20,
    "ciudad": "Sayula"
}

print(persona["nombre"])
print(persona["edad"])

persona["edad"] = 21


# ============================================================
# 23. RECORRER DICCIONARIO
# ============================================================

for clave, valor in persona.items():

    print(clave, ":", valor)


# ============================================================
# 24. TUPLAS
# ============================================================

coordenada = (10, 20)

x = coordenada[0]
y = coordenada[1]

print(x, y)


# ============================================================
# 25. SET
# ============================================================

numeros = {1, 2, 2, 3, 3, 4}

print(numeros)

# El set elimina repetidos.


# ============================================================
# 26. FUNCIONES
# ============================================================

def saludar():

    print("Hola")


saludar()


# ============================================================
# 27. FUNCIÓN CON PARÁMETRO
# ============================================================

def saludar(nombre):

    print(f"Hola {nombre}")


saludar("Abner")


# ============================================================
# 28. FUNCIÓN CON RETURN
# ============================================================

def sumar(a, b):

    return a + b


resultado = sumar(5, 3)

print(resultado)


# ============================================================
# 29. FUNCIÓN PARA SABER SI ES PAR
# ============================================================

def es_par(numero):

    return numero % 2 == 0


print(es_par(10))
print(es_par(7))


# ============================================================
# 30. TRY / EXCEPT
# ============================================================

try:

    numero = int(input("Número: "))

    print(numero * 2)

except ValueError:

    print("Debes escribir un número.")


# ============================================================
# 31. ENUMERATE
# ============================================================

frutas = ["manzana", "pera", "uva"]

for posicion, fruta in enumerate(frutas):

    print(posicion, fruta)


# ============================================================
# 32. ZIP
# ============================================================

nombres = ["Ana", "Luis", "Pedro"]
edades = [20, 25, 30]

for nombre, edad in zip(nombres, edades):

    print(nombre, edad)


# ============================================================
# 33. LIST COMPREHENSION
# ============================================================

numeros = [1, 2, 3, 4, 5]

cuadrados = [numero ** 2 for numero in numeros]

print(cuadrados)


# ============================================================
# 34. RANDOM
# ============================================================

import random

numero = random.randint(1, 10)

print(numero)


# ============================================================
# 35. RANDOM.CHOICE
# ============================================================

opciones = ["piedra", "papel", "tijera"]

computadora = random.choice(opciones)

print(computadora)


# ============================================================
# 36. PIEDRA, PAPEL O TIJERA
# ============================================================

jugador = input("Piedra, papel o tijera: ").lower()

computadora = random.choice(opciones)

gana = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel"
}

if jugador == computadora:

    print("Empate")

elif gana.get(jugador) == computadora:

    print("Ganaste")

else:

    print("Perdiste")


# ============================================================
# 37. SHUFFLE
# ============================================================

cartas = ["A", "K", "Q", "J"]

random.shuffle(cartas)

print(cartas)


# ============================================================
# 38. FUNCIONES LAMBDA
# ============================================================

sumar = lambda a, b: a + b

print(sumar(5, 3))


# Lambda significa una función pequeña de una sola expresión.


# ============================================================
# 39. LAMBDA CON SORT
# ============================================================

personas = [
    ("Ana", 30),
    ("Luis", 20),
    ("Pedro", 25)
]

personas.sort(key=lambda persona: persona[1])

print(personas)


# Ordenamos utilizando la edad.


# ============================================================
# 40. RECURSIVIDAD
# ============================================================

def cuenta_regresiva(numero):

    # CASO BASE
    # Aquí detenemos la función.
    if numero == 0:

        print("¡Fin!")

        return

    print(numero)

    # LA FUNCIÓN SE LLAMA A SÍ MISMA
    cuenta_regresiva(numero - 1)


cuenta_regresiva(5)


# ============================================================
# 41. FACTORIAL RECURSIVO
# ============================================================

def factorial(numero):

    if numero == 1:

        return 1

    return numero * factorial(numero - 1)


print(factorial(5))


# 5 * 4 * 3 * 2 * 1 = 120


# ============================================================
# 42. TORRES DE HANÓI
# ============================================================

def hanoi(n, origen, auxiliar, destino):

    # CASO BASE
    if n == 1:

        print(f"{origen} -> {destino}")

        return

    # Mover los pequeños al auxiliar
    hanoi(n - 1, origen, destino, auxiliar)

    # Mover el grande al destino
    print(f"{origen} -> {destino}")

    # Mover los pequeños al destino
    hanoi(n - 1, auxiliar, origen, destino)


hanoi(3, "A", "B", "C")


# ============================================================
# 43. BÚSQUEDA LINEAL
# ============================================================

numeros = [4, 8, 2, 9, 5]

buscar = 9

for numero in numeros:

    if numero == buscar:

        print("Encontrado")

        break


# ============================================================
# 44. CONTAR CUÁNTAS VECES APARECE
# ============================================================

numeros = [1, 2, 2, 3, 2, 4]

buscar = 2
contador = 0

for numero in numeros:

    if numero == buscar:

        contador += 1

print(contador)


# ============================================================
# 45. ENCONTRAR EL MAYOR
# ============================================================

numeros = [8, 3, 15, 2, 10]

mayor = numeros[0]

for numero in numeros:

    if numero > mayor:

        mayor = numero

print(mayor)


# ============================================================
# 46. ORDENAMIENTO BURBUJA
# ============================================================

numeros = [5, 2, 8, 1, 3]

for i in range(len(numeros)):

    for j in range(len(numeros) - 1):

        if numeros[j] > numeros[j + 1]:

            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)


# ============================================================
# 47. PALÍNDROMO
# ============================================================

texto = input("Palabra: ").lower()

if texto == texto[::-1]:

    print("Es palíndromo")

else:

    print("No es palíndromo")


# ============================================================
# 48. CONTAR VOCALES
# ============================================================

texto = input("Texto: ").lower()

vocales = "aeiou"
contador = 0

for letra in texto:

    if letra in vocales:

        contador += 1

print("Vocales:", contador)


# ============================================================
# 49. NÚMERO PRIMO
# ============================================================

numero = int(input("Número: "))

es_primo = True

if numero < 2:

    es_primo = False

else:

    for i in range(2, numero):

        if numero % i == 0:

            es_primo = False
            break


if es_primo:

    print("Es primo")

else:

    print("No es primo")


# ============================================================
# 50. FIBONACCI
# ============================================================

a = 0
b = 1

for i in range(10):

    print(a)

    a, b = b, a + b


# ============================================================
# 51. MEMORIA DE CINCO GENIOS
# ============================================================

# Cinco personas están sentadas en una mesa.
# Cada una debe realizar una acción por turnos.
# Simulamos los turnos con un bucle.

genios = ["Einstein", "Newton", "Tesla", "Curie", "Darwin"]

for ronda in range(3):

    print(f"\nRonda {ronda + 1}")

    for genio in genios:

        print(f"{genio} está pensando...")

    print("Todos terminaron su turno.")


# ============================================================
# 52. CINCO GENIOS ALTERNANDO
# ============================================================

import time

genios = ["Einstein", "Newton", "Tesla", "Curie", "Darwin"]

for ronda in range(3):

    for genio in genios:

        print(f"{genio} piensa...")

        time.sleep(1)

        print(f"{genio} termina.")


# ============================================================
# 53. CONTADOR DE PALABRAS
# ============================================================

texto = input("Escribe una frase: ")

palabras = texto.split()

print("Palabras:", len(palabras))


# ============================================================
# 54. MENÚ CON WHILE
# ============================================================

while True:

    print("\n1. Saludar")
    print("2. Mostrar números")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "1":

        print("Hola")

    elif opcion == "2":

        for i in range(1, 6):

            print(i)

    elif opcion == "3":

        break

    else:

        print("Opción incorrecta")