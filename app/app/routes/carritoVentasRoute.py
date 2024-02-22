from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.Productos import Productos
from app.models.carritoVentas import CarritoVentas

bp = Blueprint('carritos', __name__)

carritoVentas = CarritoVentas()

@bp.route('/')
def vistaProductos():
    data = Productos.query.all()  
    tamano = tCarrito()  
    return render_template('index.html', data=data, tamano=tamano)

@bp.route('/ListarCarrito')
def listar():
    items = carritoVentas.getItems()
    return render_template('productos/list.html', items=items)

@bp.route('/ListarProductos')
def index():
 subTotal = 0
 for carritoP in carritoVentas.getItems():
   subTotal +=  int(carritoP['producto'].precioProductos)
   print("subtotal",subTotal)
 return render_template('carrito/carritoVentas.html',carritoVentas=carritoVentas.getItems(),subTotal=subTotal)

@bp.route('/agregar/<int:idProductos>', methods=['POST'])
def agregarAlCarrito(idProductos):
    cantidad = 1
    carritoVentas.agregarProducto(idProductos, cantidad)
    return redirect(url_for('carritos.vistaProductos'))
    #return "Entra a agregar corrito"

@bp.route('/realizarCompra')
def realizarCompra():
    total = carritoVentas.calcularTotal()
    return render_template('realizarCompra.html', total=total)

@bp.route('/generarFactura', methods=['POST'])
def generarFactura():
    total = carritoVentas.calcularTotal()
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carritoVentas.carrito = []
    return render_template('factura.html', total=total) #debo mirar bien a donde voy a direccionar

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carritoVentas.tamanoD()
    return a

@bp.route('/eliminar/<int:idProductos>', methods=['GET', 'POST'])
def eliminarDelCarrito(idProductos):
    global subTotal
    print(idProductos)
    carritoVentas.eliminarProducto(idProductos)
    subTotal = 0  # Inicializa el subtotal antes de recalcularlo
    for carritoP in carritoVentas.getItems():
        subTotal += int(carritoP['producto'].precioProductos)
    print("subtotal", subTotal)
    return render_template('carrito/carritoVentas.html', idProductos=idProductos, carritoVentas=carritoVentas.getItems(), subTotal=subTotal)

@bp.route('/vaciarCarrito/<int:idProductos>',methods=['GET', 'POST'])
def vaciarCarrito(idProductos):
    carritoVaciado = carritoVentas.query.get(idProductos)
    
    if carritoVaciado:
        carritoVaciado.vaciarcarrito()
        flash('carrito vaciado correctamente', 'success')
        return render_template('index.html')
    else: flash('no se encontro el producto en el carrito', 'danger')