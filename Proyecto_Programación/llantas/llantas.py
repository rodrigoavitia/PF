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
    
def vender_llanta(usuario_id, id_llanta, cantidad_vender):
    try:
        cursor = conexion.cursor()
        
        # 1. Verificar stock y obtener precio de la llanta
        cursor.execute("""
            SELECT l.cantidad, l.precio 
            FROM llantas l 
            WHERE l.id=%s AND l.usuario_id=%s
        """, (id_llanta, usuario_id))
        
        resultado = cursor.fetchone()
        if not resultado:
            cursor.close()
            return "no_llanta"
            
        stock_actual, precio_unitario = resultado
        
        # 2. Validar stock suficiente
        if cantidad_vender > stock_actual:
            cursor.close()
            return "no_stock"
        
        # 3. Calcular total de la venta
        total_venta = precio_unitario * cantidad_vender
        
        # 4. Actualizar stock en llantas
        nuevo_stock = stock_actual - cantidad_vender
        cursor.execute("""
            UPDATE llantas 
            SET cantidad=%s 
            WHERE id=%s AND usuario_id=%s
        """, (nuevo_stock, id_llanta, usuario_id))
        
        # 5. Registrar la venta en la tabla de registro_ventas
        cursor.execute("""
            INSERT INTO registro_ventas (
                llanta_id, 
                usuario_id, 
                cantidad, 
                total, 
                fecha
            ) VALUES (%s, %s, %s, %s, CURDATE())
        """, (id_llanta, usuario_id, cantidad_vender, total_venta))
        
        conexion.commit()
        cursor.close()
        return "ok"
        
    except Exception as e:
        print(f"Error al vender llanta: {e}")
        conexion.rollback()
        return "error"
    
def mostrar_ventas(usuario_id):
    try:
        cursor.execute("""
            SELECT rv.id, l.marca, rv.cantidad, rv.total, rv.fecha 
            FROM registro_ventas rv 
            JOIN llantas l ON rv.llanta_id = l.id 
            WHERE l.usuario_id = %s
        """, (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar ventas:", e)
        return []