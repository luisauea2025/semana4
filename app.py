import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_ferreteria'

# Enlace a la base de datos de PostgreSQL en Render
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://ferreteria_db_anq5_user:cLv9Bdrp9N9mVXrWqvYJIPC8NHxcMF1I@dpg-dassfhfpn0mc739rms20-a.oregon-postgres.render.com/ferreteria_db_anq5')

def obtener_conexion():
    return psycopg2.connect(DATABASE_URL)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        clave = request.form.get('clave') or request.form.get('contrasena')
        
        try:
            conn = obtener_conexion()
            cur = conn.cursor()
            cur.execute("SELECT * FROM usuarios WHERE usuario = %s AND (clave = %s OR contrasena = %s)", (usuario, clave, clave))
            user = cur.fetchone()
            cur.close()
            conn.close()
            
            if user:
                session['usuario'] = usuario
                return redirect(url_for('productos'))
            else:
                return render_template('login.html', error="Usuario o contraseña incorrectos")
        except Exception as e:
            return f"Error en inicio de sesión: {e}", 500

    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        usuario = request.form.get('usuario', '')
        correo = request.form.get('correo', '')
        clave = request.form.get('clave') or request.form.get('contrasena', '')

        try:
            conn = obtener_conexion()
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO usuarios (nombre, usuario, correo, clave, contrasena) VALUES (%s, %s, %s, %s, %s)",
                (nombre, usuario, correo, clave, clave)
            )
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('login'))
        except Exception as e:
            return f"Error al registrar usuario: {e}", 500

    return render_template('registro.html')

@app.route('/productos')
def productos():
    try:
        conn = obtener_conexion()
        cur = conn.cursor()
        cur.execute("SELECT * FROM productos")
        prods = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('productos.html', productos=prods)
    except Exception as e:
        return f"Error al cargar productos: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)