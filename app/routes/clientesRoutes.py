from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Cliente import Cliente
from app import db

bp = Blueprint('clientes', __name__)

@bp.route('/')
def index():
    data = Cliente.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('clientes/index.html', data=data)

@bp.route('/clientes/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        idClientes = request.form['idClientes']
        nombreClientes = request.form['nombreClientes']
        cedulaClientes = request.form['cedulaClientes']
        correoClientes = request.form['correoClientes']
        
        new_Clientes = Cliente(idClientes=idClientes, nombreClientes=nombreClientes, cedulaClientes=cedulaClientes, correoClientes=correoClientes)
        db.session.add(new_Clientes)
        db.session.commit()
        
        return redirect(url_for('clientes.index'))

    return render_template('clientes/add.html')

@bp.route('/Clientes/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    clientes = clientes.query.get_or_404(id)

    if request.method == 'POST':
        clientes.idClientes = request.form['idClientes']
        clientes.nombreClientes = request.form['nombreClientes']
        clientes.cedulaClientes = request.form['cedulaClientes']
        clientes.correoClientes
        db.session.commit()
        return redirect(url_for('clientes.index'))

    return render_template('clientes/edit.html', clientes=clientes)
    

@bp.route('/Clientes/delete/<int:id>')
def delete(id):
    clientes = clientes.query.get_or_404(id)
    
    db.session.delete(clientes)
    db.session.commit()

    return redirect(url_for('clientes.index'))
