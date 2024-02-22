from flask import Blueprint, render_template, request, redirect, url_for
from app.models.Productos import Productos
from app.models.Clientes import Clientes, db


bp = Blueprint('productos', __name__)

@bp.route('/productos'  , methods=['GET', 'POST'])
def index():
    data = Productos.query.all()
    return render_template('productos/index.html', data=data)


@bp.route('/productos/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descripcionProductos = request.form['descripcionProductos']
        precioProductos = request.form['precioProductos']
        cantidadProductos = request.form['cantidadProductos']
        nombreImagen = request.form['nombreImagen']
        
        new_Producto = Productos(descripcionProductos=descripcionProductos, precioProductos=precioProductos, cantidadProductos=cantidadProductos, nombreImagen=nombreImagen)
        db.session.add(new_Producto)
        db.session.commit()
        
        return redirect(url_for('productos.index'))
    data = Productos.query.all()
    return render_template('Productos/add.html', data=data)

@bp.route('/productos/edit/<int:idProductos>', methods=['GET', 'POST'])
def edit(idProductos):
    print(f"El valor es: {idProductos}")
    data = Productos.query.get_or_404(idProductos)
    #print(f"El producto es: {data}")

    if request.method == 'POST':
        data.descripcionProductos = request.form['descripcionProductos']
        data.precioProductos = request.form['precioProductos']
        data.cantidadProductos = request.form['cantidadProductos']
        db.session.commit()
        
        return redirect(url_for('productos.index'))
    return render_template('productos/edit.html', data=data)

@bp.route('/productos/delete/<int:idProductos>')
def delete(idProductos):
    productos = Productos.query.get_or_404(idProductos)
    
    db.session.delete(productos)
    db.session.commit()

    return redirect(url_for('productos.index'))
