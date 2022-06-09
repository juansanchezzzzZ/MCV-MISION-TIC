#libreria externa para darle colores a prints en la terminal
from termcolor import colored as colorear
# menu del sistema
def mostrar_menu():
    print()
    print(colorear("------------------------------------","yellow",attrs=["reverse"]))
    print("1.Ingresar info tripulantes")
    print("2.Imprimir info tripulantes")
    print("3.Calificaciones retos")
    print("4.Definitiva ciclo I")
    print("5.Cargar info tripulantes Json")
    print("6.Grabar info tripulantes en Json")
    print()
    print("0.Salir")
    print(colorear("------------------------------------","yellow",attrs=["reverse"]))
    numero_opcion = input("-->")
    print()
    return numero_opcion

# funcion para darle sensación de pausa mientras el usuario escoge


def pausa():
    print()
    input("[ENTER]para continuar")

# en caso de que el usuario elija otra opción a las que estan en el menu


def numero_opciones_permitidas(numero_opcion_elegida):
    numero_opciones_permitidas_elegir = ("1", "2", "3", "4", "5", "6", "0")
    if(numero_opcion_elegida not in numero_opciones_permitidas_elegir):
        print("opcion incorrecta")
        return False
    else:
        return True

# en caso de que el usuario elija la opción 0 (salir)


def salir_del_sistema(opcion_escogida_0):
    if(opcion_escogida_0 != "0"):
        return True
    else:
        print("Has salido del sistema")
        return False
