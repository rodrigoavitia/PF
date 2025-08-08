from conexionBD_llantas import *

def agregar_llanta(usuario_id, marca, categoria, medida, estado, precio, cantidad):
    try:
        cursor.execute("""
            INSERT INTO llantas (usuario_id, marca, categoria, medida, estado, precio, cantidad)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (usuario_id, marca, categoria, medida, estado, precio, cantidad))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al agregar llanta:", e)
        return False

def mostrar_llantas(usuario_id):
    try:
        cursor.execute("SELECT * FROM llantas WHERE usuario_id = %s", (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar llantas:", e)
        return []

def buscar_llanta(usuario_id, marca):
    try:
        cursor.execute("SELECT * FROM llantas WHERE usuario_id = %s AND marca LIKE %s", (usuario_id, "%" + marca + "%"))
        return cursor.fetchall()
    except Exception as e:
        print("Error al buscar llantas:", e)
        return []

def eliminar_llanta(usuario_id, llanta_id):
    try:
        cursor.execute("DELETE FROM llantas WHERE usuario_id = %s AND id = %s", (usuario_id, llanta_id))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar llanta:", e)
        return False
