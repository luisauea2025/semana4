import os
import psycopg2

def obtener_conexion():
    try:
        # Lee la variable DATABASE_URL de Render
        database_url = os.environ.get('DATABASE_URL')
        if not database_url:
            raise ValueError("No se encontró la variable DATABASE_URL")
        
        conexion = psycopg2.connect(database_url)
        return conexion
    except Exception as e:
        print(f"Error al conectar con PostgreSQL: {e}")
        return None