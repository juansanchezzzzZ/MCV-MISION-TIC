# funciones de cada una de las opciones del menu


# importar archivo python logica-negocio
import logica.logica_negocio as Logica


# funcion opcion 1 (ingresar a la base de datos documento,nombres y apellidos)
def opcion_1(numero_opcion, Base_Datos_Tripulantes):
    if numero_opcion == "1":
        Base_Datos_Tripulantes_2 = Logica.leer_base_datos(
            Base_Datos_Tripulantes)
        return Base_Datos_Tripulantes_2
    else:
        return Base_Datos_Tripulantes

#funcion opcion 2 (imprimir la informacion de la base de datos: documento,nombres,apellidos)
def opcion_2(numero_opcion, Base_Datos_Tripulantes):
    if numero_opcion=="2":
        if Logica.imprimir_base_datos(Base_Datos_Tripulantes)!=False:
            for Tripulantes in Logica.imprimir_base_datos(Base_Datos_Tripulantes):
                print(Tripulantes)
        return True
    else:
        return False

#funcion opcion 5 (esta opción nace como complemento de la opción 2 como ejercicio del profe)
def opcion_5(numero_opcion, Base_Datos_Tripulantes):
    if numero_opcion == "5":
        Base_Datos_Tripulantes2=Logica.cargar_info_Json(Base_Datos_Tripulantes)
        return Base_Datos_Tripulantes2
    else:
        return Base_Datos_Tripulantes  

#funcion opcion 6 (esta opción nace como complemento de la opción 2 como ejercicio del profe)
def opcion_6(numero_opcion, Base_Datos_Tripulante):
    if numero_opcion == "6":
        Logica.guardar_info_Json(Base_Datos_Tripulante)
        return True
    else:
        return False
#funcion opcion 4 (esta opción es para introdicir las notas y grabarlas)
def opcion_3(numero_opcion, Base_Datos_Tripulante):
    if numero_opcion == "3":
        Base_Datos_Tripulante2=Logica.leerNotas(Base_Datos_Tripulante)
        return Base_Datos_Tripulante2
    else:
        return Base_Datos_Tripulante
    