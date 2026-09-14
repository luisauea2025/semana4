import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',             # Cambia si tu usuario de MySQL es diferente
            password='tu_password',   # Coloca tu contraseña de MySQL
            database='ferreteria_db'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None