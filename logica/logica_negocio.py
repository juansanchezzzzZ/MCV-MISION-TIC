# funcion opcion de alimentar la base de datos y retornarla
# --------------------------------
# informacion del tripulante x:
# ingresar documento del tripulante x
# ingresar nombres del tripulante x
# ingresar apellidos del tripulante x
# --------------------------------
import json  # este impor se generó automaticamente debido a la linea 47


def leer_base_datos(Base_Datos_Tripulantes):
    numero_Tripulantes = len(Base_Datos_Tripulantes)
    # agregar tripulantes
    Continuar = True
    while(Continuar):
        print("Informacion del tripulante: ", str(numero_Tripulantes+1))
        documento = input("Documento del tripulante: ")

        if(documento == "0"):
            Continuar = False
        else:
            nombres = input("Nombres del tripulante: ")
            apellidos = input("Apellidos del tripulante: ")
            # agrego el tripulante a la base de datos
            Base_Datos_Tripulantes[documento] = [nombres, apellidos]

            numero_Tripulantes = numero_Tripulantes+1
    return Base_Datos_Tripulantes

# funcion para imprimir la informacion de los tripulantes


def imprimir_base_datos(Base_Datos_Tripulantes):
    Lista_info_Tripulantes=[]
    if len(Base_Datos_Tripulantes)==0:
        print("No hay Tripulantes")
        return False
    else:
        for documento, lista_info in sorted(Base_Datos_Tripulantes.items(), reverse=True):
            informacion_Tripulante = "Documento=", documento, "-->", lista_info[0], lista_info[1]
            Lista_info_Tripulantes.append(informacion_Tripulante)
    return Lista_info_Tripulantes

# FUNCION COMPLEMENTO DE la funcion "LEER BASE" DE DATOS
# la siguiente funcion ABRE el archivo json alojado en la carpeta base de datos
# el archivo json alojado en base de datos es la información de los tripulantes
def cargar_info_Json(Base_Datos_Tripulantes):
    print("¿Seguro que desea cargar la información?")
    print()
    print("Si:[Enter]     No:[Presione: 0]")
    confirmar=input()
    if confirmar=="0":
        print("Carga de datos cancelada")
        return Base_Datos_Tripulantes
    else:
        Base_Datos_Tripulantes2={}
        with open("Base_de_datos/Tripulantes.json", encoding="UTF-8") as Archivojson:
            temporal=json.load(Archivojson)
            Base_Datos_Tripulantes2=temporal["Base_Datos_TripulantesJson"]
            print("Información guardados exitosamente")
        return Base_Datos_Tripulantes2

# FUNCION COMPLEMENTO DE la funcion "LEER BASE" DE DATOS
# la siguiente funcion GUARDA  el archivo json alojado en la carpeta base de datos
# el archivo json alojado en base de datos es la información de los tripulantes
def guardar_info_Json(Base_Datos_Tripulantes):
    print("¿Seguro que desea guardar la información?")
    print()
    print("Si:[Enter]     No:[Presione: 0]")
    confirmar=input()
    if confirmar=="0":
        print("Los datos no han sido guardados")
        return False  
    else:
        with open("Base_de_datos/Tripulantes.json","w", encoding="UTF-8") as Archivojson:
            temporal={"Base_Datos_Tripulantes":{}}
            temporal["Base_Datos_TripulantesJson"]=Base_Datos_Tripulantes
            json.dump(temporal,Archivojson,ensure_ascii=False,indent=2)
            print("La información ha sido guardada exitosamente")
        return True
