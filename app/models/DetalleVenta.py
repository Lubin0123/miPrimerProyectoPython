from flask_login import UserMixin
from app import db
from app.models.Productos import Productos
from app.models.FacturaVentas import FacturaVentas

class DetalleVentas(db.Model, UserMixin):

    __tablename__ ="detalleVenta"
    idDetalleVenta = db.Column(db.Integer, primary_key=True)
    cantidadDetalleVenta =db.Column(db.Integer, nullable= False)
    idProductos = db.Column(db.Integer, db.ForeignKey('producto.idProductos'), nullable=False)
    idFactura = db.Column(db.Integer, db.ForeignKey('facturaVenta.idFacturaVentas'), nullable=False)
    idClientes = db.Column(db.Integer, db.ForeignKey('cliente.idClientes'), nullable=False)
