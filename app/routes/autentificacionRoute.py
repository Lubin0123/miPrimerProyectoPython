from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField, PasswordField ,validators
from flask_bcrypt import Bcrypt
from app.models.Clientes import Clientes
from app import db

bp = Blueprint('autentificacionBp', __name__)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        bcrypt = Bcrypt()
        nombreclientes = request.form['nombreClientes']
        password = request.form['password']
        
        cliente = Clientes.query.filter_by(nombreClientes=nombreclientes).first()
        
        if cliente:
            clientePasswordBd = cliente.password
            if bcrypt.check_password_hash (clientePasswordBd, password):
                login_user(cliente)
                flash("Login successful!", "success")
                return redirect(url_for('autentificacion.dashboard'))
            
        flash("Invalid credentials. Please try again.", "error")

    
    if current_user.is_authenticated:
        return redirect(url_for('autentificacion.dashboard'))
    return render_template("autentificacion/login.html")

@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombreclientes = request.form['nombreClientes']
        password = request.form['password']

        # Verificar si el usuario ya existe
        if Clientes.query.filter_by(nombreClientes=nombreclientes).first():
            flash("El usuario ya existe. Por favor, elige otro nombre de usuario.", "error")
        else:
            # Crear una nueva cuenta
            hashed_password = Bcrypt.generate_password_hash(password).decode('utf-8')
            nuevo_cliente = Clientes(nombreClientes=nombreclientes, password=hashed_password)
            db.session.add(nuevo_cliente)
            db.session.commit()
            flash("Cuenta creada con éxito. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for('autentificacion.login'))

    return render_template("autentificacion/registro.html")
         
@bp.route('/dashboard')
@login_required
def dashboard():
    user_name = current_user.nombreclientes
    return f'Welcome, {user_name}! This is your dashboard.'

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('autentificacion.login'))
