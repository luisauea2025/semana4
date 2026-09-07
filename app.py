import os
import sqlite3
from flask import Flask, render_template, redirect, url_for, flash
from forms.producto_form import ProductoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta'

# Ruta hacia la carpeta data/ y el archivo de base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'ferreteria.db')

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializamos la base de datos
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    form = ProductoForm()

    if form.validate_on_submit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Se convierte form.precio.data a float() para evitar el error de sqlite3
        cursor.execute(
            'INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)',
            (form.nombre.data, float(form.precio.data), form.stock.data)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('productos'))

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, precio, stock FROM productos')
    lista_productos = cursor.fetchall()
    conn.close()

    return render_template('productos.html', form=form, productos=lista_productos)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

if __name__ == '__main__':
    app.run(debug=True)