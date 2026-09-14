from flask import Flask, render_template, request, redirect, url_for, flash
from conexion.conexion import obtener_conexion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_ferreteria'

# --- RUTAS EXISTENTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')


# --- MÓDULO PRODUCTOS (CRUD MySQL) ---

# 1. LISTAR (SELECT con JOIN)
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

# 2. AGREGAR (INSERT INTO)
@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')
        categoria_id = request.form.get('categoria_id')

        conexion = obtener_conexion()
        if conexion:
            cursor = conexion.cursor()
            query = "INSERT INTO productos (nombre, precio, stock, categoria_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre, precio, stock, categoria_id))
            conexion.commit()
            cursor.close()
            conexion.close()
            flash('Producto agregado correctamente', 'success')
            return redirect(url_for('productos'))

    return render_template('producto_form.html')

# 3. MODIFICAR (SELECT WHERE + UPDATE WHERE)
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        query = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        cursor.execute(query, (nombre, precio, stock, id))
        conexion.commit()
        cursor.close()
        conexion.close()
        flash('Producto actualizado correctamente', 'warning')
        return redirect(url_for('productos'))

    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
    prod = cursor.fetchone()
    cursor.close()
    conexion.close()

    return render_template('producto_form.html', producto=prod)

# 4. ELIMINAR (DELETE WHERE)
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
        flash('Producto eliminado correctamente', 'danger')
    return redirect(url_for('productos'))


if __name__ == '__main__':
    app.run(debug=True)