# Debe tener un menú con las siguientes opciones:
# 1. Leer info tripulantes
# (para cada tripulante se debe leer documento,nombres y apellidos)
# (Debe tener MEMORIA,cuando se agreguen más tripulantes debe conservar los anteriores)
# (Si se escribe un documento existente debe sobrescribir el anterior)
# 2.Imprimir info tripulantes
# (La información se debe imprimir de manera ordenada por valor del documento)
# (Si no hay información de tripulantes debe imprimir:No hay tripulantes !!!)
# 3. Calificaciones retos
# (Para cada tripulante debe pedirNnotas de retos)
# (Ncorrespondeala cantidad de notas,debe ser una constante al inicio del programa)
# 4.Definitiva cicloI
# (Debe imprimir las definitivas de cada documento,en orden inverso,sin nombres para efectos de
# (Solo se realiza el cálculo para los tripulantes que tengan información de notas de los retos)


# Memoria del sistema
from msilib.schema import Control
import controlador.controlador_opciones as Controlador
import vistas.menu as Menu
Base_Datos_Tripulantes = {}


# importar el archivo python menu
# importar el archivo python controladores

# ciclo para mantenerse en el sistema (mientras Continuar=True se mantiene en el sistema)
Continuar = True
while (Continuar):
    # abrir el menu
    numero_opcion = Menu.mostrar_menu()

    # en caso de que el usuario elija otra opcion a las permitidas
    Continuar = Menu.numero_opciones_permitidas(numero_opcion)

    # controladores

    #opción 1 "Leer info tripulantes"
    Base_Datos_Tripulantes=Controlador.opcion_1(numero_opcion, Base_Datos_Tripulantes)
    #opción 2 "imprimir info tripulantes"
    Controlador.opcion_2(numero_opcion, Base_Datos_Tripulantes)
    #opción adicional (5) "cargar info tripulantes desde un Json"
    Base_Datos_Tripulantes=Controlador.opcion_5(numero_opcion, Base_Datos_Tripulantes)
    #opción adicional (6) "guardar info tripulantes desde un Json"
    Controlador.opcion_6(numero_opcion, Base_Datos_Tripulantes)
    #opción adicional (3) "ingresar notas de los tripulantes"
    Base_Datos_Tripulantes=Controlador.opcion_3(numero_opcion, Base_Datos_Tripulantes)

    # cerrar menu en caso de que se elija 0
    Continuar = Menu.salir_del_sistema(numero_opcion)
    # hacer una pausa para darle sensación de pausa al sistema
    Menu.pausa()

