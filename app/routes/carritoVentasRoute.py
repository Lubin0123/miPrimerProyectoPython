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

@bp.route('/eliminar/<int:idProductos>', methods=['GET'])
def eliminarDelCarrito(idProductos):
    carritoVentas.eliminarProducto(idProductos)
    return render_template('carrito/carritoVentas.html')
    #return "Entra a eliminar del carrito"
