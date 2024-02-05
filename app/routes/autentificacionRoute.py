from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms import StringField, PasswordField ,validators
from flask_bcrypt import Bcrypt
from app.models.Clientes import Clientes
from app import db

bp = Blueprint('autentificaionBp', __name__)

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
                return redirect(url_for('autenticaciónBp.dashboard'))
            
        flash("Invalid credentials. Please try again.", "error")

    
    if current_user.is_authenticated:
        return redirect(url_for('autenticaciónBp.dashboard'))
    return render_template("autentificacion/login.html")

@bp.route('/crearCuenta')
def crearCuentas():
    if current_user.is_authenticated:
        return redirect(url_for ('autentificaciónBp.index')) 
    return render_template('crearCuenta.html')


class RegistrationForm(FlaskForm):
    nombreclientes = StringField('Nombre de Usuario', validators=[validators.DataRequired()])
    password = PasswordField('Contraseña', validators=[
        validators.DataRequired(),
        validators.Length(min=6, message='La contraseña debe tener al menos 6 caracteres'),
        validators.EqualTo('confirm_password', message='Las contraseñas deben coincidir')
    ])
    confirm_password = PasswordField('Confirmar Contraseña')
    submit = SubmitField('Registrarse')

@bp.route('/Registro', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm()

    if form.validate_on_submit():
        idClientes = form.user_name.data   
        nombreclientes = form.user.data
    return redirect(url_for('inicio'))

    return render_template('registro.html', form=form)

         
   


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
    return redirect(url_for('autenticación.login'))
