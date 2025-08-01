from conexionBD_llantas import *
import datetime
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar(nombre, apellidos, correo, password):
    try:
        fecha = datetime.datetime.now()
        correo = correo.lower().strip()
        password = hash_password(password)
        print("Registrando:", correo, password)         #Esto lo puse para depuracion al final lo eliminamos
        cursor = conexion.cursor()
        cursor.execute(
            "insert into usuarios (nombre, apellidos, correo, password, fecha) values (%s, %s, %s, %s, %s)",
            (nombre, apellidos, correo, password, fecha)
        )
        conexion.commit()
        cursor.close()
        return True
    except Exception as e:
        print("Error:", e)  # Para depuración y checar si hay errores
        return False

def inicio_sesion(correo, password):
    try:
        correo = correo.lower().strip()
        password = hash_password(password)
        print("Buscando: ", correo, password)         #Esto lo puse para depuracion al final lo eliminamos
        cursor = conexion.cursor()
        cursor.execute(
            "select * from usuarios where correo=%s and password=%s",
            (correo, password)
        )                                                                       
        resultado = cursor.fetchone()
        cursor.close()
        return resultado if resultado else []            #Con esto si no encuentra el usuario, retorna una lista vacia
    except Exception as e:
        print("Error:", e)
        return []