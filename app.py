from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    lista_productos = [
        {"id": 101, "nombre": "Laptop Pro 15", "categoria": "Equipos", "precio": 850.00, "stock": 12},
        {"id": 102, "nombre": "Monitor IPS 24", "categoria": "Pantallas", "precio": 175.50, "stock": 25},
        {"id": 103, "nombre": "Teclado Mecánico RGB", "categoria": "Periféricos", "precio": 45.00, "stock": 40}
    ]
    return render_template('productos.html', productos=lista_productos)

@app.route('/clientes')
def clientes():
    lista_clientes = [
        {"id": 1, "nombre": "Carlos Mendoza", "identificacion": "1712345678", "correo": "carlos.m@mail.com", "telefono": "0991234567"},
        {"id": 2, "nombre": "Empresa TechSA", "identificacion": "1790011223001", "correo": "contacto@techsa.com", "telefono": "022555444"}
    ]
    return render_template('clientes.html', clientes=lista_clientes)

@app.route('/proveedores')
def proveedores():
    lista_proveedores = [
        {"id": 50, "empresa": "Distribuidora Global S.A.", "contacto": "Ana Torres", "telefono": "0987654321", "ciudad": "Quito"},
        {"id": 51, "empresa": "Importaciones ImportTech", "contacto": "Luis Gomez", "telefono": "0998877665", "ciudad": "Guayaquil"}
    ]
    return render_template('proveedores.html', proveedores=lista_proveedores)

@app.route('/facturacion')
def facturacion():
    resumen_facturas = [
        {"num": "FAC-0001", "cliente": "Carlos Mendoza", "fecha": "2026-08-10", "total": 1025.50, "estado": "Completada"},
        {"num": "FAC-0002", "cliente": "Empresa TechSA", "fecha": "2026-08-15", "total": 350.00, "estado": "Pendiente"}
    ]
    return render_template('facturacion.html', facturas=resumen_facturas)

if __name__ == '__main__':
    app.run(debug=True)