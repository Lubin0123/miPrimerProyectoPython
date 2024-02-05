from flask import Blueprint, render_template, request, redirect, url_for
from app.models.FacturaVentas import FacturaVentas, db

bp = Blueprint('facturaVentas', __name__)

@bp.route('/facturaVenta')
def index():
    data = FacturaVentas.query.all()
    return render_template('facturaVentas/index.html', data=data)

@bp.route('/facturaVenta/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':       
        horaFacturaVenta = request.form['horaFacturaVenta']
        totalFacturaVenta = request.form['totalFacturaVenta']    
        new_FacturaVentas = FacturaVentas(idClientes=None, horaFacturaVenta=horaFacturaVenta, totalFacturaVenta=totalFacturaVenta )
        db.session.add(new_FacturaVentas)
        db.session.commit()
        
        return redirect(url_for('facturaVentas.index'))

    return render_template('facturaVentas/add.html')

@bp.route('/facturaVenta/edit/<int:idFacturaVenta>', methods=['GET', 'POST'])
def edit(idFacturaVenta):
    facturaVenta = FacturaVentas.query.get_or_404(idFacturaVenta)

    if request.method == 'POST':

        facturaVenta.horaFacturaVenta = request.form['horaFacturaVenta']
        facturaVenta.totalFacturaVenta = request.form['totalFacturaVenta']
        db.session.commit()
        return redirect(url_for('facturaVentas.index'))

    return render_template('facturaVentas/edit.html', facturaVenta=facturaVenta)


@bp.route('/facturaVenta/delete/<int:idFacturaVenta>')
def delete(idFacturaVenta):
    facturaVenta = FacturaVentas .query.get_or_404(idFacturaVenta)
    
    db.session.delete(facturaVenta)
    db.session.commit()

    return redirect(url_for('facturaVentas.index'))

#@bp.route('/totalFactura')
#def totalFactura(totalFacturaVenta):
    #total = calcularTotalFactura(totalFacturaVenta)
    #return 'Total de facturas: {totalFactura}'