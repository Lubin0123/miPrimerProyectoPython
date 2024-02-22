from flask import Blueprint, render_template, request, redirect, url_for
from app.models.FacturaVentas import FacturaVentas, db
from datetime import datetime
from app.routes.carritoVentasRoute import carritoVentas
from app.models.Clientes import Clientes
from app.models.Productos import Productos
from flask_login import current_user
from app.models.DetalleVenta import DetalleVentas

bp = Blueprint('facturaVentas', __name__)

@bp.route('/facturaVenta')
def index():
    

    if current_user.is_authenticated:
        fechaActual = datetime.now()
        fechaFormateada = fechaActual.strftime("%Y-%m-%d")

        subTotal = 0
        for carritoP in carritoVentas.getItems():
            subTotal +=  int(carritoP['producto'].precioProductos)
            print("subtotal",subTotal)

        iva = subTotal * 0.19
        subTotalFinal = iva + subTotal
        
        horaActual = datetime.now()
        formatoHora = horaActual.strftime("%H:%M:%S")
        print(formatoHora)

        
        new_FacturaVenta = FacturaVentas(
        idFacturaVentas=None,
        idClientes=current_user.idClientes,
        horaFacturaVentas=horaActual,
        totalFacturaVentas=subTotalFinal
        )
                
        db.session.add(new_FacturaVenta)
        db.session.commit()

        for carrito in carritoVentas.getItems():
            idProductos = carrito["producto"].idProductos        
            detallefactura = DetalleVentas(idDetalleVenta=None,cantidadDetalleVenta=1,idFactura=new_FacturaVenta.idFacturaVentas,idClientes=current_user.idClientes, idProductos=idProductos)
            db.session.add(detallefactura)
            db.session.commit() 
        #carritoVentas.vaciarcarrito()
            
        Detalles =DetalleVentas.query.filter_by(idFactura=new_FacturaVenta.idFacturaVentas).all()


        return render_template('facturaVentas/vistaFactura.html', fecha=fechaFormateada, hora=formatoHora,subTotal=subTotal, total=subTotalFinal,DetalleVentas=Detalles, iva=iva, car=carritoVentas.getItems())
    return redirect(url_for('carritos.eliminarDelCarrito'))


    