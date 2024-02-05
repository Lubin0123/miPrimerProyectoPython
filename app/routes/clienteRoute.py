from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Clientes import Clientes, db
from flask_bcrypt import Bcrypt

bp = Blueprint('clientes', __name__)

@bp.route('/cliente')
def index():
    data = Clientes.query.all()
    return render_template('clientes/index.html', data=data)

@bp.route('/clientes/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':       
        bcrypt=Bcrypt()
        nombreClientes = request.form['nombreClientes']
        cedulaClientes = request.form['cedulaClientes']
        correoClientes = request.form['correoClientes']   
        password =request.form['password'] 
        hashedpassword = bcrypt.generate_password_hash(password).decode('utf-8')
    
        new_Clientes = Clientes(nombreClientes=nombreClientes, cedulaClientes=cedulaClientes, correoClientes=correoClientes, password=hashedpassword)
        db.session.add(new_Clientes)
        db.session.commit()
        
        return redirect(url_for('clientes.index'))

    return render_template('clientes/add.html')

@bp.route('/clientes/edit/<int:idClientes>', methods=['GET', 'POST'])
def edit(idClientes):
    clientes = Clientes.query.get_or_404(idClientes)

    if request.method == 'POST':

        clientes.nombreClientes = request.form['nombreClientes']
        clientes.cedulaClientes = request.form['cedulaClientes']
        clientes.correoClientes = request.form['correoClientes']
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('clientes/edit.html', clientes=clientes)


@bp.route('/Clientes/delete/<int:idClientes>')
def delete(idClientes):
    cliente = Clientes.query.get_or_404(idClientes)
    
    db.session.delete(cliente)
    db.session.commit()

    return redirect(url_for('clientes.index'))
