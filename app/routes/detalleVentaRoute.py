from flask import Blueprint, render_template, request, redirect, url_for
from app.models.DetalleVenta import DetalleVentas, db

bp = Blueprint('DetalleVenta', __name__)

@bp.route('/index')
def index():
    data = DetalleVentas.query.all()
    return render_template('detalleVenta/index.html', data=data)

@bp.route('/detalleVenta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':  
        cantidadDetalleVenta = request.form['cantidadDetalleVenta']     
        new_DetalleVeta = DetalleVentas(cantidadDetalleVenta=cantidadDetalleVenta)
        db.session.add(new_DetalleVeta)
        db.session.commit()
        
       # return redirect(url_for('productos.index'))
    #data = DetalleVentas.query.all()
    #eturn render_template('Productos/add.html', data=data)