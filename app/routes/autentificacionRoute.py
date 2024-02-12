import bcrypt
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField, PasswordField ,validators
from flask_bcrypt import Bcrypt
from app.models.Clientes import Clientes
from app import db

bp = Blueprint('autentificacionBp', __name__)

from flask import redirect, url_for, flash
bcrypt = Bcrypt()
@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        nombreclientes = request.form['nombreClientes']
        password = request.form['password']
        
        cliente = Clientes.query.filter_by(nombreClientes=nombreclientes).first()
        
        if cliente and bcrypt.check_password_hash(clientePasswordBd, password):

            clientePasswordBd = cliente.password
            login_user(cliente)
            flash("Login successful!", "success")
                #return redirect(url_for('autentificacionBp.dashboard'))
            return render_template('autentificacion/index.html')
            
        flash("Invalid credentials. Please try again.", "error")

    if current_user.is_authenticated:
       # return redirect(url_for('autentificacionBp.dashboard'))
        return render_template('clientes/index.html')
    else:
        flash("No hay clientes registrados. Por favor, regístrate antes de iniciar sesión.", "info")
        return redirect(url_for('autentificacionBp.registro'))



@bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombreclientes = request.form['nombreClientes']
        cedulaclientes = request.form['cedulaClientes']
        correoclientes = request.form['correoClientes']
        password = request.form['password']
        print("Antes de imprir el pass")
        print(password)
        # Verificar si el usuario ya existe
        if Clientes.query.filter_by(nombreClientes=nombreclientes).first():
            flash("El usuario ya existe. Por favor, elige otro nombre de usuario.", "error")
            return redirect(url_for('autentificacionBp.registro'))

        # Crear una nueva cuenta
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        nuevo_cliente = Clientes(
            nombreClientes=nombreclientes,
            cedulaClientes=cedulaclientes,
            correoClientes=correoclientes,
            password=hashed_password
        )

        # Agregar el nuevo cliente a la base de datos
        db.session.add(nuevo_cliente)
        db.session.commit()

        flash("Cuenta creada con éxito. Ahora puedes iniciar sesión.", "success")
        print("antes de direccionar al login")
        return redirect(url_for('autentificacionBp.login'))

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
