import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from models import Usuario
from forms.login_form import LoginForm
from forms.usuario_form import RegistroForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta_semana14_ferreteria'

# Configuración de Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta sección.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(int(user_id))

# --- RUTAS DE AUTENTICACIÓN ---

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    
    form = RegistroForm()
    if form.validate_on_submit():
        exito = Usuario.crear(form.usuario.data, form.password.data)
        if exito:
            flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error al registrar usuario en la base de datos.', 'danger')
            
    return render_template('registro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.get_by_username(form.usuario.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'¡Bienvenido/a, {user.usuario}!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas. Verifique usuario y contraseña.', 'danger')
            
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))

# --- RUTAS PRINCIPALES Y PROTEGIDAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Mantén la lógica previa que tengas en tus rutas protegidas
@app.route('/productos')
@login_required
def productos():
    return render_template('productos.html')

@app.route('/clientes')
@login_required
def clientes():
    return render_template('clientes.html')

@app.route('/proveedores')
@login_required
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
@login_required
def facturacion():
    return render_template('facturacion.html')

if __name__ == '__main__':
    app.run(debug=True)