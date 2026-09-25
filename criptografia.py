# ============================================================
# 🔐 LABORATORIO DE CRIPTOGRAFÍA
# De César → sustitución → XOR → hash
# ============================================================

import hashlib
import string


# ============================================================
# 1. CIFRADO CÉSAR
# ============================================================

def cesar(texto, desplazamiento):

    resultado = ""

    # Recorremos cada carácter del mensaje
    for letra in texto:

        # Si es una letra
        if letra.isalpha():

            # Convertimos a mayúscula
            letra = letra.upper()

            # ord() convierte una letra en un número ASCII/Unicode
            numero = ord(letra)

            # A = 65
            # B = 66
            # C = 67
            #
            # Sumamos el desplazamiento
            nuevo = numero + desplazamiento

            # % 26 hace que después de Z volvamos a A
            nuevo = (nuevo - 65) % 26 + 65

            # chr() convierte el número nuevamente en letra
            resultado += chr(nuevo)

        else:

            # Espacios y símbolos quedan igual
            resultado += letra

    return resultado


mensaje = "HOLA MUNDO"

cifrado = cesar(mensaje, 3)

print("Original:", mensaje)
print("Cifrado :", cifrado)


# ============================================================
# DESCIFRAR CÉSAR
# ============================================================

descifrado = cesar(cifrado, -3)

print("Descifrado:", descifrado)


# ============================================================
# 2. FUERZA BRUTA DE CÉSAR
# ============================================================

print("\n===== POSIBLES CLAVES =====")

texto = "KROD PXQGR"

for clave in range(26):

    resultado = cesar(texto, -clave)

    print(f"Clave {clave}: {resultado}")


# ============================================================
# 3. CIFRADO POR SUSTITUCIÓN
# ============================================================

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
clave =   "QWERTYUIOPASDFGHJKLZXCVBNM"


def sustitucion(texto):

    resultado = ""

    for letra in texto.upper():

        if letra in alfabeto:

            posicion = alfabeto.index(letra)

            resultado += clave[posicion]

        else:

            resultado += letra

    return resultado


mensaje = "HOLA"

print("\n===== SUSTITUCIÓN =====")
print("Original:", mensaje)
print("Cifrado :", sustitucion(mensaje))


# ============================================================
# 4. HASH SHA-256
# ============================================================

def hash_sha256(texto):

    # Convertimos texto a bytes
    datos = texto.encode()

    # Calculamos SHA-256
    resultado = hashlib.sha256(datos)

    # Convertimos a hexadecimal
    return resultado.hexdigest()


print("\n===== SHA-256 =====")

print(hash_sha256("Hola"))
print(hash_sha256("Hola!"))


# ============================================================
# 5. COMPROBAR INTEGRIDAD
# ============================================================

mensaje = "Archivo importante"

hash_original = hash_sha256(mensaje)

mensaje_recibido = "Archivo importante"

hash_recibido = hash_sha256(mensaje_recibido)


if hash_original == hash_recibido:

    print("\nEl mensaje no cambió.")

else:

    print("\nEl mensaje fue modificado.")