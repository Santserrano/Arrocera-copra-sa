def opcion_1():
    print("Has seleccionado la opción 1")

def opcion_2():
    print("Has seleccionado la opción 2")

def opcion_3():
    print("Has seleccionado la opción 3")

def opcion_default():
    print("Opción no válida. Por favor, selecciona una opción válida.")


def menu():
    print("Bienvenido al menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("0. Salir")

    while True:
        opcion = input("Por favor, selecciona una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            opcion_default()