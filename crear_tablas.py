import psycopg2

URL_EXTERNA = "postgresql://ferreteria_db_anq5_user:cLv9Bdrp9N9mVXrWqvYJIPC8NHxcMF1I@dpg-dassfhfpn0mc739rms20-a.oregon-postgres.render.com/ferreteria_db_anq5"

# SQL con la estructura exacta que utiliza app.py
sql = """
DROP TABLE IF EXISTS productos, proveedores, usuarios CASCADE;

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(100) UNIQUE NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    clave VARCHAR(255) NOT NULL,
    contrasena VARCHAR(255)
);

CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10, 2) NOT NULL,
    stock INT NOT NULL,
    proveedor_id INT REFERENCES proveedores(id) ON DELETE SET NULL
);
"""

try:
    conexion = psycopg2.connect(URL_EXTERNA)
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()
    print("¡ESTRUCTURA COMPLETA CREADA CON EXITO EN POSTGRESQL!")
    cursor.close()
    conexion.close()
except Exception as e:
    print(f"Error: {e}")