from conexionBD_llantas import *

def agregar_llanta(marca, categoria, medida, estado, precio, cantidad):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO llantas (marca, categoria, medida, estado, precio, cantidad) VALUES (%s, %s, %s, %s, %s, %s)",
            (marca, categoria, medida, estado, precio, cantidad)
        )
        conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error al agregar llanta: {e}")
        return False
    
def mostrar_llantas():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM llantas")
        llantas = cursor.fetchall()
        cursor.close()
        return llantas
    except Exception as e:
        print(f"Error al mostrar llantas: {e}")
    return []
        

    # AQUI EN LLANTAS.py LO QUE ESCRIBIMOS ES LO QUE COMUNICAMOS CON LA BASE DE DATOS, NO LO QUE HARA EL CODIGO EN LA TERMINAL, PUEDES CORROBORAR
    # EN NOTAS.PY DEL PROFE DAGOBERTO