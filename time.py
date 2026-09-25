import time 



#configuramos para un temporizador 

def temporizador(segundos):
    while segundos > 0:
        print(f"tiempo restante {segundos} segundos")
        time.sleep(1)
        segundos -= 1
    print("tiempo terminado")

def iniciar():
    while True:
        print("\nTemporizador")
        print("1. iniciar")
        print("2. salir")

        opcion = input("selecciona: ")
        if opcion == "1":
            segundos = int(input("¿cuantos segundos?: "))
            temporizador(segundos)
        elif opcion == "2":
            print("programa terminado")
            break
        else:
            print("operacion no valida")