from os import system 
system("cls")

'''
esta son las listas donde se almacenas las gestiones de administradores
'''
admins=[]
respons=[]
clientes=[]


'''
este es el menu principal de todas las gestiones 
este menu es lo basico y lo que hace es que cada 1 es un modulo
'''
def menu():
    '''
    este es el menu principal de todas las gestiones 
    este menu es lo basico y lo que hace es que cada 1 es un modulo
    '''
    while(True):
        print("      MENU PRINCIPAL     ")
        print("-------------------------")
        print("1. GESTION DE CLIENTES   ")
        print("2. GESTION DE RESERVAS   ")
        print("3. GESTION DE ARBITROS   ")
        print("4. GESTION DE PROMOCIONES")
        print("5. GESTION DE REPORTES   ")
        print("6. SALIR                 ")
        print("-------------------------")
        print("\n")
        opcion = int(input("que opcion desea realizar: "))
        if (opcion == 1):
            Gestion_Clientes()
        elif(opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif(opcion == 4):
            pass
        elif(opcion == 5):
            pass
        elif(opcion == 6):
            exit(0)
        else:
            print("No selecionaste ninguna opcion")
            continue

def validaciones():
    '''
    Este es el modulo de gestion de administradores o de validaciones que te va a permitir acceder a  los otros items que tengas 
    una vez registres a los administradores o cualquiera de los que esten en este menu te redirigira al menu principal que es donde vas a agregar
    los otros modulos 
    '''
    while(True):
        print("      MENU PRINCIPAL     ")
        print("-------------------------")
        print("1.   ADMINISTRADORES     ")
        print("2.   RESPONSABLES        ")
        print("3.   CLIENTES            ")
        print("-------------------------")
        print("\n")
        opcion = int(input("IDENTIFIQUE SU ROL: "))
        if(opcion>3):
            print("error")
        if(opcion == 1):
            print("Ingrese su codigo")
            cod = int(input())
            print("ingrese su nombre")
            nombre = input()
            print("ingrese su apellido")
            apellido = input()
            print("Ingrese su direccion")
            dirrecion = input()
            print("Registre su telefono")
            telefono = int(input())
            admins.append(cod)
            admins.append(nombre)
            admins.append(apellido)
            admins.append(dirrecion)
            admins.append(telefono)
            print("desea agregar otro administrador s/n")
            opcion=input()
            if(opcion=="s"):
                continue
            else:
                print(admins)
                menu()
        elif(opcion == 2):
            print("Ingrese su codigo")
            cod = int(input())
            print("ingrese su nombre")
            nombre = input()
            print("ingrese su apellido")
            apellido = input()
            print("Ingrese su direccion")
            dirrecion = input()
            print("Registre su telefono")
            telefono = int(input())
            respons.append(cod,nombre,apellido,dirrecion,telefono)
            print(respons)
        elif(opcion == 3): 
            Gestion_Clientes()
        else:
            print("tu opcion no se encuentra")
            exit(0)


def Gestion_Clientes():
    '''
    Esta es la gestion de clientes  lo que hace es registrar a los clientes para que puedas hacer las reservas 
    y puedas opcionar a los otros modulos
    '''
    while(True):
        print("Ingrese su codigo")
        cod = int(input())
        print("ingrese su nombre")
        nombre = input()
        print("ingrese su apellido")
        apellido = input()
        print("Ingrese su direccion")
        dirrecion = input()
        print("Registre su telefono")
        telefono = int(input())
        clientes.append(cod)
        clientes.append(nombre)
        clientes.append(apellido)
        clientes.append(dirrecion)
        clientes.append(telefono)
        opcion = input("desea agregar otro cliente s/n")
        if(opcion=="s"):
            continue
        else:
            print(clientes)
            menu()