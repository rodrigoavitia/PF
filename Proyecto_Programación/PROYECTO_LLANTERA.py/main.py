import funciones
import getpass
from usuarios import usuarios
from llantas import llantas
#---------------------------------------------------------------------------------------------------------------------------------------------
def main():
    while True:
        funciones.borrar_pantalla()
        opcion = funciones.menu_inicio_sesion()

        if opcion == "1" or opcion.upper() == "INICIAR SESION":
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: INICIO DE SESIÓN :::.")
            correo = input("\n\t\t\t Ingrese su Email: ").lower().strip()
            password = getpass.getpass("\n\t\t\t Contraseña: ").strip()

            lista_usuarios = usuarios.inicio_sesion(correo, password)
            if len(lista_usuarios) > 0:
                menu_llantas2(lista_usuarios[0], lista_usuarios[1], lista_usuarios[2])
            else:
                print(f"\n\tEmail y/o contraseña incorrectas por favor verifique ....")
                funciones.esperar_tecla()

        elif opcion == "2" or opcion.upper() == "REGISTRARSE":
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: REGISTRO DE USUARIO :::.")
            nombre = input("\n\t\t\t Nombre: ").strip()
            apellidos = input("\n\t\t\t Apellidos:").strip()
            correo = input("\n\t\t\t Email: ").lower().strip()
            password = getpass.getpass("\n\t\t\t Contraseña: ").strip()
            resultado = usuarios.registrar(nombre, apellidos, correo, password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
                funciones.esperar_tecla()
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")
                funciones.esperar_tecla()

        elif opcion == "3" or opcion.upper() == "SALIR":
            respuesta = input("\n\t\t\t ¿Está seguro de que desea salir? (S/N): ").strip().upper()
            if respuesta == 'S':
                print("\n\t\t\t Hasta luego . . .")
                break
            elif respuesta == 'N':
                print("\n\t\t\t Regresando al menú principal ...")
                funciones.esperar_tecla()
            else:
                print("\n\t\t\t Opción no válida, por favor intente de nuevo ...")
                funciones.esperar_tecla()

#----------------------------------------------------------------------------------------------------------------------------------------------
def menu_llantas2(usuario_id, nombre, apellidos):
    while True:
        funciones.borrar_pantalla()
        print(f"\n\t\t\t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion = funciones.menu_llantas(usuario_id, nombre, apellidos)

        if opcion == '1' or opcion.upper() == "AGREGAR":
            funciones.borrar_pantalla()
            print(f"\n\t.:: Agregar Llanta ::.")
            # Pide los datos necesarios para agregar una llanta
            marca = input("\tMarca: ")
            categoria = input("\tCategoría: ")
            medida = input("\tMedida: ")
            estado = input("\tEstado: ")
            precio = float(input("\tPrecio: "))                                                             
            cantidad = int(input("\tCantidad: "))
           # En main.py
            respuesta = llantas.agregar_llanta(marca, categoria, medida, estado, precio, cantidad)
            if respuesta:
                print(f"\n\tSe agregaron {cantidad} llantas {marca} {medida} con éxito")
            else:
                print(f"\n\t..No fue posible agregar la llanta, intenta más tarde")
            funciones.esperar_tecla()

        elif opcion == '2' or opcion.upper() == "MOSTRAR":
            funciones.borrar_pantalla()
            lista_llantas = llantas.mostrar_llantas()
            if len(lista_llantas) > 0:
                print(f"\n\tMostrar las llantas")
                print(f"{'ID':<10}{'Marca':<15}{'Modelo':<15}{'Medida':<15}")
                print(f"-"*60)
                for fila in lista_llantas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
            else:
                print("\n\t¡No hay llantas para este usuario!")
            funciones.esperar_tecla()

        elif opcion == '3' or opcion.upper() == "CAMBIAR":
            funciones.borrar_pantalla()
            lista_llantas = llantas.mostrar_llantas(usuario_id)
            if len(lista_llantas) > 0:
                print(f"\n\tMostrar las llantas")
                print(f"{'ID':<10}{'Marca':<15}{'Modelo':<15}{'Medida':<15}")
                print(f"-"*60)
                for fila in lista_llantas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
                print(f"-"*60)
                resp = input("¿Deseas modificar alguna llanta? (si/no): ").lower().strip()
                if resp == "si":
                    print(f"\n\t.:: {nombre} {apellidos}, vamos a modificar una llanta ::.\n")
                    id_llanta = input("\tID de la llanta a actualizar: ")
                    marca = input("\tNueva marca: ")
                    modelo = input("\tNuevo modelo: ")
                    medida = input("\tNueva medida: ")
                    respuesta = llantas.cambiar_llanta(id_llanta, marca, modelo, medida)
                    if respuesta:
                        print(f"\n\tSe actualizó la llanta con éxito")
                    else:
                        print(f"\n\t..No fue posible actualizar la llanta, intenta más tarde")
                funciones.esperar_tecla()
            else:
                print("\n\t¡No hay llantas para este usuario!")
                funciones.esperar_tecla()

        elif opcion == '4' or opcion.upper() == "ELIMINAR":
            funciones.borrar_pantalla()
            lista_llantas = llantas.mostrar_llantas(usuario_id)
            if len(lista_llantas) > 0:
                print(f"\n\tMostrar las llantas")
                print(f"{'ID':<10}{'Marca':<15}{'Modelo':<15}{'Medida':<15}")
                print(f"-"*60)
                for fila in lista_llantas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
                print(f"-"*60)
                resp = input("¿Deseas eliminar alguna llanta? (si/no): ").lower().strip()
                if resp == "si":
                    print(f"\n\t.:: {nombre} {apellidos}, vamos a eliminar una llanta ::.\n")
                    id_llanta = input("\tID de la llanta a eliminar: ")
                    if not id_llanta.isdigit():
                        print("\n\tEl ID debe ser un número entero. Intenta de nuevo.")
                        funciones.esperar_tecla()
                        continue
                    respuesta = llantas.eliminar_llanta(id_llanta)
                    if respuesta:
                        print(f"\n\tSe borró la llanta {id_llanta} con éxito")
                    else:
                        print(f"\n\t..No fue posible eliminar la llanta, intenta más tarde")
                funciones.esperar_tecla()
            else:
                print("\n\t¡No hay llantas para este usuario!")
                funciones.esperar_tecla()

        elif opcion == '5' or opcion.upper() == "BUSCAR":
            funciones.borrar_pantalla()
            lista_llantas = llantas.mostrar_llantas(usuario_id)
            if len(lista_llantas) > 0:
                print(f"\n\tMostrar las llantas")
                print(f"{'ID':<10}{'Marca':<15}{'Modelo':<15}{'Medida':<15}")
                print(f"-"*60)
                for fila in lista_llantas:
                    print(f"{fila[0]:<10}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}")
                print(f"-"*60)
                id_llanta = input("Ingrese el ID de la llanta a buscar: ").strip()
                resultado = llantas.buscar_llanta(id_llanta)
                if resultado:
                    print(f"\n\tLlantas encontrada: {resultado[2]} - {resultado[3]} - {resultado[4]}")
                else:
                    print("\n\tNo se encontró la llanta con el ID proporcionado.")
            else:
                print("\n\t¡No hay llantas para este usuario!")
            funciones.esperar_tecla()

        elif opcion == '6' or opcion.upper() == "SALIR":
            break

        else:
            print("\n\t\tOpción no válida. Intenta de nuevo.")
            funciones.esperar_tecla()


if __name__ == "__main__":
    main()    

    