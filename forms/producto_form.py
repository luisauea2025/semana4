from flask import Flask, render_template, request, redirect, url_for, flash
from conexion.conexion import obtener_conexion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_ferreteria'

@app.route('/')
def index():
    return render_template('index.html')

# 1. LISTAR PRODUCTOS DESDE MYSQL (SELECT + JOIN)
@app.route('/productos')
def productos():
    conexion = obtener_conexion()
    lista_productos = []
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        query = """
            SELECT p.id, p.nombre, p.precio, p.stock, c.nombre AS categoria 
            FROM productos p 
            LEFT JOIN categorias c ON p.categoria_id = c.id
        """
        cursor.execute(query)
        lista_productos = cursor.fetchall()
        cursor.close()
        conexion.close()
    return render_template('productos.html', productos=lista_productos)

# 2. AGREGAR PRODUCTO (INSERT INTO)
@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria_id = request.form.get('categoria_id') or None

        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO productos (nombre, precio, stock, categoria_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, precio, stock, categoria_id))
            conexion.commit()
            cursor.close()
            conexion.close()
            return redirect(url_for('productos'))

    return render_template('producto_form.html', producto=None)

# 3. EDITAR PRODUCTO (SELECT WHERE + UPDATE WHERE)
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    conexion = obtener_conexion()
    if not conexion:
        return redirect(url_for('productos'))

    cursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        categoria_id = request.form.get('categoria_id') or None

        query = "UPDATE productos SET nombre = %s, precio = %s, stock = %s, categoria_id = %s WHERE id = %s"
        cursor.execute(query, (nombre, precio, stock, categoria_id, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return redirect(url_for('productos'))

    # Obtener el registro a editar
    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
    producto = cursor.fetchone()
    cursor.close()
    conexion.close()

    return render_template('producto_form.html', producto=producto)

# 4. ELIMINAR PRODUCTO (DELETE FROM WHERE)
@app.route('/productos/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        cursor.close()
        conexion.close()
    return redirect(url_for('productos'))

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