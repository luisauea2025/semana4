import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',         # Tu usuario de MySQL
            password='tu_password', # Tu contraseña de MySQL
            database='ferreteria_db'
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        return None