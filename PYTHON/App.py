from Gestion_Canchas import menu
from Gestion_Canchas import validaciones
from os import system
system("cls")
'''
siempre que vayas a ejecutar algo hazlo desde aca porque estamos trabajando con modularidad
no toques este modulo al menos que necesites ejecutar algo directamente de el otro archivo...
'''

def inicio():
    '''
    este es el archivo principal donde se van a empezar a ejecutar los otros modulos
    '''
    print("BIENVENIDOS AL SISTEMA DE GESTION DE CANCHAS")
    print("presione S para continuar o N para salir: ")
    opcion = input().lower()
    if(opcion == "s"):
        system("cls")
        validaciones()
    elif(opcion=="n"):
        print("saliendo del sistema...")
        exit(0)



if __name__=="__main__":
    inicio()