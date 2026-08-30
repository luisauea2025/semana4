from flask import Flask, render_template, redirect, url_for, flash
from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.factura_form import FacturaForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta_super_segura_123'

lista_productos = [{"id": 101, "nombre": "Laptop Pro", "precio": 1200.00, "stock": 5}]
lista_clientes = []
lista_proveedores = []
lista_facturas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('productos.html', productos=lista_productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        nuevo_item = {
            "id": len(lista_productos) + 101,
            "nombre": form.nombre.data,
            "precio": float(form.precio.data),
            "stock": form.stock.data
        }
        lista_productos.append(nuevo_item)
        return redirect(url_for('productos'))
    return render_template('producto_form.html', form=form)

@app.route('/clientes')
def clientes():
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html', proveedores=lista_proveedores)

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html', facturas=lista_facturas)

if __name__ == '__main__':
    app.run(debug=True)