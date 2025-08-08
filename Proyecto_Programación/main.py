import funciones
import getpass
from usuarios import usuarios
from llantas import llantas

# ---------------------------------------------------------------------------------------------------------------------------------------------
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
            if lista_usuarios:
                menu_llantas(lista_usuarios[0], lista_usuarios[1], lista_usuarios[2])
            else:
                print("\n\t❌ Email y/o contraseña incorrectas. Intente de nuevo.")
                funciones.esperar_tecla()

        elif opcion == "2" or opcion.upper() == "REGISTRARSE":
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: REGISTRO DE USUARIO :::.")
            nombre = input("\n\t\t\t Nombre: ").strip()
            apellidos = input("\n\t\t\t Apellidos:").strip()
            correo = input("\n\t\t\t Email: ").lower().strip()
            password = getpass.getpass("\n\t\t\t Contraseña: ").strip()

            if usuarios.registrar(nombre, apellidos, correo, password):
                print(f"\n\t✅ Usuario {nombre} {apellidos} registrado correctamente.")
            else:
                print("\n\t❌ No fue posible registrar el usuario en este momento.")
            funciones.esperar_tecla()

        elif opcion == "3" or opcion.upper() == "SALIR":
            respuesta = input("\n\t\t\t ¿Está seguro de que desea salir? (S/N): ").strip().upper()
            if respuesta == 'S':
                print("\n\t\t\t Hasta luego...")
                break
            elif respuesta == 'N':
                print("\n\t\t\t Regresando al menú principal...")
                funciones.esperar_tecla()
            else:
                print("\n\t\t\t ❌ Opción no válida.")
                funciones.esperar_tecla()

        else:
            print("\n\t❌ Opción inválida. Intente de nuevo.")
            funciones.esperar_tecla()

# ---------------------------------------------------------------------------------------------------------------------------------------------
def menu_llantas(usuario_id, nombre, apellidos):
    while True:
        funciones.borrar_pantalla()
        print(f"\n\t\t\t Bienvenido {nombre} {apellidos}")
        opcion = funciones.menu_llantas(usuario_id, nombre, apellidos)

        if opcion == '1' or opcion.upper() == "AGREGAR":
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: AGREGAR LLANTA :::.")
            marca = input("\tMarca: ").strip()
            categoria = input("\tCategoría: ").strip()
            medida = input("\tMedida: ").strip()
            estado = input("\tEstado (Nueva/Usada): ").strip()
            try:
                precio = float(input("\tPrecio: "))
                cantidad = int(input("\tCantidad: "))
            except ValueError:
                print("\n\t❌ Precio y cantidad deben ser valores numéricos.")
                funciones.esperar_tecla()
                continue

            if llantas.agregar_llanta(usuario_id, marca, categoria, medida, estado, precio, cantidad):
                print("\n\t✅ Llanta agregada exitosamente.")
            else:
                print("\n\t❌ No se pudo agregar la llanta.")
            funciones.esperar_tecla()

        elif opcion == '2' or opcion.upper() == "MOSTRAR":
            funciones.borrar_pantalla()
            registros = llantas.mostrar_llantas(usuario_id)
            if registros:
                imprimir_tabla_llantas(registros)
            else:
                print("\n\tNo hay llantas registradas.")
            funciones.esperar_tecla()

        elif opcion == '3' or opcion.upper() == "BUSCAR":
            funciones.borrar_pantalla()
            print("\n\t\t\t .::: BUSCAR LLANTA :::.")
            marca = input("Ingrese la marca a buscar: ").strip()
            resultados = llantas.buscar_llanta(usuario_id, marca)
            if resultados:
                imprimir_tabla_llantas(resultados)
            else:
                print("\n\tNo se encontraron llantas con esa marca.")
            funciones.esperar_tecla()

        elif opcion == '4' or opcion.upper() == "MODIFICAR":
            funciones.borrar_pantalla()
            registros = llantas.mostrar_llantas(usuario_id)
            if registros:
                imprimir_tabla_llantas(registros)
                id_llanta = input("\n\tID de la llanta a actualizar: ").strip()
                marca = input("\tNueva marca: ").strip()
                categoria = input("\tNueva categoría: ").strip()
                medida = input("\tNueva medida: ").strip()
                estado = input("\tNuevo estado: ").strip()
                try:
                    precio = float(input("\tNuevo precio: "))
                    cantidad = int(input("\tNueva cantidad: "))
                except ValueError:
                    print("\n\t❌ Precio y cantidad deben ser numéricos.")
                    funciones.esperar_tecla()
                    continue

                if llantas.cambiar_llanta(usuario_id, id_llanta, marca, categoria, medida, estado, precio, cantidad):
                    print("\n\t✅ Llanta actualizada con éxito.")
                else:
                    print("\n\t❌ No se pudo actualizar la llanta.")
            else:
                print("\n\tNo hay llantas registradas.")
            funciones.esperar_tecla()

        elif opcion == '5' or opcion.upper() == "ELIMINAR":
            funciones.borrar_pantalla()
            registros = llantas.mostrar_llantas(usuario_id)
            if registros:
                imprimir_tabla_llantas(registros)
                id_llanta = input("\n\tID de la llanta a eliminar: ")
                if llantas.eliminar_llanta(usuario_id, id_llanta):
                    print("\n\t^ llanta eliminada exitosamente.")
                else:
                    print("\n\t^ No se pudo eliminar la llanta.")
            else:
                print("\n\tNo hay llantas registradas.")
            funciones.esperar_tecla()

        elif opcion == '6' or opcion.upper() == "VENDER":
            funciones.borrar_pantalla()
            registros = llantas.mostrar_llantas(usuario_id)

            if registros:
                imprimir_tabla_llantas(registros)
                id_llanta = input("\n\tID de la llanta a vender: ")

            try:
                cantidad_vender = int(input("\tCantidad a vender: "))
                if cantidad_vender <= 0:
                    print("\n\t^ La cantidad debe ser mayor a cero.")
                    funciones.esperar_tecla()
                    continue
                    
                # Obtener precio para mostrar el total
                llanta_seleccionada = next((llanta for llanta in registros if str(llanta[0]) == id_llanta), None)

                if not llanta_seleccionada:
                    print("\n\t^ ID de llanta no válido.")
                    funciones.esperar_tecla()
                    continue

                total_venta = llanta_seleccionada[5] * cantidad_vender
                print(f"\n\tTotal de la venta: ${total_venta:.2f}")
                
                confirmar = input("\t¿Confirmar venta? (S/N): ").upper()
                if confirmar != 'S':
                    print("\n\t^ Venta cancelada.")
                    funciones.esperar_tecla()
                    continue
                    
                resultado = llantas.vender_llanta(usuario_id, id_llanta, cantidad_vender)
                
                if resultado == "ok":
                    print("\n\t^ Venta registrada exitosamente.")
                elif resultado == "no_stock":
                    print("\n\t^ No hay suficiente stock para realizar la venta.")
                elif resultado == "no_llanta":
                    print("\n\t^ La llanta no existe.")
                else:
                    print("\n\t^ Error al procesar la venta.")
                    
            except ValueError:
                print("\n\t^ La cantidad debe ser un número entero.")
                
            funciones.esperar_tecla()
        elif opcion == '7' or opcion.upper() == "HISTORIAL":
            funciones.borrar_pantalla()
            ventas = llantas.mostrar_ventas(usuario_id)

            if ventas:
                # Función para imprimir en formato de tabla (ajusta según tus necesidades)
                print("\n\t=== HISTORIAL DE VENTAS ===")
                # Versión corregida (5 columnas)
                print("\t{:<5} {:<15} {:<8} {:<10} {:<12}".format(
                    "ID", "Marca", "Cantidad", "Total", "Fecha"
                ))
                print("\t" + "-" * 55)
                for venta in ventas:
                    print("\t{:<5} {:<15} {:<8} ${:<9.2f} {:<12}".format(
                        venta[0],      # ID
                        venta[1],      # Marca
        venta[2],      # Cantidad
        venta[3],      # Total
        venta[4].strftime("%d/%m/%Y") if venta[4] else ""  # Fecha
    ))
            else:
                print("\n\tNo hay ventas registradas.")

            funciones.esperar_tecla()

#-----------------------------------------------------------------------------------------------------------------------------------------------
def imprimir_tabla_llantas(registros):
    print(f"\n{'ID':<5}{'Marca':<15}{'Categoría':<15}{'Medida':<12}{'Estado':<10}{'Precio':<10}{'Cantidad':<10}")
    print("-" * 77)
    for l in registros:
        print(f"{l[0]:<5}{l[1]:<15}{l[2]:<15}{l[3]:<12}{l[4]:<10}${l[5]:<9}{l[6]:<10}")
# ---------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
