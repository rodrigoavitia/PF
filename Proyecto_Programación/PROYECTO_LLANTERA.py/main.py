import funciones
import getpass
from usuarios import usuarios
from llantas import llantas
#---------------------------------------------------------------------------------------------------------------------------------------------
def main():
    opcion=True
    while opcion:
        funciones.borrar_pantalla()
        opcion=funciones.menu_inicio_sesion()

        if opcion=="1" or opcion=="INICIAR SESION":                                   # Todo indica que ya inicia sesión correctamente
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: INICIO DE SESIÓN :::.")
            correo=input("\n\t\t\t Ingrese su Email: ").lower().strip()
            password=getpass.getpass("\n\t\t\t Contraseña: ").strip()

            lista_usuarios=usuarios.inicio_sesion(correo,password)
            if len(lista_usuarios)>0:                       # Tengo un error aqui, no puedo iniciar sesión ( Parece ya esta resuelto )
              funciones.menu_llantas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
              print(f"\n\tEmail y/o contraseña incorrectas por favor verifique ....")
              funciones.esperar_tecla()

#---------------------------------------------------------------------------------------------------------------------------------------------

        elif opcion=="2" or opcion=="REGISTRARSE":
              funciones.borrar_pantalla()
              print("\n\t\t\t .::: REGISTRO DE USUARIO :::.")
              nombre=input("\n\t\t\t Nombre: ").strip()
              apellidos=input("\n\t\t\t Apellidos:").strip()
              correo=input("\n\t\t\t Email: ").lower().strip()
              password=getpass.getpass("\n\t\t\t Contraseña: ").strip()               #Registro de usuarios parece estar ya listo
              resultado=usuarios.registrar(nombre,apellidos,correo,password)
              if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
                funciones.esperar_tecla()
              else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
                funciones.esperar_tecla()

#---------------------------------------------------------------------------------------------------------------------------------------------

        elif opcion=="3" or opcion=="SALIR": 
            respuesta = input("\n\t\t\t ¿Está seguro de que desea salir? (S/N): ").strip().upper()
            if respuesta == 'S':                                  
                print("\n\t\t\t Hasta luego . . .")
                break
            elif respuesta == 'N':                                                          #Aqui simplemente regresamos al menu principal
                print("\n\t\t\t Regresando al menú principal ...")
                funciones.esperar_tecla()

            else:
                print("\n\t\t\t Opción no válida, por favor intente de nuevo ...")      #Simple manejo de errores
                funciones.esperar_tecla()

#----------------------------------------------------------------------------------------------------------------------------------------------
def menu_llantas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrar_pantalla()
        print(f"\n\t\t\t Bienvenido {nombre} {apellidos} (ID: {usuario_id})")
        opcion = funciones.menu_llantas(usuario_id,nombre,apellidos)

        if opcion == "1" or opcion == "AGREGAR":
            llantas.agregar_llanta(usuario_id)
        elif opcion == "2" or opcion == "MOSTRAR":
            llantas.mostrar_llantas(usuario_id)
        elif opcion == "3" or opcion == "BUSCAR":       #Por el momento solo llega hasta el menu de las llantas falta hacer todo lo demas
            llantas.buscar_llanta(usuario_id)  

        elif opcion == "4" or opcion == "ELIMINAR":
            llantas.eliminar_llanta(usuario_id)

        elif opcion == "5" or opcion == "SALIR":
            break

    funciones.esperar_tecla()


if __name__ == "__main__":
    main()    

    